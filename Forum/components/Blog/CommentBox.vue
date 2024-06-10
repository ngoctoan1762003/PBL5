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
    commentUserId: {
      type: String,
      default: '',
    },
    sellerId: {
      type: String,
      default: '',
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
      if (!localStorage.getItem('accessToken')){
        this.$notify({
          title: 'Lỗi',
          text: 'Bạn phải đăng nhập để bình luận',
          type: 'error',
          group: 'foo',
        })
        return
      }
      const authorization = localStorage.getItem('accessToken')
      const userId = localStorage.getItem('userId')
      const user = JSON.parse(localStorage.getItem('user'))
      console.log(user)

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
          .then((res) => {
            this.$notify({
              title: 'Thành công',
              text: 'Bình luận thành công',
              type: 'success',
              group: 'foo',
            })

            if (this.commentUserId !== '') {
              console.log("for comment", this.sellerId, user.Name)
              axios({
                method: 'post',
                url: `${constant.base_url}/notification/new_notif`,
                data: {
                  receiver_id: this.commentUserId,
                  content: `${user.Name} đã bình luận về bình luận của bạn`,
                },
              })
            }

            console.log("for seller", this.sellerId, user.Name)
            axios({
              method: 'post',
              url: `${constant.base_url}/notification/new_notif`,
              data: {
                receiver_id: this.sellerId,
                content: `${user.Name} đã bình luận về sách của bạn`,
              },
            })

            this.$emit('send')
          })
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
