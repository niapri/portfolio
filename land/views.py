from django.shortcuts import render

# Create your views here.

def update_list(request):
    return render(request, 'land/landing_page.html')
