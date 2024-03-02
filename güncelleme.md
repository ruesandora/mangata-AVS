// mevcut avs-operator-setup klasörü içindeki .env dosyasını yedek alın

```
cd avs-operator-setup

docker compose down

git reset --hard

git pull

git checkout tags/v0.2 -b v0.2
```

//yedek aldığın .env dosyasını açıp yeni dosyadaki boşluk olan yerlerde değiştir. Eigende stETH min 1 olacak şekilde stake arttır
  
``` 
docker compose pull

docker compose up -d

docker logs -f avs-finalizer-node
```
