from django.db import models
from django.utils import timezone

class Note(models.Model):
    title = models.CharField(max_length=200, verbose_name="Başlık")
    content = models.TextField(verbose_name="İçerik")
    created_date = models.DateTimeField(default=timezone.now, verbose_name="Oluşturulma Tarihi")
    updated_date = models.DateTimeField(auto_now=True, verbose_name="Güncellenme Tarihi")

    class Meta:
        verbose_name = "Not"
        verbose_name_plural = "Notlar"
        ordering = ['-created_date']

    def __str__(self):
        return self.title 