# C Syntax Highlighter (Gerçek Zamanlı C Sözdizimi Vurgulayıcı)

C diliyle çalışanlar için, **gerçek zamanlı sözdizimi vurgulama** ve **sözcüksel/sentaks analiz** özellikli görsel bir Python uygulaması.

---

## 🚀 Proje Özeti

Bu uygulama, C kodunuzu **anlık olarak**:
- Renkli şekilde vurgular (syntax highlighting)
- Token’lara ayırır (lexical analysis)
- Parse tree (sözdizimi ağacı) gösterir
- Token listesini ayrıntılı şekilde görüntüler
- Kodunuzun C diline uygun olup olmadığını analiz eder

Kullanıcı arayüzü (GUI) ile kodunuzu yazarken anında vurgulanmış ve analiz edilmiş şekilde görebilirsiniz.

---

## 🖥️ Ekran Görüntüsü

> *Kendi ekran görüntünüzü `screenshot.png` adıyla proje köküne ekleyin!*

![C Syntax Highlighter Screenshot](screenshot.png)

---

## 📂 Dosya Yapısı

proje-dizini/
│
├── c_syntax_highlighter.py # Ana uygulama dosyası
├── README.md # Bu belge
└── screenshot.png # (Opsiyonel) Ekran görüntüsü

yaml
Kopyala
Düzenle

---

## ⚙️ Kurulum & Çalıştırma

### Gereksinimler

- Python 3.7+ (Tkinter yüklü olmalı, çoğu Python kurulumunda varsayılan gelir)

### Çalıştırmak için:

```bash
python c_syntax_highlighter.py
GUI Açıldıktan Sonra
Sol panele C kodunuzu yazın veya yapıştırın

Kodunuz anında renklenecek ve sağda Parse Tree ile Token Listesi güncellenecek

Alt kısımdaki durum çubuğundan kodun geçerliliğini (Valid/Invalid) görebilirsiniz

📋 Özellikler
Anlık Sözdizimi Vurgulama:
Anahtar kelimeler, tanımlayıcılar, sabitler, yorumlar, stringler ve daha fazlası farklı renklerde.

Sözcüksel Analiz:
Kodunuzda geçen her token tipi ve değerini listeler.

Sentaks Analizi & Parse Tree:
Kodunuzun yapısını ağaç olarak görselleştirir.

Geçerlilik Kontrolü:
Kodunuzun temel C sözdizimine uyup uymadığını belirtir.

Modern & Temiz Arayüz:
Tkinter tabanlı, kolay kullanımlı arayüz.

✨ Kullanım Örneği
Basit Kod Parçası:
c
Kopyala
Düzenle
int main() {
    int x = 10;
    // Bu bir yorum satırı
    if (x > 5) {
        printf("Merhaba!");
    }
    return 0;
}
Yukarıdaki kodu sol panele yazdığınızda, şunları görürsünüz:

int, return, if gibi anahtar kelimeler mavi

Yorumlar gri

String sabitleri turuncu

Sayılar yeşil

Operatörler kırmızı

Sağda Parse Tree (kodun yapısal analizi) ve Token Listesi (her satırda tip-değer olarak)

🛠️ Koddan Kısa Kesitler
Aşağıda, sözcüksel analiz kısmına örnek bir kod kesiti:

python
Kopyala
Düzenle
self.patterns = [
    (TokenType.COMMENT, r'//.*$|/\*[\s\S]*?\*/'),
    (TokenType.STRING, r'"[^"\\]*(\\.[^"\\]*)*"'),
    (TokenType.NUMBER, r'\b\d+(\.\d+)?\b'),
    ...
]
🤔 Sıkça Sorulan Sorular
S: C derleyicisi mi?

Hayır, bu uygulama kodu çalıştırmaz, sadece vurgulama ve temel analiz yapar.

S: Harici kütüphane gerek var mı?

Hayır, sadece Python’un standart kütüphaneleri (Tkinter, re, enum, vs.) ile çalışır.

S: Windows/Mac/Linux destekli mi?

Evet! Python 3 ve Tkinter kurulu olan her işletim sisteminde çalışır.

💡 Katkı ve Geliştirme
Fork’layın veya projeyi klonlayın.

Geliştirme yapın, isterseniz yeni özellikler ekleyin (ör: C++ desteği, daha gelişmiş parser, temalar, kaydetme/açma vs.)

Pull request gönderebilirsiniz!

📄 Lisans
MIT Lisansı
Detaylar için LICENSE dosyasına bakınız (eklemediyseniz ekleyebilirsiniz).

🧑‍💻 İletişim / Geliştirici
Projeyi geliştiren: [Adınızı veya kullanıcı adınızı yazabilirsiniz]
Sorularınız için Issues kısmını veya e-posta adresinizi paylaşabilirsiniz.
