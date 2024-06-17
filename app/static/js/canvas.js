const clx = document.getElementById('line-chart').getContext('2d')
$.ajax({
        url: "/dashboard/get_data",
        type: "get",
        success: function(response) {
            console.log("Response Data:", response);
            _data = response.data;
            _labels = response.labels;
            _forecast_data = response.forecast_data;
            _forecast_labels = response.forecast_labels;

            new Chart(clx, {
                type: 'line',
                data: {
                    labels: _labels.concat(_forecast_labels),
                    datasets: [{
                        label: 'Revenue',
                        data: _data,
                        backgroundColor: 'black',
                        borderColor: 'blue',
                        borderWidth: 1
                    },{
                        labels:_forecast_labels,
                        label: 'Forecast',
                        data: Array(_data.length).fill(null).concat(_forecast_data),
                        backgroundColor: 'orange',
                        borderColor: 'white',
                        borderWidth: 1 
                    }]
                },
                options: {
                    legend: {display: false},
                    scales: {
                        y: {  // Use 'y' for y-axis in Chart.js v3 and above
                            beginAtZero: true
                        }
                    }
                }
            });
        }
});