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
      <input
        ref="quantityInput"
        class="bg-gray-300 py-1 w-[50px] text-center"
        :value="localQuantity"
        @keyup.enter="handleQuantityChange"
        @focus="saveCurrentQuantity"
      />
      <button class="bg-gray-300 px-4 py-1" @click="increaseQuantity">+</button>
    </div>
    <div class="w-[20%] text-[14px] font-semibold">
      {{ getPriceFormat(book.price * book.quantity) }}
    </div>
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
  data() {
    return {
      localQuantity: this.book.quantity,
      previousQuantity: this.book.quantity,
    }
  },
  methods: {
    decreaseQuantity() {
      this.localQuantity--;
      this.$emit('decreaseQuantity', this.book._id)
    },
    increaseQuantity() {
      this.localQuantity++;
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
    saveCurrentQuantity() {
      this.previousQuantity = this.localQuantity
    },
    handleQuantityChange(event) {
      const newQuantity = parseInt(event.target.value, 10)
      if (newQuantity > this.book.quantity) {
        this.$notify({
          title: 'Thất bại',
          text: 'Số lượng trong kho không đủ',
          type: 'error',
          group: 'foo',
        })
        this.localQuantity = this.previousQuantity // Revert to previous quantity
        event.target.value = this.previousQuantity // Update the input value
      } else if (!isNaN(newQuantity) && newQuantity > 0) {
        this.localQuantity = newQuantity
        this.$emit('updateQuantity', {
          id: this.book._id,
          quantity: this.localQuantity,
        })
      }
      this.$refs.quantityInput.blur() // Remove focus from the input field
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
