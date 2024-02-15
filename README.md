<h1 align="center"> Mangata X - AVS </h1>


## Notlar:

> Selamlar, bir süredir mangata çalıştırıyorum lakin 30 kişi ile sınırlıydı ve artık sınır kalktı.

> Neden Mangata kuruyor Eigen AVS ekosistemine önem veriyorum [buradan](https://x.com/Ruesandora0/status/1754194993592275362?s=20) okuyabilirsiniz.

> Testnet ne kadar sürürecek bilinmiyor, rewards var evet - KYC olabilir.

> Ayrıca Mangatanın bir tokeni mevcut, yatırımcıları oldukça iyi ileride daha iyi hale gelecek bir protokol ve testnet önemli.

> Ricamdır notları ve satır aralarını okumanızda, bu repoyu paylaştıktan sonra uçakta olacağım her şeyi yazıyorum size.

> Son olarak, hocam şu node ile bu node yan yana olur mu diye sormayın [buraya](https://x.com/Ruesandora0/status/1744023547805061515?s=20) bakın arkadaşlar <3

> Topluluk kanalları: [Sohbet Kanalımız](https://t.me/RuesChat) - [Duyurular ve Gelişmeler](https://t.me/RuesAnnouncement) - [Whatsapp](https://whatsapp.com/channel/0029VaBcj7V1dAw1H2KhMk34) - [Mangata Discord](https://discord.gg/mangata)

#

<h1 align="center"> Donanım </h1>

> Görseldekine benzer bir cihaz yeterli, bunun için [Hetzner](https://github.com/ruesandora/Hetzner) kullanıyorum

<img width="782" alt="Ekran Resmi 2024-02-07 13 45 17" src="https://github.com/ruesandora/mangata-AVS/assets/101149671/9c040e48-ca4b-44e2-a777-3a31b6cee06d">

<h1 align="center"> Kurulum </h1>

```console
# Güncelleme ve docker kurulumu, komutları sırasıyla girebilirsiniz
sudo apt update -y && sudo apt upgrade -y
for pkg in docker.io docker-doc docker-compose podman-docker containerd runc; do sudo apt-get remove $pkg; done

sudo apt-get update
sudo apt-get install ca-certificates curl gnupg
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg

# bu komut satırını toplu girebilirsiniz
echo \
  "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# docker güncelleme ve run
sudo apt update -y && sudo apt upgrade -y
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
sudo docker run hello-world

# Go kurulumu
cd $HOME
ver="1.21.0"
wget "https://golang.org/dl/go$ver.linux-amd64.tar.gz"
sudo rm -rf /usr/local/go
sudo tar -C /usr/local -xzf "go$ver.linux-amd64.tar.gz"
rm "go$ver.linux-amd64.tar.gz"
echo "export PATH=$PATH:/usr/local/go/bin:$HOME/go/bin" >> $HOME/.bash_profile
source $HOME/.bash_profile
go version
```

<h1 align="center"> EigenLayer CLI kurulumu </h1>

```console
# eigen klonlayalım
git clone https://github.com/Layr-Labs/eigenlayer-cli.git
cd eigenlayer-cli
mkdir -p build
go build -o build/eigenlayer cmd/eigenlayer/main.go

# Binary dosyamızı PATH yoluna gönderiyoruz
cd
sudo cp eigenlayer-cli/build/eigenlayer /usr/local/bin/
```

> Altta ki komutlar ile KEY oluşturuyoruz..

> `ecdsa` KEY bize bir `evm` adresi, `private key` ve dosya `path` (yolu) verecek

> `bls` KEY ise bir `private key` verecek. Hepsini kaydedin.

> Kapalı parantez dahil, `<key-ismi>` değiştirin, <> parantezleri kaldırın..

> Her komuttan sonra şifre oluşturmanızı isteyecek, şifre karmaşık olmalı.

> Örnek şifre DenemeSifre123.,#%

```
eigenlayer operator keys create --key-type ecdsa <key-ismi>
eigenlayer operator keys create --key-type bls <key-ismi>
```

> Listeleyerek keyleri ve dosya yollarını kontrol edin

```
eigenlayer operator keys list
```

>  Örnek ecdsa key create çıktısı

![image](https://github.com/ruesandora/mangata-AVS/assets/101149671/e72d6567-013a-492f-a6e0-1d610a286a45)


<h1 align="center"> Operator kaydı </h1>

```console
# Bu komutun istediği verileri giriyoruz, veriler aşağıda yazdım.
eigenlayer operator config create
```

> Sırasıyla bunlarıda yazıyorum kolaylık için, en aşağıda görselide olcak:

> y diyoruz

> operator adresi olarak, `ecdsa key` oluşturduğumuzda verdiği `evm` adresini girin.

> earning operator adres yine aynı ecdsa-evm adresi girin, yukarıdaki ile aynı.

> goerli eth RPC isteyecek, [infuradan](https://app.infura.io/) aldım ben ücretsiz goerli RPC

> `ecdsa key` oluşturduğumuzda bize verdiği key pathi tam şekilde giriyoruz

> aynı şekilde `bls key` path giriyoruz - path ne olduğunu bilmeyenler için görsele bakabilir

> goerli seçiyoruz ve bitiyor. 

> Bu bize operator.yaml ve metadata.json dosyalarını oluşturacak..

![image](https://github.com/ruesandora/mangata-AVS/assets/101149671/28554c5b-873d-4296-8e1b-8cda670c8e6f)

#

### peki metadata'da işlemlerimiz biraz farklı hemen anlatıyorum:

> `nano metadata.json` komutu ile içeriği kopyalıyoruz.

> metadata.json içeriğini kendinize göre düzenleyeceksiniz ve public erişilebilir bir yere upload edeceksiniz.

> Bunun için githubda bir repo oluşturup metadata.json içeriğinizi oraya yazın ve raw linkini kenarda tutabilirsiniz. Hem metadata.json içinde düzenleyeceksiniz hem de github reponuzda.

> Aşağıya görsel bırakıyorum:

![image](https://github.com/ruesandora/mangata-AVS/assets/101149671/e44e223f-b94a-43c8-9fc0-b909fc8f1564)

#

### raw'ı hallettiysek kaydımıza devam edelim


```console
# Operator.yaml dosyasını nano ile açıyoruz
nano operator.yaml
```

> Burada yine değişiklik yapacağız

> `metadata_url` için `metadata.json` dosyamızın public `raw linki`

> `el_slasher_address` için: 0x3865B5F5297f86c5295c7f818BAD1fA5286b8Be6

> `bls_public_key_compendium_address` için: 0xc81d3963087Fe09316cd1E032457989C7aC91b19

> ctrl + x + y ile kaydedip çıkıyoruz.

![image](https://github.com/ruesandora/mangata-AVS/assets/101149671/e61df955-89ac-4f31-8318-46c013d78817)

```console
# operatoru kaydetmeden önce yukarıda aldığınız EVM cüzdanınıza biraz goerli ETH gönderin
# Operatörü kaydediyoruz
eigenlayer operator register operator.yaml
# Loglar aksın başarılı bir şekilde sonlanana kadar müsade edin

# Durumunu kontrol etmek için
eigenlayer operator status operator.yaml

# metadata herhangi bir değişiklik yaptığınızda güncellemek için
eigenlayer operator update operator.yaml
```

<h1 align="center"> Eigen bitti şimdi Mangata AVS </h1>

> reth temini için [buradan](https://app.uniswap.org/swap??outputCurrency=0x178e141a0e3b34152f73ff610437a7bf9b83267a) swap

> steth temini için [buradan](https://app.uniswap.org/swap??outputCurrency=0x1643e812ae58766192cf7d2cf9567df2c37e9b7f
) swap 

>  Elimizdeki reth ve steth stake etmemiz gerekiyor. 

> Elinizdeki `ecsda private keyi` Metamaska `import` edin ve swap ile temin ettiğiniz tokenleri bu cüzdana gönderin.

> Sonrasında [buradan](https://goerli.eigenlayer.xyz/) cüzdanı bağlıyoruz ve bu iki poola stake ediyoruz.

![image](https://github.com/ruesandora/mangata-AVS/assets/101149671/9eeea1ad-ee92-42b9-b56d-5ed7fe32c632)


>  Txler onaylandıktan sonra terminalimize dönüyoruz ve AVS operatörümüzü kuruluma geçiyoruz

```console
git clone https://github.com/mangata-finance/avs-operator-setup.git
cd avs-operator-setup
chmod +x run.sh
nano .env
```

![image](https://github.com/ruesandora/mangata-AVS/assets/101149671/009b304b-23ed-4045-b23f-b0593ce76f89)

```console
# Üst kısma dokunmuyorsunuz. SADECE: TODO yazan satırın altı bizi ilgilendiriyor.
ETH_RPC_URL= goerli eth rpc http linki
ETH_WS_URL= goerli eth wss linki
# bu linkleri infuradan almıştık, zorlanırsan rues chatten yardım talep edin.

# key yolundan kastım path, yukarıda öğrenmiştiniz.
ECDSA_KEY_FILE_HOST=/.eigenlayer/operator_keys/<key-name>.ecdsa.key.json
BLS_KEY_FILE_HOST=/.eigenlayer/operator_keys/<key-name>.bls.key.json

# yukarıda bir şifre belirlemiştik her yerde kullandığımız.
ECDSA_KEY_PASSWORD= eigen cli kurulumda belirlediğimiz karmaşık key şifresi
BLS_KEY_PASSWORD= eigen cli kurulumda belirlediğimiz karmaşık key şifresi

# ctrl + x + y yapıp kaydedip çıkıyoruz

# şimdi opt-in yapalım son hamleler..
./run.sh opt-in

# key yolunda, şifrede vs hata yoksa bu adımlardan sonra docker compose up yapıyoruz ve sona geliyoruz.
docker compose up -d

# bir sorun olup olmadığını kontrol etmek için docker ps ile container id alın
docker logs -f <container_id>
# container id başta olur ve kurduğunuz node'un isminden hangi id olduğunu anlayabilirsiniz.
```

> Loglarınızı Mangata AVS kanalına atıp rolünüzüde alabilirsiniz.

> işlemler bu kadardı, sırf sorun var mı diye tekrar test edip kurdum sorun yok çünkü bu repoyu eskiden yazdım.

> İlla ki eksiğim vardır, PR atarsınız veya ben commitlerim, ben yolculuktayken siz öğrenmeye bakın bir şeyler.
