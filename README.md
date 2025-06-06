# Gerçek Zamanlı C Dili Sözdizimi Vurgulayıcı

<div align="center">
  <img src="https://img.shields.io/badge/python-3.8+-blue.svg">
  <img src="https://img.shields.io/badge/gui-tkinter-informational">
  <img src="https://img.shields.io/badge/durum-aktif-success">
  <br>
  <strong>Anında sözcüksel ve sözdizimsel analiz, canlı vurgulama — modern, eğitim odaklı masaüstü uygulama</strong>
</div>

---

## 🚀 Genel Bakış

**C Dili Gerçek Zamanlı Sözdizimi Vurgulayıcı**, C kodunu yazarken canlı sözcüksel analiz (tokenizasyon), sözdizimi analizi (parse tree) ve renklendirme (syntax highlighting) özelliklerini bir arada sunan bir masaüstü uygulamadır.  
Kodunuzu yazarken:
- **Hemen renklendirilmiş haliyle** görürsünüz
- **Token listesine** ve
- **Sözdizimi ağacına (parse tree)** anında ulaşabilirsiniz  
Sadece Python standart kütüphaneleri ile geliştirilmiştir. Eğitim, öğretim ve deneme amaçları için idealdir.

---

## ✨ Özellikler

- **Gerçek Zamanlı Geri Bildirim:** Kod yazılırken anında renklendirme, token ve parse tree güncellenir.
- **Eğitsel Parse Tree:** C kodunun hiyerarşik yapısını görsel olarak inceleyin.
- **Modüler Mimari:** Lexer (sözcüksel analiz), parser (sözdizimi analiz) ve arayüz (GUI) tamamen ayrık ve geliştirilebilir.
- **Hata Farkındalığı:** Tanınmayan veya eksik yapılar "UNKNOWN" olarak belirtilir, hata tespiti kolaylaşır.

---

## 🖥️ Ekran Görüntüsü

<p align="center">
  <img src="https://i.imgur.com/B5LtsDG.png" alt="syntax highlighter screenshot" width="600"><br>
  <em>Kod yaz, token ve parse tree anında gör!</em>
</p>

---

## 📦 Kurulum

**Gereksinimler:**  
- Python 3.8 veya üzeri  
- Ekstra kütüphane gerekmez (`tkinter`, `re`, `enum` Python ile birlikte gelir)

```bash
git clone https://github.com/kullanici-adin/c-syntax-highlighter.git
cd c-syntax-highlighter
python c_syntax_highlighter.py
```
Nasıl Çalışır?
Lexer (Sözcüksel Analiz):
C kodunu anahtar kelime, tanımlayıcı, operatör, sayı, string, yorum, ön işlemci ve ayraçlara böler.

Parser (Sözdizimi Analizi):
Recursive descent algoritması ile sadeleştirilmiş C dilinin grammar’ına uygun olarak parse tree oluşturur (fonksiyon, değişken, atama, kontrol yapıları, ifadeler).

Arayüz (GUI / Tkinter):

Sol: Canlı kod editörü

Sağ: Parse tree ve token listesi

Alt: Kodun geçerli olup olmadığını gösteren durum çubuğu
```
int main() {
  int a = 5;
  if (a > 0) {
    a = a + 1;
  }
  return a;
}
```
Sonuçlar anında:

Token listesi: KEYWORD int, IDENTIFIER main, PAREN_OPEN (, ...

Parse Tree: Fonksiyon, değişken tanımı, kontrol yapıları ve daha fazlası görselleştirilir

Renkler:

Token Türü	Renk
Anahtar Kelime	Mavi
Tanımlayıcı	Siyah
Operatör	Kırmızı
Sayı	Yeşil
String	Turuncu
Yorum	Gri
Ön İşlemci	Mor

Proje Dosya Yapısı
```
c_syntax_highlighter.py              # Ana Python uygulaması (tüm mantık ve arayüz)
DOKUMANTASYON.md                     # Teknik ve detaylı Türkçe dokümantasyon
README.md                            # (Bu dosya)

```
Sınırlamalar ve Geliştirme Fikirleri
Sadece temel C yapılarını destekler (fonksiyon, atama, kontrol yapıları, temel ifadeler).

Gelişmiş C özellikleri (struct, pointer, dizi, fonksiyon işaretçisi vb.) için parser’ı genişletebilirsiniz.

Çok büyük kod dosyalarında arayüz yavaşlayabilir (Tkinter kısıtlaması).

Regex tabanlı tokenizer; uç durumlar için ek ince ayar gerekebilir.
📚 Detaylı Teknik Dökümantasyon
Daha fazla detay ve kod içi açıklamalar için:
📄 DOKUMANTASYON.md

