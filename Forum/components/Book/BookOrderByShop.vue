<template>
    <div class="py-5">
        <div class="flex bg-[#FFCA42] items-center gap-5 px-5 py-3">
            <div class="w-[20px]">
                <input class="w-[100%] h-[100%]" type="checkbox">
            </div>
            <div class="text-[#1B3764] text-[16px] font-semibold">
                A shop
            </div>
            <div>
                >
            </div>
        </div>
        <div class="flex flex-col gap-3">
            <BookOrderCard/>
            <BookOrderCard/>
            <BookOrderCard/>
        </div>
    </div>
</template>

<script>
import BookOrderCard from '~/components/Book/BookOrderCard.vue'
export default {
    components: {
        BookOrderCard,
    }
}
</script>