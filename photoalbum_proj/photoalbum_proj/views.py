from django.shortcuts import render
from organizer_app.models import Website



def qrc_view(request):
    name = "Welcome to "

    obj = Website.objects.get(id=2)
    context = {
        'name': name,
        'obj': obj,
    }

    return render(request, 'organizer_app\home.html', context)