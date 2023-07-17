from django.shortcuts import render

members = [
    {
        'id': '0001',
        'name': 'Richard Hine',
        'email': 'rhine59@gmail.com',
        'date_joined': 'July 15 2023'
    },
    {
        'id': '0002',
        'name': 'Jeanne Hine',
        'email': 'rhine59@gmail.com',
        'date_joined': 'July 15 2023'
    }
]

def home(request):
    context = {
        'members': members
    }
    return render(request, 'members/home.html', context)

def about(request):
    return render(request, 'members/about.html', {'title': 'We have passed a title'})

