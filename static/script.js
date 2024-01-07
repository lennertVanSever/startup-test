function htmlToElement(html) {
    const template = document.createElement('template');
    html = html.trim();
    template.innerHTML = html;
    return template.content.firstChild;
}

function createTextarea(id, className) {
    return htmlToElement(`<textarea id="${id}" name="${id}" class="${className}"></textarea>`);
}

window.onload = function () {
    const formContainer = document.getElementById('formContainer');
    const summaryContainer = document.getElementById('summaryContainer');

    for (let i = 1; i <= 4; i++) {
        const textareaInput = createTextarea('input' + i + '1', 'textarea-large');
        formContainer.prepend(textareaInput);

        const textareaSummary = createTextarea('summary' + i, 'textarea-small');
        summaryContainer.append(textareaSummary);
    }
}

function submitForm() {
    const formData = new FormData();
    for (let i = 1; i <= 4; i++) {
        formData.append('input' + i, document.getElementById('input' + i + '1').value);
    }

    fetch('/submit', {
        method: 'POST',
        body: formData
    })
        .then(response => response.json())
        .then(data => {
            for (let i = 1; i <= 4; i++) {
                document.getElementById('summary' + i).value = data['input' + i];
            }
        })
        .catch(error => console.error('Error:', error));
}
