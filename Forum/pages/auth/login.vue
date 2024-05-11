<template>
  <div class="relative flex flex-col items-center h-[100vh]">
    <TopNaviBarGuest />
    <!-- <div class="absolute w-full h-full border-2"></div> -->
    <div class="z-10 flex justify-start gap-[80px]">
      <form
        action=""
        class="flex flex-col form gap-7 py-[60px] justify-center items-center w-[400px] rounded-md px-10"
        @keydown.enter="userLogin"
      >
        <div class="text-3xl font-bold text-gray-700">Sign in</div>
        <div class="w-full flex flex-col gap-2">
          <label for="" class="text-sm text-gray-700 font-medium">Email</label>
          <input
            v-model="login.email"
            type="text"
            class="focus:outline-0 text-gray-700 h-[50px] w-full rounded-md pl-5 border-2"
            placeholder="Email"
            :class="{ invalid: !validateEmail }"
            required
          />
        </div>
        <div class="w-full relative flex flex-col gap-2">
          <label for="" class="text-sm text-gray-700 font-medium"
            >Password</label
          >
          <input
            v-model="login.password"
            :type="isShowPassword ? 'text' : 'password'"
            class="focus:outline-0 text-gray-700 h-[50px] w-full rounded-md pl-5 pr-8 border-2"
            placeholder="Password"
            required
          />
          <img
            v-if="isShowPassword"
            src="~assets/icon/eye.svg"
            class="absolute w-[20px] h-[16px] right-[10px] bottom-[17px] cursor-pointer"
            alt=""
            @click="toggleShowPassword()"
          />
          <img
            v-else
            src="~assets/icon/eye-slash.svg"
            class="absolute w-[20px] h-[16px] right-[10px] bottom-[17px] cursor-pointer"
            alt=""
            @click="toggleShowPassword()"
          />
        </div>
        <hr />
        <div class="flex justify-between w-full">
          <button
            class="text-sm text-gray-700"
            type="button"
            @click.prevent="toSignup"
          >
            Đăng ký
          </button>
          <button
            class="text-sm text-[#FF4B26] font-medium"
            type="button"
            @click.prevent="toFogotPassword"
          >
            Quên mật khẩu?
          </button>
        </div>
        <div class="flex justify-center items-center w-full">
          <button
            type="button"
            class="text-[16px] font-bold text-white bg-[#FF4401] rounded-[25px] py-[8px] px-[40px]"
            @click="userLogin()"
          >
            Đăng nhập
          </button>
        </div>
      </form>
      <img src="~/assets/icon/login-decor.svg" class="w-[40vw]" />
    </div>
    <modal-alert
      v-if="alert.isShowModal"
      :width="480"
      v-bind="alert"
      @close="onCloseModal"
    />
  </div>
</template>

<script>
import axios from 'axios'
import ModalAlert from '~/components/Modal/ModalAlert.vue'
import TopNaviBarGuest from '~/components/TopNaviBarGuest.vue'
import constant from '~/constant'
export default {
  components: { ModalAlert, TopNaviBarGuest },
  layout: 'empty',
  data() {
    return {
      alert: {
        isShowModal: false,
        title: 'Xác nhận',
        type: 'confirm',
        content: 'Cần được xác nhận',
        buttonCancelContent: '',
        buttonOkContent: 'Ok',
        typeSubmit: '',
      },
      login: {
        email: '',
        password: '',
      },
      isShowPassword: false,
    }
  },
  computed: {
    validateEmail() {
      const regex =
        /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|.(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
      if (this.login.email) return this.login.email.toLowerCase().match(regex)
      else return true
    },
    checkData() {
      return this.login.email && this.login.password
    },
  },
  methods: {
    toggleShowPassword() {
      this.isShowPassword = !this.isShowPassword
    },

    userLogin() {
      if (!this.validateEmail || !this.checkData) {
        if (!this.validateEmail)
          this.$notify({
            group: 'foo',
            title: 'Lỗi',
            text: 'Vui lòng điền email đúng định dạng',
            type: 'error',
          })
        else
          this.$notify({
            group: 'foo',
            title: 'Lỗi',
            text: 'Vui lòng điền đầy đủ thông tin',
            type: 'error',
          })
      } else
        try {
          axios({
            method: 'post',
            url: `${constant.base_url}/auth/login`,
            data: {
              email: this.login.email.toLowerCase().trim(),
              password: this.login.password,
            },
          })
            .then( (res) => {
              const token = `${res.data.token}`
              localStorage.setItem('accessToken', token)
              localStorage.setItem('userId', res.data.user.User_id)
              localStorage.setItem('user', res.data.user)
              this.$router.push('/')
            })
            .catch((err) => {
              this.alert = {
                ...this.alert,
                ...{
                  isShowModal: true,
                  title: 'Lỗi',
                  buttonOkContent: 'Đóng',
                  content: err.response.data.error,
                  type: 'failed',
                },
              }
            })
        } catch (err) {
          console.log(err)
        }
    },
    toSignup() {
      this.$router.push('/auth/signup')
    },
    toFogotPassword() {
      this.$router.push('/auth/forgot-password')
    },
    onCloseModal(typeSubmit) {
      switch (typeSubmit) {
        case '':
          this.resetAlert()
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

<style lang="scss" scoped>
@import '~assets/scss/variables.scss';
</style>
