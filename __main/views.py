from django.template import loader
from django.http import HttpResponse

# Create your views here.
def index(request):
	template = loader.get_template('__main/public/index.html')
	context = {
		'imie': 'Artur',
		'nazwisko': 'Slomowski',
		'dataUrodzenia': '1990',
	}
	return HttpResponse(template.render(context, request))