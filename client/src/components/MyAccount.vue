<template>
  <div id="myAccount">
    <div class="members">
      <app-navbar>My Account</app-navbar>
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
            v-model="newUserInfo.username"
            :counter="20"
            :rules="nameRules"
            label="User Name"
            required
          ></v-text-field>
        </p>
        <p>
          <v-text-field
            v-model="newUserInfo.email"
            :rules="emailRules"
            label="Email"
            required
          ></v-text-field>
        </p>
        <p>
          <v-select
            v-model="newUserInfo.gender"
            :items="gender"
            :rules="[v => !!v || 'gender is required']"
            label="gender"
            item-text="label"
            item-value="value"
            required
          ></v-select>
        </p>
        <p>
          <v-textarea
            v-model="newUserInfo.profile"
            label="Profile"
            :rules="profileRules"
            rows="3"
          ></v-textarea>
        </p>
        <div class="submit">
          <v-spacer></v-spacer>
          <v-spacer></v-spacer>
          <v-btn
            color="warning"
            :disabled="!(isEdited && valid)"
            @click="submit()"
          >
            update
          </v-btn>
        </div>
      </v-form>
    </div>
    <!-- leftNavi -->
    <left-navi :isLoggedIn="isLoggedIn" :userInfo="userInfo"></left-navi>
  </div>
</template>
<script>
import { mapActions } from "vuex";
import LeftNavi from "./LeftNavi.vue";
import gender from "../static/gender.js";
export default {
  components: {
    LeftNavi: LeftNavi
  },
  name: "MyAccount",
  data() {
    return {
      valid: false,
      nonFieldErrors: [],
      nameRules: [
        v => !!v || "Name is required",
        v => (v && v.length <= 20) || "Name must be less than 20 characters"
      ],
      email: "",
      emailRules: [
        v => !!v || "E-mail is required",
        v => /.+@.+\..+/.test(v) || "E-mail must be valid"
      ],
      profileRules: [
        v =>
          (v && v.length <= 1000) || "Profile must be less than 1000 characters"
      ],
      gender: gender,
      lazy: false,
      newUserInfo: {
        username: null,
        email: null,
        gender: null,
        profile: null
      }
    };
  },
  created() {
    let self = this;
    this.getUserInfo().then(function(res) {
      self.newUserInfo.username = res.username;
      self.newUserInfo.email = res.email;
      self.newUserInfo.gender = res.gender;
      self.newUserInfo.profile = res.profile;
    });
  },
  computed: {
    isLoggedIn() {
      return this.$store.getters.isLoggedIn;
    },
    userInfo() {
      return this.$store.getters.userInfo;
    },
    isEdited() {
      if (
        this.newUserInfo.username !== this.userInfo.username ||
        this.newUserInfo.email !== this.userInfo.email ||
        this.newUserInfo.gender !== this.userInfo.gender ||
        this.newUserInfo.profile !== this.userInfo.profile
      ) {
        return true;
      }
      return false;
    }
  },
  methods: {
    ...mapActions(["getUserInfo"]),
    ...mapActions(["userUpdate"]),
    ...mapActions(["login"]),
    submit() {
      this.resetValidation();
      let self = this;
      this.nonFieldErrors = [];
      let data = new FormData();
      //更新されている項目だけ
      data = this.setPram(data);
      this.userUpdate(data).then(
        /* eslint-disable */
        res => {
          self.afterUpdate();
          alert("update completed");
        },
        err => {
          self.nonFieldErrors = this.getApiError(err.response.data);
        }
      );
    },
    setPram(data){
      //必須項目
      data.append("username", this.newUserInfo.username);
      data.append("email", this.newUserInfo.email);
      data.append("is_active", true);
    
      if(this.newUserInfo.gender !== this.userInfo.gender){
        data.append("gender", this.newUserInfo.gender);
      }
      if(this.newUserInfo.profile !== this.userInfo.profile){
        data.append("profile", this.newUserInfo.profile);
      }
      return data
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
      afterUpdate(){
        self = this;
        this.getUserInfo().then(function(){
          self.login([this.userInfo.email, this.userInfo.password])
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
