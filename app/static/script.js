const hamburger = document.querySelector("#toggle-btn")
const ctx = document.getElementById('myChart');

hamburger.addEventListener("click", function(params) {
   document.querySelector("#sidebar").classList.toggle("expand");
});

new Chart(ctx, {
   type: 'bar',
   data: {
     labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
     datasets: [{
       label: '# of Votes',
       data: [12, 19, 3, 5, 2, 3],
       borderWidth: 1
     }]
   },
   options: {
     scales: {
       y: {
         beginAtZero: true
       }
     }
   }
 });