from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from .models import Observation,Species

class index(generic.ListView):
    template_name = "Dashboard/index.html"
    model = Observation

    def get_queryset(self):
        """
        Return the first 10 rows of the observation table
        """
        return Observation.objects.all()[:5]
    
