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
            <img src="~/assets/icon/person.svg" alt="" />
            <div class="category__item__info">
              <span class="name">Quản lý sách</span>
            </div>
          </div>
          <div class="category__item" @click="changeOption(3)">
            <img src="~/assets/icon/person.svg" alt="" />
            <div class="category__item__info">
              <span class="name">Thêm sách</span>
            </div>
          </div>
          <div class="category__item" @click="changeOption(4)">
            <img src="~/assets/icon/person.svg" alt="" />
            <div class="category__item__info">
              <span class="name">Quản lý mã giảm giá</span>
            </div>
          </div>
          <div class="category__item" @click="changeOption(5)">
            <img src="~/assets/icon/person.svg" alt="" />
            <div class="category__item__info">
              <span class="name">Thêm mã giảm giá</span>
            </div>
          </div>
        </div>
      </div>
      <div v-show="manageOption === 1 && !isLoading" class="w-full">
        <ChartistChart
          :data="chartData"
          :options="chartOptions"
          :responsiveOptions="responsiveOptions"
        />
        <div class="ct-chart ct-perfect-fourth"></div>
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
      chartData: {
        labels: [
          'Jan',
          'Feb',
          'Mar',
          'Apr',
          'Mai',
          'Jun',
          'Jul',
          'Aug',
          'Sep',
          'Oct',
          'Nov',
          'Dec',
        ],
        series: [
          [5, 4, 3, 7, 5, 10, 3, 4, 8, 10, 6, 8],
          [3, 2, 9, 5, 4, 6, 4, 6, 7, 8, 7, 4],
        ],
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
  created() {
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

    axios({
      method: 'get',
      url: `${constant.base_url}/discount/${userId}`,
      headers: {
        'ngrok-skip-browser-warning': 'skip-browser-warning',
      },
    })
      .then((res) => {
        console.log(res.data)
        this.discounts = res.data
      })
      .catch((err) => {
        console.log(err)
      })
      .finally(() => {
        this.isLoading = false
      })
  },
  methods: {
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
      axios({
        method: 'get',
        url: `${constant.base_url}/discount/${userId}`,
        headers: {
          'ngrok-skip-browser-warning': 'skip-browser-warning',
        },
      })
        .then((res) => {
          console.log(res.data)
          this.discounts = res.data
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
