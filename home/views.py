from django.shortcuts import render

# home page view
def homePage(request):
    return render(request, 'home/homePage.html', {})
