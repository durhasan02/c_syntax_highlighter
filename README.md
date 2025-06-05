# 🚀 C Dili Gerçek Zamanlı Sözdizimi Vurgulayıcı

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Tkinter](https://img.shields.io/badge/Tkinter-GUI-green)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

> **C kodunuzu anında analiz edin, vurgulayın ve yapısını keşfedin!**

---

## 📚 Proje Hakkında
Bu masaüstü uygulaması, C programlama dilinde yazılmış kodları **gerçek zamanlı** olarak analiz eder. Kodunuzu yazarken hem sözcüksel (token) hem de sözdizimsel (parse tree) analizini ve vurgulamasını anında görebilirsiniz. Eğitim, öğretim ve pratik için idealdir.

---

## 🎯 Özellikler
- **Gerçek Zamanlı Sözdizimi Vurgulama**: Kod yazarken anında renkli vurgulama
- **Sözcüksel Analiz (Tokenization)**: Kodun tokenlara ayrılmış hali
- **Sözdizimi Analizi (Parse Tree)**: Kodun yapısal ağacı
- **Kullanıcı Dostu Arayüz**: Modern ve sade Tkinter GUI
- **Durum Çubuğu**: Kodun geçerli olup olmadığını anında gösterir
- **Akademik Kullanıma Uygun**: Rapor ve sunumlar için ideal
- **Sadece Standart Kütüphaneler**: Ekstra bağımlılık yok

---

## ⚡️ Hızlı Başlangıç
1. **Python 3.x** yüklü olmalı.
2. Proje klasöründe terminal açın ve çalıştırın:
   ```bash
   python c_syntax_highlighter.py
   ```
3. Sol panelde C kodunuzu yazın veya yapıştırın.
4. Sağda hem **parse tree** hem de **token listesi** anında güncellenir.

---

## 🖥️ Ekran Görüntüsü
![Ekran Görüntüsü](docs/screenshot.png)

---

## 💡 Örnek Kod ve Analiz
```c
int main() {
    int a = 5;
    a = a + 10;
    return 0;
}
```

| Token Türü         | Renk      | Açıklama                       |
|--------------------|-----------|--------------------------------|
| Anahtar Kelime     | Mavi      | int, if, return, ...           |
| Tanımlayıcı        | Siyah     | main, a, counter, ...          |
| Operatör           | Kırmızı   | +, -, *, /, =, ==, ...         |
| Sayı               | Yeşil     | 42, 3.14, ...                  |
| String             | Turuncu   | "Merhaba"                      |
| Yorum              | Gri       | // yorum, /* ... */            |
| Ön İşlemci         | Mor       | #include, #define, ...         |

---

## 🛠️ Özelleştirme ve Geliştirme
- **Daha fazla C özelliği** (struct, dizi, fonksiyon çağrısı, pointer) ekleyebilirsiniz.
- **Parse tree**'yi grafiksel olarak gösterebilirsiniz.
- Kod tamamlama, hata öneri sistemi gibi gelişmiş özellikler eklenebilir.

---

## 👩‍💻 Katkı ve İletişim
- Katkıda bulunmak için fork'layın ve pull request gönderin.
- Sorularınız veya önerileriniz için issue açabilirsiniz.
- Akademik kullanımda kaynak gösterebilirsiniz.

---

## 📄 Lisans
MIT Lisansı. Ayrıntılar için `LICENSE` dosyasına bakınız.

---

## 🎓 Akademik Kullanım
Bu proje, üniversite derslerinde, ödevlerde ve sunumlarda kullanılmak üzere tasarlanmıştır. Dökümantasyon ve rapor örnekleri için `PROJE_DOKUMANTASYON.md` dosyasına bakabilirsiniz.

---

## ❓ Sıkça Sorulan Sorular (SSS)

**S: Proje neden sadece standart kütüphaneleri kullanıyor?**  
C: Kolay kurulum ve taşınabilirlik için, ek bağımlılık gerektirmeden çalışır.

**S: Parse tree neden bazı kodlarda UNKNOWN gösteriyor?**  
C: Şu anki parser temel C yapıları için optimize edilmiştir. Daha gelişmiş C özellikleri için parser genişletilebilir.

**S: Renkleri veya arayüzü nasıl değiştirebilirim?**  
C: `c_syntax_highlighter.py` dosyasındaki renk ve stil ayarlarını güncelleyebilirsiniz.

---

**Hazırlayan:** [Adınız Soyadınız]  
**Tarih:** [Tarih]
