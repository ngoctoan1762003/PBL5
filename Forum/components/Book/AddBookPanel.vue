<template>
  <div
    class="bg-[#1B3764] py-5 rounded-[20px] flex flex-col gap-5 justify-center items-center w-full"
  >
    <div class="text-white font-bold text-[20px]">Thêm sách mới</div>
    <!-- <div class="book__component">
            <div class="book__component__label">Hình ảnh</div>
            <input type="text" class="book__component__content">
        </div> -->
    <div class="flex justify-center gap-5 w-full pl-10">
      <div
        class="avt flex flex-col gap-[20px] justify-center items-center w-[100px]"
      >
        <!-- <div
                      class="text-[#1B3764] font-[500] text-[16px] w-full flex justify-center items-cnter"
                    >
                      Bìa sách
                    </div> -->
        <div class="avt-preview relative ml-[10px] w-[100px]">
          <img :src="previewImage" class="rounded-full w-[100px] h-[100px]" />
          <label
            for="file"
            class="absolute top-0 left-0 w-[100px] h-[100px] rounded-full bg-[#5f6c8580] flex justify-center items-center cursor-pointer"
          >
            <img
              src="~/assets/icon/upload.svg"
              class="w-[30px] h-[30px]"
              alt="Upload"
            />
          </label>
        </div>
        <input
          id="file"
          class="hidden"
          type="file"
          accept="image/jpeg"
          @change="handleImageUpload"
        />
      </div>
      <div class="w-full">
        <div class="book__component">
          <div class="book__component__label">Tiêu đề</div>
          <input type="text" v-model="title" class="book__component__content" />
        </div>
        <div class="book__component">
          <div class="book__component__label">Nhà xuất bản</div>
          <input
            type="text"
            v-model="publisher"
            class="book__component__content"
          />
        </div>
      </div>
    </div>
    <div class="book__component">
      <div class="book__component__label">Tác giả</div>
      <input
        type="text"
        v-model="authorName"
        class="book__component__content"
      />
    </div>
    <div class="book__component">
      <div class="book__component__label">Miêu tả</div>
      <textarea class="book__component__content" v-model="description" />
    </div>
    <div class="book__component">
      <div class="book__component__label">Thể loại</div>
      <select class="book__component__content" @change="handleGenreChange">
        <option
          v-for="genreOption in genres"
          :key="genreOption._id"
          :value="genreOption._id"
        >
          {{ genreOption.Theloai }}
        </option>
      </select>
    </div>
    <div class="w-full flex justify-center items-center gap-10">
      <div class="book__component">
        <div class="book__component__label">Giá</div>
        <input
          type="text"
          v-model="price"
          @input="validateNumberInputPrice"
          @paste="onPastePrice"
          class="book__component__content"
        />
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
import UploadImage from '~/api/uploadImage.js'
import constant from '~/constant'

export default {
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
      authorName: '',
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
      if (this.previewImage === '') {
        this.$notify({
          title: 'Thất bại',
          text: 'Vui lòng thêm ảnh',
          type: 'error',
          group: 'foo',
        })
        return
      }
      if (this.title === '') {
        this.$notify({
          title: 'Thất bại',
          text: 'Vui lòng thêm tiêu đề',
          type: 'error',
          group: 'foo',
        })
        return
      }
      if (this.quantity === 0) {
        this.$notify({
          title: 'Thất bại',
          text: 'Vui lòng thêm số lượng',
          type: 'error',
          group: 'foo',
        })
        return
      }
      if (this.price === 0) {
        this.$notify({
          title: 'Thất bại',
          text: 'Vui lòng thêm giá',
          type: 'error',
          group: 'foo',
        })
        return
      }
      if (this.authorName === 0) {
        this.$notify({
          title: 'Thất bại',
          text: 'Vui lòng thêm tên tác giả',
          type: 'error',
          group: 'foo',
        })
        return
      }
      if (this.publisher === 0) {
        this.$notify({
          title: 'Thất bại',
          text: 'Vui lòng thêm nhà xuất bản',
          type: 'error',
          group: 'foo',
        })
        return
      }
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
          author_name: this.authorName,
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
              text: error.response,
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