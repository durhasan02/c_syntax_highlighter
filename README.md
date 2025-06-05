# C Syntax Highlighter

<div align="center">
  <img src="https://img.shields.io/badge/python-3.7+-blue.svg" alt="Python 3.7+">
  <img src="https://img.shields.io/badge/Tkinter-GUI-brightgreen.svg" alt="Tkinter GUI">
  <img src="https://img.shields.io/badge/license-MIT-yellow.svg" alt="MIT License">
</div>

> **Modern ve interaktif bir “C Dili Gerçek Zamanlı Sözdizimi Vurgulayıcı ve Analiz Aracı”  
> Python & Tkinter ile, sade ve etkili bir masaüstü deneyimi.**

---

## 🚩 Kısa Tanıtım

**C Syntax Highlighter**:  
C programlama dili için hazırlanmış, gerçek zamanlı vurgulama ve sözdizim analiz aracı.  
Kendi C kodunuzu yazarken hem renklendirme hem de “parse tree” ve “token listesi” anlık gösterilir.

---

## 🎯 Temel Özellikler

- **Gerçek zamanlı sözdizimi vurgulama**: Anahtar kelimeler, tanımlayıcılar, sayılar, stringler, yorumlar ve operatörler otomatik renklenir.
- **Sözcüksel analiz**: Kodun tüm parçaları (token) listelenir.
- **Sentaks analizi**: Kodun yapısı “parse tree” olarak gösterilir.
- **Modern ve anlaşılır arayüz**: Tkinter ile responsive ve kolay kullanılır GUI.
- **Tamamen Python standardı**: Ekstra paket kurulumu gerekmez.

---

## 📸 Ekran Görüntüsü



---

## 📝 Kullanım Senaryosu

1. Uygulamayı başlat:
    ```bash
    python c_syntax_highlighter.py
    ```
2. Açılan pencerede sol tarafa C kodunuzu yazın.
3. Kodunuzu yazdıkça:
    - Kodunuz renklenecek
    - Sağ panelde “Parse Tree” ve “Token Listesi” anında güncellenecek
    - Alt kısımda geçerlilik durumu görünecek


🔬 Nasıl Çalışıyor?
LexicalAnalyzer: Regex kullanarak C kodunu token’lara böler.

Parser: Temel C gramerini analiz eder, parse tree oluşturur.

GUI: Tkinter ile kod editörü + analiz çıktısı paneli.

Kodunuzu yazarken veya yapıştırırken, hem görsel vurgulama hem de yapısal analiz elde edersiniz.
🏗️ Proje Dosya Yapısı
├── c_syntax_highlighter.py   # Tüm kod burada
├──README.md
├──Dökümantasyon

🔥 Özellikleri Kısaca
Renkli kod vurgusu:

int, if, while, return → Mavi

Stringler → Turuncu

Sayılar → Yeşil

Operatörler → Kırmızı

Yorumlar → Gri

Preprocessor → Mor

Parse Tree:
Kodun yapısal analizi hiyerarşik olarak gösterilir.

Token Listesi:
Her satırda; tip ve değer olarak.

Medium Makale:



