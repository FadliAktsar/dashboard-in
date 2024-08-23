const transaction_canvas = document.getElementById('transaction').getContext('2d');
const forecast_canvas = document.getElementById('forecast').getContext('2d');

const forecastPeriodSelect = document.getElementById('forecast-period');
const download = document.getElementById('download');
const dataModeSelect = document.getElementById('data-mode');  // Dropdown baru untuk memilih daily/weekl

let transaction = null;
let forecast = null;



function fetchForecastData(periods, mode = 'weekly') {
    
    $.ajax({
            url: "/dashboard/get_data",
            type: "GET",
            data: { 
                periods: periods,
                mode: mode },
            success: function(response) {
                console.log("Response Data:", response);
                _data = response.data;
                _labels = response.labels;
                _forecast_data = response.forecast_data;
                _forecast_labels = response.forecast_labels;

                // Clear the previous chart if it exists
                if (transaction) {
                    transaction.destroy();
                }

                if (forecast) {
                    forecast.destroy();
                    }

                transaction = new Chart(transaction_canvas, {
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
                                text: mode == 'daily' ? 'Data Revenue per Hari' : 'Data Revenue per Minggu'
                            },
                            tooltip:{
                                enabled: true
                            }
                        }
                    },
                });
                
                forecast = new Chart(forecast_canvas, {
                    type: 'line',
                    data: {
                        labels: _forecast_labels,
                        datasets: [{
                            label: 'Peramalan',
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

fetchForecastData(4, 'weekly')

function updateChart() {
    const mode = dataModeSelect.value;          // Ambil nilai mode (daily/weekly) dari dropdown
    const periods = forecastPeriodSelect.value; // Ambil nilai periode dari dropdown
    fetchForecastData(periods, mode);           // Panggil fetchForecastData dengan kedua parameter
}

// Event listener untuk dropdown mode
dataModeSelect.addEventListener('change', function() {
    console.log("Mode changed to:", dataModeSelect.value);
    updateChart();   
});

forecastPeriodSelect.addEventListener('change', function() {
    console.log("Period changed to:", forecastPeriodSelect.value);
    updateChart();   
});

download.addEventListener('click', function() {
    window.location.href = "/dashboard/download_csv";
 })