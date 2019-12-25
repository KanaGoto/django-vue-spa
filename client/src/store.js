import Vue from "vue";
import Vuex from "vuex";
import client from "@/api/index.js";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    isLoggedIn: false, //ログイン状態,
    products: null,
    userProducts: null,
    prodCategory: [],
    reviews: [],
    setIsReviewCreated: [],
    hedgehogs: [],
    user: null,
    userInfo: null,
    isAuthenticated: false,
    userFavolites: [],
    message: "初期メッセージ"
  },
  mutations: {
    loggedIn(state, token) {
      state.isLoggedIn = true;
      client.defaults.headers.common["Authorization"] = `JWT ${token}`;
      localStorage.setItem("token", token);
    },
    loggedOut(state) {
      state.isLoggedIn = false;
      delete client.defaults.headers.common["Authorization"];
      localStorage.clear();
    },
    setProducts(state, payload) {
      state.products = payload;
    },
    setUserProducts(state, payload) {
      state.userProducts = payload;
    },
    setProdCategory(state, payload) {
      state.prodCategory = payload;
    },
    setReviews(state, payload) {
      state.reviews = payload;
    },
    setHedgehogs(state, payload) {
      state.hedgehogs = payload;
    },
    setUser(state, payload) {
      state.user = payload;
    },
    setUserInfo(state, payload) {
      state.userInfo = payload;
    },
    setIsAuthenticated(state, payload) {
      state.isAuthenticated = payload;
    },
    setUserFavolites(state, payload) {
      state.userFavolites = payload;
    },
    setMessage(state, payload) {
      state.message = payload.message;
    }
  },
  actions: {
    login({ commit }, [username, password]) {
      return (
        client.auth
          .login(username, password)
          .then(res => {
            commit("loggedIn", res.data.token);
            return res;
          })
          // eslint-disable-next-line
        .catch(e => {
            alert("ログイン失敗");
          })
      );
    },
    logout({ commit }) {
      commit("loggedOut");
    },
    tryLoggedIn({ commit }) {
      const token = localStorage.getItem("token");
      if (token) {
        client.auth.verify(token).then(
          () => {
            commit("loggedIn", token);
          },
          () => {
            // 不正なtoken
            localStorage.clear();
          }
        );
      }
    },
    userRegister({ commit }, userInfo) {
      return new Promise((resolve, reject) => {
        client.auth
          .userRegister(userInfo)
          .then(res => {
            // eslint-disable-next-line
            console.log(res.data);
            commit("setUserInfo", res.data);
            resolve(res.data);
          })
          .catch(err => {
            commit("setUserInfo", []);
            alert("会員登録失敗");
            reject(err);
          });
      });
    },
    getUserInfo({ commit }) {
      return new Promise((resolve, reject) => {
        client.auth
          .getUserInfo()
          .then(res => {
            commit("setUserInfo", res.data);
            resolve(res.data);
          })
          .catch(err => {
            commit("setUserInfo", []);
            alert("会員情報取得失敗");
            reject(err);
          });
      });
    },
    getProducts({ commit }, pageNo) {
      return new Promise((resolve, reject) => {
        client.products
          .findAll(pageNo)
          .then(res => {
            commit("setProducts", res.data);
            resolve(res.data);
          })
          .catch(err => {
            commit("setProducts", []);
            alert("プロダクト取得失敗");
            reject(err);
          });
      });
    },
    // eslint-disable-next-line
    createProduct({ commit }, prodInfo) {
      return new Promise((resolve, reject) => {
        client.products
          .create(prodInfo)
          .then(res => {
            resolve(res.data);
          })
          .catch(err => {
            alert("プロダクト登録失敗");
            alert(err);
            reject(err);
          });
      });
    },
    getUserProducts({ commit }, user_id) {
      return new Promise((resolve, reject) => {
        client.products
          .findByUser(user_id)
          .then(res => {
            commit("setUserProducts", res.data);
            resolve(res.data);
          })
          .catch(err => {
            commit("setProducts", []);
            alert("ユーザーのプロダクト取得失敗");
            reject(err);
          });
      });
    },
    getCategory({ commit }) {
      return new Promise((resolve, reject) => {
        client.products
          .category()
          .then(res => {
            commit("setProdCategory", res.data);
            resolve(res.data);
          })
          .catch(err => {
            alert("プロダクトカテゴリー取得失敗");
            reject(err);
          });
      });
    },
    createReview({ commit }, [star, title, comment, prod, user]) {
      return (
        client.reviews
          .create(star, title, comment, prod, user)
          .then(res => {
            commit("setIsReviewCreated", res.data);
            return res.data;
          })
          // eslint-disable-next-line
        .catch(e => {
            alert("レビュー投稿失敗");
          })
      );
    },
    getReviews({ commit }, pageNo) {
      return (
        client.reviews
          .findAll(pageNo)
          .then(res => {
            // eslint-disable-next-line
            console.log(res.data);
            commit("setReviews", res.data);
            return res.data;
          })
          // eslint-disable-next-line
        .catch(e => {
            commit("setReviews", []);
            alert("レビュー一覧取得失敗");
          })
      );
    }
    // userSignOut({ commit }) {
    //   firebase
    //     .auth()
    //     .signOut()
    //     .then(() => {
    //       commit("setUser", null);
    //       commit("setIsAuthenticated", false);
    //       router.push("/");
    //     })
    //     .catch(() => {
    //       commit("setUser", null);
    //       commit("setIsAuthenticated", false);
    //       router.push("/");
    //     });
    // },
    // getUserFavolites({ state, commit }) {
    //   return firebase
    //     .database()
    //     .ref("users/" + state.user.user.uid)
    //     .once("value", snapshot => {
    //       commit("setUserFavolites", snapshot.val());
    //     });
  },
  getters: {
    isLoggedIn: state => state.isLoggedIn,
    isAuthenticated(state) {
      return state.user !== null && state.user !== undefined;
    },
    doUpdate({ commit }, message) {
      commit("setMessage", { message });
    },
    getMessage(state) {
      return state.message;
    },
    userInfo: state => state.userInfo,
    products: state => state.products,
    userProducts: state => state.userProducts,
    prodCategory: state => state.prodCategory,
    reviews: state => state.reviews
  }
});
