const buttons = document.querySelectorAll(".AnimatedButton");
const sidebar = document.getElementById("sidebar");

let activeButton = null;

buttons.forEach(function(button) {
  button.addEventListener("click", function(event) {
    if (activeButton === button.id) {
      activeButton = null;
      sidebar.classList.remove("expanded");
    } else {
      activeButton = button.id;
      sidebar.classList.add("expanded");
    }
    event.stopPropagation();
  });
});

document.addEventListener("click", function(event) {
  if (!sidebar.contains(event.target)) {
    activeButton = null;
    sidebar.classList.remove("expanded");
  }
});
