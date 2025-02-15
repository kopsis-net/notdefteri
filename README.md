# Kopsis Docker Kurulum Talimatları

## CasaOS Üzerinde Kurulum

1. CasaOS'da "App Store" bölümüne gidin
2. "Docker Compose" seçeneğini seçin
3. Aşağıdaki compose içeriğini yapıştırın:

\```yaml
version: '3.8'
name: kopsis

services:
  web:
    image: ghcr.io/kullaniciadi/kopsis_docker:latest
    container_name: kopsis_web
    restart: unless-stopped
    ports:
      - "8000:8000"
    volumes:
      - kopsis_static:/app/staticfiles
      - kopsis_media:/app/media
    environment:
      - DEBUG=False
      - SECRET_KEY=degistirin-buraya-guvenli-bir-anahtar-yazin
      - ALLOWED_HOSTS=*
      - DJANGO_SETTINGS_MODULE=config.settings.production
      - POSTGRES_DB=kopsis_db
      - POSTGRES_USER=kopsis_user
      - POSTGRES_PASSWORD=kopsis_password
      - DATABASE_URL=postgresql://kopsis_user:kopsis_password@db:5432/kopsis_db
    depends_on:
      - db

  db:
    image: postgres:13
    container_name: kopsis_db
    restart: unless-stopped
    volumes:
      - kopsis_postgres_data:/var/lib/postgresql/data
    environment:
      - POSTGRES_DB=kopsis_db
      - POSTGRES_USER=kopsis_user
      - POSTGRES_PASSWORD=kopsis_password

volumes:
  kopsis_postgres_data:
  kopsis_static:
  kopsis_media:
\```

4. "Deploy" butonuna tıklayın
5. Kurulum tamamlandıktan sonra tarayıcınızdan `http://sunucu-ip:8000` adresine giderek uygulamaya erişebilirsiniz

## Güvenlik Notları

- Varsayılan şifreleri değiştirmeyi unutmayın
- `SECRET_KEY` değerini mutlaka değiştirin
- Gerekirse `ALLOWED_HOSTS` değerini kısıtlayın

## Güncelleme

Yeni bir sürüm çıktığında güncelleme yapmak için:

1. CasaOS'da "My Apps" bölümüne gidin
2. Kopsis uygulamasını bulun
3. "Recreate" butonuna tıklayın

## Yedekleme

Veritabanını yedeklemek için:

1. CasaOS terminal'e girin
2. Aşağıdaki komutu çalıştırın:

\```bash
docker exec kopsis_db pg_dump -U kopsis_user kopsis_db > backup.sql
\```

## Sorun Giderme

Logları kontrol etmek için:

\```bash
docker logs kopsis_web
docker logs kopsis_db
\```

### Sık Karşılaşılan Sorunlar:

1. ALLOWED_HOSTS hatası:
   - `ALLOWED_HOSTS` ayarını kontrol edin
   - Sunucu IP adresini ALLOWED_HOSTS'a ekleyin

2. Veritabanı erişim sorunları:
   - Klasör izinlerini kontrol edin
   - Veritabanı dosyasının varlığını kontrol edin

3. Statik dosya sorunları:
   - Statik dosyaların doğru konumda olduğunu kontrol edin
   - Volume bağlantılarını kontrol edin

## 📝 Lisans

Bu proje MIT lisansı altında lisanslanmıştır.

## 📧 İletişim

- Proje Sahibi: [Mustafa KOPARIR](mailto:your.email@example.com)
- Proje Linki: [GitHub](https://github.com/kopsis-net/notdefteri) 