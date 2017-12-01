from django.shortcuts import render
from django.utils import timezone
from .models import Update 

# Create your views here.

def update_list(request):
    updates = Update.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'land/landing_page.html', {'updates':updates})
