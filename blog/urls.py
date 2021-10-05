from django.urls import path,include
from blog.views import iletisim ,anasayfa

urlpatterns = [
    path('iletisim/', iletisim,name='iletisim'),
     path('', anasayfa,name='anasayfa'),
]