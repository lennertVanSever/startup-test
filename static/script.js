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
        // Create and append textareas for input
        const textareaInput = createTextarea('input' + i + '1', 'textarea-large');
        formContainer.appendChild(textareaInput); // Changed from prepend to append

        // Create and append textareas for summary
        const textareaSummary = createTextarea('summary' + i, 'textarea-small');
        summaryContainer.appendChild(textareaSummary);
    }

    // Create and append the submit button at the end
    const submitButton = htmlToElement('<input type="button" value="Submit" id="submitButton" onclick="submitForm()">');
    formContainer.appendChild(submitButton);
}

function submitForm() {
    const submitButton = document.getElementById('submitButton');
    // Change button text and disable it
    submitButton.value = 'Loading...';
    submitButton.disabled = true;

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
            // Update the summary textareas
            for (let i = 1; i <= 4; i++) {
                document.getElementById('summary' + i).value = data['input' + i];
            }
            // Revert button text and enable it
            submitButton.value = 'Submit';
            submitButton.disabled = false;
        })
        .catch(error => {
            console.error('Error:', error);
            // Revert button text and enable it even in case of error
            submitButton.value = 'Submit';
            submitButton.disabled = false;
        });
}

