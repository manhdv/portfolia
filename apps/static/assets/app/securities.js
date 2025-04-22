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

  // Các phương thức khác của securities...
};
