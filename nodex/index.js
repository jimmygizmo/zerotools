//

var express = require('express');
var backsocket = require('socket.io');

var app = express();
var server = app.listen(8765, function(){
  console.log('nodex listening on port 8765');
});

app.use(express.static('pubstatic'));

var io = backsocket(server);

io.on('connection', function(backsocket){

  console.log('a client just connected - id:', backsocket.id);

  backsocket.on('chatmsgobj', function(data){
    io.sockets.emit('chatmsgobj', data);
  });

  backsocket.on('istyping', function(data){
    backsocket.broadcast.emit('istyping', data);
  });

});




////
//
