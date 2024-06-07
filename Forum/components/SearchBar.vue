<template>
  <div class="relative bg-[#1B3764] flex justify-center items-center p-5">
    <div class="relative w-[80%]">
      <input
        type="text"
        class="border-[1px] shadow-md text-[14px] px-5 py-3 rounded-[20px] w-full"
        placeholder="Tìm kiếm"
        v-model="keyword"
        @keyup.enter="search"
      />
      <img
        src="~/assets/icon/search.svg"
        class="absolute right-5 top-[30%] w-[20px] h-[20px]"
      />
      <div
        class="absolute right-[-50px] top-[30%] w-[20px] h-[20px] flex gap-5 items-center"
      ></div>
    </div>
    <div
      @mouseenter="isShowFilter = true"
      @mouseleave="isShowFilter = false"
      class="relative"
    >
      <button>
        <img src="~/assets/icon/sortByName.svg" class="h-[40px]" alt="" />
      </button>
      <div
        v-show="isShowFilter"
        class="absolute w-[500px] h-[100px] right-[0px]"
      >
        <div
          class="absolute bg-white shadow-lg mt-[-10px] right-[0px] top-[30px] p-3 w-[500px] flex gap-5 text-[12px] flex items-start shadow-md"
          v-show="isShowFilter"
          @mouseenter="isShowFilter = true"
        >
          <div>
            <label for="">Chọn thể loại</label>
            <select
              name=""
              id=""
              class="py-3 w-[150px] text-[13px]"
              @change="onGenreChange"
            >
              <option value="">Tất cả</option>
              <option
                class="py-2 px-3 text-[13px]"
                :value="genre.Theloai"
                v-for="genre in genres"
                :key="genre._id"
              >
                {{ genre.Theloai }}
              </option>
            </select>
          </div>
          <div class="flex flex-col w-[150px]">
            <label for="">Xếp theo tên</label>
            <label class="flex items-center">
              <input
                type="radio"
                name="sortOrder"
                value="asc"
                v-model="sortOrder"
                @change="onSortOrderChange"
              />
              <span class="ml-2 text-[13px]">Từ trên xuống</span>
            </label>
            <label class="flex items-center">
              <input
                type="radio"
                name="sortOrder"
                value="desc"
                v-model="sortOrder"
                @change="onSortOrderChange"
              />
              <span class="ml-2 text-[13px]">Từ dưới lên</span>
            </label>
          </div>
          <div class="flex flex-col w-[150px]">
            <label for="">Xếp theo giá</label>
            <label class="flex items-center">
              <input
                type="radio"
                name="priceSortOrder"
                value="asc"
                v-model="priceSortOrder"
                @change="onPriceSortOrderChange"
              />
              <span class="ml-2 text-[13px]">Từ trên xuống</span>
            </label>
            <label class="flex items-center">
              <input
                type="radio"
                name="priceSortOrder"
                value="desc"
                v-model="priceSortOrder"
                @change="onPriceSortOrderChange"
              />
              <span class="ml-2 text-[13px]">Từ dưới lên</span>
            </label>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import constant from '~/constant'

export default {
  data() {
    return {
      keyword: '',
      genres: [],
      isShowFilter: false,
      sortOrder: '',
      priceSortOrder: '',
      selectedGenre: '',
    }
  },
  mounted() {
    axios({
      method: 'get',
      url: `${constant.base_url}/book/genre`,
      headers: {
        'ngrok-skip-browser-warning': 'skip-browser-warning',
      },
    })
      .then((res) => {
        this.genres = res.data
        // Set the selectedGenreId after genres have been populated
        if (this.genres.length > 0) {
          this.selectedGenreId = this.genres[0]._id // Assuming _id is the correct property
        }
        console.log(this.genres)
      })
      .catch((e) => {
        console.log(e)
      })
  },
  methods: {
    toCart() {
      this.$router.push('/cart')
    },
    toMessage() {
      this.$router.push('/chat')
    },
    search() {
      this.$emit('search', this.keyword) // Emit event with updated keyword
    },
    onGenreChange(event) {
      const genre = event.target.value
      console.log(genre)
      this.selectedGenre = genre
      this.$emit('filterChange', genre, this.sortOrder, this.priceSortOrder)
    },
    onSortOrderChange(event) {
      this.sortOrder = event.target.value
      console.log(this.sortOrder)
      this.$emit(
        'filterChange',
        this.selectedGenre,
        this.sortOrder,
        this.priceSortOrder
      )
    },
    onPriceSortOrderChange(event) {
      this.priceSortOrder = event.target.value
      console.log(this.priceSortOrder)
      this.$emit(
        'filterChange',
        this.selectedGenre,
        this.sortOrder,
        this.priceSortOrder
      )
    },
  },
}
</script>

<style scoped>
/* Optional: Add some styles to improve the appearance of the dropdown */
.dropdown {
  display: none;
}

.show-dropdown {
  display: block;
}
</style>