from django.db import models

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