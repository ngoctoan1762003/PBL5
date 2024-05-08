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
        <div class="text-3xl font-bold text-gray-700">Đăng ký</div>
        <div class="w-full flex flex-col gap-2">
          <label for="" class="text-sm text-gray-700 font-medium">Email</label>
          <input
            v-model="email"
            type="text"
            class="focus:outline-0 text-gray-700 h-[50px] w-full rounded-md pl-5 border-2"
            placeholder="Email"
            :class="{ invalid: !validateEmail }"
          />
        </div>
        <div class="w-full relative flex flex-col gap-2">
          <label for="" class="text-sm text-gray-700 font-medium"
            >Mật khẩu</label
          >
          <input
            v-model="password"
            :type="isShowPassword ? 'text' : 'password'"
            class="focus:outline-0 text-gray-700 h-[50px] w-full rounded-md pl-5 pr-8 border-2"
            placeholder="Mật khẩu"
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
        <div class="w-full relative flex flex-col gap-2">
          <label for="" class="text-sm text-gray-700 font-medium"
            >Xác nhận mật khẩu</label
          >
          <input
            v-model="password_confirm"
            :type="isShowPasswordConfirm ? 'text' : 'password'"
            class="focus:outline-0 text-gray-700 h-[50px] w-full rounded-md pl-5 pr-8 border-2"
            placeholder="Xác nhận mật khẩu"
            :class="{ invalid: !validateMatchPassword }"
          />
          <img
            v-if="isShowPasswordConfirm"
            src="~assets/icon/eye.svg"
            class="absolute w-[20px] h-[16px] right-[10px] bottom-[17px] cursor-pointer"
            alt=""
            @click="toggleShowPasswordConfirm()"
          />
          <img
            v-else
            src="~assets/icon/eye-slash.svg"
            class="absolute w-[20px] h-[16px] right-[10px] bottom-[17px] cursor-pointer"
            alt=""
            @click="toggleShowPasswordConfirm()"
          />
        </div>
        <hr />
        <div class="flex justify-between w-full">
          <button
            class="text-sm text-[#FF4B26] font-medium"
            @click.prevent="toSignin"
          >
            Đi đến đăng nhập
          </button>
        </div>
        <div class="flex justify-center items-center w-full">
          <button
            type="button"
            @click="submit"
            class="text-[16px] font-bold text-white bg-[#FF4401] rounded-[25px] py-[8px] px-[40px]"
          >
            Đăng ký
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
  </div>
</template>

<script>
import axios from 'axios'
import constant from '~/constant'
import ModalAlert from '~/components/Modal/ModalAlert.vue'
import TopNaviBarGuest from '~/components/TopNaviBarGuest.vue'
export default {
  components: { ModalAlert, TopNaviBarGuest },
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
      if (
        !this.checkData ||
        !this.validateEmail ||
        !this.validateMatchPassword
      ) {
        if (!this.checkData) {
          this.$notify({
            title: 'Lỗi',
            text: 'Vui lòng điền đầy đủ thông tin',
            type: 'error',
            group: 'foo',
          })
        } else if (!this.validateEmail) {
          this.$notify({
            group: 'foo',
            title: 'Lỗi',
            text: 'Vui lòng điền email đúng định dạng',
            type: 'error',
          })
        } else {
          this.$notify({
            group: 'foo',
            title: 'Lỗi',
            text: 'Password confirm không khớp',
            type: 'error',
          })
        }
      } else {
        axios({
          method: 'post',
          url: `${constant.base_url}/auth/register`,
          data: {
            email: this.email.toLowerCase().trim(),
            password: this.password,          
            username: "nonee",
            name: "nonee",
            phone: "00000000",
            address: "none",
            role: "user",
            isactive: "1",
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
          })
          .catch((res) => {
            this.alert = {
              ...this.alert,
              ...{
                isShowModal: true,
                title: 'Thất bại',
                content: res.response.data.message[0].message,
                type: 'failed',
                buttonOkContent: 'Đóng',
              },
            }
          })
      }
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
