<template>
  <v-app>
    <v-content transition="slide-x-transition">
      <router-view></router-view>
    </v-content>
  </v-app>
</template>

<script>
export default {
  name: "App"
};
</script>

<style>
* :not(.v-icon) {
  font-family: "Verdana", "メイリオ", sans-serif !important;
}
body {
  margin: 0 auto;
  background-color: #00a0e9;
  background-image: radial-gradient(#ffffb1 15%, transparent 20%),
    radial-gradient(#ffffb1 15%, transparent 20%);
  background-position: 0 0, 15px 15px;
}
</style>
