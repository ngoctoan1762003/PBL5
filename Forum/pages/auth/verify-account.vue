<template>
  <div class="relative flex flex-col items-center h-[100vh]">
    <!-- <img src="~/assets/img/Cool-Background-GIF.gif" alt="" class="absolute w-full h-full"> -->
    <!-- <div class="absolute w-full h-full bg-[#2C353D]"></div> -->
    <TopNaviBarGuest />
    <div class="z-10 flex gap-[80px]">
      <form
        action=""
        class="flex flex-col form gap-5 py-[30px] justify-center items-center w-[400px] rounded-md px-10"
      >
        <div class="text-3xl font-bold text-gray-700">
          Nhập mã xác nhận được gửi qua email
        </div>
        <div class="w-full flex flex-col gap-2">
          <label for="" class="text-sm text-gray-700 font-medium"
            >Mã xác nhận</label
          >
          <input
            v-model="code"
            type="text"
            class="focus:outline-0 text-gray-700 h-[50px] w-full rounded-md pl-5 border-2"
            placeholder="Mã xác nhận"
            :class="{ invalid: !validateEmail }"
          />
        </div>

        <hr />
        <div class="flex justify-center items-center w-full">
          <button
            type="button"
            @click="submit"
            class="text-[16px] font-bold text-white bg-[#FF4401] rounded-[25px] py-[8px] px-[40px]"
          >
            Xác nhận
          </button>
        </div>
      </form>
      <img src="~/assets/icon/login-decor.svg" class="w-[40vw]" />
    </div>
    <modal-alert
      v-if="alert.isShowModal"
      v-bind="alert"
      @close="onCloseModal"
    />
    <div
      v-if="isLoading"
      class="flex justify-center items-center w-screen h-screen bg-black opacity-70 absolute z-[10]"
    >
      <LoadingSpinner />
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import constant from '~/constant'
import ModalAlert from '~/components/Modal/ModalAlert.vue'
import TopNaviBarGuest from '~/components/TopNaviBarGuest.vue'
import LoadingSpinner from '~/components/Animation/LoadingSpinner.vue'

export default {
  components: { ModalAlert, TopNaviBarGuest, LoadingSpinner },
  layout: 'empty',
  data() {
    return {
      email: '',
      password: '',
      password_confirm: '',
      isShowPassword: false,
      isShowPasswordConfirm: false,
      alert: {
        isShowModal: false,
        title: 'Xác nhận',
        type: 'failed',
        content: 'Cần được xác nhận',
        buttonCancelContent: '',
        buttonOkContent: 'Ok',
        typeSubmit: '',
      },
      code: '',
      isLoading: false,
    }
  },
  computed: {
    validateEmail() {
      const regex =
        /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|.(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
      if (this.email) return this.email.toLowerCase().match(regex)
      else return true
    },
    validateMatchPassword() {
      if (this.password_confirm) return this.password_confirm === this.password
      else return true
    },
    checkData() {
      return this.email && this.password && this.password_confirm
    },
  },
  methods: {
    submit() {
      this.isLoading = true
      const email = localStorage.getItem('signupEmail')
      const password = localStorage.getItem('signupPassword')
      axios({
        method: 'post',
        url: `${constant.base_url}/auth/check/${email}`,
        data: {
          activation_code: this.code,
          password,
        },
      })
        .then((res) => {
          this.alert = {
            ...this.alert,
            ...{
              isShowModal: true,
              title: 'Thành công',
              content:
                'Bạn đã đăng kí thành công, hãy đăng nhập để sử dụng trang web',
              type: 'success',
              buttonOkContent: 'Đến sign in',
              typeSubmit: 'gotologin',
            },
          }
          localStorage.removeItem('signupEmail')
          localStorage.removeItem('signupPassword')
        })
        .catch((res) => {
          this.alert = {
            ...this.alert,
            ...{
              isShowModal: true,
              title: 'Thất bại',
              content: res.response,
              type: 'failed',
              buttonOkContent: 'Đóng',
            },
          }
        })
        .finally(() => {
          this.isLoading = false
        })
    },
    toSignin() {
      this.$router.push('/auth/login')
    },
    toggleShowPassword() {
      this.isShowPassword = !this.isShowPassword
    },
    toggleShowPasswordConfirm() {
      this.isShowPasswordConfirm = !this.isShowPasswordConfirm
    },
    toFogotPassword() {
      this.$router.push('/auth/forgot-password')
    },
    onCloseModal(typeSubmit) {
      switch (typeSubmit) {
        case 'gotologin':
          this.$router.push('/auth/login')
          break
        default:
          this.resetAlert()
          break
      }
    },
    resetAlert() {
      this.alert = {
        isShowModal: false,
        title: '',
        type: 'failed',
        content: '',
        buttonCancelContent: '',
        buttonOkContent: '',
        typeSubmit: '',
      }
    },
  },
}
</script>
