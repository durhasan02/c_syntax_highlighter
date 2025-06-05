# C Dili Gerçek Zamanlı Sözdizimi Vurgulayıcı

Bu proje, **C programlama dili** ile yazılmış kodların gerçek zamanlı olarak sözcüksel ve sözdizimsel analizini yapan, aynı zamanda sözdizimi vurgulaması (syntax highlighting) sağlayan bir masaüstü uygulamasıdır.

Kullanıcılar, C kodu yazarken kodun yapısı ve tokenları anında görsel olarak sunulmakta; hem eğitim hem de pratik amaçlı, C dilinin temel özellikleri kolayca anlaşılabilmektedir.

---

## Özellikler

- C dilinin temel sözdizimi kurallarına uygun **sözcüksel ve sözdizimsel analiz**
- En az 5 farklı token türünü **gerçek zamanlı vurgulama**
- **Kullanıcı dostu ve etkileşimli arayüz**
- **Token listesi** ve **sözdizimi ağacı** (parse tree) görsel gösterimi
- Akademik standartlara uygun **belgelenmiş rapor**

---

## Dil ve Gramer

**Neden C Dili?**
- Hem eğitimde hem de endüstride yaygın, açık gramerli, sembolik bir dil olduğu için tercih edilmiştir.

**Kullanılan Basit C Grameri:**
```bnf
program           -> statement_list
statement         -> declaration | function_definition | assignment | if_stmt | while_stmt | for_stmt | expression_stmt
declaration       -> type IDENTIFIER [= expression] ;
function_definition -> type IDENTIFIER ( [params] ) block
expression        -> simple_expression ([comparison_op] simple_expression)*
simple_expression -> term ((+|-) term)*
term              -> factor ((*|/) factor)*
factor            -> NUMBER | IDENTIFIER | STRING | ( expression )
```


Analiz Süreci
Sözcüksel Analiz (Lexical Analysis):
Kod, anlamlı en küçük birimlere (token) ayrılır ve her biri tipine göre sınıflandırılır.

Sözdizimi Analizi (Syntax Analysis):
Tokenlar, gramer kurallarına göre bir sözdizimi ağacına (parse tree) dönüştürülür



| Token Türü     | Renk    | Açıklama                |
| -------------- | ------- | ----------------------- |
| Anahtar Kelime | Mavi    | int, if, return, ...    |
| Tanımlayıcı    | Siyah   | main, a, counter, ...   |
| Operatör       | Kırmızı | +, -, \*, /, =, ==, ... |
| Sayı           | Yeşil   | 42, 3.14, ...           |
| String         | Turuncu | "Merhaba"               |
| Yorum          | Gri     | // yorum, /\* ... \*/   |
| Ön İşlemci     | Mor     | #include, #define, ...  |


Teknik Detaylar

Kullanılan Teknolojiler
Python 3
Tkinter (GUI için)

Arayüz Özellikleri

Kod Editörü: Sol panelde C kodu yazma ve düzenleme

Parse Tree Görselleştirmesi: Sağ üstte anlık olarak gösterim

Token Listesi: Sağ altta tokenların listesi

Durum Çubuğu: Alt kısımda sözdizimi geçerliliği

Gerçek Zamanlı Vurgulama: Kodda her değişiklikte analiz ve vurgulama

Klavye Kısayolları: Temel editör kısayolları desteği


Örnek
c
Kopyala
Düzenle
int main() {
    int a = 5;
    a = a + 10;
    return 0;
}
Token Listesi Tablosu:

Token Tipi	Değer
KEYWORD	int
IDENTIFIER	main
...	...

Örnek Parse Tree (Metinsel):

yaml
Kopyala
Düzenle
Program
  FUNCTION_DEFINITION
    TYPE: int
    NAME: main
    BODY
      DECLARATION: int a = 5
      ASSIGNMENT: a = a + 10
      RETURN_STATEMENT: 0

      

