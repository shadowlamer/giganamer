document.addEventListener("DOMContentLoaded", onDocumentLoad);

function onDocumentLoad() {
    const form = document.getElementById("myform");
    form.addEventListener("submit", onFormSubmit);
    const copyButton = document.getElementById("copy-button");
    copyButton.addEventListener("click", onCopyClick);
}

function onCopyClick() {
    const respbox = document.getElementById("response-box");
    const text = respbox.innerHTML;
    if (text != "") {
        navigator.clipboard.writeText(respbox.innerHTML).then(r => {
            alert("Имя переменной скопировано в буфер обмена.")
        });
    }
}

function onFormSubmit(e) {
    e.preventDefault();
    const description = document.getElementById("description")
    const template = document.getElementById("template")
    fetch("/", {
        method: 'POST',
        body: JSON.stringify({
            "description": description.value,
            "template": template.value
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((response) => {
        const respbox = document.getElementById("response-box");
        response.text().then((text) => {
            respbox.innerHTML = text
        });
    });
}