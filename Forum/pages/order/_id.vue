<template>
  <div>
    <div
      class="fixed w-[100vw] h-[100vh] top-0 z-20 flex justify-center items-center"
      v-show="isOrdering"
    >
      <div class="absolute bg-gray-500 opacity-50 w-full h-full"></div>
      <BookOrderPanel
        @cancel="cancel()"
        :book="book"
        :amount="parseInt(amount)"
        class="relative z-[1]"
      />
    </div>

    <TopNaviBar v-if="isLogedIn == true" />
    <TopNaviBarGuest v-else />
    <SearchBar />
    <div class="flex px-10 py-32 gap-10 justify-center">
      <div class="bg-[#F5F8FC] p-10 min-w-[300px] min-h-[300px]">
        <img :src="book.image" class="shadow-md h-[400px]" alt="" />
      </div>
      <div>
        <div class="max-w-[500px] flex flex-col gap-10">
          <div class="flex flex-col gap-5">
            <div class="text-[#1B3764] text-[30px] font-semibold">
              {{ book.Title }}
            </div>
            <div class="text-[#FFCA42] text-[25px] font-semibold">
              {{ getPriceFormat }}
            </div>
            <div class="text-[#969AA0] text-[14px]">
              {{ book.Description }}
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
              @input="validateNumberInput"
              @paste="onPaste"
              v-model="amount"
            />
            <button
              class="flex gap-4 bg-[#FFCA42] py-3 px-5 text-[13px] font-semibold items-center text-[#1B3764]"
              @click="showOrderPanel()"
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
import axios from 'axios'
import TopNaviBar from '~/components/TopNaviBar.vue'
import SearchBar from '~/components/SearchBar.vue'
import FooterBar from '~/components/FooterBar.vue'
import BookOrderPanel from '~/components/Book/BookOrderPanel.vue'
import constant from '~/constant'
import TopNaviBarGuest from '~/components/TopNaviBarGuest.vue'

export default {
  layout: 'empty',
  components: {
    TopNaviBar,
    TopNaviBarGuest,
    SearchBar,
    FooterBar,
    BookOrderPanel,
  },
  data() {
    return {
      book: {},
      amount: {
        type: Number,
        default: 0,
      },
      isLoading: true,
      isOrdering: false,
      isLogedIn: false,
    }
  },

  async created() {
    if (localStorage.getItem('accessToken')) {
      this.isLogedIn = true
    } else {
      this.isLogedIn = false
    }
    this.amount = 0
    const id = this.$route.params.id
    await axios({
      method: 'get',
      url: `${constant.base_url}/book/id/${id}`,
      headers: {
        'ngrok-skip-browser-warning': 'skip-browser-warning',
      },
    })
      .then((res) => {
        console.log(res)
        this.book = res.data
      })
      .catch((err) => {
        if (err.response.data.status === 401)
          this.alert = {
            ...this.alert,
            ...{
              isShowModal: true,
              title: 'Lỗi',
              buttonOkContent: 'Đăng nhập lại',
              content: 'Hết phiên đăng nhập, vui lòng đăng nhập lại',
              type: 'failed',
              typeSubmit: 'loginagain',
            },
          }
        else
          this.alert = {
            ...this.alert,
            ...{
              isShowModal: true,
              title: 'Lỗi',
              buttonOkContent: 'Đóng',
              content: err.response.data.error,
              type: 'failed',
            },
          }
      })
    this.isLoading = false
  },
  computed: {
    getPriceFormat() {
      if (this.isLoading) return
      const formattedPrice = this.book.Price.toString().replace(
        /\B(?=(\d{3})+(?!\d))/g,
        '.'
      )
      return `${formattedPrice} VND`
    },
  },
  methods: {
    cancel() {
      this.isOrdering = false
    },
    showOrderPanel() {
      if (this.isLogedIn === false) {
        this.$notify({
          title: 'Thất bại',
          text: 'Bạn phải đăng nhập mới có thể thêm vào giỏ hàng',
          type: 'error',
          group: 'foo',
        })
        return
      }
      if (this.amount === 0) {
        this.$notify({
          title: 'Thất bại',
          text: 'Số lượng phải lớn hơn 0',
          type: 'error',
          group: 'foo',
        })
        return
      }

      this.isOrdering = true
    },
    validateNumberInput() {
      this.amount = this.amount.replace(/\D/g, '')
    },
    onPaste(event) {
      event.preventDefault()
      const pastedText = (event.clipboardData || window.clipboardData).getData(
        'text'
      )
      this.amount = pastedText.replace(/\D/g, '')
    },
  },
}
</script>