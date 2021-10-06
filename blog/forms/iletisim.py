from django import forms
from blog.models import IletisimModel


class IletisimForm(forms.Form):
    email = forms.EmailField(max_length=20)
    isim_soyisim = forms.CharField(max_length=15)
    mesaj = forms.CharField(widget=forms.Textarea)

    # class Meta:
    #     model = IletisimModel
    #     fields = ('email', 'isim_soyisim','mesaj',)
