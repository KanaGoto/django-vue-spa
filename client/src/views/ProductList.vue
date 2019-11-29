<template>
  <div class="product-list">
    <h1>商品リスト</h1>
    <ul>
      <li v-for="{ id, name } in products" :key="id">
        <router-link :to="'/product/${id}'">{{ name }}</router-link>
      </li>
    </ul>
    <nav>
      <router-link to="/list" tag="button">list</router-link><br />
      <router-link to="/detail">detail</router-link>
    </nav>
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
  computed: {
    initData() {
      return this.$store.getters.products;
    },
    isLoggedIn() {
      return this.$store.getters.isLoggedIn;
    }
  },
  methods: {
    getProduct() {
      this.$store.dispatch("getProducts", 1);
      //console.log(this.$store.getters.products);
      this.products = this.productsData.results;
      this.previousUrl = this.productsData.previous;
      this.nextUrl = this.productsData.next;
    }
  },
  created() {
    this.$store.dispatch("getProducts", 1);
    this.products = this.$store.getters.products.results;
    this.previousUrl = this.$store.getters.products.previous;
    this.nextUrl = this.$store.getters.products.next;
  }
};
</script>
