<template>
  <div class="members">
    <app-navbar>Members Registration</app-navbar>
    <v-alert :value="nonFieldErrors.length" type="error">
      <div v-for="error in nonFieldErrors" :key="error">
        <h5>
          {{ error }}
        </h5>
      </div>
    </v-alert>
    <v-form ref="form" v-model="valid" :lazy-validation="lazy">
      <p>
        <v-text-field
          v-model="userInfo.username"
          :counter="20"
          :rules="nameRules"
          label="User Name"
          required
        ></v-text-field>
      </p>
      <p>
        <v-text-field
          v-model="userInfo.email"
          :rules="emailRules"
          label="Email"
          required
        ></v-text-field>
      </p>
      <p>
        <v-select
          v-model="select"
          :items="gender"
          :rules="[v => !!v || 'gender is required']"
          label="gender"
          required
        ></v-select>
      </p>
      <p>
        <v-text-field
          v-model="userInfo.password"
          label="password"
          :append-icon-cb="() => (showPassword = !showPassword)"
          :type="showPassword ? 'text' : 'password'"
          :rules="passwordRules"
          required
        ></v-text-field>
      </p>
      <p>
        <v-textarea label="Profile" rows="3"></v-textarea>
      </p>
      <div class="submit">
        <v-spacer></v-spacer>
        <v-spacer></v-spacer>
        <v-checkbox
          v-model="checkbox"
          :rules="[v => !!v || 'You must agree to continue!']"
          label="agree with our membership"
          required
        ></v-checkbox>
        <v-btn color="warning" :disabled="!valid" @click="submit()">
          complete
        </v-btn>
      </div>
    </v-form>
  </div>
</template>
<script>
import { mapActions } from "vuex";
export default {
  name: "Login",
  data() {
    return {
      valid: false,
      userInfo: {
        username: null,
        password: null,
        email: "",
        is_active: true
      },
      showPassword: false,
      nonFieldErrors: [],
      usernameRules: [v => !!v || "your name is required"],
      passwordRules: [v => !!v || "password is required"],
      nameRules: [
        v => !!v || "Name is required",
        v => (v && v.length <= 20) || "Name must be less than 20 characters"
      ],
      email: "",
      emailRules: [
        v => !!v || "E-mail is required",
        v => /.+@.+\..+/.test(v) || "E-mail must be valid"
      ],
      select: null,
      gender: ["female", "male", "secret"],
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
    ...mapActions(["userRegister"]),
    ...mapActions(["login"]),
    submit() {
      this.resetValidation();
      let self = this;
      this.nonFieldErrors = [];
      this.userRegister(this.userInfo).then(
        /* eslint-disable */
        res => {
          this.afterRegist()
        },
        err => {
          self.nonFieldErrors = this.getApiError(err.response.data);
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
      afterRegist(){
        self = this;
        this.login([this.userInfo.email, this.userInfo.password]).then(
          res => {
            if(self.isLoggedIn === true){
              self.$router.push("/mypage");
            }
          },
          err => {
            self.nonFieldErrors = err.response.data.nonFieldErrors;
          })
      },
      getApiError(obj){
        return Object.keys(obj).map(function (key) { return obj[key][0]; })
      }
  }
};
</script>

<style scoped>
.members {
  position: relative;
  text-align: center;
  margin: 30px auto;
  padding: 20px 50px 20px;
  width: 500px;
  background: white;
  border-radius: 3px;
  -webkit-box-shadow: 0 0 200px rgba(255, 255, 255, 0.5), 0 1px 2px rgba(0, 0, 0, 0.3);
  box-shadow: 0 0 200px rgba(255, 255, 255, 0.5), 0 1px 2px rgba(0, 0, 0, 0.3);
}

.submit {
  text-align: right;
}

</style>
