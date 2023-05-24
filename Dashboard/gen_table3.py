import io
import base64
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from .models import Observation

def generate_graph_data_table3(model):
    # Fetch the relevant data from the Observation table
    observations = Observation.objects.all()

    # Extract the values from the observations
    sepal_length = [observation.sepal_length for observation in observations]
    sepal_width = [observation.sepal_width for observation in observations]
    species = [observation.species_id for observation in observations]


    # Create a DataFrame from the static data
    data = {'sepal_length': sepal_length, 'sepal_width': sepal_width, 'species': species}
    df = pd.DataFrame(data)

    # Create a FacetGrid using seaborn
    grid = sns.FacetGrid(df, hue="species", height=5)
    grid.map(sns.histplot, "sepal_width", kde=True, stat="density", kde_kws=dict(cut=3), alpha=.4, edgecolor=(1, 1, 1, .4))
    grid.add_legend()

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
