const express = require('express');
const http = require('http');
const WebSocket = require('ws');
const path = require('path');

const app = express();
const server = http.createServer(app);
const wss = new WebSocket.Server({ noServer: true });

const clients = {}; // Object to store connected WebSocket clients with their IDs

wss.on('connection', (ws) => {
  console.log('Client connected');
  
  ws.on('message', (message) => {
    const parsedMessage = JSON.parse(message);
    if (parsedMessage.type === 'clientId') {
      const clientId = parsedMessage.clientId;
      clients[clientId] = ws; // Store the WebSocket connection with the client's ID
    } else if (parsedMessage.type === 'privateMessage') {
      const recipientId = parsedMessage.recipientId;
      const senderId = parsedMessage.senderId;
      const recipient = clients[recipientId];
      const sender = clients[senderId];
      if (recipient && recipient.readyState === WebSocket.OPEN) {
        recipient.send(JSON.stringify(parsedMessage)); // Forward the message to the recipient
      } else {
        console.log(`Recipient with ID ${recipientId} is not available.`);
      }
      if (sender && sender.readyState === WebSocket.OPEN) {
        sender.send(JSON.stringify(parsedMessage)); // Forward the message to the recipient
      } else {
        console.log(`Sender with ID ${senderId} is not available.`);
      }
    }
  });

  ws.on('close', () => {
    console.log('Client disconnected');
    // Remove the disconnected client from the clients object
    const disconnectedClientId = Object.keys(clients).find(clientId => clients[clientId] === ws);
    if (disconnectedClientId) {
      delete clients[disconnectedClientId];
    }
  });
});

server.on('upgrade', (request, socket, head) => {
  wss.handleUpgrade(request, socket, head, (ws) => {
    wss.emit('connection', ws, request);
  });
});

// Serve the Vue.js app
app.use(express.static(path.join(__dirname, 'dist')));

app.get('*', (req, res) => {
  res.sendFile(path.join(__dirname, 'dist', 'index.html'));
});

server.listen(5000, () => {
  console.log('Server running on port 5000');
});
