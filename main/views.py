from django.shortcuts import render
from django import views
from django.views.generic.base import TemplateView

class Home(TemplateView):
	template_name = "main/index.html"
