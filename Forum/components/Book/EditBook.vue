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
        <div>Giỏ hàng</div>
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
                <div class="flex gap-5">
                  <div
                    class="avt flex flex-col gap-[20px] justify-center items-center w-[100px]"
                  >
                    <!-- <div
                      class="text-[#1B3764] font-[500] text-[16px] w-full flex justify-center items-cnter"
                    >
                      Bìa sách
                    </div> -->
                    <div class="avt-preview relative ml-[10px] w-[100px]">
                      <img
                        :src="previewImage"
                        class="rounded-full w-[100px] h-[100px]"
                      />
                      <label
                        for="fileInput"
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
                      id="fileInput"
                      class="hidden"
                      type="file"
                      accept="image/jpeg"
                      @change="handleImageUpload"
                    />
                  </div>
                  <div class="w-full">
                    <div class="book__component">
                      <div class="book__component__label">Tiêu đề</div>
                      <input
                        type="text"
                        v-model="title"
                        class="book__component__content"
                      />
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
                <textarea
                  class="book__component__content"
                  v-model="description"
                />
              </div>
              <div class="book__component">
                <div class="book__component__label">Thể loại</div>
                <select
                  class="book__component__content"
                  @change="handleGenreChange"
                  v-model="selectedGenre"
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
                    v-model="price"
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
      title: '',
      publisher: '',
      description: '',
      genres: [], // Assuming you have a list of genres
      selectedGenre: '',
      authorName: '',
      quantity: 0,
      price: 0,
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
    updateData() {
      this.updatePreviewImage()
      this.updateTitle()
      this.updatePublisher()
      this.updateDescription()
      this.updateQuantity()
      this.updatePrice()
      this.updateAuthorName()
      this.updateGenre()
    },
    updatePreviewImage() {
      this.previewImage = this.book.image || ''
    },
    updateTitle() {
      this.title = this.book.Title || ''
    },
    updateAuthorName() {
      this.authorName = this.book.AuthorName || ''
    },
    updatePublisher() {
      this.publisher = this.book.PublisherName || ''
    },
    updateGenre() {
      const genre = this.genres.find((g) => g.Theloai === this.book.Genre)
      if (genre) {
        this.selectedGenre = genre._id
      }
    },
    updateDescription() {
      this.description = this.book.Description || ''
    },
    updateQuantity() {
      this.quantity = this.book.Quantity || 0
    },
    updatePrice() {
      this.price = this.book.Price || 0
    },
    save() {
      const authorization = `Bearer ${localStorage.getItem('accessToken')}`
      axios({
        method: 'put',
        url: `${constant.base_url}/book/${this.book._id}`,
        headers: {
          Authorization: authorization,
        },
        data: {
          title: this.title,
          description: this.description,
          genre: this.selectedGenre,
          quantity: this.quantity,
          price: this.price,
          author_name: this.authorName,
          publisher_name: this.publisher,
          image: this.previewImage,
        },
      })
        .then((res) => {
          this.$notify({
            title: 'Thành công',
            text: 'Chỉnh sửa thành công',
            type: 'success',
            group: 'foo',
          })
          this.$emit('reload')
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
  