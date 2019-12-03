<template>
  <div class="review-create">
    <v-form v-model="valid">
      <v-text-field
        v-model="star"
        label="星"
        :rules="starRules"
        required
      ></v-text-field>
      <v-text-field
        v-model="title"
        label="タイトル"
        :rules="titleRules"
        required
      ></v-text-field>
      <v-text-field
        v-model="star"
        label="コメント"
        :rules="commentRules"
        required
      ></v-text-field>
      <v-btn :disabled="!valid" @click="submit">投稿する</v-btn>
    </v-form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      nextUrl: null,
      previousUrl: null,
      list: [],
      star: null,
      title: null,
      comment: null,
      user: null,
      prod: this.id
    };
  },
  props: {
    id: Number
  },
  created() {
    this.getReviews(1);
    let self = this;
    this.list = this.$store.getters.reviews["results"].filter(function(el) {
      return el.prod === self.id;
    });
  },
  computed: {
    initData() {
      return this.$store.getters.reviews["results"].filter(function(el) {
        return el.prod === self.prodId;
      });
    },
    isLoggedIn() {
      return this.$store.getters.isLoggedIn;
    }
  },
  methods: {
    async getReviews(pageNo) {
      this.$store.dispatch("getReviews", pageNo);
    }
  }
};
</script>
