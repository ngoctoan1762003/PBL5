<template>
  <div class="flex items-center px-5 py-3 bg-[#F5F8FC] text-[#1B3764]">
    <div class="flex items-center gap-5 w-[35%]">
      <input
        type="checkbox"
        :checked="book.isChosen"
        @click="handleCheckboxChange"
      />
      <img class="w-[100px]" :src="book.image" />
      <div class="text-[16px] font-semibold">{{ book.title }}</div>
    </div>
    <div class="w-[20%] text-[14px] font-semibold">
      {{ getPriceFormat(book.price) }}
    </div>
    <div class="flex w-[20%] text-[16px] font-semibold">
      <button class="bg-gray-300 px-4 py-1" @click="decreaseQuantity">-</button>
      <div class="bg-gray-300 px-4 py-1 w-[50px]">{{ book.quantity }}</div>
      <button class="bg-gray-300 px-4 py-1" @click="increaseQuantity">+</button>
    </div>
    <div class="w-[20%] text-[14px] font-semibold">{{ getPriceFormat(book.total_price) }}</div>
    <button class="w-[5%]">
      <img src="~/assets/icon/bin.svg" alt="" @click="deleteCart" />
    </button>
  </div>
</template>

<script>
export default {
  props: {
    book: Object,
  },
  methods: {
    decreaseQuantity() {
      this.$emit('decreaseQuantity', this.book._id)
    },
    increaseQuantity() {
      this.$emit('increaseQuantity', this.book._id)
    },
    handleCheckboxChange() {
      if (this.book.isChosen === false) {
        this.$emit('checkBoxChecked', this.book._id)
      } else {
        this.$emit('checkBoxUnchecked', this.book._id)
      }
    },
    deleteCart() {
      this.$emit('deleteBookFromCart', this.book._id)
    },
    getPriceFormat(price) {
      if (this.amount === 0) return '' // Return empty string if book is not defined
      const formattedPrice = price
        .toString()
        .replace(/\B(?=(\d{3})+(?!\d))/g, '.')
      return `${formattedPrice} VND`
    },
  },
  computed: {
    isChosen() {
      return this.book.isChosen
    },
  },
}
</script>
