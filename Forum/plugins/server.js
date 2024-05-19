const app = require('express')
const server = require('http').createServer(app)

const io = require('socket.io')(server, {
  cors: {
    origin: '*',
    methods: ['get', 'post']
  }
});
io.on('connection', () => {
  console.log('connect')
})

server.listen(5000, () => console.log('server run port 5000'))