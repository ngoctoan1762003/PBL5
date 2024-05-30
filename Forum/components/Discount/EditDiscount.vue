<!-- eslint-disable vue/no-mutating-props -->
<template>
  <div
    class="main bg-[#1B3764] rounded-[20px] flex flex-col gap-5 justify-center items-center w-full"
    @click="cancel"
  >
    <div class="container relative rounded border bg-white" @click.stop>
      <div
        class="relative text-[#1B3764] font-semibold text-[21px] bg-[#FFCA42] py-3 px-5"
      >
        <div>Sửa thông tin khuyến mãi</div>
        <img
          class="absolute right-5 top-[30%] w-[20px] h-[20px] cursor-pointer"
          @click="cancel()"
          src="~/assets/icon/x.svg"
          alt=""
        />
      </div>
      <form>
        <div class="flex justify-center w-full">
          <div class="w-full">
            <div class="form">
              <div class="w-full flex flex-col items-center">
                <!-- <label class="label" for="name">Status</label> -->
                <div class="w-full">
                  <div class="book__component">
                    <div class="book__component__label">Mã giảm giá</div>
                    <input
                      type="text"
                      v-model="discountCode"
                      class="book__component__content"
                    />
                  </div>
                  <div class="book__component">
                    <div class="book__component__label">Nhà xuất bản</div>
                    <input
                      type="text"
                      v-model="discountAmount"
                      class="book__component__content"
                    />
                  </div>
                </div>
              </div>
              <div class="book__component">
                <div class="book__component__label">Lượng giảm</div>
                <div class="relative w-full flex">
                  <div class="relative">
                    <input
                      type="text"
                      v-model="discountPercent"
                      class="book__component__content"
                      v-show="selectedType === 'Theo giá tiền'"
                    />
                    <input
                      type="text"
                      v-model="discountAmount"
                      class="book__component__content"
                      v-show="selectedType === 'Theo phần trăm'"
                    />
                    <div
                      class="absolute right-5 flex top-1"
                      v-show="selectedType === 'Theo giá tiền'"
                    >
                      VND
                    </div>
                    <div
                      class="absolute right-5 flex top-1"
                      v-show="selectedType === 'Theo phần trăm'"
                    >
                      %
                    </div>
                  </div>
                  <select name="" id="" @change="handleTypeChange">
                    <option value="type.content" v-for="type in types" :key="type">
                      {{ type.content }}
                    </option>
                  </select>
                </div>
              </div>
              <div class="book__component">
                <div class="book__component__label">Tác giả</div>
                <input
                  type="text"
                  v-model="discountPercent"
                  class="book__component__content"
                />
              </div>
              <div class="book__component">
                <div class="book__component__label">Miêu tả</div>
                <textarea class="book__component__content" v-model="EndDay" />
              </div>
              <div class="book__component">
                <div class="book__component__label">Thể loại</div>
                <select
                  class="book__component__content"
                  @change="handleTypeChange"
                >
                  <option
                    v-for="genreOption in genres"
                    :key="genreOption._id"
                    :value="genreOption._id"
                  >
                    {{ genreOption.Theloai }}
                  </option>
                </select>
              </div>
              <div class="flex gap-5">
                <div class="book__component">
                  <div class="book__component__label">Số lượng</div>
                  <input
                    type="text"
                    v-model="quantity"
                    class="book__component__content"
                  />
                </div>
                <div class="book__component">
                  <div class="book__component__label">Giá cả</div>
                  <input
                    type="text"
                    v-model="StartDay"
                    class="book__component__content"
                  />
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="button-group space-x-4 mt-8 mb-8">
          <button
            type="button"
            class="save py-2 px-4 bg-blue-500 text-white rounded hover:bg-blue-600 active:bg-blue-700 disabled:opacity-50"
            @click="save"
          >
            Lưu
          </button>
          <button
            class="cancel py-2 px-4 bg-white border border-gray-200 text-gray-600 rounded hover:bg-gray-100 active:bg-gray-200 disabled:opacity-50"
            @click="cancel"
          >
            Thoát
          </button>
        </div>
      </form>
    </div>
  </div>
</template>
<script>
import axios from 'axios'
import constant from '~/constant'
import UploadImage from '~/api/uploadImage.js'

export default {
  props: {
    book: {
      type: Object,
      default: () => ({}),
    },
  },
  data() {
    return {
      userProfile: {},
      selectedRole: '',
      selectedStatus: '',
      previewImage: '',
      discountCode: '',
      discountAmount: '',
      description: '',
      genres: [], // Assuming you have a list of genres
      selectedGenre: '',
      discountPercent: '',
      EndDay: '',
      StartDay: '',
      quantity: 0,
      price: 0,
      selectedType: 'Theo giá tiền',
      types: [{ content: 'Theo giá tiền' }, { content: 'Theo phần trăm' }],
    }
  },
  mounted() {
    this.fetchGenres()
  },
  watch: {
    book: {
      handler() {
        this.updateData()
      },
      immediate: true,
      deep: true,
    },
    genres: {
      handler() {
        this.updateGenre()
      },
      immediate: true,
      deep: true,
    },
  },
  methods: {
    handleTypeChange(event) {
      this.selectedType = event.target.value
      console.log(this.selectedType)
    },
    fetchGenres() {
      axios({
        method: 'get',
        url: `${constant.base_url}/book/genre`,
        headers: {
          'ngrok-skip-browser-warning': 'skip-browser-warning',
        },
      })
        .then((res) => {
          this.genres = res.data
        })
        .catch((e) => {
          console.log(e)
        })
    },
    handleChange(e) {},
    updateData() {
      this.updatePreviewImage()
      this.updateTitle()
      this.updatePublisher()
      this.updateDescription()
      this.updateQuantity()
      this.updatePrice()
      this.updateAuthorName()
      this.updateGenre()
      console.log(
        JSON.stringify({
          DiscountAmount: this.book.DiscountAmount,
          DiscountCode: this.book.DiscountCode,
          DiscountPercent: this.book.DiscountPercent,
          EndDay: this.book.EndDay,
          Quantity: this.book.Quantity,
          StartDay: this.book.StartDay,
          _id: this.book._id,
        })
      )
    },
    updatePreviewImage() {
      this.previewImage = this.book.image || ''
    },
    updateTitle() {
      this.discountCode = this.book.DiscountCode || ''
    },
    updateAuthorName() {
      this.discountPercent = this.book.DiscountPercent || 0
    },
    updatePublisher() {
      this.discountAmount = this.book.DiscountAmount || ''
    },
    updateGenre() {
      const genre = this.genres.find((g) => g.Theloai === this.book.Genre)
      if (genre) {
        this.selectedGenre = genre._id
      }
    },
    updateDescription() {
      this.StartDay = this.book.StartDay || ''
    },
    updateQuantity() {
      this.quantity = this.book.Quantity || 0
    },
    updatePrice() {
      this.EndDay = this.book.EndDay || 0
    },
    save() {
      const authorization = localStorage.getItem('accessToken')
      axios({
        method: 'put',
        url: `${constant.base_url}/book/${this.book._id}`,
        headers: {
          Authorization: authorization,
        },
        data: {
          title: this.discountCode,
          description: this.description,
          genre: this.selectedGenre,
          quantity: this.quantity,
          price: this.price,
          author_name: this.discountPercent,
          publisher_name: this.discountAmount,
          image: this.previewImage,
        },
      })
        .then((res) => {
          this.$notify({
            title: 'Thành công',
            text: 'Đăng bài thành công',
            type: 'success',
            group: 'foo',
          })
        })
        .catch((err) => {
          this.$notify({
            title: 'Thành công',
            text: err.response,
            type: 'error',
            group: 'foo',
          })
        })
      this.$emit('save')
    },
    cancel() {
      this.$emit('cancel')
    },
    async handleImageUpload(event) {
      const selectedImage = event.target.files[0]
      const res = await UploadImage(selectedImage)
      // this.userProfile.profileImage = res
      // const url = await cloudinary.image(`${res}`, {height: 250, width: 250, crop: "fill"})
      this.previewImage = res
      //   if (file) {
      //     const reader = new FileReader()
      //     reader.onload = (e) => {
      //       this.previewImage = e.target.result
      //     }
      //     reader.readAsDataURL(file)
      //   }
    },
    handleGenreChange(event) {
      this.selectedGenre = event.target.value
      console.log(this.selectedGenre)
    },
  },
}
</script>

</script>

<style lang="scss" scoped>
@import '~/assets/scss/variables.scss';

.main {
  position: fixed;
  inset: 0;
  background: rgba(71, 79, 98, 0.8);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 100;

  .container {
    max-width: 600px;

    h1 {
      margin-bottom: 40px;
      text-align: center;
    }

    .form {
      label {
        color: $orange;
      }

      .label {
        display: flex;
        margin-bottom: 8px;
        font-size: 14px;
      }

      input {
        outline: none;
      }
    }

    .button-group {
      display: flex;
      width: 100%;
      justify-content: center;
      align-items: center;

      .save {
        background: $orange;
      }

      .cancel {
        background: $gray;
      }
    }
  }
}
.book__component {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: flex-start;
  gap: 10px;
  width: 100%;
  padding: 10px 30px;

  &__label {
    color: #1b3764;
    font-weight: 500;
    font-size: 14px;
  }

  input {
    border-radius: 5px;
    padding: 5px 20px;
    border: 1px solid #1b3764;
  }

  textarea {
    border: 1px solid #1b3764;
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
    border: 1px solid #1b3764;
    border-radius: 5px;
    padding: 5px 20px;
  }

  &__content {
    width: 100%;
  }
}
</style>
  