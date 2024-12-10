function getCookie(cname) {
    let name = cname + "=";
    let decodedCookie = decodeURIComponent(document.cookie);
    let ca = decodedCookie.split(';');
    for (let i = 0; i < ca.length; i++) {
        let c = ca[i];
        while (c.charAt(0) == ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }
    return "";
}

async function getChannel() {
    const response = await fetch("/stock/channel/register/")
    const data = await response.json()
    return await data.channel
}

// Função para iniciar a conexão SSE
async function iniciarSSE() {
    let channel = await getChannel();
    var es = new ReconnectingEventSource(`/events/${channel}/`);

    es.addEventListener('message', async function (e) {
        const data = JSON.parse(await e.data)
        console.log(data);
        exibirNotificacao(data.text)
    }, false);
}

// Função para exibir a notificação com Toastify
function exibirNotificacao(message) {
    Toastify({
        text: message,
        duration: 3000,
        close: true,
        gravity: "bottom",
        position: "right",
        style: {
            background: "linear-gradient(to right, #005954, #00adaf)",
        }
    }).showToast();
}

// Iniciar a conexão SSE ao carregar a página
document.addEventListener('DOMContentLoaded', iniciarSSE);
