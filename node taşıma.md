<h1>mangata-avs-node-tasima-</h1>

## 
> cc: [ruesandora](https://github.com/ruesandora/mangata-AVS)

> Kendi node'umu taşırken size yardımcı olması için bir repo yaptım.
Başlayalım.( Önceki kurulumunuz başarılı değilse bu repo sizin için uygun değildir. )

```console
# Öncelikle eski sunucunuza bu komutları uygulayın.
cd avs-operator-setup
docker ps -a
docker stop <containerid> ( tırnakları kaldırıp aldığımız iki adet container id'i ayrı ayrı komut olarak girelim. )

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
ver="1.20.2"
wget "https://golang.org/dl/go$ver.linux-amd64.tar.gz"
sudo rm -rf /usr/local/go
sudo tar -C /usr/local -xzf "go$ver.linux-amd64.tar.gz"
rm "go$ver.linux-amd64.tar.gz"
echo "export PATH=$PATH:/usr/local/go/bin:$HOME/go/bin" >> $HOME/.bash_profile
source $HOME/.bash_profile
go version
```
EigenLayer CLI kurulumu
```console
# eigen klonlayalım
git clone https://github.com/Layr-Labs/eigenlayer-cli.git
cd eigenlayer-cli
mkdir -p build
go build -o build/eigenlayer cmd/eigenlayer/main.go

# Binary dosyamızı PATH yoluna gönderiyoruz
cd
sudo cp eigenlayer-cli/build/eigenlayer /usr/local/bin/
mkdir -p /root/.eigenlayer/operator_keys
```

<h2> Simdi burada önemli bir kısım var. Burayı dikkatli yapalım. </h2>

```console
# keylerimizi yeni sunucumuza import edelim.(parantezler olmadan)
#ecdsa key için aşağıdaki komut.
eigenlayer operator keys import --key-type ecdsa <keyname> <privatekey>

# bls key için aşağıdaki komut.
eigenlayer operator keys import --key-type bls [keyname] [privatekey] 

# bu komut ile keylerimizi kontrol edelim.doğru ise devam.
eigenlayer operator keys list

# keylerimizi taşımış olduk.

```
Operator kaydı
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
# daha önceden register ettiğimiz için tekrar etmemize gerek yok.
# Durumunu kontrol etmek için
eigenlayer operator status operator.yaml

# metadata herhangi bir değişiklik yaptığınızda güncellemek için
eigenlayer operator update operator.yaml
```
Eigen bitti şimdi Mangata AVS
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
ECDSA_KEY_FILE_HOST= eigen cli kurulumda aldığımız ecdsa key yolumuz
BLS_KEY_FILE_HOST= eigen cli kurulumda aldığımız bls key yolumuz

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
# container id başta olur ve kurduğunuz node un isminden hangi id olduğunu anlayabilirsiniz.
```
