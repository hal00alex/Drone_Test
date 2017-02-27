def main ():
    x = 1;
    #get SQL Variables here 
    f1 = "3"; 
    html_str1 =  """
<html>
<head>
  <meta charset="UTF-8">
  <title>Line Chart Test</title>
  <h1> Drone Dis-Play Height and Velocity </h1>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/1.0.2/Chart.min.js"></script>

  
  <script language="JavaScript">
  function displayLineChart() {
    var data = {
        labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        datasets: [{label: "Prime and Fibonacci",fillColor: "rgba(220,220,220,0.2)",strokeColor: "rgba(220,220,220,1)",
                pointColor: "rgba(220,220,220,1)",
                pointStrokeColor: "#fff",
                pointHighlightFill: "#fff",
                pointHighlightStroke: "rgba(220,220,220,1)",
                """
    #change array to be 5 SQL varaibles and change labels to be time
    html_str2 = "data: [" + f1 + ",3, 5, 7, 11, 13, 17, 19, 23, 29]}," 
    html_str3 = """
            {
                label: "My Second dataset",
                fillColor: "rgba(151,187,205,0.2)",
                strokeColor: "rgba(151,187,205,1)",
                pointColor: "rgba(151,187,205,1)",
                pointStrokeColor: "#fff",
                pointHighlightFill: "#fff",
                pointHighlightStroke: "rgba(151,187,205,1)",
                data: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
            }
        ]
    };
    var ctx = document.getElementById("lineChart").getContext("2d");
    var options = { };
    var lineChart = new Chart(ctx).Line(data, options);
  }
  </script>
</head>
<body onload="displayLineChart();">
 
  <div class="box">
    <canvas id="lineChart" height="450" width="800"></canvas>
  </div>
</body>
</html>
"""
    print ("Hello")
    Html_file = open("graphpy.html", "w")
    Html_file.write(html_str1)
    Html_file.write(html_str2)
    Html_file.write(html_str3)
    Html_file.close()
main() 
