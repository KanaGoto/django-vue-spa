<template>
  <v-container>
    <v-container grid-list-lg>
      <v-layout column>
        <input v-model.number="budget" />円以下に絞り込む
        <input v-model.number="limit" /> 件に絞り込む
        <p>{{ matched.length }}件中、{{ limited.length }}件を表示中</p>
        <ul>
          <li v-for="item in limited" v-bind:key="item.id">
            {{ item.name }} {{ item.price }}円
          </li>
        </ul>
        <v-btn v-on:click="getBtnName()">{{ btnName }}</v-btn>
      </v-layout>
    </v-container>
  </v-container>
</template>

<!-- sort機能などloadash -->
<script src="https://cdn.jsdelivr.net/npm/lodash@4.17.11/lodash.min.js"></script>
<script>
import _ from "lodash";
/* eslint-disable */
export default {
  name: "test1",
  data() {
    return {
      //フォームの入力と紐づけられるデータ
      budget: 800,
      limit: 10,
      limit: 10,
      //商品リスト
      list: [
        { id: 1, name: "りんご", price: 100 },
        { id: 2, name: "バナナ", price: 90 },
        { id: 3, name: "梨", price: 160 },
        { id: 4, name: "みかん", price: 380 },
        { id: 5, name: "スイカ", price: 200 },
        { id: 6, name: "メロン", price: 500 },
        { id: 7, name: "イチゴ", price: 210 },
        { id: 8, name: "アボカド", price: 80 }
      ],
      order: "desc",
      btnName: "安い順"
    };
  },
  computed: {
    // あるbudget以下のリストを返す算出プロパティ
    matched: function() {
      return this.list.filter(function(el) {
        return el.price <= this.budget;
      }, this);
    },
    //上記と同様
    //   matched: function(){
    //       return this.list.filter(this.getMatched)
    //   },
    limited: function() {
      return this.sorted.slice(0, this.limit);
    },
    // ソート機能
    sorted: function() {
      return _.orderBy(this.matched, ["price"], [this.order]);
      //return _.orderBy(this.matched, "price", this.order ? "desc" : "asc");
    }
  },
  methods: {
    getMatched: function(val) {
      return val.price <= this.budget;
    },
    getBtnName: function() {
      if (this.order == "desc") {
        this.order = "asc";
        this.btnName = "高い順";
      } else {
        this.order = "desc";
        this.btnName = "安い順";
      }
    }
  }
};
</script>

<style scoped></style>
