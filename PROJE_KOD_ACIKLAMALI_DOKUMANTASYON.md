# C Dili Gerçek Zamanlı Sözdizimi Vurgulayıcı - Kod Açıklamalı Dökümantasyon

---

## 1. Dil ve Gramer Seçimi (Language and Grammar Choice)

### 1.1. Kullanılan Programlama Dili
Bu proje Python programlama dili ile geliştirilmiştir. Python, hızlı prototipleme, güçlü regex desteği ve Tkinter ile kolay GUI geliştirme imkanı sunduğu için tercih edilmiştir.

### 1.2. Seçilen Gramer
Projede, C dilinin temel yapılarını kapsayan, sadeleştirilmiş bir context-free grammar (bağlamdan bağımsız gramer) kullanılmıştır. Bu grammar, fonksiyon tanımı, değişken tanımı, atama, kontrol yapıları ve ifadeleri kapsar.

**Kullanılan Grammar:**
```
program           -> statement_list
statement         -> declaration | function_definition | assignment | if_stmt | while_stmt | for_stmt | expression_stmt
declaration       -> type IDENTIFIER [= expression] ;
function_definition -> type IDENTIFIER ( [params] ) block
expression        -> simple_expression ([comparison_op] simple_expression)*
simple_expression -> term ((+|-) term)*
term              -> factor ((*|/) factor)*
factor            -> NUMBER | IDENTIFIER | STRING | ( expression )
```

**Kodda Yansıması:**
Her grammar kuralı için parser'da bir fonksiyon bulunur. Örneğin, `parse_function_definition`, `parse_declaration`, `parse_assignment` gibi.

---

## 2. Sözdizimi Analiz Süreci (Syntax Analysis Process)

Sözdizimi analizi iki ana aşamadan oluşur:
1. **Sözcüksel Analiz (Lexical Analysis):** Kod, anlamlı en küçük birimlere (token) ayrılır.
2. **Sözdizimi Analizi (Syntax Analysis):** Token dizisi, grammar kurallarına göre bir parse tree'ye dönüştürülür.

**Kodda Akış:**
```python
# highlight_syntax fonksiyonu, kod değiştikçe tetiklenir
def highlight_syntax(self, event=None):
    content = self.text.get("1.0", tk.END)
    # Tokenization
    tokens = self.lexer.tokenize(content)
    # Syntax analysis (parsing)
    parser = Parser(tokens)
    is_valid, parse_tree = parser.parse()
    # Sonuçlar GUI'da gösterilir
```

---

## 3. Sözcüksel Analiz Detayları (Lexical Analysis Details)

### 3.1. Token Türleri ve Regex Desenleri
Kod, aşağıdaki türlerde tokenlara ayrılır:
- Anahtar Kelimeler (KEYWORD)
- Tanımlayıcılar (IDENTIFIER)
- Operatörler (OPERATOR)
- Sayılar (NUMBER)
- Stringler (STRING)
- Yorumlar (COMMENT)
- Ön İşlemci Direktifleri (PREPROCESSOR)
- Ayraçlar (parantez, süslü parantez, noktalı virgül, ...)

**Koddan Örnek:**
```python
self.patterns = [
    (TokenType.COMMENT, r'//.*$|/\*[\s\S]*?\*/'),
    (TokenType.STRING, r'"[^"\\]*(\\.[^"\\]*)*"'),
    (TokenType.NUMBER, r'\b\d+(\.\d+)?\b'),
    (TokenType.KEYWORD, r'\b(' + '|'.join(sorted(self.keywords, key=len, reverse=True)) + r')\b'),
    (TokenType.PREPROCESSOR, r'#\s*[a-zA-Z]+'),
    (TokenType.OPERATOR, r'==|!=|<=|>=|&&|\|\||[+\-*/%=<>!&|^~?:]'),
    (TokenType.SEMICOLON, r';'),
    (TokenType.BRACKET_OPEN, r'\['),
    (TokenType.BRACKET_CLOSE, r'\]'),
    (TokenType.PAREN_OPEN, r'\('),
    (TokenType.PAREN_CLOSE, r'\)'),
    (TokenType.BRACE_OPEN, r'\{'),
    (TokenType.BRACE_CLOSE, r'\}'),
    (TokenType.IDENTIFIER, r'\b[a-zA-Z_][a-zA-Z0-9_]*\b')
]
```

### 3.2. Tokenization Fonksiyonu
```python
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
```

---

## 4. Ayrıştırma Yöntemi (Parsing Methodology)

### 4.1. Recursive Descent (Top-Down) Parser
Her grammar kuralı için ayrı bir fonksiyon yazılmıştır. Parser, token listesini baştan sona dolaşır ve parse tree (sözdizimi ağacı) oluşturur.

**Koddan Örnek:**
```python
def parse(self) -> Tuple[bool, ParseTreeNode]:
    self.parse_tree = ParseTreeNode("Program")
    while self.peek():
        node = self.parse_statement()
        if not node:
            node = self.parse_function_definition()
        if not node:
            node = self.parse_unknown()
        self.parse_tree.children.append(node)
    return True, self.parse_tree
```

### 4.2. Expression Parsing (İfade Ayrıştırma)
Aritmetik ve mantıksal ifadeler, recursive descent ile ayrıştırılır:
```python
def parse_expression(self) -> Optional[ParseTreeNode]:
    left = self.parse_simple_expression()
    token = self.peek()
    if token and token.type == TokenType.OPERATOR and token.value in ['==', '!=', '<', '>', '<=', '>=']:
        op_token = self.advance()
        right = self.parse_simple_expression()
        return ParseTreeNode("EXPRESSION", [left, ParseTreeNode("OPERATOR", [op_token.value]), right])
    return left
```

---

## 5. Vurgulama Şeması (Highlighting Scheme)

Her token türü için bir renk atanır ve Tkinter Text widget'ında ilgili aralık renklendirilir.

**Koddan Örnek:**
```python
self.style.configure("Keyword.TText", foreground="blue")
self.style.configure("Identifier.TText", foreground="black")
self.style.configure("Operator.TText", foreground="red")
self.style.configure("Number.TText", foreground="green")
self.style.configure("String.TText", foreground="orange")
self.style.configure("Comment.TText", foreground="gray")
self.style.configure("Preprocessor.TText", foreground="purple")
```

**Renk Tablosu:**
| Token Türü         | Renk      |
|--------------------|-----------|
| Anahtar Kelime     | Mavi      |
| Tanımlayıcı        | Siyah     |
| Operatör           | Kırmızı   |
| Sayı               | Yeşil     |
| String             | Turuncu   |
| Yorum              | Gri       |
| Ön İşlemci         | Mor       |

---

## 6. GUI Uygulaması (GUI Implementation)

### 6.1. Yapı
- **Tkinter** ile geliştirilmiştir.
- Sol panel: Kod editörü (Text widget)
- Sağ panel: Parse tree ve token listesi (Text widget)
- Durum çubuğu: Kodun geçerli olup olmadığını gösterir.

**Koddan Örnek:**
```python
self.text = tk.Text(self.main_frame, wrap=tk.WORD, font=("Courier", 12))
self.parse_tree_text = tk.Text(self.right_panel, width=50, height=20, font=("Courier", 10), bg="#f8f8f8")
self.token_list_text = tk.Text(self.right_panel, width=50, height=15, font=("Courier", 10), bg="#f0f0ff")
self.text.bind("<KeyRelease>", self.highlight_syntax)
```

### 6.2. Gerçek Zamanlı Güncelleme
Kullanıcı kodu yazdıkça, `highlight_syntax` fonksiyonu tetiklenir ve hem vurgulama hem de analizler anında güncellenir.

**Koddan Örnek:**
```python
def highlight_syntax(self, event=None):
    content = self.text.get("1.0", tk.END)
    # ...
    tokens = self.lexer.tokenize(content)
    # ...
    parser = Parser(tokens)
    is_valid, parse_tree = parser.parse()
    # ...
```

---

## Sonuç
Bu dökümantasyon, projenin her aşamasını hem kavramsal hem de kod düzeyinde detaylıca açıklamaktadır. Kodun her bölümü, ilgili başlık altında örneklerle ve açıklamalarla desteklenmiştir. Proje, C dilinin temel sözdizimi analizini ve vurgulamasını gerçek zamanlı olarak sunan, eğitim ve pratik için ideal bir araçtır. 