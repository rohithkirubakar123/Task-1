<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Industrial IoT Predictive Maintenance System</title>
    <style>
        /* Basic CSS for layout */
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        h1 {
            text-align: center;
        }
        .sensor-data {
            margin-top: 20px;
            border-collapse: collapse;
            width: 100%;
        }
        .sensor-data th, .sensor-data td {
            border: 1px solid #ddd;
            padding: 8px;
            text-align: center;
        }
        .sensor-data th {
            background-color: #f2f2f2;
        }
    </style>
</head>
<body>
    <h1>Industrial IoT Predictive Maintenance System</h1>
    
    <div id="sensorData">
        <table class="sensor-data">
            <thead>
                <tr>
                    <th>Sensor ID</th>
                    <th>Sensor Type</th>
                    <th>Last Value</th>
                    <th>Last Updated</th>
                    <th>Predicted Maintenance</th>
                </tr>
            </thead>
            <tbody>
                <!-- Placeholder rows for data (to be dynamically populated) -->
                <tr>
                    <td>1</td>
                    <td>Temperature</td>
                    <td>25°C</td>
                    <td>2024-06-25 10:00 AM</td>
                    <td>OK</td>
                </tr>
                <tr>
                    <td>2</td>
                    <td>Vibration</td>
                    <td>0.5 mm/s</td>
                    <td>2024-06-25 10:05 AM</td>
                    <td>Attention</td>
                </tr>
                <!-- Add more rows as needed -->
            </tbody>
        </table>
    </div>

    <script>
        // Simulated data update (for demonstration)
        setInterval(function() {
            // Update values dynamically (simulated)
            var rows = document.querySelectorAll('.sensor-data tbody tr');
            rows.forEach(function(row) {
                var lastUpdatedCell = row.querySelector('td:nth-child(4)');
                var predictedMaintenanceCell = row.querySelector('td:nth-child(5)');
                // Simulate updating last updated time
                var now = new Date();
                lastUpdatedCell.textContent = now.toLocaleString('en-US');
                // Simulate predictive maintenance status change
                var randomNum = Math.random();
                if (randomNum < 0.3) {
                    predictedMaintenanceCell.textContent = 'OK';
                } else if (randomNum < 0.7) {
                    predictedMaintenanceCell.textContent = 'Attention';
                } else {
                    predictedMaintenanceCell.textContent = 'Critical';
                }
            });
        }, 5000); // Update every 5 seconds (for demo purposes)
    </script>
</body>
</html>
