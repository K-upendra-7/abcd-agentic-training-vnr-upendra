// DOM Elements
    const suggestions = document.querySelectorAll('.suggestion-btn');
    const chatForm = document.getElementById('chatForm');
    const chatInput = document.getElementById('chatInput');
    const chatLog = document.getElementById('chatLog');

    // Suggestions click-to-fill
    suggestions.forEach(btn => {
        btn.addEventListener('click', () => {
            chatInput.value = btn.textContent;
            chatInput.focus();
        });
    });

    // Chat interaction, looping messages
    chatForm.addEventListener('submit', async function(e) {
        e.preventDefault();
        const userInput = chatInput.value.trim();
        if (!userInput) return;
        addMessage(userInput, 'user');
        chatInput.value = '';
        // Get bot reply
        try {
            const botReply = await getBotReply(userInput);
            addMessage(botReply, 'bot');
        } catch (error) {
            addMessage("Bot Error: " + error.message, 'bot');
        }
    });

    function addMessage(text, sender) {
        const msgEl = document.createElement('div');
        msgEl.classList.add('chat-message', sender);
        msgEl.textContent = text;
        chatLog.appendChild(msgEl);
        chatLog.scrollTo({ top: chatLog.scrollHeight, behavior: 'smooth' });
    }

    // Example bot connection (plug in your API logic)
    async function getBotReply(prompt, retries = 3) {

        const apiKey = "YOUR_API_KEY_HERE";
        const apiUrl = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent";

        // Add a system prompt for style, role, and output guidelines
        const systemPrompt = `You are a helpful, friendly, conversational AI assistant for student coding and entrepreneurship projects. 
            Respond concisely and clearly. Use an encouraging and supportive tone. If sharing code, use clean formatting. 
            If the user asks for ideas, offer practical examples. simple answer without "*" in paragraph form`;

        const payload = { 
            contents: [
                { 
                    parts: [
                        { text: systemPrompt },
                        { text: prompt }
                    ]
                }
            ] 
        };

        try {
            const response = await fetch(`${apiUrl}?key=${apiKey}`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(payload)
            });
            if (!response.ok) {
                throw new Error(`API error ${response.status} - ${response.statusText}`);
            }
            const data = await response.json();
            const botText = data?.candidates?.[0]?.content?.parts?.[0]?.text;
            if(!botText || typeof botText !== "string"){
                throw new Error("Invalid bot response received");
            }

        // Return trimmed and formatted reply
            return botText.trim();
        }catch(err){
            throw new Error(`Failed to fetch bot reply: ${err.message}`);
        }
    }

        
    