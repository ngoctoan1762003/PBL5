import Vue from 'vue'
import VueSocketIO from 'vue-socket.io'
import SocketIO from 'socket.io-client'

export default ({ store }) => {
  Vue.use(new VueSocketIO({
    debug: true,
    connection: SocketIO('http://localhost:3000'), // Your socket server URL
    vuex: {
      store,
      actionPrefix: 'SOCKET_',
      mutationPrefix: 'SOCKET_'
    }
  }))
}
