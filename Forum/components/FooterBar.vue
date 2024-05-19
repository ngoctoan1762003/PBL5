<template>
  <div class="bg-[#1B3764] pt-[50px] pb-[10px] flex flex-col gap-4 justify-center">
    <div class="flex gap-20 justify-center items-start mb-[80px]">
      <div>
        <div class="flex flex-col gap-2">
          <div class="flex gap-5">
            <img class="w-[20px]" src="~/assets/icon/Logo.svg" alt="" />
            <div class="text-white text-[25px] font-semibold">LOGO</div>
          </div>
          <div class="flex gap-3">
            <img
              class="w-[40px] border-[1px] border-[#FFCA42]"
              src="~assets/icon/facebook-blue.svg"
              alt=""
            />
            <img
              class="w-[40px] border-[1px] border-[#FFCA42]"
              src="~assets/icon/twitter-blue.svg"
              alt=""
            />
            <img
              class="w-[40px] border-[1px] border-[#FFCA42]"
              src="~assets/icon/linkedin-blue.svg"
              alt=""
            />
            <img
              class="w-[40px] border-[1px] border-[#FFCA42]"
              src="~assets/icon/insta-blue.svg"
              alt=""
            />
          </div>
        </div>
      </div>
      <div class="footer__section">
        <div class="footer__section__header">Khám phá</div>
        <div class="footer__section__element__container">
          <div class="footer__section__element">Trang chủ</div>
          <div class="footer__section__element">Về chúng tôi</div>
          <div class="footer__section__element">Dịch vụ</div>
          <div class="footer__section__element">Blog</div>
          <div class="footer__section__element">Liên hệ</div>
        </div>
      </div>
      <div class="footer__section">
        <div class="footer__section__header">Sách</div>
        <div class="footer__section__element__container">
          <div class="footer__section__element">Dare to be fearless</div>
          <div class="footer__section__element">Dare to be healthy</div>
          <div class="footer__section__element">Dare to be wealthy</div>
        </div>
      </div>
      <div class="footer__section">
        <div class="footer__section__header">Liên hệ</div>
        <div class="footer__contact">
          <div class="footer__contact__header">Địa chỉ</div>
          <div class="footer__contact__header">:</div>
          <div class="footer__section__element">
            24A Kingston St, Los Vegas NC 28202, USA.
          </div>
        </div>
        <div class="footer__contact">
          <div class="footer__contact__header">Mail</div>
          <div class="footer__contact__header">:</div>
          <div class="footer__section__element">myfearlessguide@gmail.com</div>
        </div>
        <div class="footer__contact">
          <div class="footer__contact__header">Số điện thoại</div>
          <div class="footer__contact__header">:</div>
          <div class="footer__section__element">(+22) 123 - 4567 - 900</div>
        </div>
      </div>
    </div>
    <div class=" flex justify-center">
        <div class="border-[1px] w-[80%] h-[1px] bg-white"></div>
    </div>
    <div class="footer__section__element flex justify-center">Web bán sách hàng đầu VN</div>
  </div>
</template>

<style lang="scss" scoped>
// @import '~assets/scss/variables.scss';
.footer {
  &__section {
    display: flex;
    flex-direction: column;
    gap: 20px;
    &__header {
      color: white;
      font-size: 20px;
      font-weight: 500;
    }
    &__element {
      color: #b4c7e7;
      font-size: 13px;
      &__container {
        display: flex;
        flex-direction: column;
        gap: 10px;
      }
    }
  }

  &__contact {
    display: flex;
    gap: 20px;
    align-items: center;

    &__header {
      color: white;
      font-size: 14px;
      font-weight: 500;
    }
  }
}
</style>