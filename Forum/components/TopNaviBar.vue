<template>
  <div class="top-nav">
    <div class="top-nav__logo" @click="$router.push('/')">
      <img src="~assets/icon/Logo.svg" alt="" />
      <div class="name-web">BOOK</div>
      <div class="top-nav__link ml-2">
        <img class="top-nav__link__icon" src="~assets/icon/Facebook.svg" alt="" />
        <img class="top-nav__link__icon" src="~assets/icon/Twitter.svg" alt="" />
        <img class="top-nav__link__icon" src="~assets/icon/LinkedIn.svg" alt="" />
      </div>
    </div>
    
    <div class="top-nav__option">
        <div class="top-nav__option__element">Trang chủ</div>
        <div class="top-nav__option__element">Sách</div>
        <div class="top-nav__option__element">Về chúng tôi</div>
        <div class="top-nav__option__element">Dịch vụ</div>
        <div class="top-nav__option__element">Liên hệ</div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
@import '~assets/scss/variables.scss';

.top-nav {
  display: inline-flex;
  padding: 20px 80px;
  flex-direction: row;
  align-items: center;
  gap: 84px;
  background: #1B3764;
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
    }
  }

  &__link {
    display: flex;
    gap: 10px;

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
