<template>
  <div class="flex flex-col items-center gap-4">
    <div class="w-auto p-[20px] bg-[#F5F8FC]">
      <img class="aspect-[3/4] shadow-md" :src="book.image" alt="" />
    </div>
    <div class="w-full flex flex-col items-start gap-4">
      <div>
        <button
          class="text-[#1B3764] text-[18px] font-semibold max-h-[30px] overflow-hidden text-ellipsis max-w-[100%]"
          @click="toBookId(book._id)"
        >
          {{ book.title }}
        </button>
        <div class="text-[#FFCA42] text-[12px] font-semibold">
          {{ getPriceFormat }}
        </div>
        <div
          class="text-[#969AA0] text-[12px] min-h-[100px] max-h-[100px] overflow-y-hidden"
        >
          {{ book.description }}
        </div>
      </div>

      <button
        class="border-[1px] border-[#FFCA42] py-3 px-5 w-auto self-start text-[13px] text-[#1B3764] font-semibold hover:bg-[#FFCA42] transition ease-in-out duration-300"
        @click="toOrder(book._id)"
      >
        Đặt ngay
      </button>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    book: Object,
  },
  data() {
    return {}
  },
  mounted() {},
  methods: {
    toBookId(id) {
      this.$router.push(`/book/${id}`)
    },
    toOrder(id) {
      this.$router.push(`/order/${id}`)
    },
  },
  computed: {
    getPriceFormat() {
      const formattedPrice = this.book.price
        .toString()
        .replace(/\B(?=(\d{3})+(?!\d))/g, '.')
      return `${formattedPrice} VND`
    },
  },
}
</script>
