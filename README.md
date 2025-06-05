# C Dili Gerçek Zamanlı Sözdizimi Vurgulayıcı

C programlama dilinde yazdığınız kodları **anında analiz eden ve renklendiren** modern bir masaüstü uygulama!

## Nedir?
Bu uygulama, C kodunuzu yazarken hem sözcüksel (token) hem de sözdizimsel (parse tree) analizini **gerçek zamanlı** olarak yapar ve kodunuzu renkli şekilde vurgular. Kodun yapısını, anahtar kelimeleri, operatörleri, değişkenleri ve daha fazlasını kolayca görebilirsiniz.

## Kimler İçin?
- C dilini öğrenen öğrenciler
- Kodun yapısını görsel olarak anlamak isteyenler
- Eğitimciler ve sunum hazırlayanlar
- C kodunu hızlıca analiz etmek isteyen herkes

## Temel Özellikler
- **Gerçek zamanlı syntax highlighting** (renkli vurgulama)
- **Parse tree** (sözdizimi ağacı) ile kodun yapısını görselleştirme
- **Token listesi** ile kodun sözcüksel analizini gösterme
- Kullanıcı dostu, sade ve hızlı arayüz
- Ekstra kütüphane gerektirmez (sadece Python ve Tkinter)

## Nasıl Çalışır?
1. Uygulamayı başlatın.
2. Sol panele C kodunuzu yazın veya yapıştırın.
3. Sağda kodun yapısını (parse tree) ve token listesini anında görün.
4. Kodunuzun geçerli olup olmadığını durum çubuğunda takip edin.



---

## 📚 Proje Hakkında
Bu masaüstü uygulaması, C programlama dilinde yazılmış kodları **gerçek zamanlı** olarak analiz eder. Kodunuzu yazarken hem sözcüksel (token) hem de sözdizimsel (parse tree) analizini ve vurgulamasını anında görebilirsiniz.

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
 
