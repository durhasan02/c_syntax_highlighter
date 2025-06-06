# C Dili Gerçek Zamanlı Sözdizimi Vurgulayıcı - Kod Açıklamalı Dökümantasyon

---

## Proje Tanıtımı
Bu proje, C programlama dilinde yazılmış kodların gerçek zamanlı olarak sözcüksel ve sözdizimsel analizini yapan, aynı zamanda sözdizimi vurgulaması (syntax highlighting) sağlayan bir masaüstü uygulamasıdır. Kullanıcı, kodunu yazarken hem tokenlara ayrılmış halini hem de kodun yapısal ağacını (parse tree) anında görebilir. Proje, eğitim, öğretim ve pratik amaçlı olarak geliştirilmiştir.

---

## 1. Dil ve Gramer Seçimi (Language and Grammar Choice)

### 1.1. Kullanılan Programlama Dili
Proje Python ile yazılmıştır. Python, hızlı geliştirme, güçlü regex desteği ve Tkinter ile kolay GUI oluşturma imkanı sunduğu için seçilmiştir. Ayrıca, Python'un okunabilirliği ve geniş topluluğu, eğitim amaçlı projeler için büyük avantaj sağlar.

### 1.2. Seçilen Gramer
Projede, C dilinin temel yapılarını kapsayan, sadeleştirilmiş bir context-free grammar (bağlamdan bağımsız gramer) kullanılmıştır. Bu grammar, fonksiyon tanımı, değişken tanımı, atama, kontrol yapıları ve ifadeleri kapsar. Gelişmiş C özellikleri (struct, pointer, dizi, fonksiyon işaretçisi vb.) kapsam dışıdır.

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
Her grammar kuralı için parser'da bir fonksiyon bulunur. Örneğin, `parse_function_definition`, `parse_declaration`, `parse_assignment` gibi. Bu fonksiyonlar, grammar kurallarının birebir kod karşılığıdır.

---

## 2. Tasarım Kararları (Design Decisions)
- **Kütüphane Seçimi:** Sadece Python standart kütüphaneleri (Tkinter, re, enum) kullanıldı. Ekstra bağımlılık yok.
- **Kullanıcı Deneyimi:** Kodun hem tokenlara ayrılmış hali hem de parse tree'si aynı anda gösteriliyor. Gerçek zamanlı güncelleme ile kullanıcı anında geri bildirim alıyor.
- **Modülerlik:** Lexical analyzer, parser ve GUI ayrı sınıflar olarak tasarlandı. Böylece kodun bakımı ve geliştirilmesi kolaylaştı.
- **Hata Toleransı:** Tanınmayan yapılar parse tree'de "UNKNOWN" olarak gösteriliyor, böylece kullanıcıya kodun hangi kısmının tanınmadığı açıkça belirtiliyor.

---

## 3. Sözdizimi Analiz Süreci (Syntax Analysis Process)

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
    self.parse_tree_text.insert(tk.END, parse_tree.to_string())
    self.token_list_text.insert(tk.END, self.tokens_to_string(tokens))
```

**Pratik Örnek:**
Kullanıcı kodu yazdıkça, her tuş basımında yukarıdaki akış tekrar çalışır ve hem vurgulama hem de analizler anında güncellenir.

---

## 4. Sözcüksel Analiz Detayları (Lexical Analysis Details)

### 4.1. Token Türleri ve Regex Desenleri
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

### 4.2. Tokenization Fonksiyonu
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

**Pratik Örnek:**
Aşağıdaki kodun tokenlara ayrılması:
```c
int main() {
    int a = 5;
    a = a + 10;
    return 0;
}
```
| Token Tipi   | Değer   |
|--------------|---------|
| KEYWORD      | int     |
| IDENTIFIER   | main    |
| PAREN_OPEN   | (       |
| PAREN_CLOSE  | )       |
| BRACE_OPEN   | {       |
| ...          | ...     |

---

## 5. Ayrıştırma Yöntemi (Parsing Methodology)

### 5.1. Recursive Descent (Top-Down) Parser
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

### 5.2. Expression Parsing (İfade Ayrıştırma)
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

**Pratik Örnek:**
Bir atama ifadesi için parse tree:
```
ASSIGNMENT
  a
  OPERATOR
    =
  EXPRESSION
    SIMPLE_EXPRESSION
      IDENTIFIER
        a
      OPERATOR
        +
      NUMBER
        10
```

---

## 6. Vurgulama Şeması (Highlighting Scheme)

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

**Pratik Örnek:**
`int`, `if`, `return` gibi anahtar kelimeler mavi, değişkenler siyah, operatörler kırmızı, sayılar yeşil, stringler turuncu, yorumlar gri, ön işlemciler mor renkte vurgulanır.

---

## 7. GUI Uygulaması (GUI Implementation)

### 7.1. Yapı
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

### 7.2. Gerçek Zamanlı Güncelleme
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

### 7.3. Kullanıcı Deneyimi ve Pratik Akış
- Kod yazılırken anında vurgulama ve analiz
- Parse tree ve token listesi görsel olarak sağda
- Durum çubuğu ile anlık sözdizimi kontrolü
- Hatalı veya tanınmayan yapılar "UNKNOWN" olarak gösterilir

---

## 8. Örnek Akış: Koddan Parse Tree'ye

1. Kullanıcı aşağıdaki kodu yazar:
```c
int main() {
    int a = 5;
    if (a > 0) {
        a = a + 1;
    }
    return a;
}
```
2. Tokenization sonucu:
| Token Tipi   | Değer   |
|--------------|---------|
| KEYWORD      | int     |
| IDENTIFIER   | main    |
| ...          | ...     |

3. Parse tree sonucu (özet):
```
FUNCTION_DEFINITION
  TYPE
    int
  NAME
    main
  BODY
    DECLARATION
      int
      IDENTIFIER
        a
      EXPRESSION
        NUMBER
          5
    IF_STATEMENT
      CONDITION
        EXPRESSION
          IDENTIFIER
            a
          OPERATOR
            >
          NUMBER
            0
      BODY
        ASSIGNMENT
          a
          OPERATOR
            =
          EXPRESSION
            SIMPLE_EXPRESSION
              IDENTIFIER
                a
              OPERATOR
                +
              NUMBER
                1
    RETURN_STATEMENT
      EXPRESSION
        IDENTIFIER
          a
```

---

## 9. Sorun Giderme ve Bilinen Sınırlamalar (Troubleshooting & Known Issues)
- Parser, sadece temel C yapıları için optimize edilmiştir. Gelişmiş C özellikleri (struct, pointer, dizi, fonksiyon işaretçisi vb.) için genişletilmesi gerekir.
- Çok karakterli operatörler (örn. `==`, `!=`, `&&`, `||`) doğru şekilde regex ile yakalanmalıdır.
- Tanınmayan veya eksik yapılar parse tree'de "UNKNOWN" olarak gösterilir.
- GUI, çok büyük dosyalarda yavaşlayabilir (Tkinter'ın doğası gereği).

---

## Sonuç
Bu dökümantasyon, projenin her aşamasını hem kavramsal hem de kod düzeyinde detaylıca açıklamaktadır. Kodun her bölümü, ilgili başlık altında örneklerle ve açıklamalarla desteklenmiştir. Proje, C dilinin temel sözdizimi analizini ve vurgulamasını gerçek zamanlı olarak sunan, eğitim ve pratik için ideal bir araçtır.
