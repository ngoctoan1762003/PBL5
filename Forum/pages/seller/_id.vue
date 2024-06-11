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
          <!-- <div class="category__item" @click="changeOption(6)">
            <div
              class="w-[30px] bg-[#2C353D] rounded-[5px] pr-[-10px] ml-[2px]"
            >
              <img class="w-[30px]" src="~/assets/icon/order.svg" alt="" />
            </div>
            <div class="category__item__info">
              <span class="name">Hóa đơn đã đặt tại cửa hàng</span>
            </div>
          </div> -->
          <div class="category__item" @click="changeOption(7)">
            <div class="bg-[#2C353D] rounded-[5px] pr-[-10px] ml-[2px]">
              <img class="w-[30px]" src="~/assets/icon/order.svg" alt="" />
            </div>
            <div class="category__item__info">
              <span class="name">Quản lý hóa đơn</span>
            </div>
          </div>
        </div>
      </div>
      <div
        v-show="manageOption === 1 && !isLoading"
        class="w-[100%] flex flex-col"
      >
        <div class="flex h-min-[200px] justify-between gap-5 px-5">
          <div
            class="bg-[#1B3764] cursor-pointer max-h-[200px] flex flex-col gap-2 py-5 px-4 min-w-[300px] max-w-[300px] rounded-[20px]"
          >
            <div class="text-white text-[22px] font-semibold">Tổng số sách</div>
            <div class="text-white text-[18px]">{{ allBookCount }} quyển</div>
          </div>
          <div
            class="bg-[#1B3764] cursor-pointer max-h-[200px] flex flex-col gap-2 py-5 px-4 min-w-[300px] max-w-[300px] rounded-[20px]"
          >
            <div class="text-white text-[22px] font-semibold">
              Số sách đã bán
            </div>
            <div class="text-white text-[18px]">{{ soldBookCount }} quyển</div>
          </div>
          <div
            class="bg-[#1B3764] cursor-pointer max-h-[200px] flex flex-col gap-2 py-5 px-4 min-w-[300px] max-w-[300px] rounded-[20px]"
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
            class="relative cursor-pointer bg-[#1B3764] max-h-[200px] flex flex-col gap-2 py-5 px-4 min-w-[300px] max-w-[300px] rounded-[20px]"
            @click="changeOption(7)"
          >
            <div
              class="absolute right-[-10px] top-[-10px] bg-red-500 w-[25px] h-[25px] z-[10] rounded-full animate-jump"
              v-show="pendingOrderCount > 0"
            ></div>
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
          <div class="flex justify-center gap-5">
            <div
              class="bg-white rounded-md shadow-md p-5 flex flex-col items-center gap-5 font-semibold w-[60%]"
            >
              <LineChart class="w-[100%]" :planetChartData="planetChartData" />
              <label for="">Biểu đồ thông tin kinh doanh</label>
            </div>
            <div
              class="bg-white rounded-md shadow-md p-5 flex flex-col items-center gap-5 font-semibold w-[30%]"
            >
              <PieChart class="w-[100%]" :planetChartData="pieChartData" />
              <label for="">Biểu đồ tỉ lệ thể loại sách</label>
            </div>
          </div>
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
import LineChart from '~/components/LineChart.vue'
import PieChart from '~/components/PieChart.vue'

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
    LineChart,
    PieChart,
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
      yearStatistic: [],
      planetChartData: {
        type: 'line',
        data: {
          labels: [
            'Tháng 1',
            'Tháng 2',
            'Tháng 3',
            'Tháng 4',
            'Tháng 5',
            'Tháng 6',
            'Tháng 7',
            'Tháng 8',
            'Tháng 9',
            'Tháng 10',
            'Tháng 11',
            'Tháng 12',
          ],
          datasets: [
            // {
            //   label: 'Số sách thêm vào mỗi tháng',
            //   data: [0, 0, 1, 2, 79, 82, 27, 14, 20, 20, 10, 309],
            //   backgroundColor: 'rgba(54,73,93,.5)',
            //   borderColor: '#36495d',
            //   borderWidth: 3,
            // },
            {
              label: 'Số sách đã bán mỗi tháng',
              data: [
                0.166, 2.081, 3.003, 0.323, 954.792, 285.886, 43.662, 51.514,
                90, 103, 120, 30,
              ],
              backgroundColor: 'rgba(71, 183,132,.5)',
              borderColor: '#47b784',
              borderWidth: 3,
            },
            {
              label: 'Số đơn đặt hàng mỗi tháng',
              data: [1, 2, 3, 4, 5, 6, 7, 8, 120, 10, 12, 12],
              backgroundColor: 'rgba(255, 0, 0,.5)',
              borderColor: '#ff0000',
              borderWidth: 3,
            },
            {
              label: 'Số khách hàng mỗi tháng',
              data: [80, 200, 30, 420, 510, 380, 209, 609, 932, 210, 290, 801],
              backgroundColor: 'rgba(0, 0, 255,.5)',
              borderColor: '#0000ff',
              borderWidth: 3,
            },
            {
              label: 'Doanh thu mỗi tháng (triệu đồng)',
              data: [800, 20, 300, 42, 51, 38, 29, 609, 20, 180, 320, 30],
              backgroundColor: 'rgba(255, 255, 0,.5)',
              borderColor: '#ffff00',
              borderWidth: 3,
            },
          ],
        },
        options: {
          responsive: true,
          lineTension: 1,
          scales: {
            yAxes: [
              {
                ticks: {
                  beginAtZero: true,
                  padding: 25,
                },
              },
            ],
          },
        },
      },
      pieChartData: {
        type: 'pie',
        data: {
          labels: [
            'Tháng 1',
            'Tháng 2',
            'Tháng 3',
            'Tháng 4',
            'Tháng 5',
            'Tháng 6',
            'Tháng 7',
            'Tháng 8',
          ],
          datasets: [
            {
              label: 'Số sách thêm vào mỗi tháng',
              data: [0, 0, 1, 2, 79, 82, 27, 14],
              backgroundColor: [
                'rgba(54,73,93,.5)',
                'rgba(71, 183,132,.5)',
                'rgba(255, 0, 0,.5)',
                'rgba(255, 165, 0,.5)',
                'rgba(0, 128, 0,.5)',
                'rgba(0, 0, 255,.5)',
                'rgba(75, 0, 130,.5)',
                'rgba(238, 130, 238,.5)',
              ],
              borderColor: [
                '#36495d',
                '#47b784',
                '#ff0000',
                '#ffa500',
                '#008000',
                '#0000ff',
                '#4b0082',
                '#ee82ee',
              ],
              borderWidth: 3,
            },
          ],
        },
        options: {
          responsive: true,
          plugins: {
            legend: {
              position: 'top',
            },
            tooltip: {
              enabled: true,
            },
          },
        },
      },
    }
  },
  async created() {
    this.isLoading = true
    const authorization = `Bearer ${localStorage.getItem('accessToken')}`
    const userId = `${localStorage.getItem('userId')}`

    try {
      const [
        booksRes,
        discountsRes,
        doneOrdersRes,
        allBookCountRes,
        pendingOrderCountRes,
        allOrderCountRes,
        soldBookCountRes,
        booksOfShopRes,
        yearStatisticRes,
      ] = await Promise.all([
        axios.get(
          `${constant.base_url}/user/books?page=1&limit=${this.recordsPerPage}`,
          {
            headers: {
              Authorization: authorization,
              'ngrok-skip-browser-warning': 'skip-browser-warning',
            },
          }
        ),
        axios.get(`${constant.base_url}/discount/${userId}`, {
          headers: { 'ngrok-skip-browser-warning': 'skip-browser-warning' },
        }),
        axios.get(`${constant.base_url}/order/shop/${userId}`, {
          headers: {
            Authorization: authorization,
            'ngrok-skip-browser-warning': 'skip-browser-warning',
          },
        }),
        axios.get(`${constant.base_url}/statistical/books_count/${userId}`, {
          headers: {
            Authorization: authorization,
            'ngrok-skip-browser-warning': 'skip-browser-warning',
          },
        }),
        axios.get(
          `${constant.base_url}/statistical/orders_count/${userId}/Đang chờ xác nhận`,
          {
            headers: {
              Authorization: authorization,
              'ngrok-skip-browser-warning': 'skip-browser-warning',
            },
          }
        ),
        axios.get(`${constant.base_url}/statistical/orders_count/${userId}`, {
          headers: {
            Authorization: authorization,
            'ngrok-skip-browser-warning': 'skip-browser-warning',
          },
        }),
        axios.get(`${constant.base_url}/statistical/sales_quantity/${userId}`, {
          headers: {
            Authorization: authorization,
            'ngrok-skip-browser-warning': 'skip-browser-warning',
          },
        }),
        axios.get(`${constant.base_url}/book/shop/${userId}`, {
          headers: {
            Authorization: authorization,
            'ngrok-skip-browser-warning': 'skip-browser-warning',
          },
        }),
        axios.get(
          `${constant.base_url}/statistical/total_amount_of_month/${userId}/2024`,
          {
            headers: {
              Authorization: authorization,
              'ngrok-skip-browser-warning': 'skip-browser-warning',
            },
          }
        ),
      ])

      this.books = booksRes.data.books
      this.bookCount = booksRes.data.count
      this.discounts = discountsRes.data
      this.doneOrders = doneOrdersRes.data.order_details
      this.allBookCount = allBookCountRes.data.books_count
      this.pendingOrderCount = pendingOrderCountRes.data.orders_count
      this.allOrderCount = allOrderCountRes.data.orders_count
      this.soldBookCount = soldBookCountRes.data[0].totalBookCount
      this.booksOfShop = booksOfShopRes.data
      this.yearStatistic = yearStatisticRes.data
      console.log(this.yearStatistic)
      console.log(this.booksOfShop)
      this.assignDataYearStatistic()
      this.assignPieData()
    } catch (err) {
      console.error(err)
    } finally {
      console.log('done order', this.doneOrders)
    }
  },
  computed: {
    pendingOrder() {
      return this.doneOrders.filter((order) => order.Status === 'Đã xác nhận')
    },
    filteredDoneOrders() {
      return this.doneOrders.filter((order) => order.Status === 'pending')
    },
  },
  methods: {
    assignPieData() {
      axios
        .get(`${constant.base_url}/book/genre`, {
          headers: {
            'ngrok-skip-browser-warning': 'skip-browser-warning',
          },
        })
        .then((res) => {
          const genres = [
            ...new Set(this.booksOfShop.books.map((book) => book.Genre)),
          ]

          // Counting the number of books in each genre
          const genreCounts = genres.map((genre) => ({
            genre: genre,
            count: this.booksOfShop.books.filter((book) => book.Genre === genre)
              .length,
          }))
          console.log(genres)
          console.log(genreCounts)
          // Preparing the pie chart data
          this.pieChartData.data = {
            labels: genreCounts.map((gc) => gc.genre),
            datasets: [
              {
                label: 'Thể loại sách',
                data: genreCounts.map((gc) => gc.count),
                backgroundColor: [
                  'rgba(255, 99, 132, 0.2)',
                  'rgba(54, 162, 235, 0.2)',
                  'rgba(255, 206, 86, 0.2)',
                  'rgba(75, 192, 192, 0.2)',
                  'rgba(153, 102, 255, 0.2)',
                  'rgba(255, 159, 64, 0.2)',
                  'rgba(99, 255, 132, 0.2)',
                  'rgba(162, 54, 235, 0.2)',
                  'rgba(206, 255, 86, 0.2)',
                  'rgba(192, 75, 192, 0.2)',
                  'rgba(102, 153, 255, 0.2)',
                ],
                borderColor: [
                  'rgba(255, 99, 132, 1)',
                  'rgba(54, 162, 235, 1)',
                  'rgba(255, 206, 86, 1)',
                  'rgba(75, 192, 192, 1)',
                  'rgba(153, 102, 255, 1)',
                  'rgba(255, 159, 64, 1)',
                  'rgba(99, 255, 132, 1)',
                  'rgba(162, 54, 235, 1)',
                  'rgba(206, 255, 86, 1)',
                  'rgba(192, 75, 192, 1)',
                  'rgba(102, 153, 255, 1)',
                ],
                borderWidth: 1,
              },
            ],
          }
        })
        .finally(() => {
          this.isLoading = false
        })
    },
    assignDataYearStatistic() {
      // Initialize the datasets to 0 for all 12 months
      // const datasetCount = this.planetChartData.data.datasets.length
      // for (let i = 0; i < datasetCount; i++) {
      //   this.planetChartData.data.datasets[i].data = Array(12).fill(0)
      // }

      // Populate the datasets with the input data
      this.yearStatistic.forEach((data) => {
        const monthIndex = data.month - 1 // Convert month to zero-based index

        this.planetChartData.data.datasets[3].data[monthIndex] =
          data.totalAmount / 1000000 // Doanh thu mỗi tháng (nghìn đồng)
        this.planetChartData.data.datasets[0].data[monthIndex] =
          data.totalBookCount // Số sách thêm vào mỗi tháng
        this.planetChartData.data.datasets[1].data[monthIndex] =
          data.totalOrderDetails // Số đơn đặt hàng mỗi tháng
        this.planetChartData.data.datasets[2].data[monthIndex] =
          data.uniqueUserCount // Số khách hàng mỗi tháng
      })
    },
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

    async reload() {
      this.isLoading = true
      const authorization = `Bearer ${localStorage.getItem('accessToken')}`
      const userId = `${localStorage.getItem('userId')}`

      try {
        const [
          booksRes,
          discountsRes,
          doneOrdersRes,
          allBookCountRes,
          pendingOrderCountRes,
          allOrderCountRes,
          soldBookCountRes,
          booksOfShopRes,
          yearStatisticRes,
        ] = await Promise.all([
          axios.get(
            `${constant.base_url}/user/books?page=1&limit=${this.recordsPerPage}`,
            {
              headers: {
                Authorization: authorization,
                'ngrok-skip-browser-warning': 'skip-browser-warning',
              },
            }
          ),
          axios.get(`${constant.base_url}/discount/${userId}`, {
            headers: { 'ngrok-skip-browser-warning': 'skip-browser-warning' },
          }),
          axios.get(`${constant.base_url}/order/shop/${userId}`, {
            headers: {
              Authorization: authorization,
              'ngrok-skip-browser-warning': 'skip-browser-warning',
            },
          }),
          axios.get(`${constant.base_url}/statistical/books_count/${userId}`, {
            headers: {
              Authorization: authorization,
              'ngrok-skip-browser-warning': 'skip-browser-warning',
            },
          }),
          axios.get(
            `${constant.base_url}/statistical/orders_count/${userId}/Đang chờ xác nhận`,
            {
              headers: {
                Authorization: authorization,
                'ngrok-skip-browser-warning': 'skip-browser-warning',
              },
            }
          ),
          axios.get(`${constant.base_url}/statistical/orders_count/${userId}`, {
            headers: {
              Authorization: authorization,
              'ngrok-skip-browser-warning': 'skip-browser-warning',
            },
          }),
          axios.get(
            `${constant.base_url}/statistical/sales_quantity/${userId}`,
            {
              headers: {
                Authorization: authorization,
                'ngrok-skip-browser-warning': 'skip-browser-warning',
              },
            }
          ),
          axios.get(`${constant.base_url}/book/shop/${userId}`, {
            headers: {
              Authorization: authorization,
              'ngrok-skip-browser-warning': 'skip-browser-warning',
            },
          }),
          axios.get(
            `${constant.base_url}/statistical/total_amount_of_month/${userId}/2024`,
            {
              headers: {
                Authorization: authorization,
                'ngrok-skip-browser-warning': 'skip-browser-warning',
              },
            }
          ),
        ])

        this.books = booksRes.data.books
        this.bookCount = booksRes.data.count
        this.discounts = discountsRes.data
        this.doneOrders = doneOrdersRes.data.order_details
        this.allBookCount = allBookCountRes.data.books_count
        this.pendingOrderCount = pendingOrderCountRes.data.orders_count
        this.allOrderCount = allOrderCountRes.data.orders_count
        this.soldBookCount = soldBookCountRes.data[0].totalBookCount
        this.booksOfShop = booksOfShopRes.data
        this.yearStatistic = yearStatisticRes.data
        this.assignDataYearStatistic()
        this.assignPieData()
      } catch (err) {
        console.error(err)
      } finally {
        this.isLoading = false
      }
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
    loadDoneOrders() {
      const authorization = `Bearer ${localStorage.getItem('accessToken')}`
      const userId = `${localStorage.getItem('userId')}`
      axios({
        method: 'get',
        url: `${constant.base_url}/order/shop/${userId}`,
        headers: {
          'ngrok-skip-browser-warning': 'skip-browser-warning',
          Authorization: authorization,
        },
      })
        .then((res) => {
          console.log('done order', res.data)
          this.doneOrders = res.data
        })
        .catch((err) => {
          console.log(err)
        })
        .finally(() => {
          this.isLoading = false
        })
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
