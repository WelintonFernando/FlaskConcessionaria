document.addEventListener('DOMContentLoaded', function() {
    const cadastroBtn = document.getElementById('cadastroBtn');
    const submenuCadastro = document.getElementById('submenuCadastro');
    const compraBtn = document.getElementById('compraBtn');
    const submenuCompra = document.getElementById('submenuCompra');

    let openMenu = null;

    function closeAll() {
        submenuCadastro.style.display = 'none';
        submenuCompra.style.display = 'none';
        cadastroBtn.style.transform = 'translateY(0)';
        compraBtn.style.transform = 'translateY(0)';
    }

    cadastroBtn.addEventListener('click', () => {
        if (openMenu === 'cadastro') {
            closeAll();
            openMenu = null;
        } else {
            closeAll();
            submenuCadastro.style.display = 'flex';
            submenuCadastro.style.flexDirection = 'column';
            submenuCadastro.style.animation = 'submenuFadeIn 0.7s cubic-bezier(.4,2,.6,1)';
            cadastroBtn.style.transition = 'transform 0.7s cubic-bezier(.4,2,.6,1)';
            compraBtn.style.transition = 'transform 0.7s cubic-bezier(.4,2,.6,1)';
            
            openMenu = 'cadastro';
        }
    });

    compraBtn.addEventListener('click', () => {
        if (openMenu === 'compra') {
            closeAll();
            openMenu = null;
        } else {
            closeAll();
            submenuCompra.style.display = 'flex';
            submenuCompra.style.flexDirection = 'column';
            submenuCompra.style.animation = 'submenuFadeIn 0.7s cubic-bezier(.4,2,.6,1)';
            cadastroBtn.style.transition = 'transform 0.7s cubic-bezier(.4,2,.6,1)';
            compraBtn.style.transition = 'transform 0.7s cubic-bezier(.4,2,.6,1)';
            openMenu = 'compra';
        }
    });

    // Navegação para páginas de cadastro
    const submenuCadastroBtns = submenuCadastro.querySelectorAll('.submenu-btn');
    submenuCadastroBtns[0].addEventListener('click', function() {
        window.location.href = 'cadastro_cliente.html';
    });
    submenuCadastroBtns[1].addEventListener('click', function() {
        window.location.href = 'cadastro_prestador.html';
    });
    submenuCadastroBtns[2].addEventListener('click', function() {
        window.location.href = 'cadastro_veiculo.html';
    });
    submenuCadastroBtns[3].addEventListener('click', function() {
        window.location.href = 'cadastro_despesa.html';
    });
    // Adicione navegação para os botões do submenuCompra se desejar
});
