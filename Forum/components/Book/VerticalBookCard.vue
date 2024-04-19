<template>
  <div class="flex flex-col items-center gap-4">
    <div class="w-auto p-[20px] bg-[#F5F8FC]">
      <img class="aspect-[3/4] shadow-md" src="~assets/img/DemoBook.png" alt="" />
    </div>
    <div class="min-w-[230px] flex flex-col gap-4">
      <div>
        <div class="text-[#1B3764] text-[18px] font-semibold">Dare To Be Fearless</div>
        <div class="text-[#FFCA42] text-[12px] font-semibold">30.000 VND</div>
        <div class="text-[#969AA0] text-[12px]">
          Many variations of passages of Lorem Ipsum willing araise alteration in
          some form.
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
  data(){
    return{
      book: {
        bookId: "",
        title: "",
        genre: "",
        description: "",
        quantity: 0,
        price: 0,
        authorId: 0,
        publisherId: 0
      }
    }
  },
  mounted() {

  }
}
</script>
