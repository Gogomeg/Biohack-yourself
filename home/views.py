from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


class Index(TemplateView):
    template_name = 'home/index.html'
