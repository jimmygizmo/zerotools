var frontsocket = io.connect('http://localhost:8765');

var message = document.getElementById('message');
    handle = document.getElementById('handle'),
    btn = document.getElementById('send'),
    output = document.getElementById('chatout');
    chatstatus = document.getElementById('chatstatus');


btn.addEventListener('click', function(){
  frontsocket.emit('chatmsgobj', {
    message: message.value,
    handle: handle.value
  });
});

message.addEventListener('keypress', function(){
  frontsocket.emit('istyping', handle.value);
});

frontsocket.on('chatmsgobj', function(data){
  chatstatus.innerHTML = '';
  output.innerHTML += '<p><strong>' + data.handle + ': </strong>' + data.message + '</p>';
});

frontsocket.on('istyping', function(data){
  chatstatus.innerHTML = '<p><em>' + data + ' is typing a message ...</em></p>';
});
