document.getElementById('chat-form').addEventListener('submit', async function (e) {
    e.preventDefault();

    const userInput = document.getElementById('user-input').value.trim();
    if (userInput === "") return;

    addMessage(userInput, 'user');
    document.getElementById('user-input').value = '';

    try {
        const botReply = await getBotReply(userInput);
        addMessage(botReply, 'bot');
    } catch (error) {
        addMessage(`Bot Error: ${error.message}`, 'bot');
        console.error(error);
    }
});

function addMessage(message, sender) {
    const chatBox = document.getElementById('chat-box');
    const messageElem = document.createElement('div');
    messageElem.classList.add('chat-message', sender);
    messageElem.textContent = message;
    chatBox.appendChild(messageElem);

    // Smooth scrolling to bottom
    chatBox.scrollTo({ top: chatBox.scrollHeight, behavior: 'smooth' });
}


async function getBotReply(userInput, retries = 3) {
    const apiKey = 'AIzaSyAdMM6vt5ATICGk8qGpdJYM0gwogj9Y0VA';
    const apiUrl = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent';

    const payload = {
        contents: [
            { parts: [{ text: userInput }] }
        ]
    };

    try {
        const response = await fetch(`${apiUrl}?key=${apiKey}`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
        });

        if (!response.ok) {
            if (response.status === 503 && retries > 0) {
                console.warn('Model overloaded. Retrying in 2 seconds...');
                await new Promise(res => setTimeout(res, 2000));  // Wait 2 seconds
                return getBotReply(userInput, retries - 1);
            }

            const errorText = await response.text();
            throw new Error(`API error: ${response.status} - ${errorText}`);
        }

        const data = await response.json();
        console.log('Full API response:', JSON.stringify(data, null, 2));

        const botText = data?.candidates?.[0]?.content?.parts?.[0]?.text;

        if (typeof botText === 'string') {
            return botText;
        }

        return 'Error: No valid bot reply in API response';
    } catch (err) {
        throw err;
    }
}

