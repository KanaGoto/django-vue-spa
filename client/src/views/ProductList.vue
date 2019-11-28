<template>
  <div class="product-list">
    <h1>商品リスト</h1>
    <ul>
      <li v-for="{ id, name } in list" :key="id">
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
import products from "@/api/products.js";
export default {
  computed: {
    list: () => products.fetch()
  }
};
</script>
