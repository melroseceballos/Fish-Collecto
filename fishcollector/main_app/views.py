from django.shortcuts import render

# DEFINING FISH DATA HERE
fish = [
    {'name': 'Geraldine', 'type': 'Oranda', 'color': 'Orange/White', 'age': 2},
    {'name': 'Beethoven', 'type': 'Ranchu', 'color': 'Black/White', 'age': 1},
    {'name': 'Mac', 'type': 'Jumbo Ranchu', 'color': 'Orange/White', 'age': 3},
    {'name': 'Dolly', 'type': 'Ranchu', 'color': 'Orange/White/Black', 'age': 1}
]



# Create your views here.

# FOR HOME
def home(request):
    return render (request, 'home.html')

# ABOUT VIEWS
def about(request):
    return render(request, 'about.html')

# INDEX VIES
def fish_index(request):
    return render(request, 'fish/index.html', {
        'fish': fish
    })