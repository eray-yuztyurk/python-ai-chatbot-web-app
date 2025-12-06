function sendMessage() {
    const userInputElem = document.getElementById('userInput');
    const sendBtn = document.getElementById('sendBtn');
    const userInput = userInputElem.value;
    if (!userInput) return;

    sendBtn.innerText = 'Waiting...';
    sendBtn.style.backgroundColor = '#28a745'; // green
    sendBtn.disabled = true;

    // Display user message
    const chatbox = document.getElementById('chatbox');
    const userMessage = document.createElement('div');
    userMessage.className = 'message user';
    userMessage.innerHTML = `<p>${userInput}</p>`;
    chatbox.appendChild(userMessage);

    userInputElem.value = '';

    // Send message to backend
    fetch('/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message: userInput })
    })
    .then(response => response.json())
    .then(data => {
        // Display bot response
        const botMessage = document.createElement('div');
        botMessage.className = 'message bot';
        botMessage.innerHTML = `<p>${data.response}</p>`;
        chatbox.appendChild(botMessage);
        chatbox.scrollTop = chatbox.scrollHeight;
        sendBtn.innerText = 'Send';
        sendBtn.style.backgroundColor = '';
        sendBtn.disabled = false;
    })
    .catch(error => { 
        sendBtn.innerText = 'Send';
        sendBtn.style.backgroundColor = '';
        sendBtn.disabled = false;
        console.error('Error:', error);
    });
}

document.getElementById('sendBtn').addEventListener('click', sendMessage);
document.getElementById('userInput').addEventListener('keypress', function (e) {
    if (e.key === 'Enter') {
        sendMessage();
    }
});