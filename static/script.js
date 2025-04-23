async function sendMessage() {
    const userInput = document.getElementById("user-input").value;
    if (!userInput.trim()) return;
  
    const response = await fetch("/chat", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ message: userInput })
    });
  
    const data = await response.json();
    const chatBox = document.getElementById("chat-box");
    chatBox.innerHTML += `<p><b>You:</b> ${userInput}</p>`;
    chatBox.innerHTML += `<p><b>Bot:</b> <span>${data.reply}</span></p>`;
    chatBox.scrollTop = chatBox.scrollHeight;
    document.getElementById("user-input").value = "";
  }
    
  
  