import Vue from "vue";
import App from "./App";
import router from "./router";
import store from "./store";
import vuetify from "./plugins/vuetify";
import VueScrollTo from "vue-scrollto";

Vue.use(VueScrollTo);

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount("#app");
