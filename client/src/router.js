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
import PurchaseComp from "@/views/PurchaseComp.vue";

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
      name: "signin",
      component: Login
    },
    {
      path: "/logout",
      name: "signout",
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
      path: "/purchase/complete",
      name: "confirmPurchase",
      component: PurchaseComp
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
  ],
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) {
      return savedPosition;
    } else {
      return { x: 0, y: 0 };
    }
  }
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
