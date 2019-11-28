<template>
  <v-container>
    <v-container grid-list-lg>
      <v-layout column>
        <p>--- storeの値を更新 --------</p>
        {{ message }} ←getterで取得<br />
        {{ stored }} ←直接参照
        <Test3EditForm />
        <br />
        <p>--- bakend --------</p>
        <button v-on:click="callApi">API呼ぶ</button>
        <br />
        <p>--- API取得 --------</p>
        <select v-model="current">
          <option
            v-for="topic in topics"
            v-bind:value="topic.value"
            v-bind:key="topic.id"
          >
            {{ topic.name }}
          </option>
        </select>
        <div v-for="item in list" v-bind:key="item.id">
          {{ item.full_name }}
        </div>
      </v-layout>
    </v-container>
  </v-container>
</template>

<!-- sort機能などloadash -->
<script src="https://cdn.jsdelivr.net/npm/lodash@4.17.11/lodash.min.js"></script>
<script>
import _ from "lodash";
import Test3EditForm from "@/components/Test3EditForm.vue";
import axios from "axios";
export default {
  name: "test2",
  components: { Test3EditForm },
  data() {
    return {
      list: [],
      current: "",
      topics: [
        { id: 1, value: "vue", name: "vue.js" },
        { id: 2, value: "jQuery", name: "jQuery" },
        { id: 3, value: "Django", name: "Django " }
      ],
      //stored: this.$store.state.testModule.message
      stored: this.$store.state.message
    };
  },
  watch: {
    current: function(val) {
      //GithubのAPIからトピックのリポジトリを検索;
      axios
        .get("https://api.github.com/search/repositories", {
          params: { q: "topic:" + val }
        })
        .then(
          function(response) {
            console.log(response.data.items);
            this.list = response.data.items;
          }.bind(this)
        );
    }
  },
  computed: {
    //storeの値は、一般的にcomputedでキャッシュさせて取得
    message() {
      return this.$store.getters.getMessage;
    },
    hello() {
      //getterの場合storeのモジュール名は書かなくて良い？
      return this.$store.getters.isAuthenticated;
    }
  }
};
</script>

<style scoped></style>
