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
              <span class="name">Quản lý người dùng</span>
            </div>
          </div>
          <div class="category__item" @click="changeOption(2)">
            <img src="~/assets/icon/person.svg" alt="" />
            <div class="category__item__info">
              <span class="name">Quản lý người bán</span>
            </div>
          </div>
          <div class="category__item" @click="changeOption(3)">
            <img src="~/assets/icon/popular.svg" alt="" />
            <div class="category__item__info">
              <span class="name">Quản lý sách</span>
            </div>
          </div>
          <div class="category__item" @click="changeOption(4)">
            <img src="~/assets/icon/popular.svg" alt="" />
            <div class="category__item__info">
              <span class="name">Quản lý đơn đặt hàng</span>
            </div>
          </div>
        </div>
      </div>
      <UserList
        class="w-full"
        :users="users"
        @reload="reload"
        v-show="manageOption === 1 && !isLoading"
        @changePage="changeUserPage"
        :count="userCount"
        :recordsPerPage="recordsPerPage"
      />
      <UserList
        class="w-full"
        :users="sellers"
        @reload="reload"
        v-show="manageOption === 2 && !isLoading"
        @changePage="changeSellerPage"
        :count="sellerCount"
        :recordsPerPage="recordsPerPage"
      />
      <BookList
        class="w-full"
        :users="books"
        @reload="reload"
        v-show="manageOption === 3 && !isLoading"
        @changePage="changeBookPage"
        :count="bookCount"
        :recordsPerPage="recordsPerPage"
      />
      <!-- <BlogList v-show="manageOption === 2 && !isLoading" @reload="reload" :news="pendingNews" class="w-full" @changePage="changePendingPage"
       :count="pendingNewsCount" @setLoading="setLoading" @doneLoading="doneLoading" :recordsPerPage="recordsPerPage"/>
      <BlogList v-show="manageOption === 3 && !isLoading" @reload="reload" :news="news" class="w-full" @changePage="changeNewsPage"
       :count="newsCount"  @setLoading="setLoading" @doneLoading="doneLoading" :recordsPerPage="recordsPerPage"/> -->
      <div
        v-if="isLoading"
        class="flex justify-center items-center w-full h-screen-60"
      >
        <LoadingSpinner />
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import UserList from '~/components/Manage/UserList.vue'
// import BlogList from '~/components/Manage/BlogList.vue'
import LoadingSpinner from '~/components/Animation/LoadingSpinner.vue'
import constant from '~/constant'
import TopNaviBar from '~/components/TopNaviBar.vue'
import BookList from '~/components/Manage/BookList.vue'

export default {
  components: {
    UserList,
    BookList,
    // BlogList,
    LoadingSpinner,
    TopNaviBar,
  },
  layout: 'empty',
  data() {
    return {
      title: '',
      content: '',
      pendingNews: [],
      news: [],
      users: [],
      sellers: [],
      books: [],
      manageOption: 1,
      userCount: Number,
      sellerCount: Number,
      bookCount: Number,
      pendingNewsCount: Number,
      newsCount: Number,
      isLoading: false,
      recordsPerPage: 5,
    }
  },
  created() {
    if (
      !localStorage.getItem('accessToken') ||
      localStorage.getItem('accessToken') === 'false'
    )
      this.$router.push('/auth/login')
  },
  mounted() {
    // this.$axios
    //   .get(`/users/?page=1&limit=${this.recordsPerPage}`)
    const authorization = `Bearer ${localStorage.getItem('accessToken')}`
    console.log(authorization)
    axios({
      method: 'get',
      withCredentials: false,
      url: `${constant.base_url}/user/getalluser?page=1&limit=${this.recordsPerPage}`,
      headers: {
        Authorization: authorization,
        'ngrok-skip-browser-warning': 'skip-browser-warning',
      },
    })
      .then((res) => {
        console.log(res)
        this.users = res.data.users
        this.userCount = res.data.count
      })
      .catch((err) => {
        console.error(err)
      })

    axios({
      method: 'get',
      withCredentials: false,
      url: `${constant.base_url}/user/role/seller?page=1&limit=${this.recordsPerPage}`,
      headers: {
        Authorization: authorization,
        'ngrok-skip-browser-warning': 'skip-browser-warning',
      },
    })
      .then((res) => {
        console.log(res)
        this.sellers = res.data.seller
        this.sellerCount = res.data.count
      })
      .catch((err) => {
        console.error(err)
      })

    axios({
      method: 'get',
      url: `${constant.base_url}/book/books?page=1&limit=${this.recordsPerPage}`,
      headers: {
        Authorization: authorization,
        'ngrok-skip-browser-warning': 'skip-browser-warning',
      },
    })
      .then((res) => {
        console.log(res)
        this.books = res.data.books
        this.bookCount = res.data.count
        // this.userCount = res.data.totalDocs
      })
      .catch((err) => {
        console.error(err)
      })
    this.isLoading = false
  },
  methods: {
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
    changeOption(optionNumber) {
      this.manageOption = optionNumber
    },
    reload() {
      this.$axios
        .get(`/users/?page=1&limit=${this.recordsPerPage}`)
        .then((res) => {
          console.log(res)
          this.users = res.data.users
          this.userCount = res.data.count
        })
        .catch((err) => {
          console.error(err)
        })

      this.$axios
        .get(`/blogs/awaiting-approval/?page=1&limit=${this.recordsPerPage}`)
        .then((res) => {
          console.log(res)
          this.pendingNews = res.data.docs
          this.pendingNewsCount = res.data.totalDocs
        })
        .catch((err) => {
          console.error(err)
        })
      this.$axios
        .get(`/blogs/?page=1&limit=${this.recordsPerPage}`, {})
        .then((res) => {
          console.log(res)
          this.news = res.data.docs
          this.newsCount = res.data.totalDocs
        })
        .catch((err) => {
          console.error(err)
        })
      this.isLoading = false
    },
    changeUserPage(page, limit) {
      console.log('page: ' + page + ' limit: ' + limit)
      console.log('oke')
      this.isLoading = true
      // this.$axios
      //   .get(`/users/?page=${page}&limit=${limit}`)
      const authorization = `Bearer ${localStorage.getItem('accessToken')}`
      axios({
        method: 'get',
        withCredentials: false,
        url: `${constant.base_url}/user/getalluser?page=${page}&limit=${limit}`,
        headers: {
          Authorization: authorization,
          'ngrok-skip-browser-warning': 'skip-browser-warning',
        },
      })
        .then((res) => {
          console.log(res.data)
          this.users = res.data.users
          this.userCount = res.data.count
        })
        .catch((err) => {
          console.log(err)
        })
        .finally(() => {
          this.isLoading = false
        })
    },

    changeSellerPage(page, limit) {
      const authorization = `Bearer ${localStorage.getItem('accessToken')}`
      console.log('page: ' + page + ' limit: ' + limit)
      console.log('oke')
      this.isLoading = true
      axios({
        method: 'get',
        url: `${constant.base_url}/user/role/seller?page=${page}&limit=${limit}`,
        headers: {
          Authorization: authorization,
          'ngrok-skip-browser-warning': 'skip-browser-warning',
        },
      })
        .then((res) => {
          this.sellers = res.data.sellers
          this.sellerCount = res.data.count
        })
        .catch((err) => {
          console.log(err)
        })
        .finally(() => {
          this.isLoading = false
        })
    },
    changeBookPage(page, limit) {
      const authorization = localStorage.getItem('accessToken')
      console.log('page: ' + page + ' limit: ' + limit)
      console.log('oke')
      this.isLoading = true
      axios({
        method: 'get',
        url: `${constant.base_url}/book/books?page=${page}&limit=${limit}`,
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
