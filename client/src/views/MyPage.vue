<template>
  <div id="MyPage">
    <v-card>
      <v-row justify="center" align="center">
        <v-toolbar color="cyan" dark flat justify="center" align="center">
          <v-app-bar-nav-icon></v-app-bar-nav-icon>
          <v-toolbar-title>Your Dashboard</v-toolbar-title>
          <v-spacer></v-spacer>

          <v-btn icon>
            <v-icon>mdi-heart</v-icon>
          </v-btn>
          <v-btn icon>
            <v-icon @click.stop="drawer = !drawer">mdi-cart</v-icon>
          </v-btn>
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

      <v-navigation-drawer
        v-model="drawer"
        absolute
        temporary
        right
        width="400"
        height="1000px"
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
        <div class="purchase">
          <v-btn
            outlined
            color="primary"
            :disabled="cartItems.length < 1 ? true : false"
          >
            purchase
          </v-btn>
        </div>
      </v-navigation-drawer>
    </v-card>

    <v-tabs-items v-model="tabs">
      <v-tab-item>
        <home></home>
      </v-tab-item>
      <v-tab-item>
        <following></following>
      </v-tab-item>
      <v-tab-item>
        <my-profile></my-profile>
      </v-tab-item>
    </v-tabs-items>
  </div>
</template>

<script>
import MyProfile from "@/components/MyProfile.vue";
import Following from "@/components/Following.vue";
import Home from "@/components/Home.vue";
import { mapActions } from "vuex";
export default {
  name: "Mypage",
  components: {
    Home,
    MyProfile,
    Following
  },
  data() {
    return {
      titles: ["home", "following", "profile"],
      tabs: null,
      drawer: null,
      count: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
      isLoggedIn: ""
    };
  },
  computed: {
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
    }
  },
  //  watch: {
  //   cartItems: function(newItem) {
  //     this.products = newProd.results;
  //     this.nextURL = newProd.next;
  //     this.previousUrl = newProd.previous;
  //   }
  // },
};
</script>
<style scoped>
.purchase {
  text-align: center;
}
.cross{
  margin: 5px
}
</style>
