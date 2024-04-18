<template>
    <div>
        <div class="relative text-[#1B3764] font-semibold text-[21px] bg-[#FFCA42] py-3 px-5">
            <div>Giỏ hàng</div>
            <img class="absolute right-5 top-[30%] w-[20px] h-[20px]" src="~/assets/icon/x.svg" alt="">
        </div>
        <div class="bg-white p-10 flex flex-col gap-5">
            <div class="flex gap-5">
                <img class="w-[80px]" src="~/assets/img/DemoBook.png" alt="">
                <div class="flex flex-col justify-between">
                    <div>
                        <div class="flex gap-4 items-center">
                            <div class="text-[#1B3764] font-semibold text-[16px]">Dare to be fearless</div>
                            <div class="bg-[#E8E8E8] py-1 px-3 min-w-[60px] text-[#969AA0] text-[12px]">2</div>
                        </div>
                        <div class="text-[#969AA0] font-semibold text-[12px]">30.000 VND</div>
                    </div>
                    <div class="text-[#1B3764] font-semibold">Hủy</div>
                </div>
            </div>
            <div class="w-full h-[1px] border-[1px] border-[#969AA0] opacity-50"></div>
            <div class="flex justify-between">
                <div class="text-[#1B3764] font-semibold text-[12px]">Tổng</div>
                <div class="text-[#1B3764] font-semibold text-[12px]">60.000VND</div>
            </div>
            <button class="text-[#1B3764] font-semibold text-[14px] text-center bg-[#FFCA42] py-3 px-5">
                Xác nhận
            </button>
        </div>
    </div>
</template>