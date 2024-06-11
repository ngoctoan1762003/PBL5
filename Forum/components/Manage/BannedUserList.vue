<template>
  <div>
    <div
      class="main fixed flex justify-center items-center w-full h-full top-0"
      v-show="isDeleting"
    >
      <div class="absolute bg-gray-500 opacity-50 w-full h-full"></div>
      <ModalDeleteAlert
        class="relative z-[1]"
        @cancel="cancel"
        @delete=" (deletingId)"
      />
    </div>
    <div>
      <EditRole
        v-if="isEditProfile"
        :user="currentUser"
        @cancel="cancelSave"
        @save="save"
        @reload="reload"
      />
    </div>
    <div
      class="user-list text-white font-medium p-5 w-full bg-[#1B3764] rounded-[16px]"
    >
      <div class="font-semibold user-list-row">
        <div class="user-list-row-cell avatar"></div>
        <div class="user-list-row-cell first-name">Tên</div>
        <!-- <div class="user-list-row-cell gender">Gender</div> -->
        <div class="user-list-row-cell phone">Số ĐT</div>
        <div class="user-list-row-cell email">Email</div>
        <div class="user-list-row-cell birthday">Vai trò</div>
        <!-- <div class="user-list-row-cell role">Role</div> -->
        <div class="user-list-row-cell status">Địa chỉ</div>
        <div class="tooltip"></div>
      </div>
      <div
        v-for="user in users"
        class="user-list-row user-list-information"
        :key="user._id"
      >
        <div class="avatar">
          <img :src="user.image" class="p-2 rounded-full" />
        </div>
        <div class="user-list-row-cell first-name">
          {{ getName(user.Name) }}
        </div>
        <!-- <div class="user-list-row-cell gender">{{ user.gender?'Male':'Female' }}</div> -->
        <div class="user-list-row-cell phone">{{ user.Phone }}</div>
        <div class="user-list-row-cell email">{{ user.Email }}</div>
        <div class="user-list-row-cell birthday">{{ user.Role }}</div>
        <!-- <div class="user-list-row-cell role">{{ user.roleName }}</div> -->
        <div class="user-list-row-cell status">
          {{ user.Address }}
        </div>
        <div class="tooltip relative">
          <button
            class="hover:bg-red-400 bg-white min-w-[100px] hover:text-white text-gray-900 group flex rounded-md items-center justify-center w-full px-2 py-2 text-sm"
            @click="onDelete(user._id)"
          >
            Mở khóa
          </button>
        </div>
      </div>
      <div class="w-full h-[1px] bg-gray-500"></div>
      <Pagination
        :count="count"
        @changePage="changePage"
        :recordsPerPage="recordsPerPage"
      />
    </div>
  </div>
</template>


<script>
import axios from 'axios'
import { format } from 'date-fns'
import EditRole from '../User/EditRole.vue'
import ModalDeleteAlert from '../Modal/ModalDeleteAlert.vue'
import constant from '~/constant'
import Pagination from '~/components/Pagination.vue'

export default {
  components: {
    EditRole,
    Pagination,
    ModalDeleteAlert,
  },
  props: {
    users: Array,
    count: Number,
    recordsPerPage: Number,
  },
  data() {
    return {
      // users: [],
      currentUser: {
        type: Object,
        default: () => {},
      },
      isEditProfile: false,
      deletingId: '',
      isDeleting: false,
    }
  },
  methods: {
    closeAllPopup() {
      this.users.forEach((p) => {
        document.querySelector('#action-' + p._id).classList.add('hidden')
      })
    },
    closeAllPopupExceptIndex(index) {
      this.users.forEach((p) => {
        if (p._id !== index)
          document.querySelector('#action-' + p._id).classList.add('hidden')
      })
    },
    displayTooltip(id) {
      this.closeAllPopupExceptIndex(id)
      const popup = document.querySelector('#action-' + id)
      popup.classList.toggle('hidden')
    },
    cancel() {
      this.isDeleting = false
    },
    cancelSave() {
      this.isEditProfile = false
    },
    save(userProp) {
      console.log(userProp)
      this.isEditProfile = false
    },
    showPopup(user) {
      this.currentUser = user
      this.isEditProfile = true
    },
    deleteAlert(id) {
      console.log(id)
      this.deletingId = id
      this.isDeleting = true
    },
    onDelete(id) {
      const authorization = `Bearer ${localStorage.getItem('accessToken')}`
      this.isDeleting = false
      axios({
        method: 'put',
        url: `${constant.base_url}/user/unban/${id}`,
        headers: {
          Authorization: authorization,
        },
      }).then((res) => {
        this.$notify({
          title: 'Thành công',
          text: 'Mở khóa thành công',
          type: 'success',
          group: 'foo',
        })
        this.reload()
      })
    },
    formatBirthday(date) {
      console.log(date)
      if (date) {
        const jsDate = new Date(date)

        return format(jsDate, 'dd/MM/yyyy')
      }
      return ''
    },
    reload() {
      this.$emit('reload')
    },
    getName(firstName, lastName) {
      if (!firstName) firstName = ''
      if (!lastName) lastName = ''
      return firstName + ' ' + lastName
    },
    changePage(page, limit) {
      console.log('to user lít ')
      this.$emit('changePage', page, limit)
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
}
.user-list-information:hover {
  background-color: $dark-4;
}

.user-list {
  display: flex;
  flex-direction: column;
  gap: 20px;

  .user-list-row {
    display: flex;
    grid-template-columns: repeat(8, minmax(0, 1fr));
    font-size: 12px;
    align-items: center;
    border-radius: 10px;
    min-height: 50px;

    &-cell {
      grid-column: span 1 / span 1;
    }

    .avatar {
      width: 10%;
      display: flex;
      justify-content: center;

      img {
        width: 50px;
      }
    }

    .first-name {
      width: 20%;
    }

    .last-name {
      width: 20%;
    }

    .gender {
      width: 8%;
    }

    .phone {
      width: 10%;
    }

    .email {
      width: 23%;
    }

    .birthday {
      width: 10%;
    }

    .role {
      width: 10%;
    }

    .status {
      width: 15%;
    }

    .tooltip {
      width: 2%;
      display: flex;
      justify-content: center;
    }
  }
}
</style>
