<template>
  <v-dialog v-model="dialogs.dialog" width="550px">
    <v-card>
      <v-list-item class="pa-0">
        <div class="prodForm">
          <app-navbar>Upload Your Product</app-navbar>
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
                v-model="newProd.name"
                :counter="30"
                :rules="nameRules"
                label="Name"
                required
              ></v-text-field>
            </p>
            <p>
              <v-select
                v-model="newProd.category.id"
                item-text="name"
                item-value="id"
                :items="categories"
                :rules="[v => !!v || 'category is required']"
                label="category"
                required
              />
            </p>
            <p>
              <img
                v-if="newProd.image"
                :src="newProd.image"
                width="100"
              />
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
                v-model="newProd.market_price"
                label="Market Price"
              ></v-text-field>
            </p>
            <p>
              <v-text-field
                v-model="newProd.shop_price"
                :rules="salesPriceRules"
                label="Sales Price"
                required
              ></v-text-field>
            </p>
            <p>
              <v-text-field
                v-model="newProd.products_num"
                label="Stock Quantity"
                required
              ></v-text-field>
            </p>
            <p>
              <v-textarea
                v-model="newProd.brief"
                label="Description"
                :counter="1000"
                :rules="descriptionRules"
                required
                rows="5"
              ></v-textarea>
            </p>
            <div class="submit">
              <v-spacer></v-spacer>
              <v-spacer></v-spacer>
              <v-checkbox
                v-model="newProd.ship_free"
                label="ship free"
              ></v-checkbox>
              <v-btn
                color="warning"
                :disabled="!(isEdited && valid)"
                @click="update()"
              >
                update
              </v-btn>
            </div>
          </v-form>
        </div>
      </v-list-item>
    </v-card>
  </v-dialog>
</template>

<script>
import { mapActions } from "vuex";
export default {
  //props: ["dialogs"],
  props: {
    dialogs: Object,
    newProd: Object,
    oldProd: Object
  },
  data() {
    return {
      valid: false,
      updateImageUrl: "",
      nonFieldErrors: [],
      salesPriceRules: [v => !!v || "sales price is required"],
      passwordRules: [v => !!v || "password is required"],
      nameRules: [
        v => !!v || "Name is required",
        v => (v && v.length <= 30) || "Name must be less than 30 characters"
      ],
      descriptionRules: [
        v => !!v || "Description is required",
        v =>
          (v && v.length <= 1000) ||
          "Description must be less than 1000 characters"
      ],
      checkbox: false,
      lazy: false,
      categories: []
    };
  },
  created() {
    let self = this;
    this.$store.dispatch("getCategory").then(res =>{
      self.categories = res;
    });
  },
  computed: {
    userInfo() {
      return this.$store.getters.userInfo;
    },
    isEdited() {
      // if (
      //   this.oldProd.name !== this.newProd.name ||
      //   this.oldProd.category !== this.newProd.category ||
      //   this.oldProd.products_num !== this.newProd.products_num ||
      //   this.oldProd.market_price !== this.newProd.market_price ||
      //   this.oldProd.shop_price !== this.newProd.shop_price ||
      //   this.oldProd.brief !== this.newProd.brief ||
      //   this.oldProd.ship_free !== this.newProd.ship_free ||
      //   this.oldProd.image !== this.newProd.image
      // ) {
      //   return true;
      // }
      return false;
    }
  },
  methods: {
    ...mapActions(["createProduct"]),
    ...mapActions(["getUserProducts"]),
    update() {
      let self = this;
      this.resetValidation();
      this.nonFieldErrors = [];
      let data = new FormData();
      data.append('name', this.newProd.name);
      data.append('category', this.newProd.category);
      data.append('products_num', this.newProd.products_num);
      data.append('market_price', this.newProd.market_price);
      data.append('shop_price', this.newProd.shop_price);
      data.append('ship_free', this.newProd.ship_free);
      data.append('brief', this.newProd.brief);
      data.append('image', this.newProd.image);
      data.append('seller', this.newProd.seller);
      this.createProduct(data).then(
        /* eslint-disable */
        res => {
          self.getUserProducts(self.userInfo.user_id);
          //商品一覧取得
          self.$store.dispatch("getProducts", 1);
          self.dialogs.dialog = false;
          self.resetValidation();
          self.reset();
          self.clearProdInfo();
        },
        err => {

          self.nonFieldErrors = self.getApiError(err);
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
      getApiError(obj){
        return Object.keys(obj).map(function (key) { return obj[key]; })
      },
      getBase64 (file) {
      return new Promise((resolve, reject) => {
        const reader = new FileReader()
        reader.readAsDataURL(file)
        reader.onload = () => resolve(reader.result)
        reader.onerror = error => reject(error)
      })
    },
    reSetUserData(){
      if (this.oldProd.image == "") {
        this.updateImageUrl = "";
      }else{
        this.updateImageUrl = this.oldProd.image;
      }
    },
    onImagePicked(file) {
        if (file !== undefined && file !== null) {
            if (file.name.lastIndexOf('.') <= 0) {
              return
            }
            this.newProd.image = file;
            const fr = new FileReader()
            fr.readAsDataURL(file)
            fr.addEventListener('load', () => {
              this.updateImageUrl = fr.result
            })
        } else {
          this.updateImageUrl = ''
        }
    }
  },
  watch: {
    dialogs: function(newDialogs) {
      this.newProd = newDialogs.newProd;
      this.oldProd = newDialogs.oldProd;
      if (newDialogs.image == "") {
        this.updateImageUrl = "";
      }else{
        this.updateImageUrl = newDialogs.image;
      }
    },
    currentPage: function(newPageNo) {
      let self = this;
      this.$store.dispatch("getProducts", newPageNo).then(function(data) {
        self.products = data.results;
        self.totalPage = data.total_pages;
      });
    }
  }
};
</script>

<style scoped>
.prodForm {
  position: relative;
  text-align: center;
  padding: 20px 50px 20px;
  width: 100%;
  background: white;
  border-radius: 3px;
  -webkit-box-shadow: 0 0 200px rgba(255, 255, 255, 0.5),
    0 1px 2px rgba(0, 0, 0, 0.3);
  box-shadow: 0 0 200px rgba(255, 255, 255, 0.5), 0 1px 2px rgba(0, 0, 0, 0.3);
}

.submit {
  text-align: right;
}
</style>