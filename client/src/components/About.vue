<template>
  <div id="about">
    <!-- leftNavi -->
    <left-navi :isLoggedIn="isLoggedIn" :userInfo="userInfo"></left-navi>
    <v-container style="margin-left:30%">
    <v-img src="../static/top.jpg" class="bg"></v-img>
    </v-container>
  </div>
</template>

<script>
import LeftNavi from "./LeftNavi.vue";
export default {
  components: {
    LeftNavi: LeftNavi
  },
  data() {
    return {
      backgroundImageSrc: require("../static/top.jpg")
    }
  },
  computed: {
    isLoggedIn() {
      return this.$store.getters.isLoggedIn;
    },
    userInfo() {
      return this.$store.getters.userInfo;
    }
  }
};
</script>

<style scoped>
.bg {
  width: 80%;
  height: 750px;
}
</style>
