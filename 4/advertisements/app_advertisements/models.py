from django.db import models
from django.contrib import admin
from django.utils import timezone, html
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Advertisement(models.Model):
    title = models.CharField("Title", max_length=128)
    description = models.TextField('Description')
    price = models.DecimalField('price', max_digits=12, decimal_places=2)
    auction = models.BooleanField('auction')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name="Пользователь")
    image = models.ImageField(verbose_name="image", upload_to="advertisements/")
    
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
    
    @admin.display(description="Маленькая картинка")
    def small_image(self):
        return html.format_html("<img src='{}' alt='Нет изображения' style='width: 50px; height: 50px'>", self.image.url)
