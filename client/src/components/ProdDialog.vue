<template>
  <v-dialog v-model="dialogs.dialog" width="500">
    <v-card class="ma-3;pa-5">
      <v-list-item>
        <v-list-item-avatar color="grey" size="62">
          <v-img :src="dialogs.prod.seller.image" />
        </v-list-item-avatar>
        <v-list-item-content>
          <v-list-item-title class="headline">
            {{ dialogs.prod.name }}</v-list-item-title
          >
          <v-list-item-subtitle>
            by {{ dialogs.prod.seller.username }}
          </v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>
      <v-img
        :src="dialogs.prod.image"
        class="white--text align-end"
        gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.1)"
        height="250px"
      >
      </v-img>
      <v-card-text>
        <br />
        <div class="price">
          <p>Sales Price {{ dialogs.prod.shop_price }}円</p>
        </div>
        <p class="box"></p>
        {{ dialogs.prod.brief }}
        <br />
        <div style="text-align:right">
          {{ dialogs.prod.add_time.slice(0, 4) }}/{{ dialogs.prod.add_time.slice(5, 7) }}/{{ dialogs.prod.add_time.slice(8, 10) }}
          {{ dialogs.prod.add_time.slice(12, 16) }}
        </div>
      </v-card-text>
      <v-divider></v-divider>

      <v-card-actions>
        <v-btn
          text
          color="deep-purple accent-4"
          @click="addCart(dialogs.prod.id)"
        >
          Add cart
        </v-btn>
        <v-spacer></v-spacer>
        <v-btn icon>
          <v-icon
            v-bind:color="
              favorite_id.indexOf(dialogs.prod.id) >= 0 && isLoggedIn
                ? 'red lighten-2'
                : ''
            "
            @click="changeFavorite(dialogs.prod.id)"
            >mdi-heart</v-icon
          >
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
import { mapActions } from "vuex";
export default {
  props: ["dialogs"],
  data() {
    return {
      favorites: [],
      favorite_id: [],
      prod_detail: []
    };
  },
  created() {},
  computed: {
    ...mapActions(["setCartItems_id"]),
    ...mapActions(["setFavorites_id"]),

    userInfo() {
      return this.$store.getters.userInfo;
    },
    cartItems_id() {
      return this.$store.getters.cartItems_id;
    },
    newCartItems() {
      return this.$store.getters.cartItems;
    },
    userFavorites() {
      return this.$store.getters.favorites;
    },
    isLoggedIn() {
      return this.$store.getters.isLoggedIn;
    }
  },
  methods: {
    addCart(prod_id) {
      //TODO
      alert("機能実装中 (商品ID:" + prod_id + ")");
      return "";
      // if (!this.isLoggedIn) {
      //   return "";
      // }
      // let self = this;
      // let data = new FormData();
      // if (this.cartItems_id.indexOf(prod_id) < 0) {
      //   data.append("item", prod_id);
      //   data.append("user", self.userInfo.user_id);
      //   data.append("amount", 1);
      //   alert("1");
      //   self.$store.dispatch("addCartItems", data).then(function() {
      //     self.$store
      //       .dispatch("getCartItems", self.userInfo.user_id)
      //       .then(function(data) {
      //         self.setCartItems_id([]);
      //         //idだけのリスト作成
      //         let arr = [];
      //         data.forEach(item => {
      //           arr.push(item.item.id);
      //           alert("カートに商品を追加しました！ 商品名:" + item.item.name);
      //         });
      //         self.setCartItems_id(arr);
      //       });
      //   });
      // } else {
      //   //既に追加されている場合は個数を更新
      //   this.newCartItems.forEach(item => {
      //     if (item.item.id == prod_id) {
      //       if (item.amount == 10) {
      //         alert("一度に購入できる同一商品は、１０個までです。");
      //         return null;
      //       }
      //       data.append("amount", (item.amount += 1));
      //       self.$store
      //         .dispatch("updateCartItems", [item.id, data])
      //         .then(function() {
      //           self.$store
      //             .dispatch("getCartItems", self.userInfo.user_id)
      //             .then(function(data) {
      //               //idだけのリスト作成
      //               self.setCartItems_id([]);
      //               let arr = [];
      //               data.forEach(item => {
      //                 arr.push(item.item.id);
      //               });
      //               self.setCartItems_id(arr);
      //             });
      //           alert("カートに商品を追加しました！ 商品名:" + item.item.name);
      //         });
      //     }
      //   });
      // }
    },
    changeFavorite(prod_id) {
      //TODO
      alert("機能実装中 (商品ID:" + prod_id + ")");
      return "";
      // if (!this.isLoggedIn) {
      //   return "";
      // }
      // let self = this;
      // let data = new FormData();
      // data.append("item", prod_id);
      // data.append("user", self.userInfo.user_id);
      // if (this.favorite_id.indexOf(prod_id) < 0) {
      //   self.$store.dispatch("addUserFavorites", data).then(function() {
      //     self.$store
      //       .dispatch("getUserFavorites", self.userInfo.user_id)
      //       .then(function(data) {
      //         self.favorites = data.results;
      //         self.favorite_id = [];
      //         //idだけのリスト作成
      //         data.results.forEach(item => {
      //           self.favorite_id.push(item.item.id);
      //         });
      //       });
      //   });
      // } else {
      //   this.favorites.forEach(item => {
      //     if (item.item.id === prod_id) {
      //       self.$store
      //         .dispatch("deleteUserFavorites", item.id)
      //         .then(function() {
      //           self.$store
      //             .dispatch("getUserFavorites", self.userInfo.user_id)
      //             .then(function(data) {
      //               self.favorites = data.results;
      //               //idだけのリスト作成
      //               self.favorite_id = [];
      //               data.results.forEach(item => {
      //                 self.favorite_id.push(item.item.id);
      //               });
      //             });
      //         });
      //     }
      //   });
      // }
    }
  }
};
</script>

<style scoped>
.price {
  margin-right: 10px;
  font-size: 120%;
}
.box {
  border-bottom: 1px dashed rgba(102, 98, 98, 0.425);
}
</style>
