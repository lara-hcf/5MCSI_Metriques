<html>
  <head>
    <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
    <script type="text/javascript">
      google.charts.load("current", {packages:["corechart"]});
      google.charts.setOnLoadCallback(drawBackgroundColor);
      function drawBackgroundColor() {
    function drawChart(data) {
    // Convertir les données récupérées en un tableau utilisable par Google Charts
    var dataTable = new google.visualization.DataTable();
    dataTable.addColumn('string', 'Date');
    dataTable.addColumn('number', 'Valeur');
    data.results.forEach(entry => {
      var date = new Date(entry.Jour * 1000);
      dataTable.addRow([date.toLocaleDateString(), entry.temp]);
    });
    // Configurer les options du graphique en ligne
    var options = {
      title: 'Évolution des températures de la ville de Tawarano',
      legend: { position: 'none' }
    };
   var chart = new google.visualization.Histogram(document.getElementById('chart_div'));
        chart.draw(dataTable, options);
  }
  // Récupération de données depuis notre API /tawarano/
  fetch('/tawarano/')
    .then(response => response.json())
    .then(data => {
      drawChart(data);
    })
}
    </script>
  </head>
  <body>
    <div id="chart_div" style="width: 900px; height: 500px;"></div>
  </body>
</html>