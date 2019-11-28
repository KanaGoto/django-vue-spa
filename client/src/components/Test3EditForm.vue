<template>
  <div class="test3-edit-form">
    <input ref="input" :value="message2" @input="doUpdate" />
  </div>
</template>

<script>
export default {
  name: "Test3EditForm",
  data() {
    return {
      list: [],
      current: ""
    };
  },
  computed: {
    //storeの値は、一般的にcomputedでキャッシュさせて取得
    message2() {
      return this.$store.getters.getMessage;
    }
  },
  methods: {
    doUpdate() {
      // inputに入力された値を使ってdispatch!
      this.$store.dispatch("doUpdate", this.$refs.input.value);
    }
  }
};
</script>

<style scoped></style>
