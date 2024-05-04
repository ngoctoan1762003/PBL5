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
      <div class="flex gap-5 pl-3">
        <button class="text-[13px] font-semibold text-[#969AA0]">Thích</button>
        <button class="text-[13px] font-semibold text-[#969AA0]">
          Bình luận
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import constant from '~/constant'

export default {
  components: {
  },
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
    submitComment() {},
    GoToDetails(id) {
      this.$router.push(`/user/${id}`)
    },
  },
}
</script>