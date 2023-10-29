document.getElementById('generatorForm').addEventListener('submit', function(event) {
    event.preventDefault();
    document.getElementById('loadingSpinner').style.display = 'block';
    
    fetch('/', {
        method: 'POST',
        body: new FormData(this)
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            // let audioURL = `{{ url_for('static', filename='${data.file}') }}`;
            let audioURL = "/static/output_with_music.wav";

            document.querySelector('audio source').src = audioURL;
            document.querySelector('audio').load();
            new bootstrap.Modal(document.getElementById('successModal')).show();
        }
        document.getElementById('loadingSpinner').style.display = 'none';
    });
});
