from django.forms import ModelForm, Textarea, TextInput, FileInput, CheckboxInput, NumberInput, ValidationError
from .models import Advertisement

class AdvertisementForm(ModelForm):
    class Meta:
        model = Advertisement
        fields = ["title", "description", "price", "auction", "image"]
        widgets = {
            'title': TextInput(attrs={'class': 'form-control form-control-lg'}),
            'description': Textarea(attrs={"class": "form-control form-control-lg"}),
            'price': NumberInput(attrs={"class": 'form-control form-control-lg'}),
            'auction': CheckboxInput(attrs={"class": "form-check-input"}),
            'image': FileInput(attrs={"class": "form-control form-control-lg"})
        }
    
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if title and title.startswith("?"):
            raise ValidationError("Нельзя начинать заголовок с '?' знака")
        return title