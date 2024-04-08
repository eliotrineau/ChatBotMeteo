let state = 'askingCity';
let city, sexe, saison;

function sendMessage() {
    const userInput = document.getElementById('user-input').value;
    document.getElementById('user-input').value = '';

    if (state === 'askingCity') {
        city = userInput;
        addMessageToChatBox(`Vous avez choisi la ville : ${city}`);
        addMessageToChatBox('Quel est votre sexe ? (homme/femme)');
        state = 'askingSexe';
    } else if (state === 'askingSexe') {
        sexe = userInput;
        addMessageToChatBox(`Vous avez choisi : ${sexe}`);
        addMessageToChatBox('Quelle est la saison ? (printemps/été/automne/hiver)');
        state = 'askingSaison';
    } else if (state === 'askingSaison') {
        saison = userInput;
        addMessageToChatBox(`Vous avez choisi : ${saison}`);
        state = 'done';

        sendQuestionnaire(city, sexe, saison);
    }
}

function addMessageToChatBox(message) {
    const chatBox = document.getElementById('chat-box');
    const messageElement = document.createElement('div');
    messageElement.textContent = message;
    chatBox.appendChild(messageElement);
}
function appendMessage(sender, message) {
  var chatBox = document.getElementById("chat-box");
  var messageElement = document.createElement("div");
  messageElement.classList.add("chat-message");

  if (sender === 'user') {
    messageElement.classList.add("user-message");
  } else if (sender === 'bot') {
    messageElement.classList.add("bot-message");
  }

  messageElement.innerText = message;
  chatBox.appendChild(messageElement);
}

function getWeather() {
    navigator.geolocation.getCurrentPosition(function(position) {
        var lat = position.coords.latitude;
        var lon = position.coords.longitude;

        fetch(`https://api.opencagedata.com/geocode/v1/json?q=${lat}+${lon}&key=db63742015484084bca52473d6341c10`)
        .then(response => response.json())
        .then(data => {
            var city = data.results[0].components.city;

            fetch(`https://3000-aent0n.githubpreview.dev/questionnaire`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ "city": city })
            })
            .then(response => response.json())
            .then(data => {
                document.getElementById('weather').innerText = data.weather;
            })
            .catch(error => console.error('Erreur:', error));
        })
        .catch(error => console.error('Erreur:', error));
    });
}

document.addEventListener('DOMContentLoaded', getWeather);

function sendQuestionnaire(sexe, saison, cityInput) {
    fetch(`https://3000-aent0n.githubpreview.dev/questionnaire`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            "sexe": sexe,
            "saison": saison,
            "cityInput": cityInput
        })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').innerText = JSON.stringify(data);
    })
    .catch(error => console.error('Erreur:', error));
}