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

<style lang="scss">
* :not(.v-icon) {
  font-family: "Verdana", "メイリオ", sans-serif !important;
}
</style>
