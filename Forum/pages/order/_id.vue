<template>
  <div>
    <div
      class="fixed w-[100vw] h-[100vh] top-0 z-20 flex justify-center items-center"
    >
      <div class="absolute bg-gray-500 opacity-50 w-full h-full"></div>
      <BookOrderPanel class="relative z-[1]" />
    </div>

    <TopNaviBarGuest />
    <SearchBar />
    <div class="flex px-10 py-32 gap-10 justify-center">
      <div class="bg-[#F5F8FC] p-10 min-w-[300px] min-h-[300px]">
        <img src="~/assets/img/DemoBook.png" class="shadow-md" alt="" />
      </div>
      <div>
        <div class="max-w-[500px] flex flex-col gap-10">
          <div class="flex flex-col gap-5">
            <div class="text-[#1B3764] text-[30px] font-semibold">
              Dare To Be Fearless
            </div>
            <div class="text-[#FFCA42] text-[25px] font-semibold">
              30.000 VND
            </div>
            <div class="text-[#969AA0] text-[14px]">
              Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
              eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut
              enim ad minim veniam, quis nostrud exercitation ullamco laboris
              nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in
              reprehenderit in voluptate velit esse cillum dolore eu fugiat
              nulla pariatur. Excepteur sint occaecat cupidatat non proident,
              sunt in culpa qui officia deserunt mollit anim id est laborum.
            </div>
            <div class="flex gap-10 items-center">
              <div class="flex flex-col gap-2">
                <div class="text-[#969AA0] text-[14px]">Nhà xuất bản</div>
                <div class="text-[#969AA0] text-[14px]">Ngôn ngữ</div>
                <div class="text-[#969AA0] text-[14px]">Số trang</div>
                <div class="text-[#969AA0] text-[14px]">Kích thước</div>
              </div>
              <div class="flex flex-col gap-2">
                <div class="text-[#969AA0] text-[14px]">:</div>
                <div class="text-[#969AA0] text-[14px]">:</div>
                <div class="text-[#969AA0] text-[14px]">:</div>
                <div class="text-[#969AA0] text-[14px]">:</div>
              </div>
              <div class="flex flex-col gap-2">
                <div class="text-[#969AA0] text-[14px]">
                  Learning Private Limited (1 January 2023)
                </div>
                <div class="text-[#969AA0] text-[14px]">English</div>
                <div class="text-[#969AA0] text-[14px]">212 trang</div>
                <div class="text-[#969AA0] text-[14px]">20 x 14 x 4 cm</div>
              </div>
            </div>
          </div>
          <div class="flex gap-10">
            <input
              type="text"
              placeholder="Số lượng"
              class="max-w-[100px] border-[1px] border-[#FFCA42] py-3 px-5 w-auto self-start text-[13px] text-[#1B3764] font-semibold text-center"
            />
            <button
              class="flex gap-4 bg-[#FFCA42] py-3 px-5 text-[13px] font-semibold items-center text-[#1B3764]"
            >
              <div>Thêm vào giỏ hàng</div>
              <img src="~/assets/icon/cart.svg" />
            </button>
          </div>
        </div>
      </div>
    </div>
    <div class="flex justify-center gap-10 pb-32 font-semibold text-[18px]">
      <button class="bg-[#1B3764] py-3 px-5">
        <div class="text-white">Mô tả sản phẩm</div>
      </button>
      <button class="bg-[#F5F8FC] py-3 px-5">
        <div class="text-[#1B3764]">Thông tin thêm</div>
      </button>
    </div>
    <FooterBar />
  </div>
</template>

<script>
import TopNaviBarGuest from '~/components/TopNaviBarGuest.vue'
import SearchBar from '~/components/SearchBar.vue'
import FooterBar from '~/components/FooterBar.vue'
import BookOrderPanel from '~/components/Book/BookOrderPanel.vue'

export default {
  layout: 'empty',
  components: {
    TopNaviBarGuest,
    SearchBar,
    FooterBar,
    BookOrderPanel,
  },
}
</script>