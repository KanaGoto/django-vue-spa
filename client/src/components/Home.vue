<template>
  <div id="home">
    <v-container>
      <v-row dense>
        <v-col v-for="prod in dispProducts" :key="prod.id" :cols="4">
          <v-card class="ma-5">
            <v-list-item>
              <v-list-item-avatar color="grey" size="40">
                <v-img :src="prod.seller.image"></v-img>
              </v-list-item-avatar>
              <v-list-item-content>
                <v-list-item-title class="title-read">{{
                  prod.name
                }}</v-list-item-title>
                <v-list-item-subtitle>
                  by {{ prod.seller.username }}
                </v-list-item-subtitle>
              </v-list-item-content>
            </v-list-item>
            <v-img
              :src="prod.image"
              class="white--text align-end"
              gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.1)"
              height="200px"
            >
            </v-img>
            <v-card-text class="box-read">
              {{ prod.brief }}
            </v-card-text>
            <v-card-actions>
              <v-btn
                slot="activator"
                text
                color="red lighten-1"
                @click="openModal(prod)"
              >
                Detail
              </v-btn>
              <v-btn
                text
                color="deep-purple accent-5"
                @click="addCart(prod.id)"
              >
                Add cart
              </v-btn>
              <v-spacer></v-spacer>
              <v-btn icon>
                <v-icon
                  v-bind:color="
                    favorite_id.indexOf(prod.id) >= 0 && isLoggedIn
                      ? 'red lighten-2'
                      : ''
                  "
                  @click="changeFavorite(prod.id)"
                  >mdi-heart</v-icon
                >
              </v-btn>
            </v-card-actions>
            <!-- dialog -->
            <app-dialog :dialogs="dialogs"></app-dialog>
          </v-card>
        </v-col>
        <v-fab-transition>
          <v-btn
            color="light-green darken-1"
            dark
            fab
            fixed
            bottom
            right
            v-show="showFab"
            @click="$vuetify.goTo('#app', { duration: 400, offset: 0 })"
          >
            <v-icon>keyboard_arrow_up</v-icon>
          </v-btn>
        </v-fab-transition>
      </v-row>
      <div class="text-center">
        <v-row justify="center">
          <v-pagination
            v-model="currentPage"
            :length="totalPage"
            :total-visible="5"
            :click="$vuetify.goTo('#app', { duration: 0, offset: 0 })"
          ></v-pagination>
        </v-row>
        <br />
      </div>
    </v-container>
  </div>
</template>
<script>
import Dialog from "./ProdDialog.vue";
import "vue-material-design-icons/styles.css";
import { mapActions } from "vuex";
export default {
  components: {
    appDialog: Dialog
  },
  data() {
    return {
      favorites: [],
      favorite_id: [],
      products: [],
      y: window.scrollY,
      currentPage: 1,
      totalPage: 1,
      showFab: false,
      dialogs: {
        dialog: false,
        prod: []
      }
    };
  },
  created() {
    let self = this;
    this.$store
      .dispatch("getProducts", 1)
      .then(function(data) {
        self.currentPage = data.current;
        self.products = data.results;
        self.totalPage = data.total_pages;
        if (self.isLoggedIn) {
          self.getOrderList(self.userInfo.user_id);
        }
      })
      .catch(function(err) {
        alert(err);
      });
    if (this.isLoggedIn) {
      //お気に入り商品を取得
      this.$store
        .dispatch("getUserFavorites", this.userInfo.user_id)
        .then(function(data) {
          self.favorites = data.results;
          //idだけのリスト作成
          data.results.forEach(item => {
            self.favorite_id.push(item.item.id);
          });
        })
        .catch(function(err) {
          alert(err);
        });
      this.$store
        .dispatch("getCartItems", this.userInfo.user_id)
        .then(function(data) {
          //idだけのリスト作成
          let arr = [];
          data.results.forEach(item => {
            arr.push(item.item.id);
          });
          self.setCartItems_id(arr);
        });
    }
  },
  computed: {
    userInfo() {
      return this.$store.getters.userInfo;
    },
    newProducts() {
      return this.$store.getters.products;
    },
    dispProducts() {
      return this.newProducts ? this.newProducts.results : this.products;
    },
    cartItems_id() {
      return this.$store.getters.cartItems_id;
    },
    newCartItems() {
      return this.$store.getters.cartItems;
    },
    isLoggedIn() {
      return this.$store.getters.isLoggedIn;
    },
    userFavorites() {
      return this.$store.getters.favorites;
    }
  },
  watch: {
    newProducts: function(newProd) {
      self.products = newProd.results;
    },
    currentPage: function(newPageNo) {
      let self = this;
      this.$store.dispatch("getProducts", newPageNo).then(function(data) {
        self.products = data.results;
        self.totalPage = data.total_pages;
      });
    }
  },
  methods: {
    ...mapActions(["setCartItems_id"]),
    ...mapActions(["setFavorites_id"]),
    ...mapActions(["getOrderList"]),

    onScroll() {
      this.showFab = window.scrollY > 0;
    },
    openModal(prod) {
      this.dialogs.dialog = true;
      this.dialogs.prod = prod;
    },
    addCart(prod_id) {
      if (!this.isLoggedIn) {
        this.$router.push("/login");
      }
      let self = this;
      let data = new FormData();
      if (this.cartItems_id.indexOf(prod_id) < 0) {
        data.append("item", prod_id);
        data.append("user", this.userInfo.user_id);
        data.append("amount", 1);
        self.$store.dispatch("addCartItems", data).then(function() {
          self.$store
            .dispatch("getCartItems", self.userInfo.user_id)
            .then(function(data) {
              self.setCartItems_id([]);
              //idだけのリスト作成
              let arr = [];
              data.forEach(item => {
                arr.push(item.item.id);
              });
              self.setCartItems_id(arr);
            });
        });
      } else {
        //既に追加されている場合は個数を更新
        this.newCartItems.forEach(item => {
          if (item.item.id == prod_id) {
            if (item.amount == 10) {
              alert("一度に購入できる同一商品は、１０個までです。");
              return null;
            }
            data.append("amount", (item.amount += 1));
            self.$store
              .dispatch("updateCartItems", [item.id, data])
              .then(function() {
                self.$store
                  .dispatch("getCartItems", self.userInfo.user_id)
                  .then(function(data) {
                    //idだけのリスト作成
                    self.setCartItems_id([]);
                    let arr = [];
                    data.forEach(item => {
                      arr.push(item.item.id);
                    });
                    self.setCartItems_id(arr);
                  });
              });
          }
        });
      }
      alert("カートに商品を追加しました！");
    },
    changeFavorite(prod_id) {
      if (!this.isLoggedIn) {
        this.$router.push("/login");
      }
      let self = this;
      let data = new FormData();
      data.append("item", prod_id);
      data.append("user", this.userInfo.user_id);
      if (this.favorite_id.indexOf(prod_id) < 0) {
        self.$store.dispatch("addUserFavorites", data).then(function() {
          self.$store
            .dispatch("getUserFavorites", self.userInfo.user_id)
            .then(function(data) {
              self.favorites = data.results;
              self.favorite_id = [];
              //idだけのリスト作成
              data.results.forEach(item => {
                self.favorite_id.push(item.item.id);
              });
            });
        });
      } else {
        this.favorites.forEach(item => {
          if (item.item.id === prod_id) {
            self.$store
              .dispatch("deleteUserFavorites", item.id)
              .then(function() {
                self.$store
                  .dispatch("getUserFavorites", self.userInfo.user_id)
                  .then(function(data) {
                    self.favorites = data.results;
                    //idだけのリスト作成
                    self.favorite_id = [];
                    data.results.forEach(item => {
                      self.favorite_id.push(item.item.id);
                    });
                  });
              });
          }
        });
      }
    },
    top() {
      // window.scrollTo({
      //   top: 0,
      //   left: 0,
      //   behavior: "smooth"
      // });
      this.$vuetify.goTo(0);
    }
  },
  mounted() {
    window.addEventListener("scroll", this.onScroll);
  },
  destroyed() {
    window.removeEventListener("scroll", this.onScroll);
  }
};
</script>

<style scoped>
.title-read {
  font-size: large;
  font-weight: 400;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}
.box-read {
  padding-bottom: 0px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}
</style>
