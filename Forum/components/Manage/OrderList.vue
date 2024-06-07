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
      class="w-full bg-[#1B3764] rounded-[16px] text-white font-medium p-5 flex justify-between text-[12px] mb-5"
    >
      <div class="w-[25%] flex justify-center items-center cursor-pointer" @click="toAll()">Tất cả</div>
      <div class="w-[25%] flex justify-center items-center cursor-pointer" @click="toPendingOrder()">Đang chờ</div>
      <div class="w-[25%] flex justify-center items-center cursor-pointer" @click="toDoneOrder()">Đã xác nhận</div>
      <div class="w-[25%] flex justify-center items-center cursor-pointer" @click="toAbandonedOrder">Đã hủy</div>
    </div>
    <div
      class="user-list text-white font-medium p-5 w-full bg-[#1B3764] rounded-[16px]"
    >
      <div class="font-semibold user-list-row">
        <!-- <div class="user-list-row-cell avatar"></div> -->
        <div class="user-list-row-cell title">Mã hóa đơn</div>
        <div class="user-list-row-cell gender">Số lượng</div>
        <div class="user-list-row-cell phone">Mã giảm giá</div>
        <div class="user-list-row-cell email">Tên shop</div>
        <div class="user-list-row-cell birthday">Trạng thái</div>
        <div class="user-list-row-cell status">Tổng tiền</div>
        <div class="tooltip"></div>
      </div>
      <div
        v-for="user in currentOrderSelect"
        class="user-list-row user-list-information"
        :key="user.OrderId"
      >
        <!-- <div class="avatar"> -->
        <!-- <img :src="user.image" class="p-2 rounded-full" /> -->
        <!-- </div> -->
        <div class="user-list-row-cell title">
          {{ user.OrderId }}
        </div>
        <div class="user-list-row-cell gender">
          {{ user.Items.length }}
        </div>
        <div class="user-list-row-cell phone">
          {{ getName(user.DiscountId) }}
        </div>
        <div class="user-list-row-cell email">{{ user.shop_name }}</div>
        <div class="user-list-row-cell birthday">{{ user.Status }}</div>
        <div class="user-list-row-cell status">
          {{ getPriceFormat(user.Total_price) }}
        </div>
        <div class="tooltip relative">
          <!-- <img
            src="~/assets/icon/more.svg"
            @mouseenter="displayTooltip(user.OrderId)"
            class="cursor-pointer"
          />
          <div
            :id="'action-' + user.OrderId"
            class="hidden absolute top-1 right-0 z-10"
            @mouseleave="closeAllPopup()"
          >
            <div class="px-1 py-1 bg-white rounded-lg">
              <button
                class="hover:bg-gray-500 hover:text-white text-gray-900 group flex rounded-md items-center w-full px-2 py-2 text-sm"
                @click="showPopup(user)"
              >
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  class="w-5 h-5 mr-2 text-violet-400"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M15.232 5.232l3.536 3.536m-2.036-5.036a2.5 2.5 0 113.536 3.536L6.5 21.036H3v-3.572L16.732 3.732z"
                  ></path>
                </svg>
                Sửa
              </button>
              <button
                class="hover:bg-red-400 hover:text-white text-gray-900 group flex rounded-md items-center w-full px-2 py-2 text-sm"
                @click="onDelete(user.OrderId)"
              >
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  class="w-5 h-5 mr-2 text-violet-400"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"
                  ></path>
                </svg>
                Xóa
              </button>
            </div>
          </div> -->
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
    }
  },
  mounted() {
    const userId = localStorage.getItem('userId')
    const authorization = `Bearer ${localStorage.getItem('accessToken')}`
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
  computed: {
  },
  methods: {
    toDoneOrder(){
      this.currentOrderSelect = this.users.filter(u => u.Status === 'Đã xác nhận');
    },
    toPendingOrder(){
      this.currentOrderSelect = this.users.filter(u => u.Status === 'đang chờ');
    },
    toAbandonedOrder(){
      this.currentOrderSelect = this.users.filter(u => u.Status === 'Đã hủy');
    },
    toAll(){
      this.currentOrderSelect = this.users;
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
      width: 21%;
    }

    .last-name {
      width: 20%;
    }

    .gender {
      width: 8%;
    }

    .phone {
      width: 23%;
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
      width: 15%;
    }

    .tooltip {
      width: 2%;
      display: flex;
      justify-content: center;
    }
  }
}
</style>
