<!--不使用-->
<template>
  <div class="product-list" m1>
    <v-container fluid grid-list-lg>
      <v-layout row m1>
        <v-flex xs12 class="text-xs-center display-1 font-weight-black my-5"
          >Item list</v-flex
        >
      </v-layout>
      <v-layout wrap justify-space-around m1>
        <v-flex
          v-for="{ id, goods_front_image, name } in initData.results"
          :key="id"
          class="item"
        >
          <v-card
            color="gray"
            dark
            width="250px"
            tag="button"
            outlined
            block
            @click="showHedgehogs(1)"
            data-cy="plansSPBtn"
          >
            <span v-if="goods_front_image != null">
              <v-img :src="goods_front_image"></v-img>
            </span>
            <span v-else>
              <v-img src="/prod/prod0.jpg"></v-img>
            </span>
            <v-card-text>
              <div>
                <h3 class="headline mb-0">{{ name }}</h3>
                <router-link
                  v-bind:to="{ name: 'product', params: { id: id } }"
                  >{{ name }}</router-link
                >
              </div>
            </v-card-text>
            <v-card-actions>
              <v-card-actions>
                <v-btn
                  outlined
                  block
                  color="green"
                  @click="showHedgehogs(1)"
                  data-cy="plansSPBtn"
                  >Add to Cart</v-btn
                >
              </v-card-actions>
              <v-btn icon><v-icon>❤️</v-icon></v-btn>
            </v-card-actions>
          </v-card>
        </v-flex>
      </v-layout>
    </v-container>
    <v-container fluid grid-list-lg>
      <v-layout wrap justify-space-around m2>
        <v-btn :disabled="this.previousPageIsNull" v-on:click="pagePrevious()">
          前のページへ
        </v-btn>
        <v-btn :disabled="this.nextPageIsNull" v-on:click="pageNext()">
          次のページへ
        </v-btn>
      </v-layout>
    </v-container>
    <router-view />
  </div>
</template>

<script>
export default {
  data() {
    return {
      nextUrl: null,
      previousUrl: null,
      products: [],
      pageNo: 1
    };
  },
  created() {
    // eslint-disable-next-line
    this.$store.dispatch("getProducts", 1);
  },
  computed: {
    initData() {
      return this.$store.getters.products;
    },
    isLoggedIn() {
      return this.$store.getters.isLoggedIn;
    },
    nextPageIsNull() {
      if (this.initData.next === null) {
        return true;
      }
      return false;
    },
    previousPageIsNull() {
      if (this.initData.previous === null) {
        return true;
      }
      return false;
    }
  },
  methods: {
    showHedgehogs(color) {
      this.$store.dispatch("getHedgehogs", color);
    },
    pageNext() {
      this.pageNo += 1;
      this.$store.dispatch("getProducts", this.pageNo);
    },
    pagePrevious() {
      this.pageNo -= 1;
      this.$store.dispatch("getProducts", this.pageNo);
    }
  }
};
</script>
<style scoped>
.m1 {
  padding-right: 100px;
  padding-left: 100px;
}
.m2 {
  padding: 20px; /* 余白指定 */
  text-align: center; /* 中央寄せ */
  background-color: #ddd; /* 背景色指定 */
  height: 100px;
}
.item {
  float: left;
  list-style: none;
  margin-right: 5px;
}
.flex {
  padding: 5px;
  flex-grow: 0;
}
.flex-empty {
  height: 0 !important;
  padding-top: 0 !important;
  padding-bottom: 0 !important;
}
</style>
