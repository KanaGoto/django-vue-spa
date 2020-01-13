<!--不使用-->
<template>
  <div class="product">
    <h1>id. {{ id }}</h1>
    <img :src="detail[0].goods_front_image" width="100" />
    <p>商品名: {{ detail[0].name }}</p>
    <p>価格: {{ detail[0].shop_price }} 円</p>
    <router-link
      v-bind:to="{ name: 'reviews-create', params: { id: id } }"
      tag="button"
    >
      レビュー投稿</router-link
    >
    <br />
    <!-- ここに子ルートを埋め込む -->
    <router-view />
    みんなのレビュー
    <ul>
      <li v-for="item in reviews" :key="item.id">
        <p>⭐️:{{ item.star }}</p>
        <p>タイトル:{{ item.title }}</p>
        <p>コメント:{{ item.comment }}</p>
        <p>ユーザ:{{ item.user }}</p>
      </li>
    </ul>
    <router-link to="/products" tag="button">商品一覧へ</router-link><br />
  </div>
</template>

<script>
export default {
  name: "product",
  data() {
    return {
      detail: [],
      list: [],
      reviews: []
    };
  },
  props: {
    id: Number
  },
  created() {
    this.getReviews(1);
    let self = this;
    this.detail = this.$store.getters.products["results"].filter(function(i) {
      return i.id === self.id;
    });
    this.reviews = this.$store.getters.reviews["results"].filter(function(el) {
      return el.prod === self.id;
    });
  },
  methods: {
    async getReviews(pageNo) {
      this.$store.dispatch("getReviews", pageNo);
    }
  }
};
</script>
