
function generateChart(data) {

    data = JSON.parse(data)
    
    var sepalLengths = data.map(obj => obj.sepal_length);
    var petalLengths = data.map(obj => obj.petal_length);
  
    var ctx = document.getElementById('myChart').getContext('2d');
    var chart = new Chart(ctx, {
      type: 'line',
      data: {
        labels: Array.from(Array(data.length).keys()), // Use index as labels
        datasets: [{
          label: 'Sepal Length',
          data: sepalLengths,
          borderColor: 'red',
          fill: false
        }, {
          label: 'Petal Length',
          data: petalLengths,
          borderColor: 'blue',
          fill: false
        }]
      },
      options: {
        responsive: true,
        scales: {
          x: {
            display: true,
            title: {
              display: true,
              text: 'Index'
            }
          },
          y: {
            display: true,
            title: {
              display: true,
              text: 'Length'
            }
          }
        }
      }
    });
  }