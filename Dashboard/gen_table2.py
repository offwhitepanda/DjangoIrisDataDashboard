import json
from .models import Observation

def generate_graph_data_table2():
    # Fetch the relevant data from the Observation table
    observations = Observation.objects.all()
    sepal_length = [observation.sepal_length for observation in observations]
    petal_length = [observation.petal_length for observation in observations]

    # Combine the data into a list of objects
    data = [{'sepal_length': sl, 'petal_length': pl} for sl, pl in zip(sepal_length, petal_length)]

    # Prepare the data for d3.js
    data_json = json.dumps(data)

    return data_json
