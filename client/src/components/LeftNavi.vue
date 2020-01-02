<template>
  <v-navigation-drawer
    v-model="drawer"
    absolute
    permanent
    width="400"
    height="100%"
  >
    <div v-if="isLoggedIn">
      <v-list-item>
        <v-list-item-avatar color="white" size="100px">
          <v-img :src="'http://localhost:8000' + userInfo.image"></v-img>
        </v-list-item-avatar>
        <v-list-item-content>
          <v-list-item-title class="title">
            {{ userInfo.username }}
          </v-list-item-title>
          <v-list-item-subtitle>
            Logged In
            <v-spacer></v-spacer> <a @click="onClick">logout</a>
          </v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>
    </div>
    <div v-else>
      <v-list-item>
        <v-list-item-avatar color="blue" size="100px"> </v-list-item-avatar>
        <v-list-item-content>
          <v-list-item-title class="title">
            unknown user
          </v-list-item-title>
          <v-list-item-subtitle>
            <a href="/login">Login</a> / Not a member ?
            <a href="/register">Join Here</a>
          </v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>
    </div>

    <v-divider></v-divider>
    <!-- ログイン時 -->
    <div v-if="isLoggedIn">
      <v-list dense nav>
        <v-list-item
          v-for="item in items"
          :key="item.title"
          link
          :to="item.link"
        >
          <v-list-item-icon>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-icon>

          <v-list-item-content>
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </div>
    <!-- 未ログイン時 -->
    <div v-else>
      <v-list dense nav>
        <v-list-item
          v-for="item in offItems"
          :key="item.title"
          link
          :to="item.link"
        >
          <v-list-item-icon>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-icon>

          <v-list-item-content>
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </div>
  </v-navigation-drawer>
</template>

<script>
import { mapActions } from "vuex";
export default {
  props: {
    userInfo: Object,
    isLoggedIn: Boolean
  },
  data() {
    return {
      items: [
        { title: "Products", icon: "mdi-image", link: "mypage" },
        {
          title: "My Account",
          icon: "mdi-account-circle",
          link: "account"
        },
        {
          title: "Order History",
          icon: "mdi-view-dashboard",
          link: "orders"
        },
        { title: "About", icon: "mdi-help-box", link: "about" }
      ],
      offItems: [
        { title: "Products", icon: "mdi-image", link: "mypage" },
        { title: "About", icon: "mdi-help-box", link: "about" }
      ],
      drawer: null
    };
  },
  methods: {
    ...mapActions(["logout"]),
    ...mapActions(["getUserInfo"]),
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
    onClick() {
      let self = this;
      this.logout()
        .then(function() {
          self.getUserInfo();
        })
        .then(function() {
          self.$router.push("/logout");
        });
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
