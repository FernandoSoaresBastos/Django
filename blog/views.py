

from django.shortcuts import render


def blog(request):
    return render(
        request,
        'blog\index.html'
    )


def exemplo(request):
    print('exemplo')
    return HttpResponse('exemplo do app 1')