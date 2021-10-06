from django.shortcuts import render,redirect
from django.http import HttpResponse
from blog.forms import IletisimForm
from blog.models import IletisimModel

def iletisim(request):
    form  = IletisimForm()
    if request.method == 'POST':
        form = IletisimForm(request.POST)
        if form.is_valid():
            iletisim = IletisimModel()
            iletisim.email = form.cleaned_data['email']
            iletisim.isim_soyisim = form.cleaned_data['isim_soyisim']
            iletisim.mesaj = form.cleaned_data['mesaj']
            print('valid')
            return redirect('anasayfa')
        else:
            print('no valid')
    return render(request,'pages/iletisim.html', {'form': form})