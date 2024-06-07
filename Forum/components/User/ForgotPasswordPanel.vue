<template>
  <div class="min-w-[300px]">
    <div
      class="relative text-[#1B3764] font-semibold text-[21px] bg-[#FFCA42] py-3 px-5"
    >
      <div>Nhập email tài khoản</div>
      <img
        class="absolute right-5 top-[30%] w-[20px] h-[20px] cursor-pointer"
        @click="cancel()"
        src="~/assets/icon/x.svg"
        alt=""
      />
    </div>
    <div class="bg-white p-10 flex flex-col gap-5">
      <div>Email</div>
      <div>
        <input type="text" v-model="email" class="px-3 py-2 border-[1px] border-gray-300 rounded-md min-w-[200px] w-full"/>
      </div>
      <button
        class="text-[#1B3764] font-semibold text-[14px] text-center bg-[#FFCA42] py-3 px-5"
        @click="submit"
      >
        Xác nhận
      </button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import constant from '~/constant'
export default {
  props: {
    book: Object,
    amount: Number,
  },
  data() {
    return {
      isLoading: true,
      email: '',
    }
  },
  created() {
    this.isLoading = false
  },
  methods: {
    cancel() {
      this.$emit('cancel')
    },
    getPriceFormat(price) {
      if (this.amount === 0) return '' // Return empty string if book is not defined
      const formattedPrice = price
        .toString()
        .replace(/\B(?=(\d{3})+(?!\d))/g, '.')
      return `${formattedPrice} VND`
    },
    submit() {
      //   const authorization = `Bearer ${localStorage.getItem('accessToken')}`
      axios({
        method: 'post',
        url: `${constant.base_url}/auth/reset_password/${this.email}`,
      })
        .then((res) => {
          this.$notify({
            title: 'Thành công',
            text: 'Vui lòng kiểm tra email để tiến hành đổi mật khẩu',
            type: 'success',
            group: 'foo',
          })
          this.$emit('done')
        })
        .catch((error) => {
          if (!error.response?.data?.error.startsWith('Blog'))
            this.$notify({
              title: 'Thất bại',
              text: error.response,
              type: 'error',
              group: 'foo',
            })
        })
    },
  },
  computed: {},
}
</script>