<template>
  <div id="myAccount">
    <v-container>
      <div class="members">
        <app-navbar>My Account</app-navbar>
        <br />
        <v-alert :value="nonFieldErrors.length" type="error">
          <div v-for="error in nonFieldErrors" :key="error">
            <h5>
              {{ error }}
            </h5>
          </div>
        </v-alert>
        <v-form ref="form" v-model="valid" :lazy-validation="lazy">
          <p>
            <img v-if="uploadImageUrl" :src="uploadImageUrl" width="100" />
            <v-file-input
              accept="image/*"
              show-size
              label="image"
              prepend-icon="mdi-image"
              @change="onImagePicked"
            ></v-file-input>
          </p>
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
    </v-container>
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
      uploadImageUrl: "",
      gender: gender,
      lazy: false,
      newUserInfo: {
        username: null,
        image: null,
        email: null,
        gender: null,
        profile: null
      }
    };
  },
  created() {
    this.reSetUserData();
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
        this.newUserInfo.image !== this.userInfo.image ||
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
      if(this.newUserInfo.image !== this.userInfo.image){
        data.append('image', this.newUserInfo.image);
      }
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
      reSetUserData(){
        let self = this;
        this.getUserInfo().then(function(res) {
          self.newUserInfo.username = res.username;
          self.newUserInfo.image = res.image;
          if (res.image != "") {
            self.uploadImageUrl = "http://localhost:8000" + res.image;
          }
          self.newUserInfo.email = res.email;
          self.newUserInfo.gender = res.gender;
          self.newUserInfo.profile = res.profile;
        });
      },
      afterUpdate(){
        this.reSetUserData();
      },
      getApiError(obj){
        return Object.keys(obj).map(function (key) { return obj[key][0]; })
      },
      onImagePicked(file) {
      if (file !== undefined && file !== null) {
          if (file.name.lastIndexOf('.') <= 0) {
            return
          }
          this.newUserInfo.image = file;
          const fr = new FileReader()
          fr.readAsDataURL(file)
          fr.addEventListener('load', () => {
            this.uploadImageUrl = fr.result
          })
      } else {
        this.uploadImageUrl = ''
      }
    }
  }
};
</script>

<style scoped>
.members {
  margin-left: 35%;
  margin-top: 25px;
  position: relative;
  text-align: center;
  padding: 20px 50px 20px;
  width: 550px;
  background: white;
  border-radius: 3px;
  -webkit-box-shadow: 0 0 200px rgba(255, 255, 255, 0.5), 0 1px 2px rgba(0, 0, 0, 0.3);
  box-shadow: 0 0 200px rgba(255, 255, 255, 0.5), 0 1px 2px rgba(0, 0, 0, 0.3);
}

.submit {
  text-align: right;
}

body {
  background-size: 30px 30px;
  margin: 0 auto;
  background-image: radial-gradient(#C6E6FB 15%, transparent 20%),
                    radial-gradient(#FCFBCA 15%, transparent 20%);
  background-position: 0 0, 15px 15px;
}

</style>
