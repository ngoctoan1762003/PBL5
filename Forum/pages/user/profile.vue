<template>
  <div>
    <div
      class="fixed w-[100vw] h-[100vh] top-0 z-20 flex justify-center items-center"
      v-show="isUpRole"
    >
      <div class="absolute bg-gray-500 opacity-50 w-full h-full"></div>
      <ModalUprole
        @submit="toRoleSeller"
        @cancel="isUpRole = false"
        class="relative z-[1]"
      />
    </div>
    <TopNavBar />
    <main class="profile-page overflow-hidden">
      <section class="relative block" style="height: 500px">
        <div
          class="absolute top-0 w-full h-full bg-center bg-cover"
          style="
            background-image: url('https://images.unsplash.com/photo-1499336315816-097655dcfbda?ixlib=rb-1.2.1&amp;ixid=eyJhcHBfaWQiOjEyMDd9&amp;auto=format&amp;fit=crop&amp;w=2710&amp;q=80');
          "
        >
          <span
            id="blackOverlay"
            class="w-full h-full absolute opacity-50 bg-black"
            >dhfdhdfjfdj</span
          >
        </div>
        <div
          class="top-auto bottom-0 left-0 right-0 w-full absolute pointer-events-none overflow-hidden"
          style="height: 70px"
        ></div>
      </section>
      <section class="relative py-16 bg-[#2C353D]">
        <div class="container mx-auto">
          <div
            class="relative flex flex-col min-w-0 break-words bg-[#2C353D] w-full mb-6 shadow-xl rounded-lg -mt-64"
          >
            <div class="px-6">
              <div class="flex flex-wrap justify-between w-full">
                <div class="w-[200px] px-4 flex justify-center">
                  <div class="relative">
                    <img
                      alt="..."
                      :src="user.image ?? require('~/assets/img/avt.png')"
                      class="shadow-xl rounded-full h-[150px] border-none absolute -m-16 -ml-20 lg:-ml-16"
                      style="max-width: 150px"
                    />
                  </div>
                </div>
                <div
                  class="info_user w-full md:ml-0 lg:ml-[255px] lg:order-3 lg:text-right lg:self-center"
                >
                  <div
                    class="pt-4 px-3 sm:mt-0 flex justify-between gap-[40px]"
                  >
                    <div class="text-left">
                      <span
                        class="text-4xl font-semibold leading-normal mb-2 text-[#fafcfe] mb-2"
                      >
                        {{ user.Name }}
                      </span>
                      <div
                        class="text-sm leading-normal mt-0 mb-2 text-[#fafcfe] font-semibold uppercase"
                      >
                        Địa chỉ: {{ user.Address }}
                      </div>
                      <div
                        class="text-sm leading-normal mt-0 mb-2 text-[#fafcfe] font-semibold uppercase"
                      >
                        Email:
                        {{ user.Email }}
                      </div>
                      <div
                        class="text-sm leading-normal mt-0 mb-2 text-[#fafcfe] font-semibold uppercase"
                      >
                        Số điện thoại: {{ user.Phone }}
                      </div>
                    </div>
                    <div class="button flex items-center">
                      <button
                        class="bg-[#FF571A] active:bg-pink-600 uppercase text-white font-bold hover:shadow-md shadow text-xs px-4 py-2 rounded outline-none focus:outline-none sm:mr-2 mb-1"
                        type="button"
                        style="transition: all 0.15s ease 0s"
                        @click="isUpRole = true"
                        v-if="user.Role !== 'seller' && user.Role !== 'admin'"
                      >
                        Trở thành người bán
                      </button>
                      <button
                        class="bg-[#FF571A] active:bg-pink-600 uppercase text-white font-bold hover:shadow-md shadow text-xs px-4 py-2 rounded outline-none focus:outline-none sm:mr-2 mb-1"
                        type="button"
                        style="transition: all 0.15s ease 0s"
                        @click="EditProfile"
                      >
                        Chỉnh sửa thông tin
                      </button>
                    </div>
                  </div>
                </div>
              </div>

              <div class="mt-8 pb-10 pt-6 border-t border-gray-300 text-center">
                <div class="w-full w-4/12 px-4 lg:order-1">
                  <div class="flex justify-center py-4 lg:pt-4 pt-8">
                    <div class="mr-4 p-3 text-center"></div>
                    <!-- <div class="mr-4 p-3 text-center">
                      <span
                        class="text-xl font-bold block uppercase tracking-wide text-[#fafcfe]"
                        >{{ countPost }}</span
                      ><span class="text-sm text-[#fafcfe]">Post</span>
                    </div>
                    <div class="lg:mr-4 p-3 text-center">
                      <span
                        class="text-xl font-bold block uppercase tracking-wide text-[#fafcfe]"
                        >{{ countLikes }}</span
                      ><span class="text-sm text-[#fafcfe]">Likes</span>
                    </div> -->
                  </div>
                </div>
                <div class="flex flex-wrap justify-center">
                  <div class="w-full lg:w-9/12 px-4">
                    <div id="main-content">
                      <div v-for="n in filternews" :key="n.id">
                        <BlogCard
                          :image-link="n.blogImage ?? null"
                          :author="`${n.userId?.firstName ?? ''} ${
                            n.userId?.lastName ?? ''
                          }`"
                          :comments="n.comments"
                          :like="
                            n.reaction?.filter((e) => {
                              return e.reaction === 'like'
                            }).length
                          "
                          :dislike="
                            n.reaction?.filter((e) => {
                              return e.reaction === 'dislike'
                            }).length
                          "
                          :title="n.title"
                          :time="n.createdAt"
                        />
                      </div>
                    </div>
                    <span
                      v-if="!compareLength"
                      class="font-normal text-[#FF571A] cursor-pointer"
                      @click="showMore()"
                      >Show more
                    </span>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
    </main>
    <EditProfile
      v-if="isEditProfile"
      :user="user"
      @save="save"
      @cancel="cancelSave"
      @fetchInfoUser="fetchInfoUser"
    />
    <!-- <div v-if="isUpdatingBlog" class="post-creator" @click="cancel">
      <div class="post-creator__container custom-scroll" @click.stop>
        <PostCreator
          class="post-creator__container custom-scroll"
          @cancel="cancel"
          @setLoading="isLoading = true"
          @doneLoading="isLoading = false"
        />
      </div>
    </div> -->

    <FooterBar />
  </div>
</template>
<script>
import axios from 'axios'
import EditProfile from '~/components/User/EditProfile.vue'
import BlogCard from '~/components/Card/BlogCard.vue'
import TopNavBar from '~/components/TopNaviBar.vue'
import FooterBar from '~/components/FooterBar.vue'
import ModalUprole from '~/components/Modal/ModalUprole.vue'
import constant from '~/constant'

// import PostCreator from '~/components/Blog/PostCreator.vue'

export default {
  name: 'Profile',
  components: {
    BlogCard,
    EditProfile,
    TopNavBar,
    FooterBar,
    ModalUprole,
    // PostCreator,
  },
  layout: 'empty',
  data() {
    return {
      user: {},
      news: [],
      filternews: [],
      isEditProfile: false,
      isUpdatingBlog: true,
      isUpRole: false,
    }
  },
  computed: {
    countPost() {
      return this.filternews.length
    },
    countLikes() {
      let totalLikes = 0
      this.filternews.forEach((e) => {
        e.reaction.forEach((r) => {
          if (r.reaction === 'like') {
            totalLikes++
          }
        })
      })
      return totalLikes
    },
    compareLength() {
      return this.filternews.length === this.news.length
    },
  },
  created() {
    // this.getProfile()
    // this.$axios.get(`/users/${this.user._id}/blogs`).then((res) => {
    //   this.filternews = res.data.docs
    // })
    const userId = localStorage.getItem('userId')
    axios({
      method: 'get',
      url: `${constant.base_url}/user/${userId}`,
      headers: {
        'ngrok-skip-browser-warning': 'skip-browser-warning',
      },
    }).then((res) => {
      console.log(res.data)
      this.user = res.data
      localStorage.setItem('user', JSON.stringify(this.user))
    })
  },
  beforeMount() {
    this.filternews = this.news.slice(0, 2)
  },
  methods: {
    toRoleSeller(shopName) {
      const authorization = `Bearer ${localStorage.getItem('accessToken')}`
      this.isUpRole = false
      axios({
        method: 'post',
        url: `${constant.base_url}/user/uprole`,
        headers: {
          Authorization: authorization,
        },
        data: {
          shopname: shopName,
        },
      })
        .then((res) => {
          console.log(res)
          this.$notify({
            title: 'Thành công',
            text: 'Bạn có thể đăng sách bán thành công',
            type: 'success',
            group: 'foo',
          })
        })
        .catch((err) => {
          this.$notify({
            title: 'Thất bại',
            text: err,
            type: 'error',
            group: 'foo',
          })
        })
    },
    getProfile() {
      this.user = JSON.parse(localStorage.getItem('user'))
    },
    showMore() {
      this.filternews = this.news
    },
    EditProfile() {
      this.isEditProfile = true
    },
    cancelSave() {
      this.isEditProfile = false
    },
    save(userProp) {
      // alert('Luu thanh cong:', JSON.stringify(userProp))
      console.log(userProp)
      const userId = localStorage.getItem('userId')
      axios({
        method: 'get',
        url: `${constant.base_url}/user/${userId}`,
        headers: {
          'ngrok-skip-browser-warning': 'skip-browser-warning',
        },
      }).then((res) => {
        console.log(res.data)
        this.user = res.data
        localStorage.setItem('user', JSON.stringify(this.user))
      })
      this.isEditProfile = false
    },
    fetchInfoUser(data) {
      console.log('Fetch user for edit')
      const userId = localStorage.getItem('userId')
      axios({
        method: 'get',
        url: `${constant.base_url}/user/${userId}`,
        headers: {
          'ngrok-skip-browser-warning': 'skip-browser-warning',
        },
      })
        .then((res) => {
          console.log(res.data)

          localStorage.setItem('user', JSON.stringify(data))
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
}
</script>

<style lang="scss" scoped>
.relative {
  img {
    width: 150px;
    height: 150px;
    object-fit: contain;
  }
}

@media screen and (max-width: 1024px) {
  .info_user {
    margin-top: 80px;
  }
}
</style>
