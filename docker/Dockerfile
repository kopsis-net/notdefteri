# Base image
FROM python:3.11-slim

# Çalışma dizinini ayarla
WORKDIR /app

# Ortam değişkenlerini ayarla
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=config.settings.local
ENV SECRET_KEY="django-insecure-your-secret-key-here"
ENV DEBUG=True
ENV ALLOWED_HOSTS=localhost,127.0.0.1,0.0.0.0,192.168.1.121

# Gerekli paketleri yükle
RUN apt-get update && \
    apt-get install -y --no-install-recommends curl && \
    rm -rf /var/lib/apt/lists/*

# Uygulama dosyalarını kopyala
COPY config/ /app/config/
COPY notes/ /app/notes/
COPY templates/ /app/templates/
COPY manage.py /app/
COPY requirements.txt /app/

# Python bağımlılıklarını yükle
RUN pip install --no-cache-dir -r requirements.txt

# Gerekli klasörleri oluştur
RUN mkdir -p staticfiles media db

# Migrationları uygula ve statik dosyaları topla
RUN python manage.py migrate && \
    python manage.py collectstatic --noinput

# Port ayarı
EXPOSE 8000

# Uygulamayı başlat (Django development server)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"] 