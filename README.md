# C Dili Gerçek Zamanlı Sözdizimi Vurgulayıcı

![Ekran Görüntüsü](docs/screenshot.png)

## Proje Hakkında
Bu proje, C programlama dilinde yazılmış kodların gerçek zamanlı olarak sözcüksel ve sözdizimsel analizini yapan, aynı zamanda sözdizimi vurgulaması (syntax highlighting) sağlayan bir masaüstü uygulamasıdır. Kodun hem tokenlara ayrılmış hali hem de sözdizimi ağacı (parse tree) kullanıcıya görsel olarak sunulur.

## Özellikler
- C dili için gerçek zamanlı syntax highlighting
- En az 5 farklı token türü (anahtar kelime, tanımlayıcı, operatör, sayı, string, yorum, ön işlemci)
- Parse tree (sözdizimi ağacı) görsel olarak gösterimi
- Token listesi (lexical analysis sonucu) gösterimi
- Kullanıcı dostu, modern ve etkileşimli arayüz (Tkinter)
- Kodun geçerli olup olmadığını gösteren durum çubuğu

## Kurulum
1. Python 3.x yüklü olmalıdır.
2. Gerekli kütüphaneler (yalnızca standart kütüphaneler kullanılmıştır):
   - `tkinter`
   - `re`
   - `enum`

## Kullanım
1. Proje klasöründe `c_syntax_highlighter.py` dosyasını çalıştırın:
   ```bash
   python c_syntax_highlighter.py
   ```
2. Sol panelde C kodunuzu yazın veya yapıştırın.
3. Sağ panelde kodun sözdizimi ağacını ve token listesini anında görebilirsiniz.

## Ekran Görüntüsü
Aşağıda uygulamanın örnek bir ekran görüntüsü yer almaktadır:

![Ekran Görüntüsü](docs/screenshot.png)

## Lisans
Bu proje MIT lisansı ile lisanslanmıştır. Ayrıntılar için `LICENSE` dosyasına bakınız.

## Katkı ve İletişim
Katkıda bulunmak veya öneri/geri bildirim iletmek için lütfen bir issue açın veya pull request gönderin.

---
**Hazırlayan:** [Adınız Soyadınız]  
**Tarih:** [Tarih] 