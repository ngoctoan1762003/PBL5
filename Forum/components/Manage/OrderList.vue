<template>
  <div>
    <div>
      <EditBook
        v-show="isEditProfile"
        :book="currentBook"
        @cancel="cancelSave"
        @save="save"
        @reload="reload"
      />
    </div>
    <div
      class="w-full bg-[#1B3764] rounded-[16px] text-white font-medium px-5 flex justify-between text-[12px] mb-5"
    >
      <div
        class="w-[25%] py-5 flex justify-center items-center cursor-pointer border-blue-500"
        :class="{ 'border-b-[3px]': currentSelectedOption === 1 }"
        @click="toAll()"
      >
        Tất cả
      </div>
      <div
        class="w-[25%] py-5 flex justify-center items-center cursor-pointer border-yellow-500"
        :class="{ 'border-b-[3px]': currentSelectedOption === 2 }"
        @click="toPendingOrder()"
      >
        Đang chờ
      </div>
      <div
        class="w-[25%] py-5 flex justify-center items-center cursor-pointer border-green-500"
        :class="{ 'border-b-[3px]': currentSelectedOption === 3 }"
        @click="toDoneOrder()"
      >
        Đã xác nhận
      </div>
      <div
        class="w-[25%] py-5 flex justify-center items-center cursor-pointer border-red-500"
        :class="{ 'border-b-[3px]': currentSelectedOption === 4 }"
        @click="toAbandonedOrder()"
      >
        Đã hủy
      </div>
    </div>
    <div
      class="user-list text-white font-medium p-5 w-full bg-[#1B3764] rounded-[16px]"
    >
      <div class="font-semibold user-list-row font-semibold">
        <!-- <div class="user-list-row-cell avatar"></div> -->
        <div class="user-list-row-cell title">Mã hóa đơn</div>
        <div class="user-list-row-cell gender">Số loại sách</div>
        <div class="user-list-row-cell phone">Mã giảm giá</div>
        <div class="user-list-row-cell email">Địa chỉ</div>
        <div class="user-list-row-cell birthday">Trạng thái</div>
        <div class="user-list-row-cell status">Tổng tiền</div>
        <div class="user-list-row-cell email">Số điện thoại</div>
        <div class="tooltip"></div>
      </div>
      <div
        v-for="user in currentOrderSelect"
        class=""
        :key="user.OrderDetailId"
        @click="toggleItemsVisibility(user.OrderDetailId)"
      >
        <div class="user-list-row bg-white hover:bg-gray-300 pr-5">
          <div
            class="user-list-row-cell font-semibold text-[#1B3764] title flex gap-3 items-center"
          >
            <div>
              {{ user.OrderDetailId }}
            </div>
            <div
              class="bg-[#FFCA42] px-3 py-2 cursor-pointer"
              @click.stop="goToChat(user.user_id)"
            >
              Chat
            </div>
          </div>
          <div
            class="user-list-row-cell font-semibold text-[#1B3764] gender mr-[9px]"
          >
            {{ user.Items.length }}
          </div>
          <div class="user-list-row-cell font-semibold text-[#1B3764] phone">
            {{ getName(user.DiscountCode) }}
          </div>
          <div class="user-list-row-cell font-semibold text-[#1B3764] email">
            {{ user.address }}
          </div>
          <div
            class="user-list-row-cell font-semibold text-[#1B3764] birthday"
            :class="{
              'text-green-500': user.Status === 'Đã xác nhận',
              'text-yellow-600': user.Status === 'Đang chờ xác nhận',
              'text-red-500': user.Status === 'Đã bị hủy',
            }"
          >
            {{ user.Status }}
          </div>
          <div class="user-list-row-cell font-semibold text-[#1B3764] status">
            {{ getPriceFormat(user.Total_price) }}
          </div>
          <div class="user-list-row-cell font-semibold text-[#1B3764] email">
            {{ user.phone }}
          </div>
          <div class="tooltip relative">
            <div
              v-show="user.Status === 'Đang chờ xác nhận'"
              class="flex gap-3 items-center justify-start ml-[-60px]"
            >
              <button
                class="w-[75px] py-2 rounded-md bg-red-500"
                @click="cancelOrder(user.OrderDetailId, user.user_id)"
              >
                Hủy
              </button>
              <button
                class="w-[75px] py-2 rounded-md bg-green-400"
                @click="confirmOrder(user.OrderDetailId, user.user_id)"
              >
                Xác nhận
              </button>
            </div>
          </div>
        </div>
        <div
          class="flex flex-col gap-3 bg-[#3573D9] rounded-md"
          v-if="isItemsVisible(user.OrderDetailId)"
        >
          <div class="user-list-row user-list-information">
            <div class="user-list-row-cell title flex gap-4 items-center">
              <div>Sách</div>
            </div>
            <div class="user-list-row-cell gender">Thể loại</div>
            <div class="user-list-row-cell phone">Giá tiền</div>
            <div class="user-list-row-cell email">Số lượng</div>
            <div class="user-list-row-cell birthday"></div>
            <div class="user-list-row-cell status">Tổng tiền</div>
          </div>
          <div
            v-for="book in user.Items"
            :key="book.BookId"
            class="user-list-row user-list-information"
          >
            <div class="user-list-row-cell title flex gap-4 items-center">
              <img :src="book.Image" class="w-[40px]" alt="" />
              <div>{{ book.Title }}</div>
            </div>
            <div class="user-list-row-cell gender">
              {{ book.Genre }}
            </div>
            <div class="user-list-row-cell phone">
              {{ getPriceFormat(book.Price) }}
            </div>
            <div class="user-list-row-cell email">{{ book.Quantity }}</div>
            <div class="user-list-row-cell birthday"></div>
            <div class="user-list-row-cell status">
              {{ getPriceFormat(book.Price * book.Quantity) }}
            </div>
          </div>
        </div>
      </div>
      <div class="w-full h-[1px] bg-gray-500"></div>
      <!-- <Pagination
        :count="count"
        @changePage="changePage"
        :recordsPerPage="recordsPerPage"
      /> -->
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { format } from 'date-fns'
import EditBook from '../Book/EditBook.vue'
import constant from '~/constant'
// import Pagination from '~/components/Pagination.vue'

export default {
  components: {
    EditBook,
    // Pagination,
  },
  props: {
    count: Number,
    recordsPerPage: Number,
  },
  data() {
    return {
      users: Array,
      currentBook: {
        type: Object,
        default: () => ({}),
      },
      isEditProfile: false,
      currentOrderSelect: [],
      currentStatus: '',
      visibleItems: {},
      currentSelectedOption: 1,
    }
  },
  mounted() {
    const userId = localStorage.getItem('userId')
    const authorization = `Bearer ${localStorage.getItem('accessToken')}`
    axios({
      method: 'get',
      url: `${constant.base_url}/user/${userId}`,
      headers: {
        'ngrok-skip-browser-warning': 'skip-browser-warning',
      },
    })
      .then((res) => {
        console.log(res.data)
        this.user = res.data
      })
      .catch((err) => {
        console.log(err)
      })

    axios
      .get(`${constant.base_url}/order/shop/${userId}`, {
        headers: {
          Authorization: authorization,
          'ngrok-skip-browser-warning': 'skip-browser-warning',
        },
      })
      .then((res) => {
        this.users = res.data.order_details
        console.log(this.users)
        this.currentOrderSelect = this.users
      })
    console.log(this.users)
  },
  computed: {},
  methods: {
    toggleItemsVisibility(orderDetailId) {
      this.$set(
        this.visibleItems,
        orderDetailId,
        !this.visibleItems[orderDetailId]
      )
    },
    isItemsVisible(orderDetailId) {
      return !!this.visibleItems[orderDetailId]
    },
    toDoneOrder() {
      this.currentOrderSelect = this.users.filter(
        (u) => u.Status === 'Đã xác nhận'
      )
      this.currentSelectedOption = 3
    },
    toPendingOrder() {
      this.currentOrderSelect = this.users.filter(
        (u) => u.Status === 'Đang chờ xác nhận'
      )
      this.currentSelectedOption = 2
    },
    toAbandonedOrder() {
      this.currentOrderSelect = this.users.filter(
        (u) => u.Status === 'Đã bị hủy'
      )
      this.currentSelectedOption = 4
    },
    toAll() {
      this.currentOrderSelect = this.users
      this.currentSelectedOption = 1
    },
    closeAllPopup() {
      this.users.forEach((p) => {
        document.querySelector('#action-' + p.OrderId).classList.add('hidden')
      })
    },
    closeAllPopupExceptIndex(index) {
      this.users.forEach((p) => {
        if (p.OrderId !== index)
          document.querySelector('#action-' + p.OrderId).classList.add('hidden')
      })
    },
    getPriceFormat(price) {
      if (price === 0) return '' // Return empty string if book is not defined
      const formattedPrice = price
        .toString()
        .replace(/\B(?=(\d{3})+(?!\d))/g, '.')
      return `${formattedPrice} VND`
    },
    displayTooltip(id) {
      this.closeAllPopupExceptIndex(id)
      const popup = document.querySelector('#action-' + id)
      popup.classList.toggle('hidden')
    },
    cancelSave() {
      this.isEditProfile = false
    },
    save() {
      this.isEditProfile = false
    },
    showPopup(book) {
      this.currentBook = book
      this.isEditProfile = true
    },
    onDelete(id) {
      const authorization = localStorage.getItem('accessToken')
      axios({
        method: 'delete',
        url: `${constant.base_url}/users/${id}`,
        headers: {
          Authorization: authorization,
        },
      }).then((res) => {
        this.reload()
      })
    },
    formatBirthday(date) {
      if (date) {
        const jsDate = new Date(date)
        return format(jsDate, 'dd/MM/yyyy')
      }
      return ''
    },
    reload() {
      this.$emit('reload')
    },
    getName(name) {
      return name || ''
    },
    changePage(page, limit) {
      this.$emit('changePage', page, limit)
    },
    confirmOrder(orderId, userId) {
      const authorization = `Bearer ${localStorage.getItem('accessToken')}`
      axios({
        method: 'put',
        url: `${constant.base_url}/order/order_confirm/${orderId}`,
        headers: {
          Authorization: authorization,
        },
      })
        .then((res) => {
          console.log(res)
          this.$notify({
            title: 'Thành công',
            text: 'Xác nhận thành công',
            type: 'success',
            group: 'foo',
          })

          this.reload()
          axios({
            method: 'post',
            url: `${constant.base_url}/notification/new_notif`,
            data: {
              receiver_id: userId,
              content: `${this.user.Name} đã xác nhận đơn hàng của bạn`,
            },
          })

          const currentUserId = localStorage.getItem('userId')
          const authorization = `Bearer ${localStorage.getItem('accessToken')}`
          axios
            .get(`${constant.base_url}/order/shop/${currentUserId}`, {
              headers: {
                Authorization: authorization,
                'ngrok-skip-browser-warning': 'skip-browser-warning',
              },
            })
            .then((res) => {
              this.users = res.data.order_details
              console.log(this.users)
              this.currentOrderSelect = this.users
            })
          console.log(this.users)
        })
        .catch((error) => {
          this.$notify({
            title: 'Thất bại',
            text: 'Xác nhận thất bại: ' + error.response,
            type: 'error',
            group: 'foo',
          })
        })
    },
    cancelOrder(orderId, userId) {
      const authorization = `Bearer ${localStorage.getItem('accessToken')}`
      axios({
        method: 'put',
        url: `${constant.base_url}/order/order_cancel/${orderId}`,
        headers: {
          Authorization: authorization,
        },
      })
        .then((res) => {
          console.log(res)
          this.$notify({
            title: 'Thành công',
            text: 'Xóa thành công',
            type: 'success',
            group: 'foo',
          })

          this.reload()

          const currentUserId = localStorage.getItem('userId')
          const authorization = `Bearer ${localStorage.getItem('accessToken')}`
          axios
            .get(`${constant.base_url}/order/shop/${currentUserId}`, {
              headers: {
                Authorization: authorization,
                'ngrok-skip-browser-warning': 'skip-browser-warning',
              },
            })
            .then((res) => {
              this.users = res.data.order_details
              console.log(this.users)
              this.currentOrderSelect = this.users
            })

          axios({
            method: 'post',
            url: `${constant.base_url}/notification/new_notif`,
            data: {
              receiver_id: userId,
              content: `${this.user.Name} đã hủy đơn hàng của bạn`,
            },
          })
        })
        .catch((error) => {
          this.$notify({
            title: 'Thất bại',
            text: 'Xóa thất bại: ' + error.response,
            type: 'error',
            group: 'foo',
          })
        })
    },
    goToChat(userId) {
      this.$router.push(`/chat/${userId}`)
    },
  },
}
</script>

<style lang="scss" scoped>
@import '~/assets/scss/variables.scss';

.user-list-information:hover {
  background-color: $dark-4;
}

.user-list {
  display: flex;
  flex-direction: column;
  gap: 20px;

  .user-list-row {
    display: flex;
    grid-template-columns: repeat(8, minmax(0, 1fr));
    font-size: 12px;
    align-items: center;
    border-radius: 10px;
    min-height: 50px;
    padding-left: 20px;
    padding-bottom: 10px;
    padding-top: 10px;

    &-cell {
      grid-column: span 1 / span 1;
    }

    .avatar {
      width: 10%;
      display: flex;
      justify-content: center;

      img {
        width: 50px;
      }
    }

    .title {
      width: 17%;
    }

    .last-name {
      width: 20%;
    }

    .gender {
      width: 8%;
    }

    .phone {
      width: 10%;
    }

    .email {
      width: 18%;
    }

    .birthday {
      width: 10%;
    }

    .role {
      width: 10%;
    }

    .status {
      width: 10%;
    }

    .tooltip {
      width: 2%;
      display: flex;
      justify-content: center;
    }
  }
}
</style>
