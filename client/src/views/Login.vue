<template>
  <div class="login">
    <v-alert :value="nonFieldErrors.length" type="error">
      <div v-for="error in nonFieldErrors" :key="error">{{ error }}</div>
    </v-alert>

    <h1>Login to Web App</h1>
    <v-form v-model="valid">
      <p>
        <v-text-field
          v-model="username"
          label="メールアドレス"
          :rules="usernameRules"
          required
        ></v-text-field>
      </p>
      <p>
        <v-text-field
          v-model="password"
          label="パスワード"
          :append-icon-cb="() => (showPassword = !showPassword)"
          :type="showPassword ? 'text' : 'password'"
          :rules="passwordRules"
          required
        ></v-text-field>
      </p>
      <p class="remember_me"></p>
      <p class="submit">
        <v-btn :disabled="!valid" @click="submit">ログイン</v-btn>
      </p>
    </v-form>
    <div class="login-help">
      <h3>Click here for <a href="/register">regisration</a>.</h3>
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
      usernameRules: [v => !!v || "ログインIDを入力してください"],
      passwordRules: [v => !!v || "パスワードを入力してください"]
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

    submit() {
      let self = this;
      this.nonFieldErrors = [];
      this.login([this.username, this.password]).then(
        /* eslint-disable */
        res => {
          if(this.isLoggedIn === true){
            //ユーザー情報取得
            this.getUserInfo().then(function(){
            //お気に入り商品名リスト取得
            self.getUserFavorites(self.$store.getters.userInfo.user_id);
            //カートアイテム取得
            self.getCartItems(self.$store.getters.userInfo.user_id);
            //購入履歴取得
            self.getOrderList(self.$store.getters.userInfo.user_id);
            self.$router.push("/mypage");
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
  padding: 20px 20px 20px;
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
  font-weight: bold;
  color: #555;
  text-align: center;
  text-shadow: 0 1px white;
  background: #f3f3f3;
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
  margin: 20px 0 0;
}

.login p:first-child {
  margin-top: 0;
}

.login input[type=text], .login input[type=password] {
  width: 278px;
}

.login p.remember_me {
  float: left;
  line-height: 31px;
}

.login p.remember_me label {
  font-size: 12px;
  color: #777;
  cursor: pointer;
}

.login p.remember_me input {
  position: relative;
  bottom: 1px;
  margin-right: 4px;
  vertical-align: middle;
}

.login p.submit {
  text-align: right;
}

.login-help {
  margin: 20px 0;
  font-size: 11px;
  color: white;
  text-align: center;
  text-shadow: 0 1px #2a85a1;
}

.login-help a {
  color: #cce7fa;
  text-decoration: none;
}

.login-help a:hover {
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
  border-color: #7dc9e2;
  outline-color: #dceefc;
  outline-offset: 0;
}

input[type=submit] {
  padding: 0 18px;
  height: 29px;
  font-size: 12px;
  font-weight: bold;
  color: #527881;
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
  background: #cde5ef;
  border-color: #9eb9c2 #b3c0c8 #b4ccce;
  -webkit-box-shadow: inset 0 0 3px rgba(0, 0, 0, 0.2);
  box-shadow: inset 0 0 3px rgba(0, 0, 0, 0.2);
}

.lt-ie9 input[type=text], .lt-ie9 input[type=password] {
  line-height: 34px;
}
body {
  font: 13px/20px "Lucida Grande", Tahoma, Verdana, sans-serif;
  color: #404040;
  background: #0ca3d2;
}
</style>