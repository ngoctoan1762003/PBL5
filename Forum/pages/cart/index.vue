<template>
  <div>
    <TopNaviBar />
    <SearchBar />
    <div class="fixed flex justify-center items-center w-full h-full top-0" v-show="isDeleting">
      <div class="absolute bg-gray-500 opacity-50 w-full h-full"></div>
      <ModalDeleteAlert class="relative z-[1]" @cancel="cancel" @delete="deleteBookFromCart(bookIdToDelete, shopIdToDelete)"/>
    </div>
    <div class="cart__header">
      <div class="cart__product">Sản phẩm</div>
      <div class="cart__price">Đơn giá</div>
      <div class="cart__quantity">Số lượng</div>
      <div class="cart__total">Số tiền</div>
      <div class="cart__ulti"></div>
    </div>
    <div v-for="bookOrders in cart" :key="bookOrders.shop_id">
      <BookOrderByShop
        :books="bookOrders.books"
        :shop_name="bookOrders.shop_name"
        :shop_id="bookOrders.shop_id"
        @addFromShop="addFromShop"
        @removeFromShop="removeFromShop"
        @addBook="addBook"
        @removeBook="removeBook"
        @increaseQuantity="increaseQuantity"
        @decreaseQuantity="decreaseQuantity"
        @deleteBookFromCart="deleteWarning"
      />
    </div>
    <div class="flex py-5">
      <div class="cart__product flex gap-4 items-center">
        <input type="checkbox" @click="handleCheckBox" />
        <div class="text-[16px] font-semibold text-[#1B3764]">Chọn tất cả</div>
      </div>
      <div
        class="w-[40%] items-center flex justify-end pr-20 text-[16px] font-semibold text-[#1B3764]"
      >
        Tổng thanh toán
      </div>
      <div
        class="w-[15%] flex items-center text-[16px] font-semibold text-[#1B3764]"
      >
        {{ calculateTotalPrice }}
      </div>
      <button
        class="w-[10%] bg-[#FFCA42] px-5 py-3 text-[16px] font-semibold text-[#1B3764]"
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
import BookOrderByShop from '~/components/Book/BookOrderByShop.vue'
import ModalDeleteAlert from '~/components/Modal/ModalDeleteAlert.vue'
import constant from '~/constant'

export default {
  layout: 'empty',
  components: {
    TopNaviBar,
    SearchBar,
    FooterBar,
    BookOrderByShop,
    ModalDeleteAlert,
  },
  data() {
    return {
      cart: [],
      selectedBook: [],
      isDeleting: false,
      bookIdToDelete: "",
      shopIdToDelete: "",
    }
  },
  mounted() {
    const authorization = `Bearer ${localStorage.getItem('accessToken')}`
    axios({
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
  computed: {
    calculateTotalPrice() {
      return this.selectedBook.reduce(
        (totalPrice, book) => totalPrice + book.price * book.quantity,
        0
      )
    },
  },
  methods: {
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
        this.deleteWarning(bookId, shopId);
        return;
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
      const book = this.getBook(shopId, bookId);
      this.isDeleting = false;
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
    cancel(){
      this.isDeleting = false;
    },
    deleteWarning(bookId, shopId){
      this.bookIdToDelete = bookId;
      this.shopIdToDelete = shopId;
      this.isDeleting = true;
    }
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