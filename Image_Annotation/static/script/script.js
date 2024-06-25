document.getElementById('annotate-button').addEventListener('click', async () => {
    const fileInput = document.getElementById('image-input');
    const file = fileInput.files[0];
    if (!file) return;

    const formData = new FormData();
    formData.append('image', file);

    const response = await fetch('/annotate', {
        method: 'POST',
        body: formData
    });

    const result = await response.blob();
    const outputImage = document.getElementById('output-image');
    outputImage.src = URL.createObjectURL(result);
});
