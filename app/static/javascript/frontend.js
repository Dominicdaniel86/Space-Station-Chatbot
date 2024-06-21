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
        })
        .catch((error) => {
            console.error(error);
            let newDiv = document.createElement("div");
            newDiv.className = "message-bot";

            let newP = document.createElement("p");
            newP.textContent = "Oh, it appears that I'm not availabe. Please check your internet connection!";
            newDiv.appendChild(newP);
            let chat = document.getElementById("chat");
            chat.insertBefore(newDiv, chat.firstChild);
        });
    }
};

function expandFeedback() {
    let feedback = document.getElementById('feedback-expandable');
    if(feedback.style.display === "none")
        feedback.style.display = "block"
    else
        feedback.style.display = "none"
}

function saveFeedback() {
    const name = document.getElementById("feedback-name").value;
    const feedback = document.getElementById("feedback-content").value;
    if(name!=="" && feedback!=="") {
        document.getElementById("feedback-name").value = "";
        document.getElementById("feedback-content").value = "";
    }
    const timestamp = new Date().toISOString();

    const message = new URLSearchParams;
    message.append("timestamp", timestamp);
    message.append("name", name);
    message.append("feedback", feedback);

    fetch("http://localhost:5000/feedback", {
        method: "POST",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded"
        },
        body: message.toString()
    });
}

function checkKeyInput(event) {
    if(event.key === 'Enter')
        sendMessage();
}