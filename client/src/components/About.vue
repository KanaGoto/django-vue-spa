<template>
  <div id="about" style="margin-left:35%">
    aaa just explanation! haha
    <!-- leftNavi -->
    <left-navi :isLoggedIn="isLoggedIn" :userInfo="userInfo"></left-navi>
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
      items: [
        {
          title: "My Account",
          icon: "mdi-image",
          link: "account"
        },
        {
          title: "Order History",
          icon: "mdi-view-dashboard",
          link: "orders"
        },
        { title: "About", icon: "mdi-help-box", link: "about" }
      ],
      titles: ["home", "following", "profile"],
      tabs: null,
      drawer: null,
      panel: false,
      count: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    };
  },
  created() {
    this.getOrderList(this.userInfo.user_id);
  },
  computed: {
    isLoggedIn() {
      return this.$store.getters.isLoggedIn;
    },
    userInfo() {
      return this.$store.getters.userInfo;
    },
    orderList() {
      return this.$store.getters.orderList.results;
    },
    nextURL() {
      return this.$store.getters.orderList.next;
    },
    beforeURL() {
      return this.$store.getters.orderList.before;
    }
  },
  methods: {
    getColor() {
      let tmp = this.colors[this.colorCount].color;
      let loopNum = 0;
      if (loopNum != Number(this.orderList.length)) {
        if (this.colorCount == Number(this.colors.length - 1)) {
          this.colorCount = 0;
        } else {
          this.colorCount += 1;
        }
        this.cardColor = tmp;
        return tmp;
      } else {
        return "";
      }
    },
    onScroll(e) {
      this.offsetTop = e.target.scrollTop;
    },
    pageNext() {
      this.pageNo += 1;
      this.$store.dispatch("getProducts", this.pageNo);
    }
  }
};
</script>

<style scoped>
.timeline {
  text-align: left;
  margin: 50px;
}
.fb {
  /* floatを解除 */
  clear: both;
}
</style>
