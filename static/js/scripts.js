document.addEventListener("DOMContentLoaded", function() {
    // Exemplo de código JavaScript
    const form = document.getElementById("form");
    form.addEventListener("submit", function(event) {
        event.preventDefault(); // Previne o envio normal do formulário

        // Captura os dados do formulário
        const data = new FormData(form);

        // Envia os dados via AJAX para o Flask
        fetch('/adicionar_livro', {
            method: 'POST',
            body: data
        })
        .then(response => response.json())
        .then(data => {
            alert("Livro cadastrado com sucesso!");
        })
        .catch(error => {
            console.error("Erro:", error);
        });
    });
});
