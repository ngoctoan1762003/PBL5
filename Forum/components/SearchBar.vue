<template>
    <div class="relative bg-[#1B3764] flex justify-center p-5">
        <div class="relative w-[80%]">
            <input type="text" class="border-[1px] shadow-md text-[14px] px-5 py-3 rounded-[20px] w-full" placeholder="Tìm kiếm">
            <img src="~/assets/icon/search.svg" class="absolute right-5 top-[30%] w-[20px] h-[20px]">
            <div class="absolute right-[-50px] top-[30%] w-[20px] h-[20px] flex gap-5 items-center">
                <img src="~/assets/icon/cart.svg" class="cursor-pointer" @click="toCart" alt="">
                <img src="~/assets/icon/message.svg" class="cursor-pointer" @click="toMessage" alt="">
            </div>
        </div>
    </div>
</template>
<script>
export default {
    methods: {
        toCart(){
            this.$router.push('/cart')
        },
        toMessage(){
            this.$router.push('/chat')
        },
    }
}
</script>