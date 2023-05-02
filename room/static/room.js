//<script id="json-roomname" type="application/json">{{room.slug}}</script>
// Get the slug from this elemenet(which is roomname)
const roomName = JSON.parse(document.getElementById('json-roomname').textContent);
// Get the username
const userName = JSON.parse(document.getElementById('json-username').textContent);

let url = `ws://${window.location.host}/ws/${roomName}/`;
// let url = `ws://${window.location.host}/ws/server/`;
console.log(url);
const chatSocket = new WebSocket(url);

// OnMessage
chatSocket.onmessage = function(e){
    let data = JSON.parse(e.data);
    console.log('Data', data);
    
    // Parse chat message broadcasted to the layer(not connect_success msg)
    if (data.type === 'chat'){
        if (data.message){
            let messages = document.getElementById('chat-messages');
            
            messages.insertAdjacentHTML('beforeend', `<div class="p-4 bg-gray-200 rounded-xl"> 
                                <p class="font-semibold">${data.username}</p> <p>${data.message}</p> </div>`);
            scrollToBottom();

        }else{
            alert('The message was empty!');
        }
    }
}

// OnSubmit
document.querySelector('#chat-message-submit').onclick = function(e) {
    e.preventDefault();
    const messageInputDom = document.querySelector('#chat-message-input');
    const msg = messageInputDom.value;
    
    //send msg
    chatSocket.send(JSON.stringify({
        'username': userName,
        'message': msg,
        'room': roomName
    }));
    
    // clear input form
    document.getElementById('msg-form').reset();
    messageInputDom.focus();
    return false;
}


// OnClose
chatSocket.onclose = function(e){
    console.log('Connection close. ');
}

// Trigger scroll to bottom of messages when we render this room's previous messages,
// and onmessage too
function scrollToBottom() {
    const div = document.querySelector('#chat-messages');
    div.scrollTop = div.scrollHeight;
    // console.log('bottom');
}

scrollToBottom();