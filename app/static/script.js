const hamburger = document.querySelector("#toggle-btn")

hamburger.addEventListener("click", function(params) {
   document.querySelector("#sidebar").classList.toggle("expand");
});