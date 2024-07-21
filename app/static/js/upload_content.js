$(document).ready(function() {
    function updateContent(searchQuery, page) {
        $.get('/upload',
             { search: searchQuery, page: page },
              function(data) {
            $('#transaction-table').html(data.table);
            $('#pagination').html(data.pagination);
        });
    }

    // Search input event listener
    $('#search-input').on('input', function(e) {
        clearTimeout(searchTimeout);
        var searchQuery = $(this).val();
        searchTimeout = setTimeout(function() {
            updateContent(searchQuery, 1); // Reset ke halaman 1 pada pencarian baru
        }, 500);
    });

    // Pagination links event listener
    $(document).on('click', '.pagination a', function(e) {
        e.preventDefault();
        var page = $(this).data('page');
        var searchQuery = $('#search-input').val();
        updateContent(searchQuery, page);
    });
});