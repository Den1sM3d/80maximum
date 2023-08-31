from django.db import models
from django.contrib import admin
from django.utils import timezone, html

# Create your models here.
class Advertisement(models.Model):
    title = models.CharField("Title", max_length=128)
    description = models.TextField('Description')
    price = models.DecimalField('price', max_digits=12, decimal_places=2)
    auction = models.BooleanField('auction')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Advertisements(id={self.id} title={self.title} price={self.price}"

    class Meta:
        db_table = "advertisements"

    @admin.display(description="Дата созданий")
    def created_date(self):
        print(timezone.now().date())
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime("%H-%M-%S")
            return html.format_html(
                "<span style='color: green; font-weight: bold;' >Сегодня в {}</span>", created_time
            )
        return self.created_at.strftime("%d.%m.%y в %H:%M:%S")
    
    @admin.display(description="Дата обновдений")
    def updated_date(self):
        if self.updated_at.date() == timezone.now().date():
            updated_time = self.updated_at.time().strftime("%H-%M-%S")
            return html.format_html(
                "<span style='color: yellow'; font-weight: bold; '>Сегодня в {}</span>", updated_time
            )
        return self.updated_at.strftime("%d.%m.%y в %H:%M:%S")
