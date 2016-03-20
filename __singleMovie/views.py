from django.http import HttpResponse
from django.template import loader
# Create your views here.
def index(request):
	template = loader.get_template('__singleMovie/public/index.html')
	context = {
		'imie': 'Artur',
		'nazwisko': 'Slomowski',
		'dataUrodzenia': '1990',
	}
	return HttpResponse(template.render(context, request))