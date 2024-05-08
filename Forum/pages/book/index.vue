<template>
  <div>
    <TopNaviBarGuest v-if="isLogedIn === false" />
    <TopNaviBar v-else/>
    <SearchBar />
    <div class="flex flex-wrap p-10 gap-10 justify-center">
      <div v-for="book in books" :key="book.BookId" class="w-[20%]">
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
    TopNaviBar
  },
  data() {
    return {
      books: [],
      isLogedIn: false,
    }
  },
  mounted() {
    if (localStorage.getItem('accessToken')) this.isLogedIn = true;
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
}
</script>