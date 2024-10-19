# PDF Karakter Sayacı

Bu Python uygulaması, bir PDF dosyasındaki karakter sayısını hesaplar ve 1 milyon karaktere ulaşıldığında kullanıcıya görsel bir bildirim sunar. Uygulama, kullanıcıya PDF dosyasını seçme imkanı veren basit bir arayüz (GUI) ile çalışır.

## Özellikler

- PDF dosyasını seçme ve işleme
- PDF içindeki karakter sayısını hesaplama
- 1 milyon karakter sınırına ulaşıldığında sayfa numarasını gösterme
- Görsel arayüz (Tkinter kullanılarak)

## Gereksinimler

- Python 3.x
- PyPDF2
- Tkinter (Python ile varsayılan olarak gelir)

## Kurulum

1. Bu projeyi yerel bilgisayarınıza klonlayın:
   ```bash
   git clone https://github.com/kullanici-adi/pdf-karakter-sayaci.git
Gerekli Python kütüphanelerini yükleyin:

bash
Kodu kopyala
pip install PyPDF2
pdf_karakter_say.py dosyasını çalıştırarak programı başlatın:

bash
Kodu kopyala
python pdf_karakter_say.py
Kullanım
Programı çalıştırdığınızda, bir arayüz açılacaktır.
PDF Seç butonuna tıklayın ve işlemek istediğiniz PDF dosyasını seçin.
Program, PDF'deki toplam karakter sayısını hesaplayacak ve 1 milyon karaktere ulaşıldığında, hangi sayfada bu sınırın dolduğunu bildiren bir mesaj kutusu gösterecektir.
Hata Giderme
Eğer bir hata alırsanız, terminaldeki hata mesajını kontrol edin. Çoğu durumda, PDF dosyasının okunamaması veya karakter çıkarma ile ilgili olabilir. PDF dosyasının düzgün bir şekilde dönüştürüldüğünden emin olun.
Katkıda Bulunma
Bu repoyu fork edin.
Yeni bir özellik geliştirin veya hatayı düzeltin.
Pull Request oluşturun.
Lisans
Bu proje MIT Lisansı ile lisanslanmıştır.

