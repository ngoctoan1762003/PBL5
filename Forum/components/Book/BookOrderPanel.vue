<template>
  <div>
    <div
      class="relative text-[#1B3764] font-semibold text-[21px] bg-[#FFCA42] py-3 px-5"
    >
      <div>Giỏ hàng</div>
      <img
        class="absolute right-5 top-[30%] w-[20px] h-[20px] cursor-pointer"
        @click="cancel()"
        src="~/assets/icon/x.svg"
        alt=""
      />
    </div>
    <div class="bg-white p-10 flex flex-col gap-5">
      <div class="flex gap-5">
        <img class="w-[80px]" src="~/assets/img/DemoBook.png" alt="" />
        <div class="flex flex-col justify-between">
          <div>
            <div class="flex gap-4 items-center">
              <div class="text-[#1B3764] font-semibold text-[16px]">
                {{ book.Title }}
              </div>
              <div
                class="bg-[#E8E8E8] py-1 px-3 min-w-[60px] text-[#969AA0] text-[12px]"
              >
                {{amount}}
              </div>
            </div>
            <div class="text-[#969AA0] font-semibold text-[12px]">
              {{ getPriceFormat(book.Price) }}
            </div>
          </div>
          <div class="text-[#1B3764] font-semibold">Hủy</div>
        </div>
      </div>
      <div
        class="w-full h-[1px] border-[1px] border-[#969AA0] opacity-50"
      ></div>
      <div class="flex justify-between">
        <div class="text-[#1B3764] font-semibold text-[12px]">Tổng</div>
        <div class="text-[#1B3764] font-semibold text-[12px]">
          {{ getPriceFormat(book.Price * amount) }}
        </div>
      </div>
      <button
        class="text-[#1B3764] font-semibold text-[14px] text-center bg-[#FFCA42] py-3 px-5"
      >
        Xác nhận
      </button>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    book: Object,
    amount: Number,
  },
  data(){
    return {
        isLoading: true,
    }
  },
  created() {
    this.isLoading = false;
  },
  methods: {
    cancel() {
      this.$emit('cancel')
    },
    getPriceFormat(price) {
      if (this.amount === 0) return '' // Return empty string if book is not defined
      const formattedPrice = price.toString().replace(
        /\B(?=(\d{3})+(?!\d))/g,
        '.'
      )
      return `${formattedPrice} VND`
    },
  },
  computed: {
  },
}
</script>