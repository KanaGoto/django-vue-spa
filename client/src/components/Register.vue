<template>
  <div class="members">
    <app-navbar>members regisration</app-navbar>
    <v-container fill-height>
      <v-layout row wrap align-center>
        <v-layout>
          <v-row align="center">
            <v-form ref="form" v-model="valid" :lazy-validation="lazy">
              <p>
                <v-text-field
                  v-model="name"
                  :counter="10"
                  :rules="nameRules"
                  label="User Name"
                  required
                ></v-text-field>
              </p>
              <p>
                <v-text-field
                  v-model="email"
                  :rules="emailRules"
                  label="Email"
                  required
                ></v-text-field>
              </p>
              <p>
                <v-select
                  v-model="select"
                  :items="gender"
                  :rules="[v => !!v || 'Item is required']"
                  label="gender"
                  required
                ></v-select>
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
              <p>
                <v-textarea label="Profile" rows="2"></v-textarea>
              </p>
              <v-checkbox
                v-model="checkbox"
                :rules="[v => !!v || 'You must agree to continue!']"
                label="Do you agree with xxxx?"
                required
              ></v-checkbox>

              <v-btn color="error" class="mr-4" @click="reset">
                Go Back
              </v-btn>
              <span class="submit">
                <v-btn color="warning" @click="resetValidation">
                  complete registration
                </v-btn>
              </span>
            </v-form>
          </v-row>
        </v-layout>
      </v-layout>
    </v-container>
  </div>
</template>
<script>
import { mapActions } from "vuex";

export default {
  name: "Login",
  data() {
    return {
      username: null,
      password: null,
      showPassword: false,
      nonFieldErrors: [],
      usernameRules: [v => !!v || "ログインIDを入力してください"],
      passwordRules: [v => !!v || "パスワードを入力してください"],
      valid: true,
      name: "",
      nameRules: [
        v => !!v || "Name is required",
        v => (v && v.length <= 10) || "Name must be less than 10 characters"
      ],
      email: "",
      emailRules: [
        v => !!v || "E-mail is required",
        v => /.+@.+\..+/.test(v) || "E-mail must be valid"
      ],
      select: null,
      gender: ["female", "male", "don't ask"],
      checkbox: false,
      lazy: false
    };
  },
  computed: {
    isLoggedIn() {
      return this.$store.getters.isLoggedIn;
    }
  },
  methods: {
    ...mapActions(["login"]),
    submit() {
      let self = this;
      this.nonFieldErrors = [];
      this.login([this.username, this.password]).then(
        /* eslint-disable */
        res => {
          if(this.isLoggedIn === true){
            alert("ok");
            self.$router.push("/mypage");
          }
        },
        err => {
          this.nonFieldErrors = err.response.data.nonFieldErrors;
        }
      );
    },
    validate () {
        if (this.$refs.form.validate()) {
          this.snackbar = true
        }
      },
      reset () {
        this.$refs.form.reset()
      },
      resetValidation () {
        this.$refs.form.resetValidation()
      },
  }
};
</script>

<style scoped>
.members {
  position: relative;
  margin: 30px auto;
  padding: 20px 20px 20px;
  width: 450px;
  background: white;
  border-radius: 3px;
  -webkit-box-shadow: 0 0 200px rgba(255, 255, 255, 0.5), 0 1px 2px rgba(0, 0, 0, 0.3);
  box-shadow: 0 0 200px rgba(255, 255, 255, 0.5), 0 1px 2px rgba(0, 0, 0, 0.3);
}

.submit {
  text-align: right;
}

</style>
