securities = {
  handleEditButtonClicks: function() {
    $('.btn-edit').on('click', function () {
        const button = $(this);
        $('#stock_id').val(button.data('id'));
        $('#edit_code').val(button.data('code'));
        $('#edit_name').val(button.data('name'));
//        $('#edit_exchange').val(button.data('exchange'));
//        $('#edit_type').val(button.data('type'));
        $('#edit_description').val(button.data('description'));
//        $('#edit_country').val(button.data('country'));
//        $('#edit_currency').val(button.data('currency'));
//        $('#edit_isin').val(button.data('isin'));
//        $('#edit_close').val(button.data('close'));
//        $('#edit_date').val(button.data('date'));
    });
  },

  setupTickerAutocomplete: function () {
    const input = document.getElementById("add_code");
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
        fetch(`securities/search/?q=${q}`)
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
        el.textContent = `${item.code} - ${item.name}`;
        el.onclick = () => {
          console.log(item);
          document.getElementById("add_code").value = item.code;
          document.getElementById("add_exchange").value = item.exchange;
          document.getElementById("add_name").value = item.name;
          document.getElementById("add_type").value = item.type;
          document.getElementById("add_description").value = item.type;
          document.getElementById("add_country").value = item.country;
          document.getElementById("add_currency").value = item.currency;
          document.getElementById("add_isin").value = item.isin;
          document.getElementById("add_close").value = item.close;
          document.getElementById("add_date").value = item.date;
          dropdown.innerHTML = "";
        };
        dropdown.appendChild(el);
      });
    }
  },

    updateModalTheme: function(modal) {
      const isLight = document.body.classList.contains("white-content");
      const $modalContent = $(modal).find('.modal-content');

      //$modalContent.removeClass('bg-dark bg-light text-white text-dark');

      if (isLight) {
          //$modalContent.addClass('bg-light text-dark');
      } else {
          $modalContent.addClass('bg-dark');
      }
  },
};
