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
import TextEditor from '../../components/Blog/TextEditor.vue'
import constant from '~/constant'
export default {
  components: { TextEditor },
  props:{
    bookId: {
      Type: String
    }
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
      if (this.content === "") return;
      const authorization =  localStorage.getItem('accessToken');
      const userId =  localStorage.getItem('userId');
      axios({
        method: 'post',
        url: `${constant.base_url}/comment`,
        headers: {
          Authorization: authorization,
        },
        data: {
          content: this.content,
          book_id: this.bookId,
          user_id: userId,
          parent_comment_id: null
        }
      })
      // this.$emit('comment', this.content)
      this.content = ''
    },
  },
}
</script>

<style lang="scss" scoped></style>
