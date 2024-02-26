# Mangata-AVS Operatörü Otomatik Yeniden Başlatma

Bu komut dosyası, Mangata operatörü "err: connection is shut down" hatasını verdiğinde konteyneri yeniden başlatır. Bu komut dosyası kendi sunucumda çalışmaktadır ve herhangi bir sorun olmamıştır. Komut dosyasını çalıştırmadan önce varsayılan konteyner adını değiştirdiyseniz `container_name` değişkenini kontrol edin (konteyner adını kontrol etmek için `docker ps` kullanın).

**Not:**

* Bu komut dosyası, kullanıcının docker kullanıcı grubuna eklenmesini gerektirir.
* Gerekli izinlere sahip değilseniz komut dosyası başarısız olabilir.

## Kurulum
```bash
## Repoyu klonlama
git clone https://github.com/walter-s0bch4k/mangata-AVS-with-auto-restart.git
# İndirilen repoda doğru klasöre gidin
cd mangata-AVS-with-auto-restart/auto-restart
# Eğer repoyu farklı bir adresten indirdiyseniz, lütfen indirdiğiniz adresin dosya isimlerini kontrol ederek
# İçerisinde `requirements.txt` ve `restart_container_if_err.py` dosyaları olan klasöre gidin.
# Doğru yerde olduğunuzu kontrol etmek için
ls -al
# Komutunun çıktısında `requirements.txt` ve `restart_container_if_err.py` dosyalarını görmelisiniz.

## pip Kurulumu
# pip kurulum komut dosyasını indirin
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
# Komut dosyasını çalıştırın, python3'ü python ile değiştirmeniz gerekebilir
sudo python3 get-pip.py

## Docker Ayarları
# docker kullanıcı grubu oluşturun
sudo groupadd docker
# Mevcut kullanıcıyı docker grubuna ekleyin
sudo usermod -aG docker $USER
# Bu adımdan sonra hesabınızdan çıkıp tekrar giriş yapmanız gerekmektedir.
# Uzak bağlantı kullanıyorsanız bağlantıyı kapatıp tekrar bağlanmayı deneyebilirsiniz.

## Komut Dosyasını Çalıştırma
# Gerekli paketleri kurun
pip install -r requirements.txt
# Arka planda çalışması için nohup kullanın, bağlantınız kesilse bile çalışmaya devam eder
nohup python3 -u restart_container_if_err.py > logs.txt &
# Logları kontrol edin. İçeriği dikkatlice okuyun, hata olmamalıdır. 
cat logs.txt

## !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
## Konteyneri manuel olarak yeniden başlattıysanız veya kapattıysanız işlemi sonlandırın!
# PID'yi alın
ps -aux | grep restart_container_if_err.py
# Ardından işlemi sonlandırın
kill -9 <PID>
```