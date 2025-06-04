// ROW CLICKER

document.addEventListener('DOMContentLoaded', function () {
  // Make table rows clickable
  const rows = document.querySelectorAll('.clickable-row');
  rows.forEach(row => {
    row.addEventListener('click', function () {
      window.location.href = this.dataset.href;
    });

    // Change cursor on hover
    row.style.cursor = 'pointer';
  });
});

// SIDEBAR TOGGLE

const body = document.querySelector("body"),
  sidebar = body.querySelector("nav"),
  sidebarToggle = body.querySelector(".sidebar-toggle"),
  dashboard = body.querySelector(".dashboard");

// Check localStorage and apply saved state
document.addEventListener("DOMContentLoaded", () => {
  const isClosed = localStorage.getItem("sidebar-closed");
  if (isClosed === "true") {
    sidebar.classList.add("close");
  }
});

// Toggle sidebar and save the state
sidebarToggle.addEventListener("click", () => {
  sidebar.classList.toggle("close");
  const isClosed = sidebar.classList.contains("close");
  localStorage.setItem("sidebar-closed", isClosed);
});

// Close sidebar when clicking on overlay
dashboard.addEventListener("click", (e) => {
  if (window.innerWidth <= 500 &&
    sidebar.classList.contains("close") &&
    !e.target.closest('nav') &&
    e.target !== sidebarToggle) {
    sidebar.classList.remove("close");
    localStorage.setItem("sidebar-closed", "false");
  }
});

// Create Form uwu

    // Initialize the form on page load
    document.addEventListener('DOMContentLoaded', function() {
      toggleFields();
    });