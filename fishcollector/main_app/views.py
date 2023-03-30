from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Fish, Plants
from .forms import FeedingForm

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
    feeding_form = FeedingForm()
    return render(request, 'fish/detail.html' , {
        'fish': fish,'feeding_form': feeding_form
    })

#ADD FEEDING ROUTE
def add_feeding(request, fish_id):
  # create a ModelForm instance using the data in request.POST
  form = FeedingForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_feeding = form.save(commit=False)
    new_feeding.fish_id = fish_id
    new_feeding.save()
  return redirect('detail', fish_id=fish_id)


#CREATE VIEW
class FishCreate(CreateView):
    model = Fish
    fields = ['name','breed', 'color', 'age']
    success_url = '/fish/'

#UPDATE VIEW
class FishUpdate(UpdateView):
    model = Fish
    fields = ['breed', 'color', 'age']
    success_url = '/fish/'

# DELETE VIEW
class FishDelete(DeleteView):
    model = Fish
    success_url = '/fish'

# PLANTS INDEX
def plants_index(request):
    plants = Plants.objects.all()
    return render(request, 'plants/index.html',{
        'plants': plants})

# PLANTS DETAILS
def plants_details(request, plants_id):
    plants = Plants.objects.get(id = plants_id)
    return render (request, 'plants/details.html', {
        'plants': plants
    })

# PLANTS CREATE
class PlantsCreate (CreateView):
    model = Plants
    fields = '__all__'
    success_url = '/plants/'

