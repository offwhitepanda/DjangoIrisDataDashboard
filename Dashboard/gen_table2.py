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