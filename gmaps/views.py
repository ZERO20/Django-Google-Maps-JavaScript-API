from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.generic.base import TemplateView
# Create your views here.

def Index(request):
	return render_to_response('index.html')
