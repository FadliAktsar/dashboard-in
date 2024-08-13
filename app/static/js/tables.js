$(document).ready(function () {
    $('#transaction-table').DataTable({
      ajax: '/api/data',
      columns: [
        {data: 'Settlement_Date'},
        {data: 'Transaction_Id'},
        {data: 'Amount', orderable: false},
        {data: 'Payment_Type'},
        ],
    });
  });