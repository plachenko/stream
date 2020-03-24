var WebSocket = require('ws');
var osc = require("osc");
var udpPort = new osc.UDPPort({
    localAddress: "0.0.0.0",
    localPort: 7001,
    metadata: true
});
const wss = new WebSocket.Server({port: 8080});
udpPort.open();
wss.on('connection', (ws) =>{
    ws.on('message', function incoming(message) {
        // console.log(parseFloat(message));
        // var f = message.split('. ');
        var m = message.split(', ');
        // var m2 = f[1].split(', ');
        
        udpPort.send(
            {
            address: "/motion",
            args: [
                {type: "f", value: parseFloat(m[0]/1)},
                {type: "f", value: parseFloat(m[1]/1)},
                {type: "f", value: parseFloat(m[2]/1)}
                ]
            }, "127.0.0.1", 7000);
    });
    
    // ws.send('something');
});