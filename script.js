const urlInput = document.getElementById('urlInput');
const shortenButton = document.getElementById('shortenButton');
const resultContainer = document.getElementById('result');

shortenButton.addEventListener('click', async () => {
    const url = urlInput.value.trim();
    if (!url) {
        resultContainer.textContent = 'Por favor, insira uma URL.';
        return;
    }

    try {
        const response = await fetch('http://127.0.0.1:5000/shorten', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ url })
        });

        const data = await response.json();

        if (!response.ok) {
            resultContainer.textContent = data.error || 'Erro ao encurtar a URL.';
            return;
        }

        resultContainer.innerHTML = `Código: <strong>${data.code}</strong><br>URL curta: <a href="${data.short_url}" target="_blank">${data.short_url}</a>`;

        const copyButton = document.createElement('button');
        copyButton.type = 'button';
        copyButton.textContent = 'Copiar';
        copyButton.style.marginTop = '12px';
        copyButton.addEventListener('click', async () => {
            try {
                await navigator.clipboard.writeText(data.short_url);
                copyButton.textContent = 'Copiado ✅';
                setTimeout(() => {
                    copyButton.textContent = 'Copiar';
                }, 2000);
            } catch (copyError) {
                copyButton.textContent = 'Erro ao copiar';
                setTimeout(() => {
                    copyButton.textContent = 'Copiar';
                }, 2000);
            }
        });

        resultContainer.appendChild(copyButton);
    } catch (error) {
        resultContainer.textContent = 'Não foi possível conectar ao backend.';
    }
});