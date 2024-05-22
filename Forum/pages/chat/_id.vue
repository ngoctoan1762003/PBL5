<template>
  <div class="h-screen">
    <TopNaviBarVue />
    <div
      v-if="popup.visible"
      :style="{ top: `${popup.y}px` }"
      class="absolute left-[110px] whitespace-nowrap bg-white px-2 py-1 rounded bg-white px-5 py-3 font-semibold rounded-2xl text-blue-900 shadow-md"
    >
      {{ popup.name }}
    </div>
    <div class="chat-container">
      <div class="h-[100%] w-[100%] flex">
        <div
          class="h-[100%] w-[100px] flex flex-col items-center gap-4 py-4 overflow-y-auto overflow-x-hidden border-[1px] shadow-md relative"
        >
          <div
            v-for="conversation in conversations"
            :key="conversation.user_id"
            @click="toConversationWith(conversation.user_id)"
            class="cursor-pointer relative"
          >
            <img
              :src="conversation.image"
              alt=""
              class="w-10 h-10 rounded-full"
              @mouseover="showPopup(conversation, $event)"
              @mouseleave="hidePopup"
            />
          </div>
        </div>
        <div class="h-[100%] w-full">
          <ul class="space-y-4 p-4 chat-container__content overflow-y-auto">
            <li
              v-for="(msg, index) in messages"
              :key="index"
              class="flex gap-5"
              :class="{
                'justify-end': msg.senderId === user.User_id,
                'justify-start': msg.senderId !== user.User_id,
              }"
            >
              <img
                :src="
                  msg.senderId === user.User_id ? user.Image : recipient.image
                "
                alt=""
                class="w-10 h-10 rounded-full"
                v-if="msg.senderId !== user.User_id"
              />
              <div
                class="bg-white px-5 py-3 font-semibold rounded-2xl text-blue-900 shadow-md"
              >
                <div>
                  {{
                    msg.senderId === user.User_id ? user.Name : recipient.Name
                  }}
                </div>
                <div>{{ msg.content }}</div>
              </div>
              <img
                :src="
                  msg.senderId === user.User_id ? user.Image : recipient.image
                "
                alt=""
                class="w-10 h-10 rounded-full"
                v-if="msg.senderId === user.User_id"
              />
            </li>
          </ul>
          <input
            v-model="message"
            placeholder="Type a message"
            @keyup.enter="sendMessage"
            class="h-10 w-full border border-gray-500 py-2 px-3 mt-2"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import constant from '~/constant'
import TopNaviBarVue from '~/components/TopNaviBar.vue'

export default {
  layout: 'empty',
  components: {
    TopNaviBarVue,
  },
  data() {
    return {
      message: '',
      messages: [],
      connection: null,
      recipientId: '',
      userId: '',
      user: {},
      recipient: {},
      conversations: [],
      popup: {
        visible: false,
        name: '',
        y: 0,
      },
    }
  },
  mounted() {
    const id = this.$route.params.id
    this.userId = localStorage.getItem('userId')
    this.user = JSON.parse(localStorage.getItem('user'))

    axios({
      method: 'get',
      url: `${constant.base_url}/user/${id}`,
      headers: {
        'ngrok-skip-browser-warning': 'skip-browser-warning',
      },
    }).then((res) => {
      this.recipient = res.data
    })

    axios({
      method: 'post',
      url: `${constant.base_url}/chat/load`,
      headers: {
        'ngrok-skip-browser-warning': 'skip-browser-warning',
      },
      data: {
        senderId: this.userId,
        receiverId: id,
      },
    }).then((res) => {
      console.log(res.data)
      this.messages = res.data
    })

    const authorization = `Bearer ${localStorage.getItem('accessToken')}`
    axios({
      method: 'get',
      url: `${constant.base_url}/chat/conversations`,
      headers: {
        'ngrok-skip-browser-warning': 'skip-browser-warning',
        Authorization: authorization,
      },
    }).then((res) => {
      console.log(res.data)
      this.conversations = res.data
    })

    this.connection = new WebSocket('ws://localhost:5000')

    this.connection.onopen = () => {
      this.recipientId = id

      setTimeout(() => {
        this.connection.send(
          JSON.stringify({ type: 'clientId', clientId: this.userId })
        )
      }, 100)
    }

    this.connection.onmessage = (event) => {
      const data = event.data
      if (data instanceof Blob) {
        const reader = new FileReader()
        reader.onload = () => {
          const msg = reader.result
          const msgObj = JSON.parse(msg)
          this.messages.push(msgObj)
        }
        reader.readAsText(data)
      } else {
        const msg = JSON.parse(data)
        this.messages.push(msg)
      }
    }

    this.connection.onclose = () => {
      console.log('Disconnected from server')
    }
  },
  methods: {
    sendMessage() {
      if (this.message.trim() !== '') {
        const msg = JSON.stringify({
          type: 'privateMessage',
          recipientId: this.recipientId,
          senderId: this.userId,
          content: this.message,
        })

        const SentTime = new Date().toISOString() // Ensure SentTime is in ISO format
        axios({
          method: 'post',
          url: `${constant.base_url}/chat/send`,
          data: {
            receiverId: this.recipientId,
            senderId: this.userId,
            content: this.message,
            SentTime,
          },
        })
          .then((response) => {
            console.log('Message sent:', response.data)
          })
          .catch((error) => {
            console.error('Error sending message:', error)
          })
          .finally(() => {
            console.log(JSON.parse(msg))
          })

        this.connection.send(msg)
        this.message = ''
      }
    },
    toConversationWith(id) {
      this.$router.push(`/chat/${id}`)
    },
    showPopup(conversation, event) {
      const rect = event.target.getBoundingClientRect()
      this.popup.visible = true
      this.popup.name = conversation.name
      this.popup.y = rect.top
      console.log('show', this.popup)
    },
    hidePopup() {
      this.popup.visible = false
    },
  },
}
</script>

<style lang="scss" scoped>
.chat-container {
  height: calc(100vh - 80px);

  &__content {
    height: calc(100% - 50px);
  }
}
</style>
