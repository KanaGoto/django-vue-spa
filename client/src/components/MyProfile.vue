<template>
  <div id="profile">
    <v-container class="pa-2" style="height:95px;">
      <v-row align="end" class="bg">
        <v-col align-self="start" class="pa-0" cols="12">
          <v-avatar class="profile" color="grey" size="155" tile>
            <v-img :src="'http://localhost:8000' + userInfo.image"></v-img>
          </v-avatar>
        </v-col>

        <v-col class="pa-0">
          <v-list-item class="username">
            <div class="title">{{ userInfo.username }}</div>
          </v-list-item>

          <div class="addBtn">
            <v-btn
              :loading="loading3"
              :disabled="loading3"
              small
              color="blue-grey"
              class="ma-1 white--text"
              @click="openProdUploadModal()"
            >
              add new products
              <v-icon right dark>mdi-cloud-upload</v-icon>
            </v-btn>
            <prod-upload-dialog
              :dialogs="prodUploadDialogs"
            ></prod-upload-dialog>
          </div>
        </v-col>
      </v-row>
    </v-container>
    <v-row justify="center" align="center">
      <p class="yourProd">Your Products</p>
    </v-row>

    <v-container class="pa-0">
      <v-row dense>
        <v-slide-group class="pa-0">
          <v-slide-item
            v-for="userItem in userProd"
            :key="userItem.id"
            v-slot:default="{ active, toggle }"
          >
            <v-card class="ma-3" width="250px">
              <v-list-item>
                <v-list-item-content>
                  <v-list-item-title class="title-read">{{
                    userItem.name
                  }}</v-list-item-title>
                </v-list-item-content>
              </v-list-item>

              <v-img
                :src="userItem.image"
                class="white--text align-end"
                gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.1)"
                height="180px"
              >
              </v-img>
              <v-card-text>
                <div class="box-read">
                  {{ userItem.brief }}
                </div>
              </v-card-text>

              <v-card-actions>
                <v-btn
                  slot="activator"
                  text
                  color="red lighten-1"
                  @click="openModal(userItem)"
                >
                  Detail
                </v-btn>
                <v-btn
                  text
                  color="deep-purple accent-4"
                  @click="doEdit(userItem)"
                >
                  Edit
                </v-btn>
                <v-spacer></v-spacer>
              </v-card-actions>
              <!-- dialog -->
              <prod-update-dialog :dialogs="prodUpdateDialogs">
              </prod-update-dialog>
              <app-dialog :dialogs="dialogs"></app-dialog>
            </v-card>
          </v-slide-item>
        </v-slide-group>
      </v-row>
    </v-container>
  </div>
</template>
<script>
import Dialog from "./ProdDialog.vue";
import prodUpdateDialog from "@/components/ProdUpdateDialog.vue";
import prodUploadDialog from "@/components/ProdUploadDialog.vue";
export default {
  components: {
    appDialog: Dialog,
    prodUploadDialog: prodUploadDialog,
    prodUpdateDialog: prodUpdateDialog
  },
  data: () => ({
    prodUploadDialogs: {
      dialog: false,
      prod: []
    },
    prodUpdateDialogs: {
      dialog: false,
      newProd: []
    },
    offsetTop: 0,
    userProd: [],
    userItemList: [],
    dialogs: {
      dialog: false,
      prod: []
    }
  }),
  created() {
    if (this.$store.getters.isLoggedIn === false) {
      document.location = "/login";
    }
    let self = this;
    this.$store.dispatch("getUserProducts", this.userInfo.user_id).then(res => {
      self.userProd = res;
    });
  },
  computed: {
    userInfo() {
      return this.$store.getters.userInfo;
    },
    newUserProd() {
      return this.$store.getters.userProducts;
    }
  },
  watch: {
    // eslint-disable-next-line
    newUserProd: function(newProd, oldProd) {
      let arr = newProd;
      this.userProd = arr;
    }
  },
  methods: {
    onScroll(e) {
      this.offsetTop = e.target.scrollTop;
    },
    openProdUploadModal() {
      this.prodUploadDialogs.dialog = true;
    },
    openModal(prod) {
      this.dialogs.dialog = true;
      this.dialogs.prod = prod;
    },
    doEdit(prod) {
      this.prodUpdateDialogs.dialog = true;
      this.prodUpdateDialogs.newProd = prod;
    }
  }
};
</script>
<style scoped>
.dot {
  background-color: #fcfcfc;
  background-image: radial-gradient(#eee 10%, transparent 20%),
    radial-gradient(#eee 10%, transparent 20%);
  background-position: 0 0, 10px 10px;
  background-size: 20px 20px;
  min-height: 1500px;
}

h3 {
  border-bottom: solid 3px #cce4ff;
  position: relative;
  width: 80%;
  margin-bottom: 10px;
}

h3:after {
  position: absolute;
  content: " ";
  display: block;
  border-bottom: solid 3px #5472cd;
  bottom: -3px;
  width: 20%;
}

.yourProd:after {
  position: absolute;
  content: " ";
  display: block;
  border-bottom: solid 3px #5472cd;
  bottom: -3px;
  width: 20%;
}
.waku {
  border: solid 1px #ccc;
  padding: 4px;
}
.bg {
  background-image: url("../static/mizutama_blue.jpg");
}

.username {
  float: left;
  padding-left: 25px;
}
.addBtn {
  text-align: right;
  margin-right: 30px;
}
.yourProd {
  margin-top: 160px;
  border-bottom: solid 3px #cce4ff;
  position: relative;
  width: 80%;
  margin-bottom: 15px;
}
.box-read {
  padding-bottom: 0px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}
.profile {
  margin-left: 20px;
  margin-top: 20px;
}
.title {
  font-size: small;
  font-weight: normal;
}
.title-read {
  font-size: large;
  font-weight: 400;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}
</style>
