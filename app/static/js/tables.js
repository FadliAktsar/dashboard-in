//const table = $('#data').DataTable();
//table.clear().draw();

$(document).ready(function () {
  if(!$.fn.DataTable.isDataTable('#data')){

    $('#data').DataTable({
      serverSide: true,
      processing: true,
      ajax: {
       url: '/upload/api',
       type: 'GET',
       dataSrc: 'data',
        error: function(xhr, error, code) {
            console.log("Error loading data:", xhr.responseText);
            alert("Failed to load data. Please check the console for details.");
          }
      },
      columns: [
        {data: 'Settlement_Date', orderable: true, searchable: true},
        {
          data: 'Transaction_Id',
          orderable: true,
          render: function (data, type, row, meta) {
            return data.length > 15 ? data.substr(0,15) + '...' : data;
          }
          },
        {data: 'Amount', orderable: false},
        {data: 'Payment_Type', orderable: false},
        ],
        //"scrollY": "400px",  // Mengaktifkan scrollbar vertikal dengan tinggi 400px
        //"scrollCollapse": false,  // Scrollbar hanya muncul saat diperlukan
        "paging": true,       // Aktifkan paginasi
        "select": true,
        "dom": 'rtip'    
    });
    // Custom search bar handler
  $('#search').on('keyup', function () {
      $('#data').DataTable().search($(this).val()).draw();
  });

  // Custom entries per page handler
  $('#entries').on('change', function () {
      $('#data').DataTable().page.len($(this).val()).draw();
  });
  }
  });

  