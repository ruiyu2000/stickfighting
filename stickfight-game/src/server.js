const io = require("socket.io")();

io.on("connection", client => {
  client.on("subscribeToMovement", interval => {
    console.log("client is subscribing to movement data ");
    client.emit("server", "ready");
  });

  client.on("movement", function(data) {
    console.log(data);
    if (data.score > 0.3) {
      client.broadcast.emit("action", data);
    } else if (data.score > 0 && data.score < 0.3) {
      client.broadcast.emit("action", data);
    }
  });
});

const port = 8000;
io.listen(port);
console.log("listening on port ", port);
