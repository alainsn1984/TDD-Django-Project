from django.shortcuts import render
from .models import Solo
# Create your views here.

def index(request):
    context = {'solos': Solo.objects.filter(
        instrument=request.GET.get('instrument', None ))
    }
    return render(request,template_name='solos/index.html', context=context)