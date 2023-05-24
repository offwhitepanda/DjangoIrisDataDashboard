  // Retrieve the data from the context and parse it
  var data = JSON.parse('{{ graph_data_list2|escapejs }}');

  // Use d3.js to generate the chart using the data
  generateChart(data);

  // Function to generate the chart using d3.js
  function generateChart(data) {
      // Set the dimensions of the chart
      var width = 400;
      var height = 300;

      // Create the SVG element
      var svg = d3.select('#chart-container')
          .append('svg')
          .attr('width', width)
          .attr('height', height);

      // Set the scales for the x and y axes
      var xScale = d3.scaleLinear()
          .domain([0, d3.max(data, function(d) { return d.sepal_length; })])
          .range([0, width]);

      var yScale = d3.scaleLinear()
          .domain([0, d3.max(data, function(d) { return d.petal_length; })])
          .range([height, 0]);

      // Create the scatter plot circles
      svg.selectAll('circle')
          .data(data)
          .enter()
          .append('circle')
          .attr('cx', function(d) { return xScale(d.sepal_length); })
          .attr('cy', function(d) { return yScale(d.petal_length); })
          .attr('r', 5)
          .attr('fill', 'steelblue');

      // Add x-axis
      svg.append('g')
          .attr('transform', 'translate(0,' + height + ')')
          .call(d3.axisBottom(xScale));

      // Add y-axis
      svg.append('g')
          .call(d3.axisLeft(yScale));
  }