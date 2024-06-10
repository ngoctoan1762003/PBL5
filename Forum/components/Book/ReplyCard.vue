<template>
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
            :class="{ 'text-blue-500': isLikedByCurrentUser(comment) }"
          >
            Thích
          </button>
          <div
            class="absolute right-[-18px] top-[5px] text-gray-500 text-[10px] font-semibold bg-blue-500 text-white px-1 py-[1px] rounded-md"
          >
            {{ comment.like.length }}
          </div>
        </div>
        <button
          class="text-[13px] font-semibold text-red-500"
          v-show="currentUserId === user._id"
          @click="deleteComment()"
        >
          Xóa
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import constant from '~/constant'

export default {
  components: {},
  props: {
    comment: {
      type: Object,
    },
    user_id: {
      type: String,
    },
  },
  data() {
    return {
      user: Object,
      currentUserId: '',
    }
  },
  computed: {
    isLikedByCurrentUser() {
      return (comment) => comment.like.includes(this.currentUserId)
    },
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
    this.currentUserId = localStorage.getItem('userId')
  },
  methods: {
    submitComment() {},
    GoToDetails(id) {
      this.$router.push(`/user/${id}`)
    },
    likeComment() {
      if (!localStorage.getItem('accessToken')) {
        this.$notify({
          title: 'Lỗi',
          text: 'Bạn phải đăng nhập để thích',
          type: 'error',
          group: 'foo',
        })
        return
      }
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
    deleteComment(id) {
      const authorization = `Bearer ${localStorage.getItem('accessToken')}`
      axios({
        method: 'delete',
        url: `${constant.base_url}/comment/${this.comment._id}`,
        headers: {
          Authorization: authorization,
        },
      }).then((res) => {
        this.$emit('send')
        this.$notify({
          title: 'Thành công',
          text: 'Xóa thành công',
          type: 'success',
          group: 'foo',
        })
      })
    },
  },
}
</script>