// mevcut avs-operator-setup klasörü içindeki .env dosyasını yedek alın

```
cd avs-operator-setup

docker-compose down

git reset --hard

git pull

git checkout tags/v0.2 -b v0.2
```

//yedek aldığın .env dosyasını açıp (`nano .env`) yeni dosyadaki boşluk olan yerleri de değiştir. Eigende stETH min 1 olacak şekilde stake arttır
  
``` 
docker-compose pull

docker-compose up -d

docker logs -f avs-finalizer-node
```


## Readonly hatası alıyorsanız:

```
# operatörü durdur
docker-compose down
```
Docker config dosyasına giriyoruz
```
nano docker-compose.yml
```

Config dosyasının içindeki iki satırın sonunda `:readonly` ibaresini siliyoruz. Sonrası Ctrl + X -> y -> Enter

Operatörü yeniden başlatıyoruz:
```
docker-compose up -d
```