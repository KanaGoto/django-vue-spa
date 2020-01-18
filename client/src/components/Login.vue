<template>
  <div class="login">
    <v-alert :value="nonFieldErrors.length" type="error">
      <div v-for="error in nonFieldErrors" :key="error">{{ error }}</div>
    </v-alert>

    <h1>Sign In to Web App</h1>
    <v-form v-model="valid">
      <p>
        <v-text-field
          v-model="username"
          label="e-mail"
          :rules="emailRules"
          required
        ></v-text-field>
      </p>
      <p>
        <v-text-field
          v-model="password"
          label="password"
          :append-icon-cb="() => (showPassword = !showPassword)"
          :type="showPassword ? 'text' : 'password'"
          :rules="passwordRules"
          required
        ></v-text-field>
      </p>
      <p class="submit">
        <v-btn :disabled="!valid" @click="submit">Sign In</v-btn>
      </p>
    </v-form>
    <div class="login-help">
      <p>Click here for <a href="/register">regisration</a></p>
    </div>
  </div>
</template>

<script>
import { mapActions } from "vuex";

export default {
  name: "Login",
  data() {
    return {
      valid: false,
      username: null,
      password: null,
      showPassword: false,
      nonFieldErrors: [],
      emailRules: [v => !!v || "e-mail is required"],
      passwordRules: [v => !!v || "password is required"]
    };
  },
  computed: {
    isLoggedIn() {
      return this.$store.getters.isLoggedIn;
    }
  },
  methods: {
    ...mapActions(["login"]),
    ...mapActions(["getUserInfo"]),
    ...mapActions(["getUserFavorites"]),
    ...mapActions(["getCartItems"]),
    ...mapActions(["getOrderList"]),
    ...mapActions(["getProducts"]),
    ...mapActions(["getUserProducts"]),

    submit() {
      let self = this;
      this.nonFieldErrors = [];
      this.login([this.username, this.password]).then(
        /* eslint-disable */
        res => {
          if(this.isLoggedIn === true){
            //ユーザー情報取得
            this.getUserInfo().then(function(){
            //商品一覧取得
            self.getProducts(1);
            //お気に入り商品名リスト取得
            self.getUserFavorites(self.$store.getters.userInfo.user_id);
            //カートアイテム取得
            self.getCartItems(self.$store.getters.userInfo.user_id);
            //購入履歴取得
            self.getOrderList(self.$store.getters.userInfo.user_id);
            //ユーザー商品取得
            self.getUserProducts([1,self.$store.getters.userInfo.user_id]);
            self.$router.push("/");
            })
          }
        },
        err => {
          this.nonFieldErrors = err.response.data.nonFieldErrors;
        }
      );
    }
  }
};
</script>

<style scoped>
.login {
  position: relative;
  margin: 30px auto;
  padding: 20px 20px;
  width: 310px;
  background: white;
  border-radius: 3px;
  -webkit-box-shadow: 0 0 200px rgba(255, 255, 255, 0.5), 0 1px 2px rgba(0, 0, 0, 0.3);
  box-shadow: 0 0 200px rgba(255, 255, 255, 0.5), 0 1px 2px rgba(0, 0, 0, 0.3);
}

.login:before {
  content: '';
  position: absolute;
  top: -8px;
  right: -8px;
  bottom: -8px;
  left: -8px;
  z-index: -1;
  background: rgba(0, 0, 0, 0.08);
  border-radius: 4px;
}

.login h1 {
  margin: -20px -20px 21px;
  line-height: 40px;
  font-size: 15px;
  color: white;
  text-align: center;
  background: rgba(2, 107, 63, 0.521);
  border-bottom: 1px solid #cfcfcf;
  border-radius: 3px 3px 0 0;
  background-image: -webkit-linear-gradient(top, whiteffd, #eef2f5);
  background-image: -moz-linear-gradient(top, whiteffd, #eef2f5);
  background-image: -o-linear-gradient(top, whiteffd, #eef2f5);
  background-image: linear-gradient(to bottom, whiteffd, #eef2f5);
  -webkit-box-shadow: 0 1px whitesmoke;
  box-shadow: 0 1px whitesmoke;
}

.login p {
  margin-top: 20px;
}

.login p:first-child {
  margin-top: 0;
}

.login input[type=text], .login input[type=password] {
  width: 278px;
}

.login p.submit {
  text-align: right;
  color: white;
  margin:0px 0px 15px;
}

.login-help {
  margin: 20px 0;
  font-size: 14px;
  text-align: center;
}
.login-help a {
  color: #101111;
  text-decoration: underline;
}

.login-help a:hover {
  color: #0f80ade7;
  text-decoration: underline;
}

:-moz-placeholder {
  color: #c9c9c9 !important;
  font-size: 13px;
}

input {
  font-family: 'Lucida Grande', Tahoma, Verdana, sans-serif;
  font-size: 14px;
}

input[type=text], input[type=password] {
  margin: 5px;
  padding: 0 10px;
  width: 200px;
  height: 34px;
  color: #404040;
  background: white;
  border: 1px solid;
  border-color: #c4c4c4 #d1d1d1 #d4d4d4;
  border-radius: 2px;
  outline: 5px solid #eff4f7;
  -moz-outline-radius: 3px;
  -webkit-box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.12);
  box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.12);
}

input[type=text]:focus, input[type=password]:focus {
  border-color: #88eccbbb;
  outline-color: #dceefc;
  outline-offset: 0;
}

input[type=submit] {
  padding: 0 18px;
  height: 29px;
  font-size: 12px;
  font-weight: bold;
  color: white;
  text-shadow: 0 1px #e3f1f1;
  background: #cde5ef;
  border: 1px solid;
  border-color: #b4ccce #b3c0c8 #9eb9c2;
  border-radius: 16px;
  outline: 0;
  -webkit-box-sizing: content-box;
  -moz-box-sizing: content-box;
  box-sizing: content-box;
  background-image: -webkit-linear-gradient(top, #edf5f8, #cde5ef);
  background-image: -moz-linear-gradient(top, #edf5f8, #cde5ef);
  background-image: -o-linear-gradient(top, #edf5f8, #cde5ef);
  background-image: linear-gradient(to bottom, #edf5f8, #cde5ef);
  -webkit-box-shadow: inset 0 1px white, 0 1px 2px rgba(0, 0, 0, 0.15);
  box-shadow: inset 0 1px white, 0 1px 2px rgba(0, 0, 0, 0.15);
}

input[type=submit]:active {
  background: #086d99;
  -webkit-box-shadow: inset 0 0 3px rgba(0, 0, 0, 0.2);
  box-shadow: inset 0 0 3px rgba(0, 0, 0, 0.2);
}

.lt-ie9 input[type=text], .lt-ie9 input[type=password] {
  line-height: 34px;
}

.background {
  background-size: 30px 30px;
  margin: 0 auto;
  background-color: #00A0E9;
  background-image: radial-gradient(#ffffb1 15%, transparent 20%),
                    radial-gradient(#ffffb1 15%, transparent 20%);
  background-position: 0 0, 15px 15px;
}
</style>