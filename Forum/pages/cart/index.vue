<template>
  <div>
    <TopNaviBar />
    <SearchBar />
    <div class="cart__header">
      <div class="cart__product">Sản phẩm</div>
      <div class="cart__price">Đơn giá</div>
      <div class="cart__quantity">Số lượng</div>
      <div class="cart__total">Số tiền</div>
      <div class="cart__ulti"></div>
    </div>
    <div>
      <BookOrderByShop />
      <BookOrderByShop />
    </div>
    <div class="flex py-5">
      <div class="cart__product flex gap-4 items-center">
        <input type="checkbox" />
        <div class="text-[20px] font-semibold text-[#1B3764]">Chọn tất cả</div>
      </div>
      <div class="w-[40%] items-center flex justify-end pr-20 text-[16px] font-semibold text-[#1B3764]">Tổng thanh toán</div>
      <div class="w-[15%] flex items-center text-[16px] font-semibold text-[#1B3764]">97500 VND</div>
      <button class="w-[10%] bg-[#FFCA42] px-5 py-3 text-[16px] font-semibold text-[#1B3764]">Đặt hàng</button>
    </div>
    <FooterBar />
  </div>
</template>

<script>
import TopNaviBar from '~/components/TopNaviBar.vue'
import SearchBar from '~/components/SearchBar.vue'
import FooterBar from '~/components/FooterBar.vue'
import BookOrderByShop from '~/components/Book/BookOrderByShop.vue'
export default {
  layout: 'empty',
  components: {
    TopNaviBar,
    SearchBar,
    FooterBar,
    BookOrderByShop,
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