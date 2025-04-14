type = ['primary', 'info', 'success', 'warning', 'danger'];

const securitiesData = [
  { id: 1, symbol: "Dakota Rice", name: "Niger", description: "Oud-Turnhout", price: "$36,738" },
  { id: 2, symbol: "Minerva Hooper", name: "Curaçao", description: "Sinaai-Waas", price: "$23,789" },
  { id: 3, symbol: "Sage Rodriguez", name: "Netherlands", description: "Baileux", price: "$56,142" },
  { id: 4, symbol: "Philip Chaney", name: "Korea, South", description: "Overland Park", price: "$38,735" },
  { id: 5, symbol: "Doris Greene", name: "Malawi", description: "Feldkirchen in Kärnten", price: "$65,542" },
  { id: 6, symbol: "Mason Porter", name: "Chile", description: "Gloucester", price: "$78,615" },
  { id: 7, symbol: "Jon Porter", name: "Portugal", description: "Gloucester", price: "$98,615" }
];

securities = {
  initSecuritiesPageCharts: function () {

    gradientChartOptionsConfigurationWithTooltipPurple = {
      maintainAspectRatio: false,
      legend: {
        display: false
      },

      tooltips: {
        backgroundColor: '#f5f5f5',
        titleFontColor: '#333',
        bodyFontColor: '#666',
        bodySpacing: 4,
        xPadding: 12,
        mode: "nearest",
        intersect: 0,
        position: "nearest"
      },
      responsive: true,
      scales: {
        yAxes: [{
          barPercentage: 1.6,
          gridLines: {
            drawBorder: false,
            color: 'rgba(29,140,248,0.0)',
            zeroLineColor: "transparent",
          },
          ticks: {
            suggestedMin: 60,
            suggestedMax: 125,
            padding: 20,
            fontColor: "#9a9a9a"
          }
        }],

        xAxes: [{
          barPercentage: 1.6,
          gridLines: {
            drawBorder: false,
            color: 'rgba(225,78,202,0.1)',
            zeroLineColor: "transparent",
          },
          ticks: {
            padding: 20,
            fontColor: "#9a9a9a"
          }
        }]
      }
    };

    var ctx = document.getElementById("chartStockChart").getContext("2d");

    var gradientStroke = ctx.createLinearGradient(0, 230, 0, 50);

    gradientStroke.addColorStop(1, 'rgba(72,72,176,0.2)');
    gradientStroke.addColorStop(0.2, 'rgba(72,72,176,0.0)');
    gradientStroke.addColorStop(0, 'rgba(119,52,169,0)'); //purple colors

    var data = {
      labels: ['MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC'],
      datasets: [{
        label: "Data",
        fill: true,
        backgroundColor: gradientStroke,
        borderColor: '#d048b6',
        borderWidth: 2,
        borderDash: [],
        borderDashOffset: 0.0,
        pointBackgroundColor: '#d048b6',
        pointBorderColor: 'rgba(255,255,255,0)',
        pointHoverBackgroundColor: '#d048b6',
        pointBorderWidth: 20,
        pointHoverRadius: 4,
        pointHoverBorderWidth: 15,
        pointRadius: 4,
        data: [80, 100, 70, 80, 120, 80, 90, 100, 90, 80],
      }]
    };

    var myChart = new Chart(ctx, {
      type: 'line',
      data: data,
      options: gradientChartOptionsConfigurationWithTooltipPurple
    });
  },



  populateSecuritiesTable: function () {
    const tbody = document.getElementById("securitiesTableBody");
    securitiesData.forEach(row => {
      const tr = document.createElement("tr");
      tr.innerHTML = `
            <td>${row.symbol}</td>
            <td>${row.name}</td>
            <td>${row.description}</td>
            <td class="text-center">${row.price}</td>
            <td class="td-actions text-right">
              <button type="button" rel="tooltip" title="" class="btn btn-link" data-id="${row.id}"
                  data-original-title="Edit Task">
                  <i class="tim-icons icon-pencil"></i>
              </button>
            </td>
        `;
      tbody.appendChild(tr);
    });
  },

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