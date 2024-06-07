<template>
  <div>
    <TopNaviBar />
    <SearchBar />
    <div
      class="fixed flex justify-center items-center w-full h-full top-0"
      v-show="isDeleting"
    >
      <div class="absolute bg-gray-500 opacity-50 w-full h-full"></div>
      <ModalDeleteAlert
        class="relative z-[1]"
        @cancel="cancel"
        @delete="deleteBookFromCart(bookIdToDelete, shopIdToDelete)"
      />
    </div>
    <div
      class="fixed flex justify-center items-center w-full h-full top-0"
      v-show="isChangingVoucher"
    >
      <div class="absolute bg-gray-500 opacity-50 w-full h-full"></div>
      <div class="w-[400px] bg-white z-[1] flex flex-col gap-5 py-5 px-3">
        <div
          class="relative text-[#1B3764] font-semibold text-[21px] bg-[#FFCA42] py-3 px-5"
        >
          <div>Các voucher hiện có</div>
          <img
            class="absolute right-5 top-[30%] w-[20px] h-[20px] cursor-pointer"
            @click="isChangingVoucher = false"
            src="~/assets/icon/x.svg"
            alt=""
          />
        </div>
        <select
          name=""
          id=""
          class="relative z-[1]"
          v-model="selectedDiscountCode"
        >
          <option
            v-for="discount in filteredDiscount"
            :key="discount._id"
            :value="discount?.DiscountCode || ''"
          >
            {{ discount?.DiscountCode || '' }} -
            {{ getDiscountValue(discount) }}
          </option>
        </select>
        <button
          class="text-[#1B3764] font-semibold text-[14px] text-center bg-[#FFCA42] py-3 px-5"
          @click="submitVoucher"
        >
          Xác nhận
        </button>
      </div>

      <!-- <div v-for="shop in changingShopVoucher.discount" :key="shop._id">
      </div> -->
    </div>
    <div class="cart__header py-3 flex flex-col gap-5 my-2">
      <div class="pl-5 text-[20px] text-[#1B3764] font-semibold">
        Thông tin nhận hàng
      </div>
      <div class="pl-5 flex gap-5 w-full items-center">
        <div class="min-w-[200px]">Địa chỉ</div>
        <input
          type="text"
          placeholder="Địa chỉ"
          class="py-3 px-5 w-[60%] rounded-[20px] text-[#1B3764]"
          v-model="address"
        />
        <!-- <div class="text-[#FFCA42]">Thay đổi</div> -->
      </div>
      <div class="pl-5 flex gap-5 w-full items-center">
        <div class="min-w-[200px]">Số điện thoại</div>
        <input
          type="text"
          placeholder="Số điện thoại"
          class="py-3 px-5 w-[60%] rounded-[20px] text-[#1B3764]"
          v-model="phone"
        />
        <!-- <div class="text-[#FFCA42]">Thay đổi</div> -->
      </div>
    </div>
    <div class="cart__header">
      <div class="cart__product">Sản phẩm</div>
      <div class="cart__price">Đơn giá</div>
      <div class="cart__quantity">Số lượng</div>
      <div class="cart__total">Số tiền</div>
      <div class="cart__ulti"></div>
    </div>
    <div class="py-5" v-for="shop in shops" :key="shop.shop_id">
      <div class="flex bg-[#FFCA42] items-center gap-5 px-5 py-2">
        <div class="text-[#1B3764] text-[16px] font-semibold">
          {{ shop.shop_name }}
        </div>
        <div>></div>
      </div>
      <div class="flex flex-col gap-3">
        <div v-for="book in shop.books" :key="book.shop_id">
          <div class="flex items-center px-5 py-3 bg-[#F5F8FC] text-[#1B3764]">
            <div class="flex items-center gap-5 w-[35%]">
              <img class="w-[100px]" :src="book.image" />
              <div class="text-[16px] font-semibold">{{ book.title }}</div>
            </div>
            <div class="w-[20%] text-[14px] font-semibold">
              {{ getPriceFormat(book.price) }}
            </div>
            <div class="flex w-[20%] text-[16px] font-semibold">
              <div class="">{{ book.quantity }}</div>
            </div>
            <div class="w-[20%] text-[14px] font-semibold">
              {{ getPriceFormat(book.price * book.quantity) }}
            </div>
            <button class="w-[5%]">
              <img src="~/assets/icon/bin.svg" alt="" />
            </button>
          </div>
        </div>
        <div
          class="bg-[#F4F8FF] py-5 px-5 flex flex-col gap-4"
          v-show="
            shop.selectedDiscount && shop.selectedDiscount?.DiscountCode !== ''
          "
        >
          <div class="text-[#1B3764] font-semibold text-[20px]">Voucher</div>
          <div class="flex flex-col">
            <div class="voucher flex w-full items-center">
              <div class="cart__product">
                <div class="w-[29%] text-[#1B3764] font-semibold">
                  {{ shop.selectedDiscount?.DiscountCode || '' }}
                </div>
              </div>
              <div class="w-[20%] text-[#1B3764] font-semibold">
                <!-- {{ getPriceFormat(5000) }} -->
              </div>
              <div class="cart__price text-[#1B3764] font-semibold"></div>
              <div class="w-[10%] text-[#1B3764] font-semibold">
                {{ getDiscountValue(shop.selectedDiscount) }}
              </div>
              <div class="cursor-pointer" @click="changeVoucher(shop)">
                Thay đổi
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="bg-[#1B3764] py-5 flex items-center gap-0">
      <div class="cart__product text-white font-semibold text-[18px]">
        Đơn vị vận chuyển
      </div>
      <select
        name=""
        id=""
        @change="handleShippingMethodChange"
        class="py-3 px-5 cart__price"
      >
        <option
          v-for="method in shippingMethod"
          :key="method._id"
          :value="method._id"
        >
          {{ method.Name }}
        </option>
      </select>
      <div class="cart__quantity"></div>
      <div class="text-[16px] text-white font-semibold ml-[-10px]">
        {{
          selectedMethod.Cost != null
            ? getPriceFormat(selectedMethod.Cost)
            : getPriceFormat(0)
        }}
      </div>
    </div>
    <!-- <div class="bg-[#F4F8FF] py-5 px-5">
      <div class="text-[#1B3764] font-semibold text-[20px]">Voucher</div>
      <div class="flex flex-col">
        <div class="voucher flex w-full items-center">
          <div class="cart__product">
            <img
              src="~/assets/img/avatar.jpg"
              class="w-[60px] h-[60px] rounded-full p-2"
              alt=""
            />
            <div class="w-[29%] text-[#1B3764] font-semibold">Name</div>
          </div>
          <div class="w-[20%] text-[#1B3764] font-semibold">
            {{ getPriceFormat(5000) }}
          </div>
          <div class="cart__price text-[#1B3764] font-semibold">1</div>
          <div class="w-[10%] text-[#1B3764] font-semibold">
            {{ getPriceFormat(5000) }}
          </div>
        </div>
      </div>
    </div> -->
    <div class="flex py-5 justify-end ml-[-30px]">
      <div
        class="w-[40%] items-center flex justify-end pr-20 text-[16px] font-semibold text-[#1B3764]"
      >
        Tổng thanh toán
      </div>
      <div
        class="w-[15%] flex items-center text-[16px] font-semibold text-[#1B3764]"
      >
        {{ getPriceFormat(calculateTotalPrice) }}
      </div>
      <button
        class="w-[10%] bg-[#FFCA42] px-5 py-3 text-[16px] font-semibold text-[#1B3764]"
        @click="confirmOrderBook"
      >
        Đặt hàng
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
// import BookOrderByShop from '~/components/Book/BookOrderByShop.vue'
import ModalDeleteAlert from '~/components/Modal/ModalDeleteAlert.vue'
import constant from '~/constant'

export default {
  layout: 'empty',
  components: {
    TopNaviBar,
    SearchBar,
    FooterBar,
    // BookOrderByShop,
    ModalDeleteAlert,
  },
  data() {
    return {
      cart: [],
      selectedBook: [],
      isDeleting: false,
      bookIdToDelete: '',
      shopIdToDelete: '',
      books: [],
      shippingMethod: [],
      selectedMethod: Object,
      shops: [],
      changingShopVoucher: Object,
      isChangingVoucher: false,
      selectedDiscountCode: '', // Initialize selected discount code
      user: {},
      address: '',
      phone: '',
    }
  },
  async mounted() {
    const shopsQuery = this.$route.query.shops
    this.user = JSON.parse(localStorage.getItem('user'))
    this.address = this.user?.Address || ''
    this.phone = this.user?.Phone || ''

    if (shopsQuery) {
      this.shops = JSON.parse(shopsQuery)
    }

    try {
      const res = await axios.get(`${constant.base_url}/shipping/method`, {
        headers: {
          'ngrok-skip-browser-warning': 'skip-browser-warning',
        },
      })
      this.shippingMethod = res.data
      this.selectedMethod = this.shippingMethod[0]
    } catch (err) {
      console.error(err)
    }

    for (let i = 0; i < this.shops.length; i++) {
      try {
        const res = await axios.get(
          `${constant.base_url}/discount/${this.shops[i].shop_id}`,
          {
            headers: {
              'ngrok-skip-browser-warning': 'skip-browser-warning',
            },
          }
        )

        this.$set(this.shops, i, {
          ...this.shops[i],
          discount: res.data,
          discount_id: '',
          selectedDiscount: '',
        })

        if (this.shops[i].discount.length > 0) {
          this.shops[i].discount_id = this.shops[i].discount[0]._id
          this.shops[i].selectedDiscount = this.shops[i].discount[0]
        }
      } catch (error) {
        console.error(
          `Error fetching discount for shop ${this.shops[i].shop_id}:`,
          error
        )
      }
    }
  },
  computed: {
    filteredDiscount() {
      // Ensure changingShopVoucher is defined and has a discount property
      if (
        this.changingShopVoucher &&
        Array.isArray(this.changingShopVoucher.discount)
      ) {
        return this.changingShopVoucher.discount.filter((d) => d.Quantity > 0)
      }
      return []
    },
    calculateTotalPrice() {
      let totalBooksPrice = this.shops.reduce((total, shop) => {
        return (
          total +
          shop.books.reduce((subtotal, book) => {
            return subtotal + book.price * book.quantity
          }, 0)
        )
      }, 0)

      this.shops.forEach((shop) => {
        console.log('shop', shop)
        if (
          shop.selectedDiscount &&
          shop.selectedDiscount?.DiscountCode !== ''
        ) {
          totalBooksPrice -= shop.selectedDiscount.DiscountAmount
          totalBooksPrice -=
            (totalBooksPrice * shop.selectedDiscount.DiscountPercent) / 100
        }
      })

      return (
        totalBooksPrice +
        (this.selectedMethod.Cost != null ? this.selectedMethod.Cost : 0)
      )
    },
  },
  watch: {
    address(newAddress) {
      this.user.Address = newAddress
      localStorage.setItem('user', JSON.stringify(this.user))
    },
    phone(newPhone) {
      this.user.Phone = newPhone
      localStorage.setItem('user', JSON.stringify(this.user))
    },
  },
  methods: {
    getPriceFormat(price) {
      if (price === 0) return '' // Return empty string if book is not defined
      const formattedPrice = price
        .toString()
        .replace(/\B(?=(\d{3})+(?!\d))/g, '.')
      return `${formattedPrice} VND`
    },
    handleShippingMethodChange(event) {
      const shippingId = event.target.value
      this.selectedMethod = this.shippingMethod.find(
        (item) => item._id === shippingId
      )
      console.log(this.selectedMethod)
    },
    handleCheckBox(event) {
      if (event.target.checked) {
        this.addAll()
      } else {
        this.removeAll()
      }
    },
    addAll() {
      for (let i = 0; i < this.cart.length; i++) {
        this.cart[i].books.forEach((book) => {
          if (book.isChosen === false) {
            book.isChosen = true
            this.selectedBook.push(book)
          }
        })
      }
    },
    removeAll() {
      for (let i = 0; i < this.cart.length; i++) {
        this.cart[i].books.forEach((book) => {
          book.isChosen = false

          const index = this.selectedBook.findIndex(
            (selectedBook) => selectedBook._id === book._id
          )

          if (index !== -1) {
            this.selectedBook.splice(index, 1)
          }
        })
      }
    },
    addFromShop(shopId) {
      for (let i = 0; i < this.cart.length; i++) {
        if (this.cart[i].shop_id !== shopId) continue
        this.cart[i].books.forEach((book) => {
          if (book.isChosen === false) {
            book.isChosen = true
            this.selectedBook.push(book)
          }
        })
      }
    },
    addBook(bookId, shopId) {
      for (let i = 0; i < this.cart.length; i++) {
        if (this.cart[i].shop_id !== shopId) continue
        this.cart[i].books.forEach((book) => {
          if (book._id === bookId) {
            book.isChosen = true
            this.selectedBook.push(book)
          }
        })
      }
      console.log('Number of selected books:', this.selectedBook.length)

      console.log(this.selectedBook)
      console.log(this.cart)
    },
    removeBook(bookId, shopId) {
      const index = this.selectedBook.findIndex(
        (selectedBook) => selectedBook._id === bookId
      )
      if (index !== -1) {
        this.selectedBook[index].isChosen = false
        this.selectedBook.splice(index, 1)
      }
      console.log('Number of selected books:', this.selectedBook.length)

      console.log(this.selectedBook)
      console.log(this.cart)
    },
    getBook(shopId, bookId) {
      for (let i = 0; i < this.cart.length; i++) {
        if (this.cart[i].shop_id !== shopId) continue
        for (const book of this.cart[i].books) {
          if (book._id === bookId) {
            return book
          }
        }
      }
      return null
    },
    removeFromShop(shopId) {
      // Filter the cart based on the shopId
      for (let i = 0; i < this.cart.length; i++) {
        if (this.cart[i].shop_id !== shopId) continue
        this.cart[i].books.forEach((book) => {
          book.isChosen = false

          const index = this.selectedBook.findIndex(
            (selectedBook) => selectedBook._id === book._id
          )

          if (index !== -1) {
            this.selectedBook.splice(index, 1)
          }
        })
      }
    },
    increaseQuantity(bookId, shopId) {
      const authorization = `Bearer ${localStorage.getItem('accessToken')}`
      const book = this.getBook(shopId, bookId)
      book.quantity += 1
      axios({
        method: 'put',
        url: `${constant.base_url}/cart/${book.cart_id}`,
        headers: {
          Authorization: authorization,
        },
        data: {
          quantity: book.quantity,
        },
      })
    },
    decreaseQuantity(bookId, shopId) {
      const authorization = `Bearer ${localStorage.getItem('accessToken')}`
      const book = this.getBook(shopId, bookId)
      if (book.quantity === 1) {
        this.deleteWarning(bookId, shopId)
        return
      }
      book.quantity -= 1
      axios({
        method: 'put',
        url: `${constant.base_url}/cart/${book.cart_id}`,
        headers: {
          Authorization: authorization,
        },
        data: {
          quantity: book.quantity,
        },
      })
    },
    async deleteBookFromCart(bookId, shopId) {
      const authorization = `Bearer ${localStorage.getItem('accessToken')}`
      const book = this.getBook(shopId, bookId)
      this.isDeleting = false
      await axios({
        method: 'delete',
        url: `${constant.base_url}/cart/${book.cart_id}`,
        headers: {
          Authorization: authorization,
        },
      }).then(() => {
        this.$notify({
          title: 'Thành công',
          text: 'Xóa thành công',
          type: 'success',
          group: 'foo',
        })
      })

      await axios({
        method: 'get',
        url: `${constant.base_url}/cart/self`,
        headers: {
          'ngrok-skip-browser-warning': 'skip-browser-warning',
          Authorization: authorization,
        },
      })
        .then((res) => {
          console.log(res.data)
          this.cart = res.data
        })
        .catch((err) => {
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
        .finally(() => {
          this.cart.forEach((cartItem) => {
            cartItem.books.forEach((book) => {
              console.log(book)
              this.$set(book, 'isChosen', false) // Ensure reactivity
            })
          })
        })
    },
    cancel() {
      this.isDeleting = false
    },
    deleteWarning(bookId, shopId) {
      this.bookIdToDelete = bookId
      this.shopIdToDelete = shopId
      this.isDeleting = true
    },
    confirmOrderBook() {
      if (this.address === '') {
        this.$notify({
          title: 'Thất bại',
          text: 'Hãy điền địa chỉ nhận hàng',
          type: 'error',
          group: 'foo',
        })
        return;
      }
      if (this.phone === '') {
        this.$notify({
          title: 'Thất bại',
          text: 'Hãy điền số điện thoại',
          type: 'error',
          group: 'foo',
        })
        return;
      }
      this.shops.forEach((shop) =>
        shop.books.forEach((book) => {
          book.price = parseInt(book.price)
        })
      )
      const userid = localStorage.getItem('userId')
      const authorization = `Bearer ${localStorage.getItem('accessToken')}`
      axios({
        method: 'post',
        url: `${constant.base_url}/order/order`,
        headers: {
          Authorization: authorization,
        },
        data: {
          userid,
          address: this.address,
          phone: this.phone,
          status: 'pending',
          shipping_id: '6624eded2b9b7db58edcb9e7',
          shops: this.shops,
        },
      })
        .then(() => {
          this.$notify({
            title: 'Thành công',
            text: 'Đặt hàng thành công',
            type: 'success',
            group: 'foo',
          })
          this.$router.push('/order/list')
        })
        .catch((error) => {
          this.$notify({
            title: 'Thất bại',
            text: 'Không thể đặt hàng ' + error,
            type: 'error',
            group: 'foo',
          })
        })
    },
    getDiscountValue(discount) {
      // Check if the discount object is null or undefined
      if (!discount) return ''

      // Check if the discount code is present
      if (!discount.DiscountCode) return ''

      // Check if there is a discount amount and format it accordingly
      if (discount.DiscountAmount && discount.DiscountAmount !== 0) {
        return this.getPriceFormat(discount.DiscountAmount)
      }

      // If there's no discount amount, return the discount percent
      if (discount.DiscountPercent) {
        return discount.DiscountPercent + '%'
      }

      // Return an empty string if no applicable discount is found
      return ''
    },
    changeVoucher(shop) {
      this.changingShopVoucher = shop
      this.isChangingVoucher = true
    },
    submitVoucher() {
      this.isChangingVoucher = false
      this.changingShopVoucher.selectedDiscount =
        this.changingShopVoucher.discount.find(
          (discount) => discount.DiscountCode === this.selectedDiscountCode
        )
    },
  },
}
</script>

<style lang="scss" scoped>
@import '~/assets/scss/variables.scss';
.cart {
  &__header {
    background-color: #f5f8fc;
    color: #969aa0;
    display: flex;
    font-size: 16px;
    padding: 15px;
    font-weight: 500;
    border-bottom: 1px solid gray;
  }

  &__product {
    width: 35%;
    padding-left: 20px;
  }

  &__price {
    width: 20%;
  }

  &__quantity {
    width: 20%;
  }

  &__total {
    width: 20%;
  }

  &__ulti {
    width: 5%;
  }
}
</style>