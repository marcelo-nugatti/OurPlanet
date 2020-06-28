from django.shortcuts import render, redirect

from .forms import *
from .models import *

def index(request):
    earth = 9.807
    marth = 3.711
    
    weight = WeightEarthForm()

    if request.method == 'POST':
        weight = WeightEarthForm(request.POST)
        if weight.is_valid():
            weight.save()
        return redirect('end')
    
    

    context = {'weight':weight}
    return render(request, 'burden/index.html', context)

def weightEnd(request):
    earth = 9.807
    marth = 3.711

    data = WeightEarth.objects.last()
    name = data.name
    weight = data.weight
    
    algorithm = (weight / earth) * marth
    
    context = {'data':data, 'algorithm':algorithm}
    
    return render(request, 'burden/end.html', context)
