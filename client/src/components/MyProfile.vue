<template>
  <div id="profile">
    <v-container class="pa-2" style="height:95px;">
      <v-row align="end" class="bg">
        <v-col align-self="start" class="pa-0" cols="12">
          <v-avatar class="profile" color="grey" size="155" tile>
            <v-img :src="imgBaseURL + userInfo.image"></v-img>
          </v-avatar>
        </v-col>

        <v-col class="pa-0">
          <v-list-item class="username">
            <div class="title">{{ userInfo.username }}</div>
          </v-list-item>

          <div class="addBtn">
            <v-btn
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

    <v-container class="con2">
      <v-row class="ma-2" style="width:1300px">
        <div style="margin-top:150px">
          <v-btn
            color="light-green darken-1"
            text
            left
            smallx
            @click="getPrevious"
            :disabled="previousUrl == null"
          >
            <v-icon>chevron_left</v-icon>
          </v-btn>
        </div>
        <div v-for="userItem in userProd" :key="userItem.id" class="ma-2">
          <v-card class="ma-1" width="250px">
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
        </div>
        <div style="margin-top:150px">
          <v-btn
            color="light-green darken-1"
            right
            text
            small
            @click="getNext"
            :disabled="nextUrl == null"
          >
            <v-icon>chevron_right</v-icon>
          </v-btn>
        </div>
      </v-row>
    </v-container>
  </div>
</template>
<script>
import Dialog from "./ProdDialog.vue";
import prodUpdateDialog from "@/components/ProdUpdateDialog.vue";
import prodUploadDialog from "@/components/ProdUploadDialog.vue";
import config from "@/api/config.js";
export default {
  components: {
    appDialog: Dialog,
    prodUploadDialog: prodUploadDialog,
    prodUpdateDialog: prodUpdateDialog
  },
  data: () => ({
    imgBaseURL: config.imgBaseURL,
    prodUploadDialogs: {
      dialog: false,
      prod: []
    },
    prodUpdateDialogs: {
      dialog: false,
      newProd: []
    },
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
  },
  computed: {
    userInfo() {
      return this.$store.getters.userInfo;
    },
    userProd() {
      return this.$store.getters.userProducts.results;
    },
    nextUrl() {
      return this.$store.getters.userProducts.next;
    },
    previousUrl() {
      return this.$store.getters.userProducts.previous;
    },
    currentPage() {
      return this.$store.getters.userProducts.current;
    },
    newUserProd() {
      return this.$store.getters.userProducts.results;
    }
  },
  methods: {
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
    },
    getPrevious() {
      this.$store.dispatch("getUserProducts", [
        this.currentPage - 1,
        this.userInfo.user_id
      ]);
    },
    getNext() {
      this.$store.dispatch("getUserProducts", [
        this.currentPage + 1,
        this.userInfo.user_id
      ]);
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
.con2 {
  padding: 0px;
  margin: 0px 80px 0px;
}
</style>
