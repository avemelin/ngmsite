from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Artiles
from .forms import ArtilesForm

def index(request):
    return render(request, 'main/layout.html')

def about(request):
    base = Artiles.objects.order_by('name')
    return render(request, 'main/index.html', {'base': base})

def create(request):
    error = ''
    if request.method == 'POST':
        form = ArtilesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('about')
        else:
            error = 'Форма была неверной'

    form = ArtilesForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'main/form.html', data)

