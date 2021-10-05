from django.contrib import admin
from blog.models import (
    KategoriModel,YazilarModel,YorumModel,IletisimModel
    )

@admin.register(YazilarModel)
class YazilarAdmin(admin.ModelAdmin):
    list_display =('baslik','olusturulma_tarihi','duzenlenme_tarihi')

@admin.register(YorumModel)
class YorumAdmin(admin.ModelAdmin):
    list_display =('yazan','yazi','yorum','olusturulma_tarihi')

@admin.register(IletisimModel)
class IletisimAdmin(admin.ModelAdmin):
    list_display =('email','isim_soyisim','mesaj','olusturulma_tarihi')

admin.site.register(KategoriModel)