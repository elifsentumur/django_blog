from django.shortcuts import render ,get_object_or_404
from blog.models import YazilarModel
import logging

logger = logging.getLogger('konu_Okuma')

def detay(request,slug):
    yazi = get_object_or_404(YazilarModel,slug=slug)
    
    logger.info('konu okundu'+ request.user.username)
    yorumlar = yazi.yorumlar.all()
    context ={
        'yazi':yazi,
        'yorumlar':yorumlar
    }
    return render(request,'pages/detay.html',context=context)
