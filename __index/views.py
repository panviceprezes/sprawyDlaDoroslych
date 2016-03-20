from django.http import HttpResponse
from django.template import loader
import os
from pydash.collections import find


def index(request):
	template = loader.get_template('public/index.html')
	context = {
		'imie': 'Artur',
		'nazwisko': 'Slomowski',
		'dataUrodzenia': '1990',
	}
	return HttpResponse(template.render(context, request))

def main(request):
	template = loader.get_template('main/public/index.html')
	context = {
		'imie': 'Artur',
		'nazwisko': 'Slomowski',
		'dataUrodzenia': '1990',
	}
	return HttpResponse(template.render(context, request))

def singleMovie(request, movieID):
	template = loader.get_template('singleMovie/public/index.html')
	context = {
		'movie': getMovieFromDB(int(movieID))
	}
	return HttpResponse(template.render(context, request))

def getMovieFromDB(movieID):
	movies = [
				{	'title' : 'Turbo Horny',
					'ID' : 1
				},
				{
				'title' : 'Last holidays with two sisters',
				'ID' : 2
				},
				{
				'title' : 'My mum seen my when I watching X videos',
				'ID' : 3
				}
			]
			
	return find(movies, {'ID' : movieID})

def saveSingleMovie(request, title):
	print 'xxx'
