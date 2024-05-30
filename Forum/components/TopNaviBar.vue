<template>
  <div class="top-nav relative">
    <div class="top-nav__logo" @click="$router.push('/')">
      <img src="~assets/icon/Logo.svg" alt="" />
      <div class="name-web">BOOK</div>
      <div class="top-nav__link ml-2 relative">
        <img
          class="top-nav__link__icon"
          src="~assets/icon/Facebook.svg"
          alt=""
        />
        <img
          class="top-nav__link__icon"
          src="~assets/icon/Twitter.svg"
          alt=""
        />
        <img
          class="top-nav__link__icon"
          src="~assets/icon/LinkedIn.svg"
          alt=""
        />
        <img
          class="top-nav__link__icon w-[25px] h-[25px]"
          src="~/assets/icon/sell.svg"
          alt=""
          v-if="user.Role === 'seller'"
          @click="toSellerPage"
        />
        <img
          src="~/assets/icon/cart.svg"
          class="cursor-pointer w-[25px] h-[25px]"
          @click="toCart"
          alt=""
        />
        <img
          src="~/assets/icon/message.svg"
          class="cursor-pointer w-[25px] h-[25px]"
          @click="toMessage"
          alt=""
        />
        <div class="relative">
          <img
            class="w-[25px] h-[25px]"
            src="~/assets/icon/notification.svg"
            alt=""
            @click="showNotify"
          />
          <div
            v-show="newNotifyCount > 0"
            class="rounded-full w-[15px] h-[15px] absolute top-[-5px] right-[-5px] bg-red-500 text-white text-[10px] flex justify-center items-center pointer-events-none"
          >
            {{ newNotifyCount }}
          </div>
        </div>
        <div
          class="absolute z-[10] max-h-[90vh] overflow-y-scroll right-0 top-[40px] bg-[#FFFFFF] px-5 py-3 font-semibold rounded-[20px] text-[#1B3764] shadow-md flex flex-col gap-2"
          v-show="isShowNotify"
        >
          <div
            v-for="noti in notifications"
            :key="noti._id"
            :class="{ 'text-gray-300': noti.isNew === 0 }"
          >
            {{ noti.content }}
            <div class="border-b-[1px] border-gray-500"></div>
          </div>
        </div>
      </div>
    </div>

    <div class="relative top-nav__option items-center">
      <div class="top-nav__option__element">Trang chủ</div>
      <div class="top-nav__option__element">Sách</div>
      <div class="top-nav__option__element">Về chúng tôi</div>
      <div class="top-nav__option__element">Dịch vụ</div>
      <div class="top-nav__option__element">Liên hệ</div>
      <img
        :src="user.image"
        @click="isShowOption = !isShowOption"
        class="flex justify-center items-center cursor-pointer w-[40px] h-[40px] rounded-full"
      />
      <div
        class="absolute top-[50px] right-[0px] bg-[#FFFFFF] px-5 py-3 font-semibold rounded-[20px] text-[#1B3764] shadow-md flex flex-col gap-3 items-center z-[10]"
        v-show="isShowOption"
      >
        <div class="text-[14px] cursor-pointer" @click="toUserDetail()">
          Thông tin
        </div>
        <div class="text-[14px] cursor-pointer" @click="logout()">
          Đăng xuất
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import constant from '~/constant'
export default {
  data() {
    return {
      user: Object,
      isShowOption: false,
      isShowNotify: false,
      notifications: [],
    }
  },
  computed: {
    newNotifyCount() {
      return this.notifications.filter((noti) => noti.isNew === 1).length
    },
  },
  mounted() {
    const userId = localStorage.getItem('userId')
    const authorization = `Bearer ${localStorage.getItem('accessToken')}`
    axios({
      method: 'get',
      url: `${constant.base_url}/user/${userId}`,
      headers: {
        'ngrok-skip-browser-warning': 'skip-browser-warning',
      },
    }).then((res) => {
      console.log(res.data)
      this.user = res.data
    })

    axios({
      method: 'get',
      url: `${constant.base_url}/notification/all_notif`,
      headers: {
        'ngrok-skip-browser-warning': 'skip-browser-warning',
        Authorization: authorization,
      },
    }).then((res) => {
      console.log(res.data)
      this.notifications = res.data.reverse()
    })
  },

  methods: {
    toUserDetail() {
      this.$router.push('/user/profile')
    },
    toSellerPage() {
      const id = localStorage.getItem('userId')
      this.$router.push(`/seller/${id}`)
    },
    logout() {
      localStorage.removeItem('accessToken')
      localStorage.removeItem('user')
      localStorage.removeItem('userId')
      this.$router.push('/auth/login')
    },
    showNotify() {
      this.isShowNotify = !this.isShowNotify
      // const userId = localStorage.getItem('userId')

      const authorization = `Bearer ${localStorage.getItem('accessToken')}`
      if (this.isShowNotify) {
        axios({
          method: 'put',
          url: `${constant.base_url}/notification/clear/all`,
          headers: {
            Authorization: authorization,
          },
        }).then((res) => {
          axios({
            method: 'get',
            url: `${constant.base_url}/notification/all_notif`,
            headers: {
              'ngrok-skip-browser-warning': 'skip-browser-warning',
              Authorization: authorization,
            },
          }).then((res) => {
            console.log(res.data)
            this.notifications = res.data.reverse()
          })
        })
      }
    },
    toCart() {
      this.$router.push('/cart')
    },
    toMessage() {
      this.$router.push('/chat')
    },
  },
}
</script>

<style lang="scss" scoped>
// @import '~assets/scss/variables.scss';

.top-nav {
  display: inline-flex;
  padding: 20px 80px;
  flex-direction: row;
  align-items: center;
  gap: 84px;
  background: #1b3764;
  height: 80px;
  width: 100%;
  justify-content: space-between;

  &__logo {
    height: 100%;
    display: flex;
    align-items: center;
    gap: 10px;
    cursor: pointer;

    img {
      height: 60%;
      object-fit: contain;
    }

    .name-web {
      color: white;
      font-family: 'Montserrat', sans-serif;
      font-size: 26px;
      font-style: normal;
      font-weight: 700;
      line-height: 38px;
      /* 146.154% */
    }
  }

  &__option {
    display: flex;
    gap: 30px;

    &__element {
      color: white;
      font-size: 14px;
      font-weight: 500;
      cursor: pointer;
    }
  }

  &__link {
    display: flex;
    gap: 10px;
    align-items: center;

    &__icon {
      width: 35px;
      height: 35px;
    }
  }

  //   &__main {
  //     display: flex;
  //     align-items: flex-start;
  //     justify-content: space-between;
  //     gap: 50px;
  //     height: 100%;
  //     width: 100%;
  //     flex: 1;

  //     &__left {
  //       display: flex;
  //       justify-content: flex-start;
  //       align-items: center;
  //       flex: 1 0 0;
  //       gap: 17px;
  //     }

  //     &__menu {
  //       display: flex;
  //       align-items: flex-start;
  //       gap: 20px;
  //       cursor: pointer;

  //       .menu__item {
  //         display: flex;
  //         justify-content: center;
  //         align-items: center;
  //         padding: 10px;
  //         border-radius: 8px;

  //         &.isActive {
  //           background: $orange;
  //         }

  //         img {
  //           display: flex;
  //           align-items: flex-start;
  //           gap: 10px;
  //         }
  //       }
  //     }

  //     &__right {
  //       height: 100%;
  //       display: flex;
  //       align-items: center;

  //       gap: 25px;

  //       .notification {
  //         display: flex;
  //         width: 20px;
  //         height: 20px;
  //         justify-content: center;
  //         align-items: center;

  //         img {
  //           width: 100%;
  //           height: 100%;
  //           object-fit: contain;
  //           cursor: pointer;
  //         }
  //       }

  //       .account {
  //         display: flex;
  //         justify-content: center;
  //         align-items: center;
  //         height: 100%;
  //         gap: 10px;
  //         padding-right: 10px;
  //         position: relative;
  //         cursor: pointer;
  //         margin-right: 40px;

  //         img {
  //           height: 100%;
  //           object-fit: contain;
  //         }

  //         .name {
  //           color: #f7f7f7;
  //           font-size: 14px;
  //           font-style: normal;
  //           font-weight: 500;
  //           line-height: 24px;
  //           /* 150% */
  //         }

  //         .icon-drop-down {
  //           position: absolute;
  //           right: -10px;
  //           top: 50%;
  //           transform: translateY(-50%);
  //         }

  //         .dropdown-menu {
  //           position: absolute;
  //           display: inline-flex;
  //           right: -20px;
  //           top: 40px;
  //           flex-direction: column;
  //           background: $gray;
  //           padding: 6px 12px;
  //           border-radius: 8px;
  //           width: 100%;

  //           .item {
  //             display: flex;
  //             width: 100%;
  //             padding: 6px 12px;
  //             color: $orange;
  //             border-radius: 8px;

  //             &:hover {
  //               color: $gray;
  //               background: $orange;
  //             }
  //           }
  //         }
  //       }
  //     }
  //   }
}
</style>
