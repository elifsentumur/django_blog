from django.urls import path,include
from blog.views import iletisim ,anasayfa,kategori,yazilarim,detay,iletisim

urlpatterns = [
    path('iletisim/', iletisim,name='iletisim'),
    path('', anasayfa,name='anasayfa'),
    path('kategori/<slug:kategoriSlug>', kategori,name='kategori'),
    path('yazilarim/', yazilarim,name='yazilarim'),
    path('detay/<slug:slug>', detay,name='detay'),
    path('iletisim/', iletisim,name='iletisim'),
]