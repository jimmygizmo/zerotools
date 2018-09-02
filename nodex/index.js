//

var express = require('express');

var app = express();
var server = app.listen(8765, function(){
  console.log('nodex listening on port 8765');
});

app.use(express.static('pubstatic'));

////
//
