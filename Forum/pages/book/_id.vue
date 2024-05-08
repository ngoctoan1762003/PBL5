<template>
  <div class="main relative">
    <TopNaviBarGuest v-if="isLogedIn === false" />
    <TopNaviBar v-else />
    <div class="section__1">
      <div class="section__1__left">
        <div>Welcome to Pages</div>
        <div class="text-[45px]">{{ book.Title }}</div>
        <div class="text-[#B4C7E7]">
          {{ book.Description }}
        </div>
        <div class="flex gap-10 items-center">
          <button class="bg-[#ffca42]" @click="toBookOrder()">
            <div class="text-[16px] font-[500] text-[#1B3764] px-5 py-3">
              Đặt ngay
            </div>
          </button>
          <button class="underline underline-offset-2">
            Đọc bản thử miễn phí
          </button>
        </div>
        <div class="flex gap-8">
          <div class="flex gap-3">
            <div class="bg-[#FFCA42] rounded-full w-4 h-4 mt-1"></div>
            <div>
              <div class="text-[16px]">Trang :</div>
              <div class="text-[#B4C7E7]">586 trang</div>
            </div>
          </div>
          <div class="flex gap-3">
            <div class="bg-[#FFCA42] rounded-full w-4 h-4 mt-1"></div>
            <div>
              <div class="text-[16px]">Đánh giá :</div>
              <div class="text-[#B4C7E7]">4.5/5 (300 đánh giá)</div>
            </div>
          </div>
        </div>
      </div>
      <img class="section__1__image" :src="book.image" />
    </div>
    <div class="section__2">
      <div class="section__2__author__img">
        <img class="w-[100%]" src="~/assets/img/Author-Background.png" alt="" />
        <div
          class="w-[100%] aspect-square absolute bg-white z-10 drop-shadow-md top-[0px] left-[-20px]"
        ></div>
      </div>
      <div class="section__2__main w-full">
        <div class="text-[#1B3764] text-[35px] font-bold">About author</div>
        <div class="h-1 w-20 bg-[#FFCA42]"></div>
        <div class="text-[#969AA0] text-[15px]">
          All the Lorem Ipsum generators on the Internet tend to repeated
          predefined chunks as necessary, making this the first true value
          generator on the Internet. It uses a dictionary of over 200 Latin
          words, combined with a handful.
        </div>
        <div class="flex gap-5 items-center">
          <div>
            <div class="text-[#1B3764] text-[45px] font-semibold">02</div>
            <div class="text-[#969AA0] text-[15px]">Books Published</div>
          </div>
          <div class="w-[1px] h-[60px] bg-[#FFCA42]"></div>
          <div>
            <div class="text-[#1B3764] text-[45px] font-semibold">4.5</div>
            <div class="text-[#969AA0] text-[15px]">User Review</div>
          </div>
          <div class="w-[1px] h-[60px] bg-[#FFCA42]"></div>
          <div>
            <div class="text-[#1B3764] text-[45px] font-semibold">04</div>
            <div class="text-[#969AA0] text-[15px]">Best Seller Awards</div>
          </div>
        </div>
      </div>
    </div>
    <div class="section__3">
      <div class="section__3__main">
        <div class="text-[35px] font-semibold">Get Book Copy Today</div>
        <div class="w-[60px] h-[1px] bg-[#FFCA42]"></div>
        <div class="text-[#B4C7E7] text-[15px]">
          This the first true value generator on the Internet. It uses alphas
          dictionary of over 200 Latin words.
        </div>
        <button
          class="border-[1px] border-[#FFCA42] py-3 px-5 w-auto self-start text-[15px]"
        >
          Đặt ngay
        </button>
      </div>
      <img class="w-[40%]" src="~/assets/img/Photo.png" />
    </div>
    <div class="section__4">
      <div class="flex justify-center items-center flex-col gap-5">
        <div class="text-[#1B3764] text-[30px] font-semibold">
          Những sách khác cùng tác giả
        </div>
        <div class="w-[160px] h-[4px] bg-[#FFCA42]"></div>
      </div>
      <div class="flex flex-wrap gap-10 justify-center items-start">
        <div v-for="book in sameAuthorBook" :key="book._id" class="w-[30%]">
          <BookCard :book="book" />
        </div>
      </div>
    </div>
    <div class="section__5">
      <div class="text-[#1B3764] text-[30px] font-semibold">Bình luận</div>
      <div class="w-[100px] h-[2px] bg-[#FFCA42]"></div>
      <div
        v-for="c in comments"
        :key="c._id"
        class="flex flex-col gap-3 p-[30px]"
      >
        <CommentCard
          :comment="c"
          :user_id="c.user_id"
          @showCommentBox="showCommentBox"
        />
      </div>
      <CommentBox :bookId="book._id" @send="getListComment()" />
    </div>
    <!-- <modal-alert
      v-if="alert.isShowModal"
      :width="480"
      v-bind="alert"
      @close="onCloseModal"
    /> -->
    <FooterBar />
  </div>
</template>

<script>
import axios from 'axios'
import constant from '~/constant'
import TopNaviBarGuest from '~/components/TopNaviBarGuest.vue'
import BookCard from '~/components/Book/BookCard.vue'
import CommentCard from '~/components/Book/CommentCard.vue'
import CommentBox from '~/components/Blog/CommentBox.vue'
import FooterBar from '~/components/FooterBar.vue'
import TopNaviBar from '~/components/TopNaviBar.vue'

export default {
  name: 'IndexPage',
  layout: 'empty',
  components: {
    // BlogCard,
    // PostCreator,
    // ModalAlert,
    // LoadingSpinner,
    TopNaviBar,
    TopNaviBarGuest,
    BookCard,
    CommentCard,
    CommentBox,
    FooterBar,
  },
  data() {
    return {
      book: Object,
      news: [],
      comments: [],
      sameAuthorBook: [],
      isLoading: true,
      searchValue: '',
      isCreatingPost: false,
      totalBlogs: 0,
      recordsPerPage: 4,
      alert: {
        isShowModal: false,
        title: '',
        type: 'failed',
        content: '',
        buttonCancelContent: '',
        buttonOkContent: '',
        typeSubmit: '',
      },
      isLogedIn: false,
    }
  },
  async created() {
    if (localStorage.getItem('accessToken')) {
      this.isLogedIn = true
    } else {
      this.isLogedIn = false
    }
    const id = this.$route.params.id
    await axios({
      method: 'get',
      url: `${constant.base_url}/book/${id}`,
      headers: {
        'ngrok-skip-browser-warning': 'skip-browser-warning',
      },
    })
      .then((res) => {
        console.log(res)
        this.book = res.data
      })
      .catch((err) => {
        if (err.response.data.status === 401)
          this.alert = {
            ...this.alert,
            ...{
              isShowModal: true,
              title: 'Lỗi',
              buttonOkContent: 'Đăng nhập lại',
              content: 'Hết phiên đăng nhập, vui lòng đăng nhập lại',
              type: 'failed',
              typeSubmit: 'loginagain',
            },
          }
        else
          this.alert = {
            ...this.alert,
            ...{
              isShowModal: true,
              title: 'Lỗi',
              buttonOkContent: 'Đóng',
              content: err.response.data.error,
              type: 'failed',
            },
          }
      })
    await axios({
      method: 'get',
      url: `${constant.base_url}/comment/book/${id}`,
      headers: {
        'ngrok-skip-browser-warning': 'skip-browser-warning',
      },
    })
      .then((res) => {
        console.log(res.data)
        this.comments = res.data.map((comment) => ({
          ...comment,
          isVisible: false, // Set isVisible to true for each comment
        }))
      })
      .catch((err) => {
        console.log(err)
      })
    await axios({
      method: 'get',
      url: `${constant.base_url}/book/author_name/${this.book.AuthorName}`,
      headers: {
        'ngrok-skip-browser-warning': 'skip-browser-warning',
      },
    })
      .then((res) => {
        console.log(res.data)
        this.sameAuthorBook = res.data
        this.sameAuthorBook = this.sameAuthorBook.filter(
          (book) => book._id !== this.book._id
        )
      })
      .catch((err) => {
        console.log(err)
      })
    this.isLoading = false
  },
  methods: {
    ScrollToTop() {
      this.$scrollToTop()
    },
    cancel() {
      this.alert = {
        ...this.alert,
        ...{
          isShowModal: true,
          title: 'Xác nhận',
          buttonCancelContent: 'Hủy',
          buttonOkContent: 'Xác nhận',
          content: 'Bạn có chưa lưu bài đăng. Bạn có muốn thoát ?',
          type: 'confirm',
          typeSubmit: 'cancelCreatePost',
        },
      }
    },
    toBookOrder() {
      const id = this.$route.params.id
      this.$router.push(`/order/${id}`)
    },
    GoToDetails(id) {
      this.$router.push(`/blog/${id}`)
    },
    async getListComment() {
      const id = this.$route.params.id

      await axios({
        method: 'get',
        url: `${constant.base_url}/comment/book/${id}`,
        headers: {
          'ngrok-skip-browser-warning': 'skip-browser-warning',
        },
      })
        .then((res) => {
          console.log(res.data)
          this.comments = res.data
          // this.comment.forEach((e) => {
          //   this.listReplyBox.isShow = false
          // })
          // console.log(this.listReplyBox)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    async getListBlog() {
      await this.$axios
        .get(`/blogs?page=1&limit=${this.recordsPerPage}`)
        .then((res) => {
          console.log(res)
          this.news = res.data.docs
          this.totalBlogs = res.data.totalDocs
        })
        .catch((err) => {
          if (err.response.data.status === 401)
            this.alert = {
              ...this.alert,
              ...{
                isShowModal: true,
                title: 'Lỗi',
                buttonOkContent: 'Đăng nhập lại',
                content: 'Hết phiên đăng nhập, vui lòng đăng nhập lại',
                type: 'failed',
                typeSubmit: 'loginagain',
              },
            }
          else
            this.alert = {
              ...this.alert,
              ...{
                isShowModal: true,
                title: 'Lỗi',
                buttonOkContent: 'Đóng',
                content: err.response.data.error,
                type: 'failed',
              },
            }
        })
    },
    changePage(page, limit) {
      this.isLoading = true
      this.$axios
        .get(`/blogs?page=${page}&limit=${limit}`)
        .then((res) => {
          this.news = res.data.docs
          this.isLoading = false
          console.log(this.news)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    modifyListBlog() {
      this.news.forEach((e) => {
        let listImage
        const imageRegex =
          /<img.*?src=['"](https?:\/\/.*?\.(?:png|jpg|jpeg|gif))['"].*?>/g
        let match

        while ((match = imageRegex.exec(e.content)) !== null) {
          listImage.push(match[1])
        }
        e.listImages = listImage
        e.blogImage = e.listImages[0]
      })
      console.log('News:', this.news)
    },
    save() {
      this.isCreatingPost = false
    },
    onCloseModal(typeSubmit) {
      switch (typeSubmit) {
        case 'loginagain':
          localStorage.setItem('accessToken', 'false')
          localStorage.setItem('user', 'false')
          this.$router.push('/auth/login')
          this.resetAlert()
          break
        case 'cancelCreatePost':
          this.isCreatingPost = false
          this.resetAlert()
          break
        default:
          this.resetAlert()
          break
      }
    },
    resetAlert() {
      this.alert = {
        isShowModal: false,
        title: '',
        type: 'failed',
        content: '',
        buttonCancelContent: '',
        buttonOkContent: '',
        typeSubmit: '',
      }
    },
    async searchBlog() {
      this.isLoading = true
      await this.$axios
        .get(`/blogs?page=1&limit=${this.recordsPerPage}`, {
          params: {
            title: this.searchValue.trim(),
          },
        })
        .then((res) => {
          console.log(res)
          this.news = res.data.docs
          this.totalBlogs = res.data.totalDocs
          this.isLoading = false
        })
        .catch((err) => {
          if (err.response.data.status === 401)
            this.alert = {
              ...this.alert,
              ...{
                isShowModal: true,
                title: 'Lỗi',
                buttonOkContent: 'Đăng nhập lại',
                content: 'Hết phiên đăng nhập, vui lòng đăng nhập lại',
                type: 'failed',
                typeSubmit: 'loginagain',
              },
            }
          else
            this.alert = {
              ...this.alert,
              ...{
                isShowModal: true,
                title: 'Lỗi',
                buttonOkContent: 'Đóng',
                content: err.response.data.error,
                type: 'failed',
              },
            }
        })
    },
    showCommentBox(evt, id) {
      console.log(id);
      this.comments.forEach((comment) => {
        if (comment._id !== id) {
          // Logic to hide the comment box
          // You might need to add a property to your comment objects to track visibility
          comment.isVisible = false // for example
        }
        else{
          comment.isVisible = true
        }
      })
    },
  },
}
</script>
<style lang="scss" scoped>
@import '~/assets/scss/variables.scss';
.section {
  &__1 {
    background-color: #1b3764;
    color: white;
    font-size: 14px;
    font-weight: 500;
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 40px 0 40px 0;
    gap: 50px;

    &__left {
      width: 40%;
      display: flex;
      flex-direction: column;
      gap: 20px;
    }

    &__image {
      width: 40%;
    }
  }

  &__2 {
    display: flex;
    gap: 50px;
    padding: 100px;
    justify-content: center;
    align-items: center;
    gap: 80px;
    background-color: #f4f8ff;

    &__author__img {
      position: relative;
      width: 30%;
    }

    &__main {
      width: 40%;
      display: flex;
      flex-direction: column;
      gap: 20px;
    }
  }

  &__3 {
    background-color: #1b3764;
    padding: 100px;
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 80px;

    &__main {
      display: flex;
      flex-direction: column;
      gap: 20px;
      width: 40%;
      color: white;
    }
  }

  &__4 {
    background-color: white;
    padding: 80px 10px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    gap: 80px;
  }

  &__5 {
    background-color: #f4f8ff;
    padding: 80px;
  }
}
</style>
