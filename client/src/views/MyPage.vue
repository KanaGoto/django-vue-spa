<template>
  <div id="MyPage">
    <v-card>
      <v-row justify="center" align="center">
        <v-toolbar
          color="teal lighten-1
"
          dark
          flat
          justify="center"
          align="center"
        >
          <v-app-bar-nav-icon
            large
            style="margin-left:15px"
            @click.stop="leftDrawer = !leftDrawer"
          ></v-app-bar-nav-icon>
          <div class="logo">
            <v-img
              src="../static/organic.png"
              width="300px"
              height="80px"
            ></v-img>
          </div>
          <v-spacer></v-spacer>
          <div v-if="isLoggedIn">
            <v-btn text small @click="doLogout">
              logout
            </v-btn>
          </div>
          <div v-else>
            <v-btn text small @click="doLogin">
              login
            </v-btn>
          </div>
          <div class="icon">
            <div v-if="isLoggedIn">
              <v-badge overlap color="blue">
                <template v-slot:badge>
                  <span>{{ cartItems.length }}</span>
                </template>
                <v-icon @click.stop="cartdrawer = !cartdrawer" large
                  >mdi-cart
                </v-icon>
              </v-badge>
            </div>
            <div v-else>
              <v-icon @click.stop="cartdrawer = !cartdrawer" large
                >mdi-cart
              </v-icon>
            </div>
          </div>
          <v-tabs
            slot="extension"
            v-model="tabs"
            background-color="transparent"
            centered
          >
            <v-tab v-for="title in titles" :key="title"> {{ title }} </v-tab>
          </v-tabs>
        </v-toolbar>
      </v-row>
    </v-card>

    <!-- カート -->
    <v-navigation-drawer
      v-model="cartdrawer"
      absolute
      temporary
      right
      width="400"
      height="100%"
    >
      <v-list-item>
        <v-list-item-content>
          <v-list-item-title>カート内の商品</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
      <v-divider></v-divider>
      <v-list>
        <v-list-item v-for="item in cartItems" :key="item.id">
          <v-list-item-icon>
            <v-img
              :src="item.item.image"
              gradient="to bottom, rgba(0,0,0,0), rgba(0,0,0,0)"
              height="80px"
              width="100px"
            ></v-img>
          </v-list-item-icon>

          <v-list-item-content>
            {{ item.item.name }}
            ( {{ item.item.seller.username }} )<br />
            {{ item.item.shop_price }}円
            <v-col lg="3.5" md="3.5" sm="3.5" xs="3.5">
              <v-select
                v-model="item.amount"
                :items="count"
                v-on:change="changeAmount(item.id, item.amount)"
              ></v-select></v-col
            >個
            <!-- 削除ボタン-->
            <v-flex
              ><v-a
                @click="deleteCartItem(item.id, item.item.id, item.item.name)"
              >
                <v-img
                  src="../static/clear.svg"
                  width="15"
                  class="cross"
                ></v-img></v-a
            ></v-flex>
          </v-list-item-content>
        </v-list-item>
      </v-list>
      <div v-if="isLoggedIn">
        <div class="purchase">
          <v-btn
            outlined
            color="primary"
            :disabled="(!isLoggedIn || cartItems.length) < 1 ? true : false"
            @click="purchase"
          >
            purchase
          </v-btn>
        </div>
      </div>
      <div v-else>
        <div class="purchase">
          <v-btn outlined color="primary" :disabled="true" @click="purchase">
            purchase
          </v-btn>
        </div>
      </div>
    </v-navigation-drawer>
    <!-- setting -->
    <v-navigation-drawer
      v-model="leftDrawer"
      absolute
      temporary
      width="400"
      height="100%"
    >
      <div v-if="isLoggedIn">
        <v-list-item>
          <v-list-item-avatar color="grey" size="100px">
            <v-img :src="'http://localhost:8000' + userInfo.image"></v-img>
          </v-list-item-avatar>
          <v-list-item-content>
            <v-list-item-title class="title">
              {{ userInfo.username }}
            </v-list-item-title>
            <v-list-item-subtitle>
              Logged In
            </v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>
      </div>
      <div v-else>
        <v-list-item>
          <v-list-item-avatar color="blue" size="100px">
            <v-img src="../static/unknown.png"></v-img>
          </v-list-item-avatar>
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
    <v-tabs-items v-model="tabs">
      <v-tab-item>
        <home></home>
      </v-tab-item>
      <!-- <v-tab-item>
        <favorites></favorites>
      </v-tab-item> -->
      <v-tab-item>
        <my-profile></my-profile>
      </v-tab-item>
    </v-tabs-items>
  </div>
</template>

<script>
import MyProfile from "@/components/MyProfile.vue";
//import Favorites from "@/components/Following.vue";
import Home from "@/components/Home.vue";
import { mapActions } from "vuex";
export default {
  name: "Mypage",
  components: {
    Home,
    MyProfile
  },
  data() {
    return {
      items: [
        { title: "Products", icon: "mdi-image", link: "/" },
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
        { title: "Products", icon: "mdi-image", link: "/" },
        { title: "About", icon: "mdi-help-box", link: "about" }
      ],
      titles: ["home", "profile"],
      tabs: null,
      leftDrawer: null,
      cartdrawer: null,
      count: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    };
  },
  computed: {
    isLoggedIn() {
      return this.$store.getters.isLoggedIn;
    },
    userInfo() {
      return this.$store.getters.userInfo;
    },
    cartItems() {
      return this.$store.getters.cartItems;
    },
    cartItems_id() {
      return this.$store.getters.cartItems_id;
    }
  },
  methods: {
    ...mapActions(["setCartItems_id"]),
    ...mapActions(["updateCartItems"]),
    ...mapActions(["logout"]),
    changeAmount(id, amount) {
      let self = this;
      let data = new FormData();
      data.append("amount", amount);
      this.updateCartItems([id, data]).then(function() {
        self.$store.dispatch("getCartItems", self.userInfo.user_id);
      });
    },
    /* eslint-disable */
    deleteCartItem(id, prod_id ,prod_name){
      //if(!window.confirm("この商品をカートから削除しますか？\n商品名："+prod_name)) return null;
      let self = this;
      this.$store.dispatch("deleteCartItems", id).then(function(){
        //削除した商品IDを取り除く
        var newCartItems_id = self.cartItems_id.filter(function(a) {
          return a !== prod_id;
        });
        self.setCartItems_id(newCartItems_id);
        self.$store.dispatch("getCartItems", self.userInfo.user_id).then(function(){
        });
      });
    },
    purchase(){
      this.$router.push("/purchase");
    },
    doLogout(){
      let self = this;
      this.logout()
        .then(function() {
          self.$router.push("/logout");
        });
    },
    doLogin(){
      this.$router.push("/login");
    }
  }
};
</script>
<style scoped>
.purchase {
  text-align: center;
}
.cross{
  margin: 5px
}
.logo{
  margin-top:40px;
  padding:10px;
}
.icon{
  margin-right:30px;
}
</style>
