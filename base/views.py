from django.shortcuts import render

rooms = [
    {'id': 1, 'name': 'lets learn python'},
    {'id': 2, 'name': 'Design with me'},
    {'id': 3, 'name': 'Frontend developers'}
]


def home(request):
    return render(request, 'base/home.html', {'rooms': rooms})


def room(request):
    return render(request, 'base/room.html')
