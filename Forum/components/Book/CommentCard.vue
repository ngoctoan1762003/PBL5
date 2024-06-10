<template>
  <div class="flex flex-col gap-5">
    <div class="flex items-center gap-5">
      <img class="w-[60px] rounded-full" :src="user.image" alt="" />
      <div class="flex flex-col gap-1">
        <div
          class="bg-[#FFFFFF] px-5 py-3 font-semibold rounded-[20px] text-[#1B3764] shadow-md"
        >
          <div
            class="font-bold mb-2 cursor-pointer"
            @click="GoToDetails(user._id)"
          >
            {{ user.Name }}
          </div>
          <div v-html="comment.content"></div>
        </div>
        <div class="flex gap-6 pl-3">
          <div class="relative">
            <button
              class="text-[13px] font-semibold text-[#969AA0]"
              @click="likeComment()"
            >
              Thích
            </button>
            <div
              class="absolute right-[-15px] top-[5px] text-gray-500 text-[10px] font-semibold bg-blue-500 text-white px-1 py-[1px] rounded-md"
            >
              {{ comment.like }}
            </div>
          </div>
          <button
            class="text-[13px] font-semibold text-[#969AA0]"
            @click="showCommentBox($event)"
          >
            Bình luận
          </button>
        </div>
      </div>
    </div>
    <div v-for="c in comment.replies" :key="c._id" class="ml-20">
      <ReplyCard :comment="c" :user_id="c.user_id" />
    </div>
    <CommentBox
      @send="send"
      :bookId="comment.book_id"
      :parentCommentId="comment._id"
      :commentUserId="user_id"
      :sellerId="sellerId"
      v-show="comment.isVisible"
    />
  </div>
</template>

<script>
import axios from 'axios'
import ReplyCard from '../Book/ReplyCard.vue'
import constant from '~/constant'
import CommentBox from '~/components/Blog/CommentBox.vue'

export default {
  components: {
    ReplyCard,
    CommentBox,
  },
  props: {
    comment: {
      type: Object,
    },
    user_id: {
      type: String,
    },
    sellerId: {
      type: String,
    },
  },
  data() {
    return {
      user: Object,
    }
  },
  mounted() {
    axios({
      method: 'get',
      url: `${constant.base_url}/user/${this.user_id}`,
      headers: {
        'ngrok-skip-browser-warning': 'skip-browser-warning',
        // Authorization: authorization
      },
    })
      .then((res) => {
        console.log(res.data)
        this.user = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  },
  methods: {
    GoToDetails(id) {
      this.$router.push(`/user/${id}`)
    },
    showCommentBox(event) {
      console.log(this.comment._id)
      this.$emit('showCommentBox', event, this.comment._id)
    },
    send() {
      this.$emit('send')
    },
    likeComment() {
      const authorization = `Bearer ${localStorage.getItem('accessToken')}`
      axios({
        method: 'put',
        url: `${constant.base_url}/comment/like/${this.comment._id}`,
        headers: {
          Authorization: authorization,
        },
      }).then((res) => {
        this.$emit('send')
        this.$notify({
          title: 'Thành công',
          text: 'Like thành công',
          type: 'success',
          group: 'foo',
        })
      })
    },
  },
}
</script>