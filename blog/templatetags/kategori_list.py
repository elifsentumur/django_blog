from django import template
from blog.models import KategoriModel

register = template.Library()

#Burada template de kendi taglarımızı oluşturuyoruz.
@register.simple_tag
def kategori_list():
    kategoriler = KategoriModel.objects.all()
    return kategoriler