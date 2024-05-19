<template>
  <div>
    <input
      v-model="message"
      placeholder="Type a message"
      @keyup.enter="sendMessage"
    />
    <ul>
      <li v-for="(msg, index) in messages" :key="index">{{ msg }}</li>
    </ul>
  </div>
</template>

<script>
export default {
  layout: 'empty',
  data() {
    return {
      message: '',
      messages: [],
    };
  },
  mounted() {
    // Connect to the main socket
    this.socket = this.$nuxtSocket({
      name: 'mainSocket',
      channel: 'main',
      reconnection: true, // Enable reconnection
      reconnectionAttempts: 5, // Number of attempts before giving up
      reconnectionDelay: 1000, // Time between reconnection attempts
      url: 'http://localhost:5000' // Ensure this URL matches your server's URL
    });

    // Listen for incoming messages
    this.socket.on('message', (msg) => {
      this.messages.push(msg);
      console.log('Message received:', msg);
    });

    this.socket.on('connect', () => {
      console.log('Connected to server');
    });

    this.socket.on('disconnect', () => {
      console.log('Disconnected from server');
    });
  },
  methods: {
    sendMessage() {
      if (this.message.trim() !== '') {
        // Send the message to the server
        this.socket.emit('message', this.message);
        this.message = '';
      }
    },
  },
}
</script>

<style scoped>
/* Add your styles here */
</style>
