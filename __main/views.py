from django.shortcuts import render

# Create your views here.
def index(request):
	template = loader.get_template('public/index.html')
	context = {
		'imie': 'Artur',
		'nazwisko': 'Slomowski',
		'dataUrodzenia': '1990',
	}
	return HttpResponse(template.render(context, request))