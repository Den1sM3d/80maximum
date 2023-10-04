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
            title = self.cleaned_data['title']
            if Advertisement.objects.filter(title.startswith("?")).exists():
                raise ValidationError('Название нельзя начинать с ? знана ')
            return title

form = AdvertisementForm()

advertisement = Advertisement.objects.get(pk=1)
form = AdvertisementForm(instance=advertisement)