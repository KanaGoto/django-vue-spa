<template>
  <v-container>
    <v-container grid-list-lg>
      <v-layout column>
        <p v-bind:class="{ child: isChild, 'is-active': isActive }">Text</p>
        <p v-bind:syle="{ color: textColor, backgroundColor: bgColor }">
          Text
        </p>
        <input v-model="message" v-on:input="input" />
        <p>{{ message }}</p>
        <br />----<br />
        名前 <input v-model="name" /> 年齢 <input v-model="age" />
        <v-btn v-on:click="doAdd" color="brown lighten-3">
          うさちゃん追加</v-btn
        >
        <ul>
          <li v-for="(item, index) in list" v-bind:key="item.id">
            <label
              ><input type="checkbox" v-model="checkVal" v-value="item.id"
            /></label>
            ID.{{ item.id }} お名前 {{ item.name }} 年齢 {{ item.age }} HP
            {{ item.hp }}
            <v-btn v-on:click="doDelete(index)" color="brown lighten-3">
              買う
            </v-btn>
            <v-btn v-on:click="doAttack(index)" color="brown lighten-3">
              攻撃
            </v-btn>
            <span v-if="item.hp < 40">やばいよ</span>
          </li>
        </ul>
        <p>{{ checkVal }}</p>
        ご飯は何にする？
        <select v-model="selectVal" multiple>
          <option value="草">草</option>
          <option value="クッキー">クッキー</option>
          <option value="りんご">りんご</option>
        </select>
        <p>{{ selectVal }}</p>
        <div v-show="tmp">条件分岐</div>
        <div v-show="tmp">結果じゃじゃーーん</div>
        <v-btn v-on:click="change" color="brown lighten-3">押してみてな</v-btn>
        --画像ファイル
        <input type="file" v-on:change="handleChange" />
        <div v-if="preview"><img v-bind:src="preview" /></div>
      </v-layout>
    </v-container>
  </v-container>
</template>

<script>
/* eslint-disable */
export default {
  name: "test",
  data() {
    return {
      isChild: true,
      isActive: true,
      textColor: "red",
      bgColor: "lightgray",
      name: "うさちゃん",
      age: null,
      tmp: false,
      list:[
        {id: 1, name: "くろちゃん", age: 1, hp:100},
        {id: 2, name: "はなちゃん", age: 3, hp:100},
        {id: 3, name: "のんちゃん", age: 5, hp:100}
      ],
      message: "デフォルト",
      checkVal: [],
      selectVal: [],
      preview: ""
    };
  },
  methods:{
    doAdd: function(){
      var max = this.list.reduce(function(a,b){
        return a.id > b.id ? a.id : b.id 
      }, 0)
      this.list.push({
        id: max+1,
        name: this.name,
        age: this.age,
        hp: 100
      })
    },
    doDelete: function(index){
      console.log(index)
      this.list.splice(index,1)
    },
    doAttack: function(index){
      this.list[index].hp -= 20
    },
    change: function(){
      this.tmp = true
    },
    input:function(event){
      this.message = event.target.value
    },
    handleChange: function(event){
      var file = event.target.files[0]
      if(file && file.type.match(/^image\/(png|jpeg)$/)){
        this.preview = window.URL.createObjectURL(file)
      }
    }
  }
};
</script>

<style scoped></style>
