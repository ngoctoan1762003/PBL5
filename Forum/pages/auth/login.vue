<template>
  <div class="relative flex flex-col items-center h-[100vh]">
    <TopNaviBarGuest />
    <div class="absolute w-[100vw] h-[100vh] flex justify-center items-center z-[100]" v-show="isForgotPassword">
      <div class="absolute w-[100vw] h-[100vh] bg-gray-500 opacity-50"></div>
      <forgot-password-panel-vue @cancel="isForgotPassword = false" @done="isForgotPassword = false" class="z-[10] min-w-[400px]"/>
    </div>
    <!-- <div class="absolute w-full h-full border-2"></div> -->
    <div class="z-10 flex justify-start gap-[80px]">
      <form
        action=""
        class="flex flex-col form gap-7 py-[60px] justify-center items-center w-[400px] rounded-md px-10"
        @keydown.enter="userLogin"
      >
        <div class="text-3xl font-bold text-gray-700">Đăng nhập</div>
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
            >Mật khẩu</label
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
          <!-- <googleSignIn
            :clientId="'924458972373-8fjviiu7k2dqkn3uo6ob1ab3seom2fob.apps.googleusercontent.com'"
            :successCallBack="getSuccessData"
            :failureCallBack="getFailureData"
          /> -->
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
// import googleSignIn from 'google-signin-vue'
import ModalAlert from '~/components/Modal/ModalAlert.vue'
import TopNaviBarGuest from '~/components/TopNaviBarGuest.vue'
import constant from '~/constant'
import LoadingSpinner from '~/components/Animation/LoadingSpinner.vue'
import ForgotPasswordPanelVue from '~/components/User/ForgotPasswordPanel.vue'

// import gAuthPlugin from 'vue3-google-oauth2';

export default {
  components: {
    ModalAlert,
    TopNaviBarGuest,
    // googleSignIn,
    LoadingSpinner,
    ForgotPasswordPanelVue,
  },
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
      isLoading: false,
      isForgotPassword: false,
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
    getSuccessData: function (user) {
      console.log(user)
    },
    getFailureData: function (errorData) {
      console.log(errorData)
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
          this.isLoading = true
          axios({
            method: 'post',
            url: `${constant.base_url}/auth/login`,
            data: {
              email: this.login.email.toLowerCase().trim(),
              password: this.login.password,
            },
          })
            .then((res) => {
              const token = `${res.data.token}`
              localStorage.setItem('accessToken', token)
              const userId = res.data.user.User_id
              localStorage.setItem('userId', userId)
              this.$router.push('/')
              axios({
                method: 'get',
                url: `${constant.base_url}/user/${userId}`,
                headers: {
                  'ngrok-skip-browser-warning': 'skip-browser-warning',
                },
              }).then((result) => {
                localStorage.setItem('user', JSON.stringify(result.data))
              })
            })
            .catch((err) => {
              console.log(err.response.data)
              if (err.response.data.error === 'account has been ban'){
                this.$notify({
                  group: 'foo',
                  title: 'Lỗi',
                  text: 'Tài khoản đã bị khóa',
                  type: 'error',
                })
                return
              }
              this.$notify({
                group: 'foo',
                title: 'Lỗi',
                text: 'Sai tài khoản hoặc mật khẩu',
                type: 'error',
              })
              this.alert = {
                ...this.alert,
                ...{
                  isShowModal: true,
                  title: 'Lỗi',
                  buttonOkContent: 'Đóng',
                  content: err.response.error,
                  type: 'failed',
                },
              }
            })
            .finally(() => {
              this.isLoading = false
            })
        } catch (err) {
          console.log(err)
        }
    },
    toSignup() {
      this.$router.push('/auth/signup')
    },
    toFogotPassword() {
      this.isForgotPassword = true;
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
