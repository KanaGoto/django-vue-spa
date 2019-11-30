<template>
  <div class="product-list">
    <h1>商品リスト</h1>
    <ul>
      <li v-for="{ id, name } in initData.results" :key="id">
        <router-link v-bind:to="{ name: 'product', params: { id: id } }">{{
          name
        }}</router-link>
      </li>
    </ul>
    <nav><router-link to="/list" tag="button">list</router-link><br /></nav>
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
  methods: {}
};
</script>
