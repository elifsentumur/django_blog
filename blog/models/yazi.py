from typing import Text
from django.db import models
from autoslug import AutoSlugField
from blog.models import KategoriModel, kategori
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from blog.abstract_models import DateAbstractModel
class YazilarModel(DateAbstractModel):
    resim = models.ImageField(upload_to= 'yazı_resimleri')
    baslik = models.CharField(max_length=50)
    icerik = RichTextField()
    slug = AutoSlugField(populate_from = 'baslik', unique=True)
    kategoriler = models.ManyToManyField(KategoriModel,related_name='yazi')
    yazar = models.ForeignKey('account.CustomUserModel', related_name='yazilar'  ,on_delete=models.CASCADE)
    duzenlenme_tarihi = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = 'Yazi'
        verbose_name_plural ='Yazilar'
        db_table= 'Yazi'

        
    def __str__(self):
        return self.baslik