var sio = io("/chat");

sio.on("status", function(data) {
    document.querySelector("#chat-history").innerHTML += `${data.msg}\n`;
});

sio.on("new_message", function(data) {
    document.querySelector("#chat-history").innerHTML += `${data.timestamp} ${data.username}: ${data.msg}\n`;
})

document.querySelector("#send-message").onclick = () => {
    data = {
        username: username,
        msg: document.querySelector("#user-message").value
    }
    document.querySelector("#user-message").value = "";
    sio.emit("send_message", data);
}
