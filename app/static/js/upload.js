document.addEventListener('DOMContentLoaded', function() {
    const notification = document.querySelector('.notification');
    const uploadForm = document.getElementById('uploadForm');

    uploadForm.addEventListener('submit', function(event) {
        event.preventDefault();

        const formData = new FormData(uploadForm);

        fetch('/upload/upload_files', {
            method: 'POST',
            body: formData
        }).then(response => response.json())
        .then(data => {
            if (notification) {
                notification.innerHTML = `<div class="alert alert-${data.success ? 'success' : 'danger'}" role="alert">${data.message}</div>`;
                if (data.success) {
                    setTimeout(() => {
                        location.reload();
                    }, 2000); // Refresh halaman setelah 2 detik
                }
            } else {
                console.error('Notification element not found');
            }
        }).catch(error => {
            console.error('There was a problem with your fetch operation:', error);
        });
    });
});