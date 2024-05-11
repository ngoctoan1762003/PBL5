<template>
  <div>
    <TopNaviBar />
    <SearchBar />
    <div class="flex flex-col justify-center items-center mt-5">
      <div
        class="w-[80%] flex justify-center items-center gap-5 px-10 py-5 bg-[#F5F8FC]"
      >
        <div class="w-[20%] text-[14px] font-semibold">Địa chỉ nhận hàng</div>
        <input class="w-full px-5 py-3 border-[1px]" type="text" />
      </div>
      <div class="cart__header w-[80%]">
        <div class="w-[20px]"></div>
        <div class="cart__product">Sản phẩm</div>
        <div class="cart__price">Đơn giá</div>
        <div class="cart__quantity">Số lượng</div>
        <div class="cart__total">Số tiền</div>
        <div class="cart__ulti"></div>
      </div>
      <div
        class="w-[80%] flex flex-col justify-center items-center gap-5 px-10 py-5 bg-[#F5F8FC]"
      >
        <div class="w-[100%]">
          <BookConfirmOrderByShop />
          <BookConfirmOrderByShop />
        </div>
        <div class="flex py-5 w-full">
          <div class="cart__product flex gap-4 items-center">
            <input type="checkbox" />
            <div class="text-[20px] font-semibold text-[#1B3764]">
              Chọn tất cả
            </div>
          </div>
          <div
            class="w-[40%] items-center flex justify-end pr-20 text-[16px] font-semibold text-[#1B3764]"
          >
            Tổng thanh toán
          </div>
          <div
            class="w-[15%] flex items-center text-[16px] font-semibold text-[#1B3764]"
          >
            97500 VND
          </div>
          <button
            class="w-[10%] bg-[#FFCA42] px-5 py-3 text-[16px] font-semibold text-[#1B3764]"
          >
            Đặt hàng
          </button>
        </div>
      </div>
    </div>
    <FooterBar />
  </div>
</template>

<script>
// import axios from 'axios'
import TopNaviBar from '~/components/TopNaviBar.vue'
import SearchBar from '~/components/SearchBar.vue'
import FooterBar from '~/components/FooterBar.vue'
import BookConfirmOrderByShop from '~/components/Book/BookConfirmOrderByShop.vue'
// import constant from '~/constant'

export default {
  components: {
    TopNaviBar,
    SearchBar,
    FooterBar,
    BookConfirmOrderByShop,
  },
  layout: 'empty',
  mounted() {
    
  },
}
</script>

<style lang="scss" scoped>
@import '~/assets/scss/variables.scss';
.cart {
  &__header {
    background-color: #f5f8fc;
    color: #969aa0;
    display: flex;
    font-size: 16px;
    padding: 30px;
    font-weight: 500;
    border-bottom: 1px solid gray;
  }

  &__product {
    width: 35%;
    padding-left: 20px;
  }

  &__price {
    width: 20%;
  }

  &__quantity {
    width: 20%;
  }

  &__total {
    width: 20%;
  }

  &__ulti {
    width: 5%;
  }
}
</style>