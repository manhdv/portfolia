securities = {
  handleEditButtonClicks: function() {
    $('.btn-edit').on('click', function () {
        const button = $(this);
        $('#stock_id').val(button.data('id'));
        $('#edit_ticker').val(button.data('ticker'));
        $('#edit_name').val(button.data('name'));
        $('#edit_description').val(button.data('description'));
    });
  },

  setupTickerAutocomplete: function () {
    const input = document.getElementById("add_ticker");
    const dropdown = document.createElement("div");
    dropdown.style.position = "absolute";
    dropdown.style.zIndex = 9999;
    dropdown.classList.add("list-group");
    document.body.appendChild(dropdown);

    let timeout;

    input.addEventListener("input", function () {
      const q = this.value;
      if (timeout) clearTimeout(timeout);
      if (q.length < 2) return dropdown.innerHTML = "";

      timeout = setTimeout(() => {
        fetch(`/api/search_stock/?q=${q}`)
          .then(r => r.json())
          .then(data => showSuggestions(data, input));
      }, 300);
    });

    document.addEventListener("click", function (e) {
      if (!dropdown.contains(e.target) && e.target !== input) {
        dropdown.innerHTML = "";
      }
    });

    function showSuggestions(data, inputEl) {
      dropdown.innerHTML = "";
      const rect = inputEl.getBoundingClientRect();
      dropdown.style.left = rect.left + "px";
      dropdown.style.top = (rect.bottom + window.scrollY) + "px";
      dropdown.style.width = rect.width + "px";

      data.forEach(item => {
        const el = document.createElement("a");
        el.className = "list-group-item list-group-item-action";
        el.textContent = `${item.ticker} - ${item.name}`;
        el.onclick = () => {
          console.log(item);
          document.getElementById("add_ticker").value = item.ticker;
          document.getElementById("add_exchange").value = item.exchange;
          document.getElementById("add_name").value = item.name;
          document.getElementById("add_description").value = item.description;
          document.getElementById("add_country").value = item.country;
          document.getElementById("add_isin").value = item.isin;
          document.getElementById("add_close").value = item.close;
          document.getElementById("add_date").value = item.date;
          dropdown.innerHTML = "";
        };
        dropdown.appendChild(el);
      });
    }
  },
};
