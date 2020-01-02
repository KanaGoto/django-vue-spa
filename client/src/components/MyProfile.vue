<template>
  <div id="profile">
    <v-container class="pa-2" style="height:280px;">
      <v-row align="end" class="bg">
        <v-col align-self="start" class="pa-0" cols="12">
          <v-avatar class="profile" color="grey" size="164" tile>
            <v-img
              :src="'http://localhost:8000' + userInfo.image"
              style="border:solid 1px padding:10px margin:10px"
            ></v-img>
          </v-avatar>
        </v-col>
        <v-col class="py-0">
          <v-list-item>
            <v-list-item-content>
              <v-list-item-title class="title">{{
                userInfo.username
              }}</v-list-item-title>
              <v-list-item-subtitle>Network Engineer</v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>
          <div class="text-right">
            <v-btn
              :loading="loading3"
              :disabled="loading3"
              color="blue-grey"
              class="ma-2 white--text"
              @click="openProdUploadModal()"
            >
              add new products
              <v-icon right dark>mdi-cloud-upload</v-icon>
            </v-btn>
            <user-dialog :dialogs="userDialogs"></user-dialog>
            <prod-upload-dialog
              :dialogs="prodUploadDialogs"
            ></prod-upload-dialog>
          </div>
        </v-col>
      </v-row>
    </v-container>
    <v-row justify="center" align="center">
      <h3>Your Products</h3>
    </v-row>

    <v-sheet id="scroll-area-2" class="overflow-y-auto" max-height="500">
      <v-container class="pa-2" style="height: 1000px;">
        <v-row dense>
          <v-col v-for="prod in userProd" :key="prod.id" :cols="3">
            <v-card class="ma-3">
              <v-list-item>
                <v-list-item-content>
                  <v-list-item-title class="headline" size="10">{{
                    prod.name
                  }}</v-list-item-title>
                </v-list-item-content>
              </v-list-item>

              <v-img
                :src="prod.image"
                class="white--text align-end"
                gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
                height="200px"
              >
              </v-img>
              <v-card-text>
                {{ prod.brief }}
              </v-card-text>

              <v-card-actions>
                <v-btn text color="deep-purple accent-4">
                  Detail
                </v-btn>
                <v-btn text color="deep-purple accent-4">
                  Edit
                </v-btn>

                <v-btn icon>
                  <v-icon>mdi-share-variant</v-icon>
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-sheet>
  </div>
</template>
<script>
import userDialog from "@/components/UserDialog.vue";
import prodUploadDialog from "@/components/ProdUploadDialog.vue";
export default {
  components: {
    userDialog: userDialog,
    prodUploadDialog: prodUploadDialog
  },
  data: () => ({
    userDialogs: {
      dialog: false,
      prod: []
    },
    prodUploadDialogs: {
      dialog: false,
      prod: []
    },
    offsetTop: 0,
    userProd: [],
    nextUrl: null,
    previousUrl: null
  }),
  created() {
    if (this.$store.getters.isLoggedIn === false) {
      document.location = "/login";
    }
    let self = this;
    this.$store.dispatch("getUserProducts", this.userInfo.user_id).then(res => {
      self.userProd = res.results;
      self.nextUrl = res.next;
      self.previousUrl = res.previous;
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
      this.userProd = newProd.results;
      this.nextURL = newProd.next;
      this.previousUrl = newProd.previous;
    }
  },
  methods: {
    onScroll(e) {
      this.offsetTop = e.target.scrollTop;
    },
    openUserModal() {
      this.userDialogs.dialog = true;
    },
    openProdUploadModal() {
      this.prodUploadDialogs.dialog = true;
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
}

h3:after {
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
</style>
