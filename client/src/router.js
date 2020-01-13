import Vue from "vue";
import Router from "vue-router";
import store from "@/store.js";
import Register from "@/views/Register.vue";
import Login from "@/views/Login.vue";
import Logout from "@/views/Logout.vue";
import MyPage from "@/views/MyPage.vue";
import ConfirmPurchase from "@/views/ConfirmPurchase.vue";
import History from "@/views/History.vue";
import MyAccount from "@/views/MyAccount.vue";

Vue.use(Router);

const router = new Router({
  mode: "history",
  base: process.env.BASE_URL,
  routes: [
    {
      path: "/register",
      name: "register",
      component: Register
    },
    {
      path: "/login",
      name: "login",
      component: Login
    },
    {
      path: "/logout",
      name: "logout",
      component: Logout
    },
    {
      path: "/",
      name: "mypage",
      component: MyPage
    },
    {
      path: "/purchase",
      name: "confirmPurchase",
      component: ConfirmPurchase
    },
    {
      path: "/orders",
      name: "history",
      component: History
    },
    {
      path: "/account",
      name: "account",
      component: MyAccount
    },
    {
      path: "/about",
      name: "about",
      component: () => import("./views/About.vue")
    }
  ]
});

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.authRequired)) {
    if (!store.state.isAuthenticated) {
      next({
        path: "/sign-in"
      });
    } else {
      next();
    }
  } else {
    next();
  }
});

export default router;
