<template>
  <div id="app">
    <v-app>
      <div>
        <v-app-bar color="gray accent-4" dark>
          <v-app-bar-nav-icon></v-app-bar-nav-icon>

          <v-toolbar-title>びゅうてぃふぁい</v-toolbar-title>

          <div class="flex-grow-1"></div>

          <v-btn icon>
            <v-icon>mdi-heart</v-icon>
          </v-btn>

          <v-btn icon>
            <v-icon>mdi-magnify</v-icon>
          </v-btn>

          <v-menu left bottom>
            <template v-slot:activator="{ on }">
              <v-btn icon v-on="on">
                <v-icon>mdi-dots-vertical</v-icon>
              </v-btn>
            </template>

            <v-list>
              <v-list-item v-for="n in 5" :key="n" @click="() => {}">
                <v-list-item-title>りんく {{ n }}</v-list-item-title>
              </v-list-item>
            </v-list>
          </v-menu>
        </v-app-bar>
      </div>
      <v-content>
        <v-container>
          <!--本文内容-->
        </v-container>
      </v-content>
      <my-footer></my-footer>
    </v-app>
  </div>
</template>

<script>
import MyFooter from "@/components/Footer";
export default {
  name: "AppNavigation",
  components: {
    MyFooter
  },
  data() {
    return {
      appTitle: "HedgeHogs 🦔 ",
      drawer: false,
      items: [
        { title: "Menu" },
        { title: "Profile" },
        { title: "Sign In" },
        { title: "Join" }
      ]
    };
  },
  computed: {
    isAuthenticated() {
      return this.$store.getters.isAuthenticated;
    }
  },
  methods: {
    logout() {
      this.$store.dispatch("userSignOut");
    }
  }
};
</script>

<style scoped>
a {
  color: white;
  text-decoration: none;
}
.router-link-exact-active {
  color: white;
  text-decoration: none;
}
.v-toolbar__title {
  color: white;
  text-decoration: none;
}
</style>
