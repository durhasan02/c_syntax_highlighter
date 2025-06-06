# C Dili Gerçek Zamanlı Sözdizimi Vurgulayıcı

C programlama dilinde yazdığınız kodları **anında analiz eden ve renklendiren** modern bir masaüstü uygulama!

## Proje Özeti
Bu uygulama, C kodunuzu yazarken hem sözcüksel (token) hem de sözdizimsel (parse tree) analizini **gerçek zamanlı** olarak yapar ve kodunuzu renkli şekilde vurgular. Kodun yapısını, anahtar kelimeleri, operatörleri, değişkenleri ve daha fazlasını kolayca görebilirsiniz.

## Temel Özellikler
- Gerçek zamanlı syntax highlighting (renkli vurgulama)
- Parse tree (sözdizimi ağacı) ile kodun yapısını görselleştirme
- Token listesi ile kodun sözcüksel analizini gösterme
- Kullanıcı dostu, sade ve hızlı arayüz
- Ekstra kütüphane gerektirmez (sadece Python ve Tkinter)

## Hızlı Başlangıç
1. Python 3.x yüklü olmalı.
2. Proje klasöründe terminal açın ve çalıştırın:
   ```bash
   python c_syntax_highlighter.py
   ```
3. Sol panele C kodunuzu yazın veya yapıştırın.
4. Sağda kodun yapısını (parse tree) ve token listesini anında görün.

## Örnek Kod
```c
int main() {
    int a = 5;
    a = a + 10;
    return 0;
}
```

## Vurgulama Renk Tablosu
| Token Türü         | Renk      |
|--------------------|-----------|
| Anahtar Kelime     | Mavi      |
| Tanımlayıcı        | Siyah     |
| Operatör           | Kırmızı   |
| Sayı               | Yeşil     |
| String             | Turuncu   |
| Yorum              | Gri       |
| Ön İşlemci         | Mor       |

## Katkı ve İletişim
Katkıda bulunmak veya öneri/geri bildirim iletmek için lütfen bir issue açın veya pull request gönderin.

---
**Hazırlayan:** [Adınız Soyadınız]  
**Tarih:** [Tarih]

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