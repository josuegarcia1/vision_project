// Función para manejar el envío del formulario con un spinner de carga
function handleFormSubmission(event) {
    event.preventDefault(); // Evita el envío tradicional del formulario

    const form = event.target;
    const formData = new FormData(form);
    const spinner = document.getElementById('loadingSpinner');

    // Mostrar el spinner de carga
    spinner.classList.remove('hidden');

    console.log('Enviando formulario con datos:', formData); // Depuración

    // Enviar los datos al servidor con Fetch API
    fetch('/', {
        method: 'POST',
        body: formData
    })
    .then(response => {
        console.log('Respuesta del servidor:', response); // Depuración
        if (response.ok) {
            return response.url; // Devuelve la URL de redirección
        }
        throw new Error('Error al procesar la imagen');
    })
    .then(url => {
        console.log('Redirigiendo a:', url); // Depuración
        window.location.href = url; // Redirige a la página de resultados
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Hubo un problema al procesar la imagen.');
    })
    .finally(() => {
        spinner.classList.add('hidden'); // Oculta el spinner si hay error
    });
}
