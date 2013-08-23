#-*- coding: utf-8 -*-
from django.shortcuts import render

def homepage(request):
	"""
	VIEW
	displays the homepage
	template used: index.html
	"""
	return render(request, 'index.html')
