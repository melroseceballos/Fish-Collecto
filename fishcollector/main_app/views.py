from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Fish

# Create your views here.

# FOR HOME
def home(request):
    return render (request, 'home.html')

# ABOUT VIEWS
def about(request):
    return render(request, 'about.html')

# INDEX VIES
def fish_index(request):
    fish = Fish.objects.all()
    return render(request, 'fish/index.html', {
        'fish': fish
    })
# SHOW VIEWS
def fish_detail(request, fish_id):
    fish = Fish.objects.get(id=fish_id)
    return render(request, 'fish/detail.html' , {
        'fish': fish
    })

#CREATE VIEW
class FishCreate(CreateView):
    model = Fish
    fields = ['name','breed', 'color', 'age']

#UPDATE VIEW
class FishUpdate(UpdateView):
    model = Fish
    fields = ['breed', 'color', 'age']

# DELETE VIEW
class FishDelete(DeleteView):
    model = Fish
    success_url = '/fish'