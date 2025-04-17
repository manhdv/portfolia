type = ['primary', 'info', 'success', 'warning', 'danger'];

securities = {

  handleEditButtonClicks: function () {
    const tbody = document.getElementById("securitiesTableBody");
    tbody.addEventListener("click", function (e) {
      const btn = e.target.closest(".btn-link");
      if (btn && btn.dataset.id) {
        console.log("Clicked ID:", btn.dataset.id);
      }
    });
  }
};