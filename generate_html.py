import csv
from datetime import datetime

# Read data from CSV
csv_file_path = "weather_data.csv"
timestamps = []
temperatures = []

with open(csv_file_path, "r") as csvfile:
    csv_reader = csv.reader(csvfile)
    # next(csv_reader)

    for row in csv_reader:
        timestamp = row[0]
        temperature = float(row[1])

        timestamps.append(timestamp)
        temperatures.append(temperature)

timestamps_ms = [
    datetime.strptime(ts, "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%dT%H:%M:%S")
    for ts in timestamps
]

# Generate HTML file
html_content = f"""
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Weather Data Plot</title>

    <!-- Plotly library -->
    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
</head>

<body>
    <h1>Weather Data Plot</h1>

    <div id="plotContainer" style="width: 80%; height: 400px;"></div>

    <script>
        // Data from CSV
        const timestamps = {timestamps_ms};
        const xValues = timestamps.map(timestamp => new Date(timestamp));
        const temperatures = {temperatures};

        // Create the plot
        const plotContainer = document.getElementById('plotContainer');

        const trace = {{
            x: xValues,
            y: temperatures,
            type: 'scatter',
            mode: 'lines+markers',
            marker: {{ color: 'blue' }},
        }};

        const layout = {{
            title: 'Weather Data Plot',
            xaxis: {{
                title: 'Timestamps',
                type: 'datetime',
            }},
            yaxis: {{ title: 'Temperature (&deg;C)' }},
        }};

        Plotly.newPlot(plotContainer, [trace], layout);
    </script>
</body>

</html>
"""

# Save HTML content to a file
html_file_path = "index.html"
with open(html_file_path, "w") as html_file:
    html_file.write(html_content)
