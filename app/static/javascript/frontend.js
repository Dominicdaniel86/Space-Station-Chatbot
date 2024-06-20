function sendMessage() {
    message = document.getElementById("inputField").value;
    if(message !== "") {

        let newDiv = document.createElement("div");
        newDiv.className = "message-user";

        let newP = document.createElement("p");
        newP.textContent = message;
        newDiv.appendChild(newP);
        let chat = document.getElementById("chat");
        chat.insertBefore(newDiv, chat.firstChild);
        // document.getElementById("chat").appendChild(newDiv);

        message = "message=" + message;
        document.getElementById('inputField').value = "";
        fetch("http://localhost:5000/sendmessage", {
            method: "POST",
            headers: {
                "Content-Type": "application/x-www-form-urlencoded"
            },
            body: message
        })
        .then((response) => response.json())
        .then((json) => {
            let botMessage = json[0].content;
            let newDiv = document.createElement("div");
            newDiv.className = "message-bot";

            let newP = document.createElement("p");
            newP.textContent = botMessage;
            newDiv.appendChild(newP);
            let chat = document.getElementById("chat");
            chat.insertBefore(newDiv, chat.firstChild);

            // document.getElementById("chat").appendChild(newDiv);
        });
    }
};

function checkKeyInput(event) {
    if(event.key === 'Enter')
        sendMessage();
}