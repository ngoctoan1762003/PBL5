<template>
  <div class="default">
    <div class="default__top">
      <!-- <TopNavBar class="top-nav" /> -->
      <TopNaviBar />
    </div>
    <div class="px-5 flex gap-5">
      <div class="tableft">
        <div class="tableft__item category">
          <div class="category__item" @click="changeOption(1)">
            <img src="~/assets/icon/person.svg" alt="" />
            <div class="category__item__info">
              <span class="name">Thống kê</span>
            </div>
          </div>
          <div class="category__item" @click="changeOption(2)">
            <img src="~/assets/icon/popular.svg" alt="" />
            <div class="category__item__info">
              <span class="name">Quản lý sách</span>
            </div>
          </div>
          <div class="category__item" @click="changeOption(3)">
            <img src="~/assets/icon/popular.svg" alt="" />
            <div class="category__item__info">
              <span class="name">Thêm sách</span>
            </div>
          </div>
          <div class="category__item" @click="changeOption(4)">
            <div class="bg-[#2C353D] rounded-[5px] pr-[-10px] ml-[2px]">
              <img class="w-[30px]" src="~/assets/icon/discount.svg" alt="" />
            </div>
            <div class="category__item__info">
              <span class="name">Quản lý mã giảm giá</span>
            </div>
          </div>
          <div class="category__item" @click="changeOption(5)">
            <div class="bg-[#2C353D] rounded-[5px] pr-[-10px] ml-[2px]">
              <img class="w-[30px]" src="~/assets/icon/discount.svg" alt="" />
            </div>
            <div class="category__item__info">
              <span class="name">Thêm mã giảm giá</span>
            </div>
          </div>
          <div class="category__item" @click="changeOption(6)">
            <div
              class="w-[30px] bg-[#2C353D] rounded-[5px] pr-[-10px] ml-[2px]"
            >
              <img class="w-[30px]" src="~/assets/icon/order.svg" alt="" />
            </div>
            <div class="category__item__info">
              <span class="name">Hóa đơn đã đặt tại cửa hàng</span>
            </div>
          </div>
          <div class="category__item" @click="changeOption(7)">
            <div class="bg-[#2C353D] rounded-[5px] pr-[-10px] ml-[2px]">
              <img class="w-[30px]" src="~/assets/icon/order.svg" alt="" />
            </div>
            <div class="category__item__info">
              <span class="name">Hóa đơn chờ xác nhận</span>
            </div>
          </div>
        </div>
      </div>
      <div v-show="manageOption === 1 && !isLoading" class="w-[100%] flex">
        <div class="flex h-min-[200px] justify-between gap-5 px-5">
          <div
            class="bg-[#1B3764] max-h-[200px] flex flex-col gap-2 py-5 px-4 min-w-[300px] max-w-[300px] rounded-[20px]"
          >
            <div class="text-white text-[22px] font-semibold">Tổng số sách</div>
            <div class="text-white text-[18px]">{{ allBookCount }} quyển</div>
          </div>
          <div
            class="bg-[#1B3764] max-h-[200px] flex flex-col gap-2 py-5 px-4 min-w-[300px] max-w-[300px] rounded-[20px]"
          >
            <div class="text-white text-[22px] font-semibold">
              Tổng số hóa đơn
            </div>
            <div class="text-white text-[16px]">
              {{ allOrderCount }} hóa đơn
            </div>
          </div>
          <!-- <div
            class="bg-[#1B3764] max-h-[200px] flex flex-col gap-2 py-5 px-4 min-w-[300px] max-w-[300px] rounded-[20px] min-w-[45%]"
          >
            <div class="text-white text-[22px] font-semibold">
              Tổng số sách đã bán
            </div>
            <div class="text-white text-[16px]">{{ soldBookCount }} quyển</div>
          </div> -->
          <!-- <div class="bg-[#1B3764] max-h-[200px] flex flex-col gap-2 py-5 px-4 min-w-[300px] max-w-[300px] rounded-[20px] min-w-[45%]">
            <div>Tổng class="text-white text-[22px] font-semibold" tiền đã nhận</div>
            <div>{{bu class="text-white text-[18px]"yerCount}}</div>
          </div> -->
          <div
            class="bg-[#1B3764] max-h-[200px] flex flex-col gap-2 py-5 px-4 mi6-w-[300px] max-w-[300px] rounded-[20px] min-w-[45%]"
          >
            <div class="text-white text-[22px] font-semibold">
              Đơn hàng đang đợi
            </div>
            <div class="text-white text-[16px]">
              {{ pendingOrderCount }} đơn hàng
            </div>
          </div>
        </div>
        <div
          class="flex flex-col w-full justify-between gap-5 p-5 w-full min-w-[500px] w-full"
        >
          <!-- <ChartistChart
            :data="chartDataComputed"
            :options="chartOptions"
            :responsiveOptions="responsiveOptions"
          /> -->
          <!-- <div class="ct-chart ct-perfect-fourth"></div> -->
        </div>
      </div>
      <div v-show="manageOption === 2 && !isLoading" class="w-full">
        <BookList
          class="w-full"
          :users="books"
          @reload="reload"
          v-if="this.books.length > 0"
          @changePage="changeBookPage"
          :count="bookCount"
          :recordsPerPage="recordsPerPage"
        />
        <div v-else class="w-full">
          <div
            class="bg-[#1B3764] w-full p-5 flex justify-center items-center text-white rounded-[20px] text-[14px] font-semibold"
          >
            Bạn chưa đăng sách nào
          </div>
        </div>
      </div>
      <AddBookPanel
        v-show="manageOption === 3 && !isLoading"
        @reload="reload"
      />
      <div
        v-if="isLoading"
        class="flex justify-center items-center w-full h-screen-60"
      >
        <LoadingSpinner />
      </div>
      <DiscountList
        class="w-full"
        :discounts="discounts"
        v-show="manageOption === 4 && !isLoading"
        @reload="reload"
      />
      <AddDiscount
        class="w-full"
        v-show="manageOption === 5 && !isLoading"
        @reload="reload"
      />
      <OrderList
        class="w-full"
        :user="doneOrders"
        v-show="manageOption === 6 && !isLoading"
        @reload="reload"
      />
      <OrderList
        class="w-full"
        :user="doneOrders"
        v-show="manageOption === 7 && !isLoading"
        @reload="reload"
      />
    </div>
  </div>
</template>

<script src="//cdn.jsdelivr.net/chartist.js/latest/chartist.min.js"></script>

<script>
import axios from 'axios'
// import UserList from '~/components/Manage/UserList.vue'
// import BlogList from '~/components/Manage/BlogList.vue'
import BarChart from '~/components/BarChart'

import LoadingSpinner from '~/components/Animation/LoadingSpinner.vue'
import BookList from '~/components/Manage/BookList.vue'
import constant from '~/constant'
import TopNaviBar from '~/components/TopNaviBar.vue'
import AddBookPanel from '~/components/Book/AddBookPanel.vue'
import DiscountList from '~/components/Discount/DiscountList.vue'
import AddDiscount from '~/components/Discount/AddDiscount.vue'
import ChartistChart from '~/components/ChartistChart.vue'
import OrderList from '~/components/Manage/OrderList.vue'

export default {
  components: {
    // UserList,
    // BlogList,
    LoadingSpinner,
    TopNaviBar,
    BookList,
    AddBookPanel,
    DiscountList,
    AddDiscount,
    BarChart,
    ChartistChart,
    OrderList,
  },
  layout: 'empty',
  data() {
    return {
      title: '',
      content: '',
      pendingNews: [],
      news: [],
      books: [],
      sellers: [],
      manageOption: 1,
      bookCount: Number,
      pendingNewsCount: Number,
      newsCount: Number,
      isLoading: false,
      recordsPerPage: 5,
      discounts: [],
      doneOrders: [],
      allBookCount: Number,
      pendingOrderCount: Number,
      allOrderCount: Number,
      soldBookCount: Number,
      buyerCount: Number,
      booksOfShop: [],
      bookJan: Number,
      bookFeb: Number,
      bookMar: Number,
      bookApr: Number,
      bookMay: Number,
      bookJun: Number,
      bookJul: Number,
      bookAug: Number,
      bookSep: Number,
      bookOct: Number,
      bookNov: Number,
      bookDec: Number,
      chartData: {
        // labels: [
        //   'Jan',
        //   'Feb',
        //   'Mar',
        //   'Apr',
        //   'Mai',
        //   'Jun',
        //   'Jul',
        //   'Aug',
        //   'Sep',
        //   'Oct',
        //   'Nov',
        //   'Dec',
        // ],
        // series: [
        //   [
        //     this.bookQuantityJan,
        //     this.bookQuantityFeb,
        //     this.bookQuantityMar,
        //     this.bookQuantityApr,
        //     this.bookQuantityMay,
        //     this.bookQuantityJun,
        //     this.bookQuantityJul,
        //     this.bookQuantityAug,
        //     this.bookQuantitySep,
        //     this.bookQuantityOct,
        //     this.bookQuantityNov,
        //     this.bookQuantityDec,
        //   ],
        //   [3, 2, 9, 5, 4, 6, 4, 6, 7, 8, 7, 4],
        // ],
      },
      chartOptions: {
        seriesBarDistance: 15,
      },
      responsiveOptions: [
        [
          'screen and (min-width: 641px) and (max-width: 1024px)',
          {
            seriesBarDistance: 10,
            axisX: {
              labelInterpolationFnc: function (value) {
                return value
              },
            },
          },
        ],
        [
          'screen and (max-width: 640px)',
          {
            seriesBarDistance: 5,
            axisX: {
              labelInterpolationFnc: function (value) {
                return value[0]
              },
            },
          },
        ],
      ],
    }
  },
  async created() {
    // if (
    //   !localStorage.getItem('accessToken') ||
    //   localStorage.getItem('accessToken') === 'false'
    // )
    //   this.$router.push('/auth/login')
    const authorization = `Bearer ${localStorage.getItem('accessToken')}`
    const userId = `${localStorage.getItem('userId')}`
    axios({
      method: 'get',
      url: `${constant.base_url}/user/books?page=1&limit=${this.recordsPerPage}`,
      headers: {
        Authorization: authorization,
        'ngrok-skip-browser-warning': 'skip-browser-warning',
      },
    })
      .then((res) => {
        console.log(res.data)
        this.books = res.data.books
        this.bookCount = res.data.count
      })
      .catch((err) => {
        console.log(err)
      })
      .finally(() => {
        this.isLoading = false
      })

    // axios({
    //   method: 'get',
    //   url: `${constant.base_url}/discount/${userId}`,
    //   headers: {
    //     'ngrok-skip-browser-warning': 'skip-browser-warning',
    //   },
    // })
    //   .then((res) => {
    //     console.log(res.data)
    //     this.discounts = res.data
    //   })
    //   .catch((err) => {
    //     console.log(err)
    //   })
    //   .finally(() => {
    //     this.isLoading = false
    //   })

    axios({
      method: 'get',
      url: `${constant.base_url}/order/shop/${userId}`,
      headers: {
        'ngrok-skip-browser-warning': 'skip-browser-warning',
        Authorization: authorization,
      },
    })
      .then((res) => {
        console.log(res.data)
        this.doneOrders = res.data
      })
      .catch((err) => {
        console.log(err)
      })
      .finally(() => {
        this.isLoading = false
      })

    axios({
      method: 'get',
      url: `${constant.base_url}/statistical/books_count/${userId}`,
      headers: {
        'ngrok-skip-browser-warning': 'skip-browser-warning',
        Authorization: authorization,
      },
    })
      .then((res) => {
        console.log(res.data)
        this.allBookCount = res.data.books_count
      })
      .catch((err) => {
        console.log(err)
      })
      .finally(() => {
        this.isLoading = false
      })
    axios({
      method: 'get',
      url: `${constant.base_url}/statistical/pending_confirmation/${userId}`,
      headers: {
        'ngrok-skip-browser-warning': 'skip-browser-warning',
        Authorization: authorization,
      },
    })
      .then((res) => {
        console.log(res.data)
        this.pendingOrderCount = res.data.pending_orders_count
      })
      .catch((err) => {
        console.log(err)
      })
      .finally(() => {
        this.isLoading = false
      })
    axios({
      method: 'get',
      url: `${constant.base_url}/statistical/orders_count/${userId}`,
      headers: {
        'ngrok-skip-browser-warning': 'skip-browser-warning',
        Authorization: authorization,
      },
    })
      .then((res) => {
        console.log(res.data)
        this.allOrderCount = res.data.orders_count
      })
      .catch((err) => {
        console.log(err)
      })
      .finally(() => {
        this.isLoading = false
      })
    axios({
      method: 'get',
      url: `${constant.base_url}/statistical/sold_books_count/${userId}`,
      headers: {
        'ngrok-skip-browser-warning': 'skip-browser-warning',
        Authorization: authorization,
      },
    })
      .then((res) => {
        console.log(res.data)
        this.soldBookCount = res.data
      })
      .catch((err) => {
        console.log(err)
      })
      .finally(() => {
        this.isLoading = false
      })
    axios({
      method: 'get',
      url: `${constant.base_url}/statistical/sold_books_count/${userId}`,
      headers: {
        'ngrok-skip-browser-warning': 'skip-browser-warning',
        Authorization: authorization,
      },
    })
      .then((res) => {
        console.log(res.data)
        this.soldBookCount = res.data
      })
      .catch((err) => {
        console.log(err)
      })
      .finally(() => {
        this.isLoading = false
      })
    await axios({
      method: 'get',
      url: `${constant.base_url}/book/shop/${userId}`,
      headers: {
        'ngrok-skip-browser-warning': 'skip-browser-warning',
        Authorization: authorization,
      },
    })
      .then((res) => {
        console.log(res.data)
        this.booksOfShop = res.data
      })
      .catch((err) => {
        console.log(err)
      })
      .finally(() => {
        this.isLoading = false
      })
    this.chartData = {
      labels: [
        'Jan',
        'Feb',
        'Mar',
        'Apr',
        'May',
        'Jun',
        'Jul',
        'Aug',
        'Sep',
        'Oct',
        'Nov',
        'Dec',
      ],
      series: [
        [
          this.bookQuantityJan,
          this.bookQuantityFeb,
          this.bookQuantityMar,
          this.bookQuantityApr,
          parseInt(this.bookQuantityMay),
          this.bookQuantityJun,
          this.bookQuantityJul,
          this.bookQuantityAug,
          this.bookQuantitySep,
          this.bookQuantityOct,
          this.bookQuantityNov,
          this.bookQuantityDec,
        ],
        [200, 200, 200, 200, 200, 200, 250, 270, 150, 290, 268, 176],
      ],
    }
  },
  computed: {
    chartDataComputed() {
      return {
        labels: [
          'Jan',
          'Feb',
          'Mar',
          'Apr',
          'May',
          'Jun',
          'Jul',
          'Aug',
          'Sep',
          'Oct',
          'Nov',
          'Dec',
        ],
        series: [
          [
            this.bookJan,
            this.bookFeb,
            this.bookMar,
            this.bookApr,
            this.bookMay,
            this.bookJun,
            this.bookJul,
            this.bookAug,
            this.bookSep,
            this.bookOct,
            this.bookNov,
            this.bookDec,
          ],
          [200, 200, 200, 200, 200, 200, 250, 270, 150, 290, 268, 176],
        ],
      }
    },
    bookQuantitySeries() {
      const currentYear = 2024 // Or dynamically get the current year
      return [
        this.getBookQuantitiesForYear(currentYear),
        [3, 2, 9, 5, 4, 6, 4, 6, 7, 8, 7, 4],
      ]
    },
    bookQuantityJan() {
      this.bookJan = this.books
        .filter((book) => {
          const { month, year } = this.parseDate(book.time_create)
          console.log('dateeee', month, year)
          return month === 0 && year === 2024
        })
        .reduce((sum, book) => sum + book.Quantity, 0)
      return this.books
        .filter((book) => {
          const { month, year } = this.parseDate(book.time_create)
          console.log('dateeee', month, year)
          return month === 0 && year === 2024
        })
        .reduce((sum, book) => sum + book.Quantity, 0)
    },
    bookQuantityFeb() {
      this.bookFeb = this.books
        .filter((book) => {
          const { month, year } = this.parseDate(book.time_create)
          console.log('dateeee', month, year)
          return month === 0 && year === 2024
        })
        .reduce((sum, book) => sum + book.Quantity, 0)
      return this.books
        .filter((book) => {
          const { month, year } = this.parseDate(book.time_create)
          console.log('dateeee', month)
          return month === 1 && year === 2024
        })
        .reduce((sum, book) => sum + book.Quantity, 0)
    },
    bookQuantityMar() {
      this.bookMar = this.books
        .filter((book) => {
          const { month, year } = this.parseDate(book.time_create)
          console.log('dateeee', month, year)
          return month === 0 && year === 2024
        })
        .reduce((sum, book) => sum + book.Quantity, 0)
      return this.books
        .filter((book) => {
          const { month, year } = this.parseDate(book.time_create)
          console.log('dateeee', month)
          return month === 2 && year === 2024
        })
        .reduce((sum, book) => sum + book.Quantity, 0)
    },
    bookQuantityApr() {
      this.bookApr = this.books
        .filter((book) => {
          const { month, year } = this.parseDate(book.time_create)
          console.log('dateeee', month, year)
          return month === 0 && year === 2024
        })
        .reduce((sum, book) => sum + book.Quantity, 0)
      return this.books
        .filter((book) => {
          const { month, year } = this.parseDate(book.time_create)
          console.log('dateeee', month)
          return month === 3 && year === 2024
        })
        .reduce((sum, book) => sum + book.Quantity, 0)
    },
    async bookQuantityMay() {
      const mayBooks = this.books.filter((book) => {
        const { month, year } = this.parseDate(book.time_create)
        console.log('dateeee', month, year)
        return month === 4 && year === 2024 // May is month 4
      })

      const sumMayBooks = mayBooks.reduce((sum, book) => sum + book.Quantity, 0)
      this.bookMay = sumMayBooks
      console.log(this.bookMay)

      return sumMayBooks
    },

    bookQuantityJun() {
      this.bookJun = this.books
        .filter((book) => {
          const { month, year } = this.parseDate(book.time_create)
          console.log('dateeee', month, year)
          return month === 0 && year === 2024
        })
        .reduce((sum, book) => sum + book.Quantity, 0)
      return this.books
        .filter((book) => {
          const { month, year } = this.parseDate(book.time_create)
          console.log('dateeee', month)
          return month === 5 && year === 2024
        })
        .reduce((sum, book) => sum + book.Quantity, 0)
    },
    bookQuantityJul() {
      this.bookJul = this.books
        .filter((book) => {
          const { month, year } = this.parseDate(book.time_create)
          console.log('dateeee', month, year)
          return month === 0 && year === 2024
        })
        .reduce((sum, book) => sum + book.Quantity, 0)
      return this.books
        .filter((book) => {
          const { month, year } = this.parseDate(book.time_create)
          console.log('dateeee', month)
          return month === 6 && year === 2024
        })
        .reduce((sum, book) => sum + book.Quantity, 0)
    },
    bookQuantityAug() {
      this.bookAug = this.books
        .filter((book) => {
          const { month, year } = this.parseDate(book.time_create)
          console.log('dateeee', month, year)
          return month === 0 && year === 2024
        })
        .reduce((sum, book) => sum + book.Quantity, 0)
      return this.books
        .filter((book) => {
          const { month, year } = this.parseDate(book.time_create)
          console.log('dateeee', month)
          return month === 7 && year === 2024
        })
        .reduce((sum, book) => sum + book.Quantity, 0)
    },
    bookQuantitySep() {
      this.bookSep = this.books
        .filter((book) => {
          const { month, year } = this.parseDate(book.time_create)
          console.log('dateeee', month, year)
          return month === 0 && year === 2024
        })
        .reduce((sum, book) => sum + book.Quantity, 0)
      return this.books
        .filter((book) => {
          const { month, year } = this.parseDate(book.time_create)
          console.log('dateeee', month)
          return month === 8 && year === 2024
        })
        .reduce((sum, book) => sum + book.Quantity, 0)
    },
    bookQuantityOct() {
      this.bookOct = this.books
        .filter((book) => {
          const { month, year } = this.parseDate(book.time_create)
          console.log('dateeee', month, year)
          return month === 0 && year === 2024
        })
        .reduce((sum, book) => sum + book.Quantity, 0)
      return this.books
        .filter((book) => {
          const { month, year } = this.parseDate(book.time_create)
          console.log('dateeee', month)
          return month === 9 && year === 2024
        })
        .reduce((sum, book) => sum + book.Quantity, 0)
    },
    bookQuantityNov() {
      this.bookNov = this.books
        .filter((book) => {
          const { month, year } = this.parseDate(book.time_create)
          console.log('dateeee', month, year)
          return month === 0 && year === 2024
        })
        .reduce((sum, book) => sum + book.Quantity, 0)
      return this.books
        .filter((book) => {
          const { month, year } = this.parseDate(book.time_create)
          console.log('dateeee', month)
          return month === 10 && year === 2024
        })
        .reduce((sum, book) => sum + book.Quantity, 0)
    },
    bookQuantityDec() {
      this.bookDec = this.books
        .filter((book) => {
          const { month, year } = this.parseDate(book.time_create)
          console.log('dateeee', month, year)
          return month === 0 && year === 2024
        })
        .reduce((sum, book) => sum + book.Quantity, 0)
      return this.books
        .filter((book) => {
          const { month, year } = this.parseDate(book.time_create)
          console.log('dateeee', month)
          return month === 11 && year === 2024
        })
        .reduce((sum, book) => sum + book.Quantity, 0)
    },
    pendingOrder(){
      return this.doneOrders.filter(order => order.Status === "đang chờ");
    }
  },
  methods: {
    parseDate(dateString) {
      // Define a mapping of month names to their corresponding numbers
      const monthNames = [
        'Jan',
        'Feb',
        'Mar',
        'Apr',
        'May',
        'Jun',
        'Jul',
        'Aug',
        'Sep',
        'Oct',
        'Nov',
        'Dec',
      ]

      // Split the date string to extract day, month, and year
      const parts = dateString.split(' ')
      const month = parts[2]
      const year = parseInt(parts[3], 10)

      // Convert month name to month number
      const monthNumber = monthNames.indexOf(month)

      return { month: monthNumber, year: year }
    },
    bookQuantityForMonthYear(month, year) {
      return this.books
        .filter((book) => {
          const date = new Date(book.time_create)
          return date.getMonth() === month && date.getFullYear() === year
        })
        .reduce((sum, book) => sum + book.quantity, 0)
    },
    getBookQuantitiesForYear(year) {
      const months = Array(12).fill(0)
      for (let month = 0; month < 12; month++) {
        months[month] = this.bookQuantityForMonthYear(month, year)
      }
      return months
    },
    reload() {
      const authorization = `Bearer ${localStorage.getItem('accessToken')}`
      const userId = `${localStorage.getItem('userId')}`
      axios({
        method: 'get',
        url: `${constant.base_url}/user/books?page=1&limit=${this.recordsPerPage}`,
        headers: {
          Authorization: authorization,
          'ngrok-skip-browser-warning': 'skip-browser-warning',
        },
      })
        .then((res) => {
          console.log(res.data)
          this.books = res.data.books
          this.bookCount = res.data.count
        })
        .catch((err) => {
          console.log(err)
        })
        .finally(() => {
          this.isLoading = false
        })
      // axios({
      //   method: 'get',
      //   url: `${constant.base_url}/discount/${userId}`,
      //   headers: {
      //     'ngrok-skip-browser-warning': 'skip-browser-warning',
      //   },
      // })
      //   .then((res) => {
      //     console.log(res.data)
      //     this.discounts = res.data
      //   })
      //   .catch((err) => {
      //     console.log(err)
      //   })
      //   .finally(() => {
      //     this.isLoading = false
      //   })
      axios({
        method: 'get',
        url: `${constant.base_url}/statistical/books_count/${userId}`,
        headers: {
          'ngrok-skip-browser-warning': 'skip-browser-warning',
          Authorization: authorization,
        },
      })
        .then((res) => {
          console.log(res.data)
          this.allBookCount = res.data.books_count
        })
        .catch((err) => {
          console.log(err)
        })
        .finally(() => {
          this.isLoading = false
        })
      axios({
        method: 'get',
        url: `${constant.base_url}/statistical/pending_confirmation/${userId}`,
        headers: {
          'ngrok-skip-browser-warning': 'skip-browser-warning',
          Authorization: authorization,
        },
      })
        .then((res) => {
          console.log(res.data)
          this.pendingOrderCount = res.data.pending_orders_count
        })
        .catch((err) => {
          console.log(err)
        })
        .finally(() => {
          this.isLoading = false
        })
      axios({
        method: 'get',
        url: `${constant.base_url}/statistical/orders_count/${userId}`,
        headers: {
          'ngrok-skip-browser-warning': 'skip-browser-warning',
          Authorization: authorization,
        },
      })
        .then((res) => {
          console.log(res.data)
          this.allOrderCount = res.data.orders_count
        })
        .catch((err) => {
          console.log(err)
        })
        .finally(() => {
          this.isLoading = false
        })
      axios({
        method: 'get',
        url: `${constant.base_url}/statistical/sold_books_count/${userId}`,
        headers: {
          'ngrok-skip-browser-warning': 'skip-browser-warning',
          Authorization: authorization,
        },
      })
        .then((res) => {
          console.log(res.data)
          this.soldBookCount = res.data
        })
        .catch((err) => {
          console.log(err)
        })
        .finally(() => {
          this.isLoading = false
        })
      axios({
        method: 'get',
        url: `${constant.base_url}/book/shop/${userId}`,
        headers: {
          'ngrok-skip-browser-warning': 'skip-browser-warning',
          Authorization: authorization,
        },
      })
        .then((res) => {
          console.log(res.data)
          this.booksOfShop = res.data
        })
        .catch((err) => {
          console.log(err)
        })
        .finally(() => {
          this.isLoading = false
        })
    },
    submit() {
      axios({
        method: 'post',
        url: `http://${process.env.BASE_URL}:3000/auth/reset-password`,
        data: {
          title: this.title,
          content: this.content,
          createdAt: Date.now(),
        },
      })
        .then((response) => {
          console.log(response)
          this.$notify({
            title: 'Success',
            text: response.data.message,
            type: 'success',
          })
          return response.data
        })
        .catch((error) => {
          console.error('Login error:', error)
          this.$notify({
            title: 'Error',
            text: error.response.data.message,
            type: 'error',
          })
        })
    },
    changeBookPage(page, limit) {
      const authorization = `Bearer ${localStorage.getItem('accessToken')}`
      console.log('page: ' + page + ' limit: ' + limit)
      console.log('oke')
      this.isLoading = true
      axios({
        method: 'get',
        url: `${constant.base_url}/user/books?page=${page}&limit=${limit}`,
        headers: {
          Authorization: authorization,
          'ngrok-skip-browser-warning': 'skip-browser-warning',
        },
      })
        // this.$axios
        //   .get(`//?page=${page}&limit=${limit}`)
        .then((res) => {
          this.books = res.data.books
          this.bookCount = res.data.count
        })
        .catch((err) => {
          console.log(err)
        })
        .finally(() => {
          this.isLoading = false
        })
    },
    changeOption(optionNumber) {
      this.manageOption = optionNumber
    },
    changePendingPage(page, limit) {
      console.log('page: ' + page + ' limit: ' + limit)
      console.log('oke')
      this.isLoading = true
      this.$axios
        .get(`/blogs/awaiting-approval/?page=${page}&limit=${limit}`)
        .then((res) => {
          this.pendingNews = res.data.docs
          this.pendingNewsCount = res.data.totalDocs
        })
        .catch((err) => {
          console.log(err)
        })
        .finally(() => {
          this.isLoading = false
        })
    },
    changeNewsPage(page, limit) {
      console.log('page: ' + page + ' limit: ' + limit)
      console.log('oke')
      this.isLoading = true
      this.$axios
        .get(`/blogs/?page=${page}&limit=${limit}`)
        .then((res) => {
          this.news = res.data.docs
          this.newsCount = res.data.totalDocs
        })
        .catch((err) => {
          console.log(err)
        })
        .finally(() => {
          this.isLoading = false
        })
    },
    setLoading() {
      this.isLoading = true
    },
    doneLoading() {
      this.isLoading = false
    },
  },
}
</script>

<style lang="scss" scoped>
@import '~/assets/scss/variables.scss';
// @import "_my-chartist-settings.scss";
@import 'chartist/dist/scss/chartist.scss';

.default {
  display: flex;
  flex-direction: column;
  background-color: #f3f6ff;
  min-height: 100vh;
  height: 100%;
  overflow: hidden;
  gap: 20px;
  position: relative;
  height: 100vh;
  overflow: auto;
  // background: $dark-2;

  &__top {
    height: 80px;
    position: sticky;
    width: 100%;
    left: 0;
    top: 0;
    z-index: 10;
  }

  &__tableft {
    height: 100%;
    max-width: 239px;
  }

  &__tabright {
    height: 100%;
    max-width: 239px;
  }

  &__body {
    display: inline-flex;
    align-items: flex-start;
    justify-content: space-between;
    gap: 20px;
    width: 100%;
    padding: 0 20px;

    &__container {
      width: 100%;
    }
  }

  .footer {
  }
}

.tableft {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 20px;

  &__item {
    border-radius: 16px;
    background: #1b3764; // $dark-3;
    display: flex;
    width: 210px;
    padding: 10px;
    flex-direction: column;
    align-items: flex-start;
    gap: 10px;

    .category {
      &__item {
        display: flex;
        align-items: center;
        width: 100%;
        padding: 6px 5px;
        gap: 10px;
        border-radius: 6px;
        // background: $dark-3;
        cursor: pointer;

        img {
          display: flex;
          height: 100%;
          object-fit: contain;
          justify-content: center;
          align-items: center;
          padding: 4px;
          gap: 10px;
        }

        &__info {
          display: flex;
          flex-direction: column;
          align-items: flex-start;
          gap: 2px;

          .name {
            color: $neutral-0;
            font-family: 'Montserrat', sans-serif;
            font-size: 12px;
            font-style: normal;
            font-weight: 600;
            line-height: 18px;
            /* 150% */
          }

          .desc {
            color: #97989d;
            /* Regular 9 */
            font-family: 'Montserrat', sans-serif;
            font-size: 10px;
            font-style: normal;
            font-weight: 400;
            line-height: 14px;
            /* 155.556% */
          }
        }

        &:hover {
          background: $dark-4;
        }
      }
    }
  }
}
</style>
