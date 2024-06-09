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
                  <!-- <div class="book__component">
                    <div class="book__component__label">Nhà xuất bản</div>
                    <input
                      type="text"
                      v-model="discountAmount"
                      class="book__component__content"
                    />
                  </div> -->
                </div>
              </div>
              <div class="book__component">
                <div class="book__component__label">Lượng giảm</div>
                <div class="relative w-full flex justify-between">
                  <div class="relative">
                    <input
                      type="text"
                      v-model="discountPercent"
                      class="book__component__content"
                      v-show="selectedType === 1"
                    />
                    <input
                      type="text"
                      v-model="discountAmount"
                      class="book__component__content"
                      v-show="selectedType === 2"
                    />
                    <div
                      class="absolute right-5 flex top-1"
                      v-show="selectedType === 1"
                    >
                      VND
                    </div>
                    <div
                      class="absolute right-5 flex top-1"
                      v-show="selectedType === 2"
                    >
                      %
                    </div>
                  </div>
                  <select name="" id="" @change="handleTypeChange">
                    <option
                      :value="type._id"
                      v-for="type in types"
                      :key="type._id"
                    >
                      {{ type.content }}
                    </option>
                  </select>
                </div>
              </div>
              <!-- <div class="book__component">
                <div class="book__component__label">Tác giả</div>
                <input
                  type="text"
                  v-model="discountPercent"
                  class="book__component__content"
                />
              </div> -->
              <!-- <div class="book__component">
                <div class="book__component__label">Miêu tả</div>
                <textarea class="book__component__content" v-model="EndDay" />
              </div> -->
              <!-- <div class="book__component">
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
              </div> -->
              <div class="flex gap-5">
                <div class="book__component">
                  <div class="book__component__label">Số lượng</div>
                  <input
                    type="text"
                    v-model="quantity"
                    class="book__component__content"
                  />
                </div>
              </div>
              <!-- <div class="book__component">
                <div class="book__component__label">Giá cả</div>
                <input
                  type="text"
                  v-model="StartDay"
                  class="book__component__content"
                />
              </div> -->
              <div class="flex justify-between">
                <div class="book__component">
                  <div class="book__component__label">Ngày bắt đầu</div>
                  <input
                    type="date"
                    v-model="startDate"
                    class="book__component__content"
                  />
                  <input
                    type="time"
                    v-model="startTime"
                    class="book__component__content"
                  />
                </div>
                <div class="book__component">
                  <div class="book__component__label">Ngày kết thúc</div>
                  <input
                    type="date"
                    v-model="endDate"
                    class="book__component__content"
                  />
                  <input
                    type="time"
                    v-model="endTime"
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
      selectedType: 1,
      types: [
        { content: 'Theo giá tiền', _id: 1 },
        { content: 'Theo phần trăm', _id: 2 },
      ],
      startDate: '',
      startTime: '',
      endDate: '',
      endTime: '',
    }
  },
  mounted() {
    this.fetchGenres()
    this.parseDateTimes()
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
    parseDateTimes() {
      if (this.book.StartDay) {
        const startParts = this.book.StartDay.split(' ')
        console.log(startParts)
        const startDate = startParts[2]
        const startTime = startParts[3]
        console.log(startDate + ' ' + startTime)
        const [day, month, year] = startDate.split('/')
        const startDateTime = new Date(`${year}-${month}-${day}T${startTime}`)
        if (!isNaN(startDateTime.getTime())) {
          this.startDate = startDateTime.toISOString().slice(0, 10)
          this.startTime = startTime.slice(0, 5)
        } else {
          console.error('Invalid StartDay:', this.book.StartDay)
        }
      }
      if (this.book.EndDay) {
        const endParts = this.book.EndDay.split(' ')
        const endDate = endParts[2]
        const endTime = endParts[3]
        console.log(endDate + ' ' + endTime)
        const [day, month, year] = endDate.split('/')
        const endDateTime = new Date(`${year}-${month}-${day}T${endTime}`)
        if (!isNaN(endDateTime.getTime())) {
          this.endDate = endDateTime.toISOString().slice(0, 10)
          this.endTime = endTime.slice(0, 5)
        } else {
          console.error('Invalid EndDay:', this.book.EndDay)
        }
      }
    },
    handleTypeChange(event) {
      this.selectedType = JSON.parse(event.target.value)
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
    updateData() {
      this.updatePreviewImage()
      this.updateTitle()
      this.updatePublisher()
      this.updateDescription()
      this.updateQuantity()
      this.updatePrice()
      this.updateAuthorName()
      this.updateGenre()
      this.parseDateTimes()
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
      const authorization = `Bearer ${localStorage.getItem('accessToken')}`
      const startDateTime = this.formatDateTime(this.startDate, this.startTime)
      const endDateTime = this.formatDateTime(this.endDate, this.endTime)
      axios({
        method: 'put',
        url: `${constant.base_url}/discount/${this.book._id}`,
        data: {
          discount_code: this.discountCode,
          amount: parseInt(this.discountAmount),
          percent: parseInt(this.discountPercent),
          quantity: parseInt(this.quantity),
          start_day: startDateTime,
          end_day: endDateTime,
        },
        headers: {
          Authorization: authorization,
        },
      })
        .then((res) => {
          this.$notify({
            title: 'Thành công',
            text: 'Sửa giảm giá thành công',
            type: 'success',
            group: 'foo',
          })
          this.$emit('reload')
        })
        .catch((error) => {
          this.$notify({
            title: 'Thất bại',
            text: error,
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
      this.previewImage = res
    },
    handleGenreChange(event) {
      this.selectedGenre = event.target.value
    },
    formatDateTime(date, time) {
      const [year, month, day] = date.split('-')
      const [hours, minutes] = time.split(':')
      const dateTime = `${year}-${month}-${day}T${hours}:${minutes}:00.000+00:00`
      // const dateTime = new Date(Date.UTC(year, month - 1, day, hours, minutes))
      return dateTime
    },
  },
}
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
  