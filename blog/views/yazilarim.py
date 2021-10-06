from django.core import paginator
from django.shortcuts import render
from blog.models import YazilarModel, yazi
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


@login_required(login_url='/')
def yazilarim(request):
    yazilar = request.user.yazilar.order_by('-id')
    sayfa = request.GET.get('sayfa')
    paginator = Paginator(yazilar,2)
    context ={
        'yazilar':paginator.get_page(sayfa)
    }
    return render(request,'pages/anasayfa.html',context=context)