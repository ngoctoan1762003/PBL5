<template>
  <div class="flex items-start gap-4">
    <div class="w-auto">
      <img class="aspect-[3/5] shadow-md min-w-[130px] h-[200px]" :src="book.image" alt="" />
    </div>
    <div class="min-w-[230px] flex flex-col gap-4">
      <div>
        <div class="text-[#1B3764] text-[18px] font-semibold cursor-pointer" @click="toBookDetail(book._id)">{{book.Title}}</div>
        <div class="text-[#969AA0] text-[12px]">
          {{book.Description}}
        </div>
      </div>
      <div>
        <div class="flex gap-8">
          <div class="flex gap-3">
            <div class="bg-[#FFCA42] rounded-full w-3 h-3 mt-1"></div>
            <div>
              <div class="text-[14px] text-[#1B3764] font-semibold">Trang:</div>
              <div class="text-[#B4C7E7] text-[12px]">586 trang</div>
            </div>
          </div>
          <div class="flex gap-3">
            <div class="bg-[#FFCA42] rounded-full w-3 h-3 mt-1"></div>
            <div>
              <div class="text-[14px] text-[#1B3764] font-semibold">Thời lượng:</div>
              <div class="text-[#B4C7E7] text-[12px]">10 giờ</div>
            </div>
          </div>
        </div>
      </div>
      <button
        class="border-[1px] border-[#FFCA42] py-3 px-5 w-auto self-start text-[13px] text-[#1B3764] font-semibold" 
      >
        Đặt ngay
      </button>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    book: Object
  },
  methods: {
    toBookDetail(id){
      this.$router.push(`/book/${id}`)
    }
  }
}
</script>