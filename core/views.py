from django.shortcuts import render
from .models import Contact
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def home(request):
    context={'home':'active'}
    return render(request, 'core/home.html', context)
def contactform(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        area=request.POST.get('area')
        fm = Contact(name=name, email=email, subject=subject, area=area)
        fm.save()
        return HttpResponse('Thanks for Contact')
    else:
        fm=UserCreationForm()
    context={'contact':'active'}
    return render(request, 'core/contact.html', context)
