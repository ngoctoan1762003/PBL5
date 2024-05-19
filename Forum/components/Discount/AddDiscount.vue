<template>
  <div
    class="bg-[#1B3764] py-5 rounded-[20px] flex flex-col gap-5 justify-center items-center w-full"
  >
    <div class="text-white font-bold text-[20px]">Thêm mã giảm giá mới</div>

    <div class="book__component">
      <div class="book__component__label">Mã giảm giá</div>
      <input type="text" v-model="title" class="book__component__content" />
    </div>
    <div class="flex items-start w-full">
      <div class="w-[50%] flex flex-col relative">
        <div class="flex">
          <div class="book__component relative">
            <div class="book__component__label w-[100%]">Lượng giảm</div>
            <div class="relative w-full">
              <input
                type="text"
                v-model="publisher"
                class="book__component__content"
              />
              <div class="absolute right-5 flex top-1">VND</div>
            </div>
          </div>
          <div class="flex gap-5 w-full items-end">
            <div class="book__component w-full">
              <div class="book__component__label"></div>
              <select name="" id="">
                <option value="">Theo giá tiền</option>
                <option value="">Theo phần trăm</option>
              </select>
            </div>
          </div>
        </div>
        <div class="book__component">
          <div
            class="book__component__label"
            @input="validateNumberInputQuantity"
            @paste="onPasteQuantity"
          >
            Số lượng
          </div>
          <input
            type="text"
            v-model="quantity"
            class="book__component__content"
          />
        </div>
      </div>

      <div class="flex font-semibold text-[14px] gap-20">
        <div class="flex flex-col gap-4">
          <label class="book__component__label">Thời gian bắt đầu</label>
          <input type="time" class="py-1 px-3 rounded-[10px]">
          <label class="book__component__label">Ngày bắt đầu</label>
          <input type="date" class="py-1 px-3 rounded-[10px]">
        </div>
        <div class="flex flex-col gap-4">
          <label class="book__component__label">Thời gian kết thúc</label>
          <input type="time" class="py-1 px-3 rounded-[10px]">
          <label class="book__component__label">Ngày kết thúc</label>
          <input type="date" class="py-1 px-3 rounded-[10px]">
        </div>
      </div>
    </div>

    <button
      class="bg-[#FFCA42] px-4 py-3 text-[#1B3764] font-semibold"
      @click="submit"
    >
      Xác nhận
    </button>
  </div>
</template>

<script>
import axios from 'axios'
// import VueDatePicker from '@vuepic/vue-datepicker';
// import '@vuepic/vue-datepicker/dist/main.css'

import UploadImage from '~/api/uploadImage.js'
import constant from '~/constant'
// import '@vuepic/vue-datepicker/dist/main.css'
export default {
        // components: { VueDatePicker },
  data() {
    return {
      previewImage: '',
      genres: [],
      title: '',
      publisher: '',
      price: 0,
      quantity: 0,
      description: '',
      selectedGenreId: '',
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
        console.log(this.genres)
      })
      .catch((e) => {
        console.log(e)
      })

    this.selectedGenreId = this.genres[0]
  },
  methods: {
    async handleImageUpload(event) {
      const selectedImage = event.target.files[0]
      console.log('Selected Image:', selectedImage)
      const res = await UploadImage(selectedImage)
      // this.userProfile.profileImage = res
      // const url = await cloudinary.image(`${res}`, {height: 250, width: 250, crop: "fill"})
      this.previewImage = res
    },

    handleGenreChange(event) {
      this.selectedGenreId = event.target.value
      console.log(this.selectedGenreId)
    },

    submit() {
      const authorization = `Bearer ${localStorage.getItem('accessToken')}`
      axios({
        method: 'post',
        url: `${constant.base_url}/book/create`,
        data: {
          title: this.title,
          genre: this.selectedGenreId,
          description: this.description,
          quantity: parseInt(this.quantity),
          price: parseInt(this.price),
          image: this.previewImage,
          author_name: this.author_name,
          publisher_name: this.publisher,
        },
        headers: {
          Authorization: authorization,
        },
      })
        .then((res) => {
          this.$notify({
            title: 'Thành công',
            text: 'Đăng bài thành công',
            type: 'success',
            group: 'foo',
          })
          this.$emit('reload')
        })
        .catch((error) => {
          if (!error.response?.data?.error.startsWith('Blog'))
            this.$notify({
              title: 'Thất bại',
              text: 'Kích cỡ file quá lớn, không thể tải lên',
              type: 'error',
              group: 'foo',
            })
        })
    },

    validateNumberInputPrice() {
      this.price = this.price.replace(/\D/g, '')
    },

    onPastePrice(event) {
      event.preventDefault()
      const pastedText = (event.clipboardData || window.clipboardData).getData(
        'text'
      )
      this.price = pastedText.replace(/\D/g, '')
    },

    validateNumberInputQuantity() {
      this.quantity = this.quantity.replace(/\D/g, '')
    },

    onPasteQuantity(event) {
      event.preventDefault()
      const pastedText = (event.clipboardData || window.clipboardData).getData(
        'text'
      )
      this.quantity = pastedText.replace(/\D/g, '')
    },
  },
}
</script>

<style lang="scss" scoped>
// @import '~assets/scss/variables.scss';
.book__component {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: flex-start;
  gap: 10px;
  width: 100%;
  padding: 10px 30px;

  &__label {
    color: white;
    font-weight: 500;
    font-size: 14px;
  }

  input {
    border-radius: 5px;
    padding: 5px 20px;
  }

  textarea {
    border-radius: 5px;
    padding: 5px 20px;
    display: grid;
    grid-template-rows: repeat(
      3,
      auto
    ); /* Creates 3 rows with automatic height */
    min-height: 100px; /* Sets a minimum height for the entire textarea */
    overflow-y: auto;
  }

  select {
    border-radius: 5px;
    padding: 5px 20px;
  }

  &__content {
    width: 100%;
  }
}
</style>