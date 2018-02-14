from django.shortcuts import render,HttpResponse

# Create your views here.

def home_view(request):
    #return HttpResponse('<b>Hoşgeldiniz</b>')
    return render(request, 'home.html', {'isim': 'Ergin'})
