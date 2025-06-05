# C Dili için Gerçek Zamanlı Sözdizimi Vurgulayıcı
# Bu program, C kodunu sözcüksel olarak analiz eder, sözdizimini kontrol eder ve GUI'da vurgular.

import tkinter as tk
from tkinter import ttk
import re
from enum import Enum
from typing import List, Tuple, Optional, Any

# Token türlerini tanımlayan enum
class TokenType(Enum):
    KEYWORD = 1  # Anahtar kelimeler (int, if, return, ...)
    IDENTIFIER = 2  # Tanımlayıcılar (değişken, fonksiyon isimleri)
    OPERATOR = 3  # Operatörler (+, -, *, /, =, ==, ...)
    NUMBER = 4  # Sayılar
    STRING = 5  # String sabitleri
    COMMENT = 6  # Yorumlar
    PREPROCESSOR = 7  # Ön işlemci direktifleri (#include, ...)
    SEMICOLON = 8  # Noktalı virgül
    BRACKET_OPEN = 9  # Köşeli parantez açma
    BRACKET_CLOSE = 10  # Köşeli parantez kapama
    PAREN_OPEN = 11  # Normal parantez açma
    PAREN_CLOSE = 12  # Normal parantez kapama
    BRACE_OPEN = 13  # Süslü parantez açma
    BRACE_CLOSE = 14  # Süslü parantez kapama

# Token nesnesi: her bir belirteç için tip, değer, satır ve sütun bilgisi
class Token:
    def __init__(self, type: TokenType, value: str, line: int, column: int):
        self.type = type
        self.value = value
        self.line = line
        self.column = column

    def __str__(self):
        return f"Token({self.type}, '{self.value}', line={self.line}, col={self.column})"

# Sözcüksel analizci (lexer): kodu tokenlara böler
class LexicalAnalyzer:
    def __init__(self):
        # C dili anahtar kelimeleri
        self.keywords = {
            'auto', 'break', 'case', 'char', 'const', 'continue', 'default', 'do',
            'double', 'else', 'enum', 'extern', 'float', 'for', 'goto', 'if',
            'int', 'long', 'register', 'return', 'short', 'signed', 'sizeof', 'static',
            'struct', 'switch', 'typedef', 'union', 'unsigned', 'void', 'volatile', 'while'
        }
        # Token desenleri: regex ile tanımlanır, sıralama önemlidir
        self.patterns = [
            (TokenType.COMMENT, r'//.*$|/\*[\s\S]*?\*/'),  # Yorumlar
            (TokenType.STRING, r'"[^"\\]*(\\.[^"\\]*)*"'),  # Stringler
            (TokenType.NUMBER, r'\b\d+(\.\d+)?\b'),  # Sayılar
            (TokenType.KEYWORD, r'\b(' + '|'.join(sorted(self.keywords, key=len, reverse=True)) + r')\b'),  # Anahtar kelimeler
            (TokenType.PREPROCESSOR, r'#\s*[a-zA-Z]+'),  # Ön işlemci
            (TokenType.OPERATOR, r'==|!=|<=|>=|&&|\|\||[+\-*/%=<>!&|^~?:]'),  # Operatörler
            (TokenType.SEMICOLON, r';'),
            (TokenType.BRACKET_OPEN, r'\['),
            (TokenType.BRACKET_CLOSE, r'\]'),
            (TokenType.PAREN_OPEN, r'\('),
            (TokenType.PAREN_CLOSE, r'\)'),
            (TokenType.BRACE_OPEN, r'\{'),
            (TokenType.BRACE_CLOSE, r'\}'),
            (TokenType.IDENTIFIER, r'\b[a-zA-Z_][a-zA-Z0-9_]*\b')  # Tanımlayıcılar
        ]

    # Koddan token listesi üretir
    def tokenize(self, text: str) -> List[Token]:
        tokens = []
        line = 1
        column = 1
        pos = 0
        while pos < len(text):
            match = None
            for token_type, pattern in self.patterns:
                regex = re.compile(pattern)
                match = regex.match(text, pos)
                if match:
                    value = match.group(0)
                    # Yorum ve boşlukları atla
                    if token_type != TokenType.COMMENT and not value.isspace():
                        tokens.append(Token(token_type, value, line, column))
                    # Satır ve sütun güncelle
                    newlines = value.count('\n')
                    if newlines > 0:
                        line += newlines
                        column = len(value.split('\n')[-1]) + 1
                    else:
                        column += len(value)
                    pos = match.end()
                    break
            if not match:
                # Boşlukları atla
                if text[pos].isspace():
                    if text[pos] == '\n':
                        line += 1
                        column = 1
                    else:
                        column += 1
                    pos += 1
                else:
                    # Tanınmayan karakterleri tanımlayıcı olarak ekle
                    tokens.append(Token(TokenType.IDENTIFIER, text[pos], line, column))
                    pos += 1
                    column += 1
        return tokens

# Parse tree düğümü: sözdizimi ağacının her bir dalı
class ParseTreeNode:
    def __init__(self, label: str, children: Optional[List[Any]] = None):
        self.label = label
        self.children = children if children is not None else []
    def to_string(self, level=0) -> str:
        indent = '  ' * level
        s = f"{indent}{self.label}\n"
        for child in self.children:
            if isinstance(child, ParseTreeNode):
                s += child.to_string(level + 1)
            else:
                s += f"{indent}  {child}\n"
        return s

# Parser: token listesini sözdizimi ağacına dönüştürür
class Parser:
    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.current = 0
        self.parse_tree = ParseTreeNode("Program")
    # Sıradaki token'ı döndür
    def peek(self) -> Optional[Token]:
        if self.current < len(self.tokens):
            return self.tokens[self.current]
        return None
    # Sıradaki token'ı tüket ve döndür
    def advance(self) -> Optional[Token]:
        if self.current < len(self.tokens):
            token = self.tokens[self.current]
            self.current += 1
            return token
        return None
    # Belirli tipteki token'ı bekle ve tüket
    def match(self, *types: TokenType) -> Optional[Token]:
        if self.peek() and self.peek().type in types:
            return self.advance()
        return None
    # Parse işlemini başlat
    def parse(self) -> Tuple[bool, ParseTreeNode]:
        self.parse_tree = ParseTreeNode("Program")
        try:
            while self.peek():
                node = self.parse_statement()
                if not node:
                    node = self.parse_function_definition()
                if not node:
                    node = self.parse_unknown()
                self.parse_tree.children.append(node)
            return True, self.parse_tree
        except Exception as e:
            print(f"Parse error: {e}")
            return False, self.parse_tree
    # Statement (ifade) ayrıştırıcı
    def parse_statement(self) -> Optional[ParseTreeNode]:
        token = self.peek()
        if not token:
            return None
        if token.type == TokenType.KEYWORD:
            if token.value in ['if', 'while', 'for']:
                return self.parse_control_structure()
            elif token.value in ['int', 'char', 'float', 'double', 'void']:
                if self.lookahead_is_function():
                    return None
                return self.parse_declaration()
            elif token.value == 'return':
                return self.parse_return()
        elif token.type == TokenType.IDENTIFIER:
            return self.parse_assignment()
        return None
    # Fonksiyon tanımı olup olmadığını kontrol et
    def lookahead_is_function(self) -> bool:
        if self.current + 2 < len(self.tokens):
            t1 = self.tokens[self.current]
            t2 = self.tokens[self.current + 1]
            t3 = self.tokens[self.current + 2]
            return (t1.type == TokenType.KEYWORD and
                    t2.type == TokenType.IDENTIFIER and
                    t3.type == TokenType.PAREN_OPEN)
        return False
    # Fonksiyon tanımını ayrıştır
    def parse_function_definition(self) -> Optional[ParseTreeNode]:
        start = self.current
        if self.current + 2 < len(self.tokens):
            t1 = self.tokens[self.current]
            t2 = self.tokens[self.current + 1]
            t3 = self.tokens[self.current + 2]
            if (t1.type == TokenType.KEYWORD and
                t2.type == TokenType.IDENTIFIER and
                t3.type == TokenType.PAREN_OPEN):
                type_token = self.advance()
                id_token = self.advance()
                self.advance()  # (
                while self.peek() and self.peek().type != TokenType.PAREN_CLOSE:
                    self.advance()
                self.match(TokenType.PAREN_CLOSE)
                if not self.match(TokenType.BRACE_OPEN):
                    return None
                body = []
                while self.peek() and self.peek().type != TokenType.BRACE_CLOSE:
                    stmt = self.parse_statement()
                    if not stmt:
                        stmt = self.parse_unknown()
                    body.append(stmt)
                self.match(TokenType.BRACE_CLOSE)
                return ParseTreeNode("FUNCTION_DEFINITION", [
                    ParseTreeNode("TYPE", [type_token.value]),
                    ParseTreeNode("NAME", [id_token.value]),
                    ParseTreeNode("BODY", body)
                ])
        self.current = start
        return None
    # Kontrol yapısı (if, while, for) ayrıştırıcı
    def parse_control_structure(self) -> Optional[ParseTreeNode]:
        token = self.advance()
        node = ParseTreeNode(f"{token.value.upper()}_STATEMENT")
        if not self.match(TokenType.PAREN_OPEN):
            return None
        # Koşulu expression olarak ayrıştır
        cond_expr = self.parse_expression()
        node.children.append(ParseTreeNode("CONDITION", [cond_expr] if cond_expr else []))
        if not self.match(TokenType.PAREN_CLOSE):
            return None
        if not self.match(TokenType.BRACE_OPEN):
            return None
        body = []
        while self.peek() and self.peek().type != TokenType.BRACE_CLOSE:
            stmt = self.parse_statement()
            if not stmt:
                stmt = self.parse_unknown()
            body.append(stmt)
        self.match(TokenType.BRACE_CLOSE)
        node.children.append(ParseTreeNode("BODY", body))
        return node
    # Değişken tanımı ayrıştırıcı
    def parse_declaration(self) -> Optional[ParseTreeNode]:
        type_token = self.advance()
        node = ParseTreeNode("DECLARATION", [type_token.value])
        if not self.match(TokenType.IDENTIFIER):
            return None
        id_token = self.tokens[self.current - 1]
        node.children.append(ParseTreeNode("IDENTIFIER", [id_token.value]))
        if self.match(TokenType.OPERATOR):
            expr = self.parse_expression()
            node.children.append(ParseTreeNode("EXPRESSION", [expr] if expr else []))
        if not self.match(TokenType.SEMICOLON):
            return None
        return node
    # Atama ifadesi ayrıştırıcı
    def parse_assignment(self) -> Optional[ParseTreeNode]:
        id_token = self.advance()
        node = ParseTreeNode("ASSIGNMENT", [id_token.value])
        if not self.match(TokenType.OPERATOR):
            return None
        op_token = self.tokens[self.current - 1]
        node.children.append(ParseTreeNode("OPERATOR", [op_token.value]))
        expr = self.parse_expression()
        node.children.append(ParseTreeNode("EXPRESSION", [expr] if expr else []))
        if not self.match(TokenType.SEMICOLON):
            return None
        return node
    # Return ifadesi ayrıştırıcı
    def parse_return(self) -> Optional[ParseTreeNode]:
        self.advance()  # 'return'
        node = ParseTreeNode("RETURN_STATEMENT")
        expr = self.parse_expression()
        node.children.append(ParseTreeNode("EXPRESSION", [expr] if expr else []))
        if not self.match(TokenType.SEMICOLON):
            return None
        return node
    # --- Expression Parsing (recursive descent) ---
    # Expression (ifade) ayrıştırıcı
    def parse_expression(self) -> Optional[ParseTreeNode]:
        left = self.parse_simple_expression()
        token = self.peek()
        if token and token.type == TokenType.OPERATOR and token.value in ['==', '!=', '<', '>', '<=', '>=']:
            op_token = self.advance()
            right = self.parse_simple_expression()
            return ParseTreeNode("EXPRESSION", [left, ParseTreeNode("OPERATOR", [op_token.value]), right])
        return left
    # Toplama ve çıkarma işlemleri
    def parse_simple_expression(self) -> Optional[ParseTreeNode]:
        node = self.parse_term()
        while True:
            token = self.peek()
            if token and token.type == TokenType.OPERATOR and token.value in ['+', '-']:
                op_token = self.advance()
                right = self.parse_term()
                node = ParseTreeNode("SIMPLE_EXPRESSION", [node, ParseTreeNode("OPERATOR", [op_token.value]), right])
            else:
                break
        return node
    # Çarpma ve bölme işlemleri
    def parse_term(self) -> Optional[ParseTreeNode]:
        node = self.parse_factor()
        while True:
            token = self.peek()
            if token and token.type == TokenType.OPERATOR and token.value in ['*', '/']:
                op_token = self.advance()
                right = self.parse_factor()
                node = ParseTreeNode("TERM", [node, ParseTreeNode("OPERATOR", [op_token.value]), right])
            else:
                break
        return node
    # Sayı, tanımlayıcı, string veya parantezli ifade ayrıştırıcı
    def parse_factor(self) -> Optional[ParseTreeNode]:
        token = self.peek()
        if not token:
            return None
        if token.type == TokenType.NUMBER:
            self.advance()
            return ParseTreeNode("NUMBER", [token.value])
        elif token.type == TokenType.IDENTIFIER:
            self.advance()
            return ParseTreeNode("IDENTIFIER", [token.value])
        elif token.type == TokenType.STRING:
            self.advance()
            return ParseTreeNode("STRING", [token.value])
        elif token.type == TokenType.PAREN_OPEN:
            self.advance()
            expr = self.parse_expression()
            self.match(TokenType.PAREN_CLOSE)
            return expr
        return None
    # Tanınmayan tokenları ayrıştırıcı
    def parse_unknown(self) -> ParseTreeNode:
        token = self.advance()
        return ParseTreeNode(f"UNKNOWN: {token.value}")

# GUI ve vurgulama işlemleri
class CSyntaxHighlighter:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("C Language Syntax Highlighter")
        self.root.geometry("1200x600")

        # Ana çerçeveyi oluştur
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(expand=True, fill=tk.BOTH)

        # Sol: Kod editörü
        self.text = tk.Text(self.main_frame, wrap=tk.WORD, font=("Courier", 12))
        self.text.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

        # Sağ: Söz dizimi ağacı ve token listesi (dikey bölünmüş)
        self.right_panel = ttk.Frame(self.main_frame)
        self.right_panel.pack(side=tk.RIGHT, fill=tk.Y)

        # Söz Dizimi Analizi (Parse tree) başlığı
        self.syntax_label = ttk.Label(self.right_panel, text="Syntax Analysis (Parse Tree)", font=("Arial", 11, "bold"))
        self.syntax_label.pack(side=tk.TOP, anchor="w", padx=4, pady=(4,0))
        # Parse tree gösterimi (üstte)
        self.parse_tree_text = tk.Text(self.right_panel, width=50, height=20, font=("Courier", 10), bg="#f8f8f8")
        self.parse_tree_text.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.parse_tree_text.insert(tk.END, "Parse tree will appear here.")
        self.parse_tree_text.config(state=tk.DISABLED)

        # Lexical Analysis (Token list) başlığı
        self.lexical_label = ttk.Label(self.right_panel, text="Lexical Analysis (Token List)", font=("Arial", 11, "bold"))
        self.lexical_label.pack(side=tk.TOP, anchor="w", padx=4, pady=(8,0))
        # Token listesi gösterimi (altta)
        self.token_list_text = tk.Text(self.right_panel, width=50, height=15, font=("Courier", 10), bg="#f0f0ff")
        self.token_list_text.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        self.token_list_text.insert(tk.END, "Token list will appear here.")
        self.token_list_text.config(state=tk.DISABLED)

        # Durum çubuğu
        self.status_var = tk.StringVar()
        self.status_bar = ttk.Label(self.root, textvariable=self.status_var)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

        # Lexical analyzer (Sözcüksel analizci)
        self.lexer = LexicalAnalyzer()

        # Renk stilleri
        self.style = ttk.Style()
        self.style.configure("Keyword.TText", foreground="blue")
        self.style.configure("Identifier.TText", foreground="black")
        self.style.configure("Operator.TText", foreground="red")
        self.style.configure("Number.TText", foreground="green")
        self.style.configure("String.TText", foreground="orange")
        self.style.configure("Comment.TText", foreground="gray")
        self.style.configure("Preprocessor.TText", foreground="purple")

        # Olayları bağla
        self.text.bind("<KeyRelease>", self.highlight_syntax)

    # Sözdizimi vurgulama ve analiz işlemi
    def highlight_syntax(self, event=None):
        content = self.text.get("1.0", tk.END)
        # Tüm etiketleri kaldır
        for tag in self.text.tag_names():
            self.text.tag_remove(tag, "1.0", tk.END)
        tokens = self.lexer.tokenize(content)
        # Sözdizimi vurgulama uygula
        for token in tokens:
            start = f"{token.line}.{token.column - 1}"
            end = f"{token.line}.{token.column - 1 + len(token.value)}"
            self.text.tag_add(token.type.name, start, end)
            self.text.tag_config(token.type.name, foreground=self.get_color(token.type))
        parser = Parser(tokens)
        is_valid, parse_tree = parser.parse()
        # Durum çubuğunu güncelle
        self.status_var.set("Valid C syntax" if is_valid else "Invalid C syntax")
        # Sağ panelde parse tree göster
        self.parse_tree_text.config(state=tk.NORMAL)
        self.parse_tree_text.delete("1.0", tk.END)
        self.parse_tree_text.insert(tk.END, parse_tree.to_string())
        self.parse_tree_text.config(state=tk.DISABLED)
        # Sağ panelde token listesini göster
        self.token_list_text.config(state=tk.NORMAL)
        self.token_list_text.delete("1.0", tk.END)
        self.token_list_text.insert(tk.END, self.tokens_to_string(tokens))
        self.token_list_text.config(state=tk.DISABLED)

    # Token listesini metne çevir
    def tokens_to_string(self, tokens):
        lines = [f"{'Type':<15} {'Value':<15}"]
        lines.append('-' * 30)
        for t in tokens:
            lines.append(f"{t.type.name:<15} {repr(t.value):<15}")
        return '\n'.join(lines)

    # Token tipine göre renk döndür
    def get_color(self, token_type):
        colors = {
            TokenType.KEYWORD: "blue",
            TokenType.IDENTIFIER: "black",
            TokenType.OPERATOR: "red",
            TokenType.NUMBER: "green",
            TokenType.STRING: "orange",
            TokenType.COMMENT: "gray",
            TokenType.PREPROCESSOR: "purple"
        }
        return colors.get(token_type, "black")

    # GUI'yi başlat
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    highlighter = CSyntaxHighlighter()
    highlighter.run() 