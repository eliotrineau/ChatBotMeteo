function sendMessage() {
    var userInput = document.getElementById("user-input").value;
    var chatBox = document.getElementById("chat-box");
    appendMessage('user', userInput);

    // Envoie le message à votre script Python
    fetch("/questionnaire", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ "message": userInput })
    })
    .then(response => response.json())
    .then(data => {
        appendMessage('bot', "Tenue 1: " + data.outfit1 + ", Tenue 2: " + data.outfit2);
    })
    .catch(error => console.error('Erreur lors de l\'envoi de la requête:', error));
    document.getElementById("user-input").value = "";
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

            fetch(`http://0.0.0.0:3000/questionnaire`, {
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