const transaction_canvas = document.getElementById('transaction').getContext('2d');
const forecast_canvas = document.getElementById('forecast').getContext('2d');

const forecastPeriodSelect = document.getElementById('forecast-period');
const download = document.getElementById('download');

//let forecast = null;
/*
forecastPeriodSelect.addEventListener('change', function() {
    const selectedPeriod = this.value;
    fetchForecastData(selectedPeriod);
});
*/
function fetchForecastData(periods) {
    
    $.ajax({
            url: "/dashboard/get_data",
            type: "get",
            //data: { periods: periods },
            success: function(response) {
                console.log("Response Data:", response);
                _data = response.data;
                _labels = response.labels;
                _forecast_data = response.forecast_data;
                _forecast_labels = response.forecast_labels;
                
                /*
                if (forecast) {
                    forecast.destroy();
                     forecast = null;
                    }
                */

                let transaction = new Chart(transaction_canvas, {
                    type: 'line',
                    data: {
                        labels: _labels,
                        datasets: [{
                            label: 'Revenue',
                            data: _data,
                            backgroundColor: 'black',
                            borderColor: 'blue',
                            borderWidth: 1
                        }]
                    },
                    options: {
                        maintainAspectRatio: false,
                        legend: {display: false},
                        scales: {
                            y: {  // Use 'y' for y-axis in Chart.js v3 and above
                                min: 0,
                                beginAtZero: true
                            },
                            x:{
                                ticks:{
                                    maxTicksLimit: 10
                                }
                            }
                        },
                        plugins: {
                            title: {
                                display: true,
                                text: 'Data Revenue'
                            },
                            tooltip:{
                                enabled: true
                            }
                        }
                    },
                });
                
                let forecast = new Chart(forecast_canvas, {
                    type: 'line',
                    data: {
                        labels: _forecast_labels,
                        datasets: [{
                            label: 'Peralaman',
                            data: _forecast_data,
                            backgroundColor: 'orange',
                            borderColor: 'black',
                            borderWidth: 1
                        }]
                    },
                    options: {
                        maintainAspectRatio: false,
                        legend: {display: false},
                        scales: {
                            y: {  // Use 'y' for y-axis in Chart.js v3 and above
                                beginAtZero: true
                            },
                            x:{
                                ticks:{
                                    maxTicksLimit: 15
                                }
                            }
                        },
                        plugins: {
                            title: {
                                display: true,
                                text: 'Data Peramalan'
                            }
                        }
                    },
                });
            }
    });
}

fetchForecastData(30)

download.addEventListener('click', function() {
    window.location.href = "/dashboard/download_csv";
 })