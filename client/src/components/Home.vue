<template>
  <v-sheet id="scroll-area-2" class="overflow-y-auto" max-height="700">
    <v-container class="pa-2" style="height: 1300px;">
      <v-row dense>
        <v-col v-for="prod in products" :key="prod.id" :cols="4">
          <v-card class="ma-3">
            <v-list-item>
              <v-list-item-avatar color="white" size="40">
                <v-img :src="prod.seller.pic"></v-img>
              </v-list-item-avatar>
              <v-list-item-content>
                <v-list-item-title class="headline">{{
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
            <v-card-text>
              {{ prod.brief }}
            </v-card-text>
            <v-card-actions>
              <v-btn
                slot="activator"
                text
                color="red lighten-2"
                @click="openModal(prod)"
              >
                Detail
              </v-btn>
              <v-btn text color="deep-purple accent-4">
                Add cart
              </v-btn>
              <v-spacer></v-spacer>
              <v-btn icon>
                <v-icon
                  v-bind:color="
                    favorite_id.indexOf(prod.id) >= 0 ? 'red lighten-2' : ''
                  "
                  >mdi-heart</v-icon
                >
              </v-btn>
              <v-btn icon>
                <v-icon>mdi-share-variant</v-icon>
              </v-btn>
            </v-card-actions>
            <!-- dialog -->
            <app-dialog :dialogs="dialogs"></app-dialog>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </v-sheet>
</template>
<script>
import Dialog from "./ProdDialog.vue";
export default {
  components: {
    appDialog: Dialog
  },
  data() {
    return {
      products: [],
      nextURL: null,
      previousUrl: null,
      favorites: [],
      favorite_id: [],
      pageNo: 1,
      offsetTop: 0,
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
        self.products = data.results;
        self.nextURL = data.next;
        self.previousUrl = data.previous;
      })
      .catch(function(err) {
        alert(err);
      });
    this.$store
      .dispatch("getUserFavorites", 1)
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
  },
  computed: {
    newProducts() {
      return this.$store.getters.products;
    },
    isLoggedIn() {
      return this.$store.getters.isLoggedIn;
    },
    nextPageIsNull() {
      if (this.nextURL === null) {
        return true;
      }
      return false;
    },
    previousPageIsNull() {
      if (this.previousUrl === null) {
        return true;
      }
      return false;
    }
  },
  watch: {
    newProducts: function(newProd) {
      this.products = newProd.results;
      this.nextURL = newProd.next;
      this.previousUrl = newProd.previous;
    }
  },
  methods: {
    onScroll(e) {
      this.offsetTop = e.target.scrollTop;
    },
    pageNext() {
      this.pageNo += 1;
      this.$store.dispatch("getProducts", this.pageNo);
    },
    pagePrevious() {
      this.pageNo -= 1;
      this.$store.dispatch("getProducts", this.pageNo);
    },
    openModal(prod) {
      this.dialogs.dialog = true;
      this.dialogs.prod = prod;
    }
  }
};
</script>
