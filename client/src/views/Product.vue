<template>
  <div class="product">
    <h1>id. {{ id }}</h1>
    <p>商品名: {{ detail[0].name }}</p>
    <p>価格: {{ detail[0].shop_price }} 円</p>
    <nav class="nav">
      <router-link :to="{ name: 'review-detail' }">レビュー</router-link>
    </nav>
    <!-- ここに子ルートを埋め込む -->
    <router-view />
  </div>
</template>

<script>
export default {
  name: "product",
  data() {
    return {
      list: [],
      detail: []
    };
  },
  props: {
    id: Number
  },
  created() {
    this.list = this.$store.getters.products["results"];
    let self = this;
    this.detail = this.list.filter(function(i) {
      return i.id === self.id;
    });
  }
  // watch: {
  //   id: {
  //     handler() {
  //       this.$store.dispatch("product/load", this.id);
  //     },
  //     immediate: true
  //   }
  // },
  // beforeDestroy() {
  //   //親ルートを移動する際、データを破棄
  //   this.$store.dispatch("product/destroy");
  // }
};
</script>
