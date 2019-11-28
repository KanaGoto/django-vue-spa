import Vue from "vue";
import App from "./App";
import router from "./router";
import store from "./store";
import vuetify from "./plugins/vuetify";
//import api from "./api";

//Vue.config.productionTip = false;

//Vue.use(api);

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount("#app");
