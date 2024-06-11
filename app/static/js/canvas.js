var _labels = [];
var _data = [];
const clx = document.getElementById('line-chart').getContext('2d')
$.ajax({
        url: "/dashboard/get_data",
        type: "get",
        success: function(response) {
            console.log("Response Data:", response);
            _data = response.data;
            _labels = response.labels;

            new Chart(clx, {
                type: 'line',
                data: {
                    labels: _labels,
                    datasets: [{
                        label: 'Data Aktual',
                        data: _data,
                        backgroundColor: 'black',
                        borderColor: 'blue',
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