from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django import forms
from .models import Advertisement

# class AdvForm(forms.Form):
#     title = forms.CharField(
#         max_length=60,
#         widget=forms.TextInput(attrs={'class':'form-control form-control-lg'})
#     )
#     description = forms.CharField(
#         widget=forms.Textarea(attrs={'class':'form-control form-control-lg'})
#     )
#     price = forms.DecimalField(
#         widget=forms.NumberInput(attrs={'class':'form-control form-control-lg'})
#     )
#     auction = forms.BooleanField(
#         required=False,
#         widget=forms.CheckboxInput(attrs={'class':'form-check-input'})
#     )
#     image = forms.ImageField(
#         required=False,
#         widget=forms.FileInput(attrs={'class':'form-control form-control-lg'})
#     )

class AdvForm(ModelForm):
    class Meta:
        model = Advertisement
        fields = ['title', 'description', 'price', 'auction', 'image']
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control form-control-lg'}),
            'description':forms.Textarea(attrs={'class':'form-control form-control-lg'}),
            'price':forms.NumberInput(attrs={'class':'form-control form-control-lg'}),
            'auction':forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'image':forms.FileInput(attrs={'class':'form-control form-control-lg'}),
        }
    def is_valid_title(self):
        if self.data['title'][0] == '?':
            raise ValidationError(f'{self.data["title"]} <-- There`s a question sign in the title.')

        else:
            return True
