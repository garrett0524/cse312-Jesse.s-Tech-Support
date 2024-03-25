function sendMessage() {
    var messageInput = document.getElementById('messageInput');
    var message = messageInput.value.trim();
    if (message !== '') {
        var data = {
            'user': username,
            'message': message
        };
        fetch('/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken
            },
            body: JSON.stringify(data)
        })
        .then(response => {
            if (response.ok) {
                messageInput.value = '';
                fetchMessages();
            }
        });
    }
}

function fetchMessages() {
    fetch('/chat_messages')
        .then(response => response.json())
        .then(data => {
            var chatBox = document.getElementById('chatBox');
            chatBox.innerHTML = '';
            for (var i = 0; i < data.length; i++) {
                var messageElement = document.createElement('div');
                messageElement.innerHTML = `
                    <p>${data[i].user}: ${data[i].message}</p>
                    <button class="like-button" onclick="likeMessage(${data[i].id})">Like</button>
                `;
                chatBox.appendChild(messageElement);
            }
            chatBox.scrollTop = chatBox.scrollHeight;
        });
}

fetchMessages();