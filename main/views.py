from django.shortcuts import render

def home_page(request):
    context = {
        'npm' : '2406347424',
        'name': 'Bermulya Anugrah Putra',
        'class': 'PBP D'
    }

    return render(request, 'home.html', context)