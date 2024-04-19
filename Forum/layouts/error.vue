<template>
  <div>
    <TopNaviBarGuest/>
    <!-- <div class="bg-[#1B3764] flex flex col justify-center items-center p-10">
      <div class="text-[30px] text-white font-semibold">Page Error</div>
    </div> -->
    <div class="relative flex justify-center items-center">
      <img src="~/assets/img/error-background.png" class="w-full">
      <img class="absolute" src="~/assets/img/error-title.png" alt="">

    </div>
    <notifications group="foo" />
    <FooterBar/>
  </div>
</template>
<script>
import FooterBar from '~/components/FooterBar.vue'
import TopNaviBarGuest from '~/components/TopNaviBarGuest.vue'
export default {
  layout: 'empty',
  components: {
    TopNaviBarGuest,
    FooterBar
  }
}
</script>
<style scoped></style>
