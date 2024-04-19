<template>
  <div>
    <TopNaviBarGuest />
    <SearchBar />
    <div class="flex flex-wrap p-10 gap-10 justify-center">
      <VerticalBookCard class="w-[20%]" />
      <VerticalBookCard class="w-[20%]" />
      <VerticalBookCard class="w-[20%]" />
      <VerticalBookCard class="w-[20%]" />
      <VerticalBookCard class="w-[20%]" />
      <VerticalBookCard class="w-[20%]" />
      <VerticalBookCard class="w-[20%]" />
      <VerticalBookCard class="w-[20%]" />
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
export default {
  layout: 'empty',
  components: {
    TopNaviBarGuest,
    SearchBar,
    VerticalBookCard,
    FooterBar,
  },
  data() {
    return {
      books: [],
    }
  },
  mounted() {
    axios({
      method: 'get',
      url: `${constant.base_url}/books`,
    })
      .then((res) => {
        console.log(res)
        const data = res.data
        this.books = data
        // console.log(data)
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