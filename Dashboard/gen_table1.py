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