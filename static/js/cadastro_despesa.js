document.getElementById('voltar').addEventListener('click', function(e) {
    window.location.href = 'inicio.html';
});

document.getElementById('registro').addEventListener('click', function(e) {
    window.location.href = 'registro_despesa.html';
});

document.getElementById('confirmar').addEventListener('click', function(e) {
    // Função para confirmar será implementada no Flask
});

document.addEventListener('DOMContentLoaded', function() {
    var labelPrestador = document.getElementById('label-prestador');
    var tooltipPrestador = document.getElementById('tooltip-prestador');
    if(labelPrestador && tooltipPrestador) {
        labelPrestador.addEventListener('mouseenter', function() {
            tooltipPrestador.style.display = 'block';
        });
        labelPrestador.addEventListener('mouseleave', function() {
            tooltipPrestador.style.display = 'none';
        });
    }
});
