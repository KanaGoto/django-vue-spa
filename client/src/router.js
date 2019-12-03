import Vue from "vue";
import Router from "vue-router";
import Home from "./views/Home.vue";
import store from "@/store.js";
import test from "./components/Test.vue";
import test1 from "./components/Test1.vue";
import test2 from "./components/Test2.vue";

import Login from "@/views/Login.vue";
import MyPage from "@/views/MyPage.vue";
import ProductList from "@/views/ProductList.vue";
import Product from "@/views/Product.vue";
import ReviewCreate from "@/views/ReviewCreate.vue";

Vue.use(Router);

const router = new Router({
  mode: "history",
  base: process.env.BASE_URL,
  routes: [
    {
      path: "/",
      name: "home",
      component: Home
    },
    {
      path: "/login",
      name: "login",
      component: Login
    },
    {
      path: "/mypage",
      name: "my-page-view",
      component: MyPage
    },
    {
      path: "/products",
      name: "product-list",
      component: ProductList
    },
    {
      path: "/product/:id",
      name: "product",
      component: Product,
      props: route => ({ id: Number(route.params.id) }),
      children: [
        {
          path: "/review", //親ルートと被らないパラメータを指定
          name: "reviews-create",
          props: route => ({ id: Number(route.params.id) }),
          component: ReviewCreate
        }
      ]
    },
    {
      path: "/about",
      name: "about",
      component: () => import("./views/About.vue")
      // meta: {
      //   authRequired: true
      // }
    },
    {
      path: "/menu",
      name: "menu",
      component: () => import("./views/Menu.vue")
    },
    {
      path: "/sign-in",
      name: "signin",
      component: () => import("./views/Signin.vue")
    },
    {
      path: "/join",
      name: "join",
      component: () => import("./views/Join.vue")
    },
    /* 以下テスト用 */
    {
      path: "/test",
      name: "test",
      component: test
    },
    {
      path: "/test1",
      name: "test1",
      component: test1
    },
    {
      path: "/test2",
      name: "test2",
      component: test2
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
