<template>
  <div class="product-list">
    <h1>商品リスト</h1>
    <ul>
      <li v-for="{ id, name } in products" :key="id">
        <router-link :to="'/product/${id}'">{{ name }}</router-link>
      </li>
    </ul>
    <button v-on:click="getProduct">GET</button>
    <p>pro: {{ productsData }}</p>
    <p>ligin: {{ isLoggedIn }}</p>
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
      products: null
    };
  },
  computed: {
    productsData() {
      return this.$store.getters.products;
    },
    isLoggedIn() {
      return this.$store.getters.isLoggedIn;
    }
  }
  // methods: {
  //   getProduct() {
  //     this.$store.dispatch("getProducts", 1);
  //     //console.log(this.$store.getters.products);
  //     this.products = this.productsData.results;
  //     this.previousUrl = this.productsData.previous;
  //     this.nextUrl = this.productsData.next;
  //   }
  // },
  // created: {
  //   getProducts() {
  //     this.$store.dispatch("getProducts", 1);
  //     this.products = this.productsData.results;
  //     this.previousUrl = this.productsData.previous;
  //     this.nextUrl = this.productsData.next;
  //   }
  // }
};
</script>
