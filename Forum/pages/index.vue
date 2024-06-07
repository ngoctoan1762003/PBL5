<template>
  <div>
    <TopNaviBarGuest v-if="isLogedIn === false" />
    <TopNaviBar v-else />
    <SearchBar @search="search" @filterChange="filterChange" />
    <div class="flex flex-wrap p-10 gap-10 justify-center">
      <div v-for="book in filterdBook" :key="book.BookId" class="w-[20%]">
        <VerticalBookCard :book="book" />
      </div>
    </div>
    <FooterBar />
  </div>
</template>

<script>
import axios from 'axios'
import constant from '~/constant'
import TopNaviBarGuest from '~/components/TopNaviBarGuest.vue'
import SearchBar from '~/components/SearchBar.vue'
import VerticalBookCard from '~/components/Book/VerticalBookCard.vue'
import FooterBar from '~/components/FooterBar.vue'
import TopNaviBar from '~/components/TopNaviBar.vue'
export default {
  layout: 'empty',
  components: {
    TopNaviBarGuest,
    SearchBar,
    VerticalBookCard,
    FooterBar,
    TopNaviBar,
  },
  data() {
    return {
      books: [],
      isLogedIn: false,
      keyword: '',
      genre: '',
      sortByName: '',
      sortByPrice: '',
    }
  },
  computed: {
    filterdBook() {
      const lowerCaseKeyword = this.keyword.toLowerCase()
      let filteredBooks = this.books.filter((book) =>
        book.title.toLowerCase().includes(lowerCaseKeyword)
      )

      console.log(this.genre)
      console.log(filteredBooks)
      if (this.genre) {
        filteredBooks = filteredBooks.filter(
          (book) => book.genre === this.genre
        )
      }

      // Sort by name
      console.log("sort", this.sortOrder)
      if (this.sortOrder) {
        filteredBooks = filteredBooks.sort((a, b) => {
          const titleA = a.title.toLowerCase()
          const titleB = b.title.toLowerCase()
          if (this.sortOrder === 'asc') {
            return titleA < titleB ? -1 : titleA > titleB ? 1 : 0
          } else {
            return titleA > titleB ? -1 : titleA < titleB ? 1 : 0
          }
        })
      }

      // // Sort by price
      console.log("price", this.priceSortOrder)
      if (this.priceSortOrder) {
        filteredBooks = filteredBooks.sort((a, b) => {
          const priceA = parseFloat(a.price)
          const priceB = parseFloat(b.price)
          if (this.priceSortOrder === 'asc') {
            return priceA - priceB
          } else {
            return priceB - priceA
          }
        })
      }

      return filteredBooks
    },
  },
  mounted() {
    if (localStorage.getItem('accessToken')) this.isLogedIn = true
    axios({
      method: 'get',
      url: `${constant.base_url}/book/getallbook`,
      headers: {
        'ngrok-skip-browser-warning': 'skip-browser-warning',
      },
    })
      .then((res) => {
        console.log(res)
        const data = res.data
        console.log(data)
        this.books = data
      })
      .catch((err) => {
        console.log(err)
        this.$notify({
          title: 'Thất bại',
          text: 'Duyệt thất bại: ' + err.response.data.message,
          type: 'success',
          group: 'foo',
        })
      })
  },
  methods: {
    search(keyword) {
      this.keyword = keyword
    },
    filterChange(genre, sortByName, sortByPrice) {
      this.sortOrder = sortByName
      this.priceSortOrder = sortByPrice
      this.genre = "h"
      this.genre = genre
      console.log(genre, sortByName, sortByPrice)
    },
  },
}
</script>