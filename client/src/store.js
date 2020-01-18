import Vue from "vue";
import Vuex from "vuex";
import client from "@/api/index.js";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    user: null,
    userInfo: null,
    isLoggedIn: false, //ログイン状態,
    addressInfo: null,
    products: null,
    userProducts: null,
    prodCategory: [],
    favorites: [],
    cartItems: [],
    cartItems_id: [],
    favorites_id: [],
    orderList: [],
    reviews: [],
    setIsReviewCreated: [],
    hedgehogs: [],
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
    setAddressInfo(state, payload) {
      state.addressInfo = payload;
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
    setUserFavorites(state, payload) {
      state.favorites = payload;
    },
    setCartItems(state, payload) {
      state.cartItems = payload;
    },
    setOrderList(state, payload) {
      state.orderList = payload;
    },
    setReviews(state, payload) {
      state.reviews = payload;
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
    setCartItem_id(state, payload) {
      state.cartItems_id = payload;
    },
    setFavorites_id(state, payload) {
      state.favorites_id = payload;
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
      return (
        client.auth
          .logout()
          .then(res => {
            commit("loggedIn", false);
            return res;
          })
          // eslint-disable-next-line
        .catch(e => {
            alert("ログアウト失敗");
          })
      );
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
    userUpdate({ commit }, userInfo) {
      return new Promise((resolve, reject) => {
        client.auth
          .userUpdate(userInfo)
          .then(res => {
            commit("setUserInfo", res.data);
            resolve(res.data);
          })
          .catch(err => {
            alert("会員情報更新失敗");
            reject(err);
          });
      });
    },
    getAddress({ commit }, user_id) {
      return new Promise((resolve, reject) => {
        client.auth
          .getAddress(user_id)
          .then(res => {
            commit("setAddressInfo", res.data);
            resolve(res.data);
          })
          .catch(err => {
            commit("setAddressInfo", []);
            alert("住所取得失敗");
            reject(err);
          });
      });
    },
    // eslint-disable-next-line
    createAddress({ commit }, addressInfo) {
      return new Promise((resolve, reject) => {
        client.auth
          .createAddress(addressInfo)
          .then(res => {
            resolve(res.data);
          })
          .catch(err => {
            alert("住所登録失敗");
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
            reject(err);
          });
      });
    },
    getUserProducts({ commit }, [pageNo, user_id]) {
      return new Promise((resolve, reject) => {
        client.products
          .findByUser(pageNo, user_id)
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
    // eslint-disable-next-line
    updateProduct({ commit }, [id, prodInfo]) {
      return new Promise((resolve, reject) => {
        client.products
          .update(id, prodInfo)
          .then(res => {
            resolve(res.data);
          })
          .catch(err => {
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
    getUserFavorites({ commit }, user_id) {
      return new Promise((resolve, reject) => {
        client.favorites
          .findByUser(user_id)
          .then(res => {
            commit("setUserFavorites", res.data);
            resolve(res.data);
          })
          .catch(err => {
            commit("setUserFavorites", []);
            alert("ユーザーのお気に入りリスト取得失敗");
            reject(err);
          });
      });
    },
    // eslint-disable-next-line
    addUserFavorites({ commit }, data) {
      return new Promise((resolve, reject) => {
        client.favorites
          .add(data)
          .then(res => {
            resolve(res.data);
          })
          .catch(err => {
            alert("お気に入り追加失敗");
            reject(err);
          });
      });
    },
    // eslint-disable-next-line
      deleteUserFavorites({ commit }, id) {
      return new Promise((resolve, reject) => {
        client.favorites
          .delete(id)
          .then(res => {
            resolve(res.data);
          })
          .catch(err => {
            alert("お気に入り削除失敗");
            reject(err);
          });
      });
    },
    getCartItems({ commit }, user_id) {
      return new Promise((resolve, reject) => {
        client.shopping
          .findByUser(user_id)
          .then(res => {
            commit("setCartItems", res.data);
            resolve(res.data);
          })
          .catch(err => {
            commit("setCartItems", []);
            alert("カート投入アイテム取得失敗");
            reject(err);
          });
      });
    },
    // eslint-disable-next-line
    addCartItems({ commit }, data) {
      return new Promise((resolve, reject) => {
        client.shopping
          .add(data)
          .then(res => {
            resolve(res.data);
          })
          .catch(err => {
            alert("カート投入失敗");
            reject(err);
          });
      });
    },
    updateCartItems({ commit }, [id, amount]) {
      return new Promise((resolve, reject) => {
        client.shopping
          .update(id, amount)
          .then(res => {
            commit("setCartItems", res.data);
            resolve(res.data);
          })
          .catch(err => {
            commit("setCartItems", []);
            alert("カート投入アイテム更新失敗");
            reject(err);
          });
      });
    },
    // eslint-disable-next-line
    deleteCartItems({ commit }, id) {
      return new Promise((resolve, reject) => {
        client.shopping
          .delete(id)
          .then(res => {
            resolve(res.data);
          })
          .catch(err => {
            alert("カートアイテム削除失敗");
            reject(err);
          });
      });
    },
    getOrderList({ commit }, user_id) {
      return new Promise((resolve, reject) => {
        client.shopping
          .orderList(user_id)
          .then(res => {
            commit("setOrderList", res.data);
            resolve(res.data);
          })
          .catch(err => {
            commit("setOrderList", []);
            alert("購入履歴取得失敗");
            reject(err);
          });
      });
    },
    // eslint-disable-next-line
    createOrder({ commit }, data) {
      return new Promise((resolve, reject) => {
        client.shopping
          .createOrder(data)
          .then(res => {
            resolve(res.data);
          })
          .catch(err => {
            alert("購入履歴作成失敗");
            reject(err);
          });
      });
    },
    // eslint-disable-next-line
      createOrderDetail({ commit }, data) {
      return new Promise((resolve, reject) => {
        client.shopping
          .createOrderDetail(data)
          .then(res => {
            resolve(res.data);
          })
          .catch(err => {
            alert("購入履歴詳細作成失敗");
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
    },
    setCartItems_id({ commit }, arr) {
      commit("setCartItem_id", arr);
    },
    setFavorites_id({ commit }, arr) {
      commit("setFavorites_id", arr);
    }
  },
  getters: {
    isLoggedIn: state => state.isLoggedIn,
    isAuthenticated(state) {
      return state.user !== null && state.user !== undefined;
    },
    userInfo: state => state.userInfo,
    addressInfo: state => state.addressInfo,
    products: state => state.products,
    userProducts: state => state.userProducts,
    prodCategory: state => state.prodCategory,
    favorites: state => state.favorites,
    cartItems: state => state.cartItems,
    reviews: state => state.reviews,
    cartItems_id: state => state.cartItems_id,
    favorites_id: state => state.favorites_id,
    orderList: state => state.orderList
  }
});
