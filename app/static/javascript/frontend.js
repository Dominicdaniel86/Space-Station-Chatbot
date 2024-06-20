function sendMessage() {
    message = document.getElementById("inputField").value;
    message = "message=" + message;
    fetch("http://localhost:5000/sendmessage", {
        method: "POST",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded"
        },
        body: message
    })
    .then((response) => response.json())
    .then((json) => {
        console.log(json[0].content);
    });
};