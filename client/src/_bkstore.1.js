import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";
//import router from "@/router";

Vue.use(Vuex);

const itemModule = {
  state: {
    hedgehogs: [],
    apiUrl: "http://127.0.0.1:51310/api/",
    user: null,
    isAuthenticated: false,
    userFavolites: []
  },
  mutations: {
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
    }
  },
  actions: {
    async getHedgehogs({ state, commit }, color) {
      try {
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
    //       commit('setUser', user);
    //       commit('setIsAuthenticated', true);
    //       router.push('/about');
    //     })
    //     .catch(() => {
    //       commit('setUser', null);
    //       commit('setIsAuthenticated', false);
    //       router.push('/');
    //     });
    // },
    //   userJoin({ commit }, { email, password }) {
    //     firebase
    //       .auth()
    //       .createUserWithEmailAndPassword(email, password)
    //       .then(user => {
    //         commit('setUser', user);
    //         commit('setIsAuthenticated', true);
    //         router.push('/about');
    //       })
    //       .catch(() => {
    //         commit('setUser', null);
    //         commit('setIsAuthenticated', false);
    //         router.push('/');
    //       });
    //   },
    //   userSignOut({ commit }) {
    //     firebase
    //       .auth()
    //       .signOut()
    //       .then(() => {
    //         commit('setUser', null);
    //         commit('setIsAuthenticated', false);
    //         router.push('/');
    //       })
    //       .catch(() => {
    //         commit('setUser', null);
    //         commit('setIsAuthenticated', false);
    //         router.push('/');
    //       });
    //   },
    //   addFavolite({ state }, payload) {
    //     firebase
    //       .database()
    //       .ref('users')
    //       .child(state.user.user.uid)
    //       .push(payload.name);
    //   },
    //   getUserFavolites({ state, commit }) {
    //     return firebase
    //       .database()
    //       .ref('users/' + state.user.user.uid)
    //       .once('value', snapshot => {
    //         commit('setUserFavolites', snapshot.val());
    //       });
    //   }
  },
  getters: {
    isAuthenticated(state) {
      return state.user !== null && state.user !== undefined;
    }
  }
};
const testModule = {
  state: {
    message: "初期メッセージ"
  },
  mutations: {
    setMessage(state, payload) {
      state.message = payload.message;
    },
    setHedgehogs(state, payload) {
      state.hedgehogs = payload;
    }
  },
  actions: {
    /* ▼ 追加 ▼ */
    doUpdate({ commit }, message) {
      commit("setMessage", { message });
    }
  },
  getters: {
    getMessage(state) {
      return state.message;
    }
  }
};
export default new Vuex.Store({
  modules: {
    itemModule,
    testModule
  }
});
