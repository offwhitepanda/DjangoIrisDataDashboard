from typing import Any
from django.db.models.query import QuerySet
import matplotlib
import matplotlib.pyplot as plt
import io
import base64
import numpy as np

from django.core.files.base import ContentFile
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from .models import Observation,Species

from .gen_table1 import generate_graph_data_table1
from .gen_table2 import generate_graph_data_table2
from .gen_table3 import generate_graph_data_table3

matplotlib.use('Agg')  # Specify non-GUI backend


class index(generic.ListView):
    template_name = "Dashboard/index.html"
    context_object_name = "observation_list"
    paginate_by = 150

    def get_queryset(self):

        model = index.get_model(self)

        queryset = model.objects.all()
        
        return queryset

    def get_model(self):

        model = None

        if self.request.path == '':
            model = Observation
        elif self.request.path == '/Dashboard/observation/':
            model = Observation
        elif self.request.path == '/Dashboard/species/':
            model = Species
        else:
            model = Observation
        
        return model


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        model = index.get_model(self)
        model_fields = model._meta.get_fields()

        # Generate the graph data for multiple tables
        graph_data_list = []
        graph_data_list2 = []
        graph_data_list3 = []

        # Generate the graph data for Table 1
        graph_data_table1 = generate_graph_data_table1()
        graph_data_list.append(graph_data_table1)

        # Generate the graph data for Table 2
        graph_data_table2 = generate_graph_data_table2()
        graph_data_list2.append(graph_data_table2)

        # Generate the graph data for Table 3
        graph_data_table3 = generate_graph_data_table3(model)
        graph_data_list3.append(graph_data_table3)

        print("Model: " + str(model))
        model_name = str(model).replace('<class \'Dashboard.models.','').replace('\'>','')

        model_field_names = []

        for model_field in model_fields:
            model_field_name = str(model_field).replace(f'Dashboard.{model_name}.','')
            model_field_names.append(model_field_name)
            print(str(model_field_name))

        context['model'] = model
        context['model_fields'] = model_fields
        context['model_field_names'] = model_field_names
        context['graph_data_list'] = graph_data_list
        context['graph_data_list2'] = graph_data_list2
        context['graph_data_list3'] = graph_data_list3

        return context



    
