<template>
  <div class="flex-col relative flex justify-end">
    <TextEditor :content="content" @textChange="updateContent" />
    <div
      class="send p-2 flex justify-end bg-[#EBEDF0] border-[1px] border-[#ccc] border-t-0"
      @click="send"
    >
      <img
        src="~/assets/icon/send.svg"
        class="w-6 h-6 mr-[10px] cursor-pointer"
      />
    </div>
  </div>
</template>
<script>
import axios from 'axios'
import TextEditor from '~/components/Blog/TextEditor.vue'
import constant from '~/constant'
export default {
  components: { TextEditor },
  props: {
    bookId: {
      type: String,
    },
    parentCommentId: {
      type: String,
      // default: null,
    },
  },
  data() {
    return {
      content: '',
    }
  },
  methods: {
    updateContent(value) {
      this.content = value
    },
    send() {
      if (this.content === '') return
      const authorization = localStorage.getItem('accessToken')
      const userId = localStorage.getItem('userId')

      try {
        axios({
          method: 'post', // Change method to 'post'
          url: `${constant.base_url}/comment/create`,
          headers: {
            Authorization: authorization,
            'ngrok-skip-browser-warning': 'skip-browser-warning',
            'Content-Type': 'application/json', // Specify Content-Type as application/json
          },
          data: {
            // Send data in the request body
            content: this.content,
            book_id: this.bookId,
            user_id: userId,
            parent_comment_id: this.parentCommentId,
          },
        })
          .then((res) => {})
          .catch((e) => {
            console.log(e)
          })
      } catch (e) {
        console.log(e)
      }
      this.$emit('send')
      this.content = ''
    },
  },
}
</script>

<style lang="scss" scoped></style>
