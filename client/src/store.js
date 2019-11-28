import Vue from "vue";
import Vuex from "vuex";
import client from "@/api/index.js";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    isLoggedIn: false, //ログイン状態
    hedgehogs: [],
    user: null,
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
    setHedgehogs(state, payload) {
      state.hedgehogs = payload;
    },
    setUser(state, payload) {
      state.user = payload;
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
            alert("成功");
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
    async getHedgehogs({ state, commit }, color) {
      try {
        // eslint-disable-next-line
        let response = await axios.get(
          `${state.apiUrl}hedgehogs/?color=` + color
        );
        commit("setHedgehogs", response.data);
      } catch (error) {
        commit("setHedgehogs", []);
      }
    }
    // userLogin({ commit }, { email, password }) {
    //   firebase
    //     .auth()
    //     .signInWithEmailAndPassword(email, password)
    //     .then(user => {
    //       commit("setUser", user);
    //       commit("setIsAuthenticated", true);
    //       router.push("/about");
    //     })
    //     .catch(() => {
    //       commit("setUser", null);
    //       commit("setIsAuthenticated", false);
    //       router.push("/");
    //     });
    // },
    // userJoin({ commit }, { email, password }) {
    //   firebase
    //     .auth()
    //     .createUserWithEmailAndPassword(email, password)
    //     .then(user => {
    //       commit("setUser", user);
    //       commit("setIsAuthenticated", true);
    //       router.push("/about");
    //     })
    //     .catch(() => {
    //       commit("setUser", null);
    //       commit("setIsAuthenticated", false);
    //       router.push("/");
    //     });
    // },
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
    // addFavolite({ state }, payload) {
    //   firebase
    //     .database()
    //     .ref("users")
    //     .child(state.user.user.uid)
    //     .push(payload.name);
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
    }
  }
});
