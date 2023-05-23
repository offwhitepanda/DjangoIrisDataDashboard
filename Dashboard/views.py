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

matplotlib.use('Agg')  # Specify non-GUI backend

def generate_graph_data_table1():
    # Fetch the relevant data from the Observation table
    observations = Observation.objects.all()
    sepal_length = [observation.sepal_length for observation in observations]
    sepal_width = [observation.sepal_width for observation in observations]

    # Create the scatter plot
    plt.scatter(sepal_length, sepal_width)
    plt.xlabel('Sepal Length')
    plt.ylabel('Sepal Width')
    plt.title('Scatter Plot: Sepal Length vs Sepal Width')

    # Save the plot to a BytesIO object
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)

    # Convert the plot to a base64-encoded string
    image_base64 = base64.b64encode(buffer.read()).decode('utf-8')

    # Generate the HTML string
    graph_data = f'<img src="data:image/png;base64,{image_base64}">'

    plt.close()  # Close the figure to release resources

    return graph_data

def generate_graph_data_table2():
    # Fetch the relevant data from the Observation table
    observations = Observation.objects.all()
    sepal_length = [observation.sepal_length for observation in observations]
    petal_length = [observation.petal_length for observation in observations]

    # Perform polynomial regression
    coeffs = np.polyfit(sepal_length, petal_length, deg=1)
    trend_line = np.poly1d(coeffs)

    # Generate data points for the trend line
    x = np.linspace(min(sepal_length), max(sepal_length), num=100)
    y = trend_line(x)

    # Create the line graph with trend line
    plt.plot(sepal_length, petal_length, 'o', label='Data')
    plt.plot(x, y, label='Trend Line')
    plt.xlabel('Sepal Length')
    plt.ylabel('Petal Length')
    plt.title('Line Graph with Trend Line: Sepal Length vs Petal Length')
    plt.legend()

    # Save the graph to a BytesIO object
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)

    # Convert the graph to a base64-encoded string
    image_base64 = base64.b64encode(buffer.read()).decode('utf-8')

    # Generate the HTML string
    graph_data = f'<img src="data:image/png;base64,{image_base64}">'

    plt.close()  # Close the figure to release resources

    return graph_data


class index(generic.ListView):

    template_name = "Dashboard/index.html"
    model = Observation

    context_object_name = "observation_list"
    paginate_by = 150

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Generate the graph data for multiple tables
        graph_data_list = []
        graph_data_list2 = []
        
        # Generate the graph data for Table 1
        graph_data_table1 = generate_graph_data_table1()
        graph_data_list.append(graph_data_table1)

        # Generate the graph data for Table 2
        graph_data_table2 = generate_graph_data_table2()
        graph_data_list2.append(graph_data_table2)

        context['graph_data_list'] = graph_data_list
        context['graph_data_list2'] = graph_data_list2
        return context
    
