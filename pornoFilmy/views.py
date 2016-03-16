from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('modules/index.html')
    context = {
        'imie': 'Artur',
        'nazwisko': 'Slomowski',
        'dataUrodzenia': '1990',
    }
    return HttpResponse(template.render(context, request))