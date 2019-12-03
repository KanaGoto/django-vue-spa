<template>
  <div class="product-list">
    <v-container fluid grid-list-lg>
      <v-layout row>
        <v-flex xs12 class="text-xs-center display-1 font-weight-black my-5"
          >Item list</v-flex
        >
      </v-layout>
      <v-layout wrap justify-space-around>
        <v-flex
          v-for="{ id, goods_front_image, name } in initData.results"
          :key="id"
          class="item"
        >
          <v-card>
            <v-responsive>
              <v-img v-bind:src="goods_front_image" height="300px"> </v-img>
              <v-card-text>
                <div>
                  <h3 class="headline mb-0">{{ name }}</h3>
                  <router-link
                    v-bind:to="{ name: 'product', params: { id: id } }"
                    >{{ name }}</router-link
                  >
                  <div>
                    The spines are white, banded with black. No more than 5% of
                    the quills are to be solid white. The face is white with a
                    black mask, ears and nose. The underbody hair is white Black
                    mottling of the underbelly is extensive. Skin on the
                    shoulders is jet-black. The nose is black.
                  </div>
                </div>
              </v-card-text>
              <v-card-actions>
                <v-btn
                  outlined
                  block
                  color="green"
                  @click="showHedgehogs(1)"
                  data-cy="plansSPBtn"
                  >Select This Color</v-btn
                >
              </v-card-actions>
            </v-responsive>
          </v-card>
        </v-flex>
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
      products: []
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
    }
  },
  methods: {
    showHedgehogs(color) {
      this.$store.dispatch("getHedgehogs", color);
    }
  }
};
</script>
<style scoped>
.item {
  float: left;
  list-style: none;
  margin-right: 5px;
}
.flex {
  flex-grow: 0;
}

.flex-empty {
  height: 0 !important;
  padding-top: 0 !important;
  padding-bottom: 0 !important;
}
</style>
