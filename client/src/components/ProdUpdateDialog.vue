<template>
  <v-dialog v-model="dialogs.dialog" persistent width="550px">
    <v-card>
      <v-list-item class="pa-0">
        <div class="prodForm">
          <div style="text-align:right">
            <v-btn small color="white" class="no-shadows" @click="close">
              <v-icon>close</v-icon>
            </v-btn>
          </div>
          <app-navbar>Edit Your Product</app-navbar>
          <div style="padding: 10px 50px 10px;">
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
                  v-model="dialogs.newProd.name"
                  :counter="30"
                  :rules="nameRules"
                  label="Name"
                  required
                ></v-text-field>
              </p>
              <p>
                <v-select
                  v-model="dialogs.newProd.category.id"
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
                  v-if="
                    updateImageUrl == '' ? dialogs.newProd.image : updateImageUrl
                  "
                  :src="
                    updateImageUrl == '' ? dialogs.newProd.image : updateImageUrl
                  "
                  width="150"
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
                  v-model="dialogs.newProd.market_price"
                  label="Market Price"
                ></v-text-field>
              </p>
              <p>
                <v-text-field
                  v-model="dialogs.newProd.shop_price"
                  :rules="salesPriceRules"
                  label="Sales Price"
                  required
                ></v-text-field>
              </p>
              <p>
                <v-text-field
                  v-model="dialogs.newProd.products_num"
                  label="Stock Quantity"
                  required
                ></v-text-field>
              </p>
              <p>
                <v-textarea
                  v-model="dialogs.newProd.brief"
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
                  v-model="dialogs.newProd.ship_free"
                  label="ship free"
                ></v-checkbox>
                <v-btn color="warning" :disabled="!valid" @click="update()">
                  Update
                </v-btn>
              </div>
            </v-form>
          </div>
        </div>
      </v-list-item>
    </v-card>
  </v-dialog>
</template>

<script>
import { mapActions } from "vuex";
export default {
  props: ["dialogs"],
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
    this.$store.dispatch("getCategory").then(res => {
      self.categories = res;
    });
  },
  computed: {
    userInfo() {
      return this.$store.getters.userInfo;
    }
  },
  methods: {
    ...mapActions(["updateProduct"]),
    ...mapActions(["getUserProducts"]),
    update() {
      let self = this;
      this.resetValidation();
      this.nonFieldErrors = [];
      let data = new FormData();
      data.append("name", this.dialogs.newProd.name);
      data.append("category", this.dialogs.newProd.category);
      data.append("products_num", this.dialogs.newProd.products_num);
      data.append("market_price", this.dialogs.newProd.market_price);
      data.append("shop_price", this.dialogs.newProd.shop_price);
      data.append("ship_free", this.dialogs.newProd.ship_free);
      data.append("brief", this.dialogs.newProd.brief);
      if (typeof this.dialogs.newProd.image != "string") {
        data.append("image", this.dialogs.newProd.image);
      }
      this.updateProduct([this.dialogs.newProd.id, data]).then(
        /* eslint-disable */
        res => {
          //ユーザーに紐づく商品再取得
          self.getUserProducts([1, self.userInfo.user_id]);
          //商品一覧取得
          self.$store.dispatch("getProducts", 1);
          self.dialogs.dialog = false;
          self.resetValidation();
          self.reset();
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
    onImagePicked(file) {
        if (file !== undefined && file !== null) {
            if (file.name.lastIndexOf('.') <= 0) {
              return
            }
            this.dialogs.newProd.image = file;
            const fr = new FileReader()
            fr.readAsDataURL(file)
            fr.addEventListener('load', () => {
              this.updateImageUrl = fr.result
            })
        } else {
          this.updateImageUrl = ''
        }
    },
    close() {
      let self = this;
      this.getUserProducts([1, self.userInfo.user_id]).then(
        function(){
          self.dialogs.dialog = false;
        }
      )
    }
  }
};
</script>

<style scoped>
.prodForm {
  position: relative;
  text-align: center;
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

.no-shadows {
    box-shadow: none!important;
}
</style>
