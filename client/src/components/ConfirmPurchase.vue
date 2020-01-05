<template>
  <div class="members">
    <app-navbar>Purchase Item</app-navbar>
    <v-alert :value="nonFieldErrors.length" type="error">
      <div v-for="error in nonFieldErrors" :key="error">
        <h5>
          {{ error }}
        </h5>
      </div>
    </v-alert>
    <v-list>
      <v-list-item v-for="item in cartItems" :key="item.id">
        <v-list-item-icon>
          <v-img
            :src="item.item.image"
            gradient="to bottom, rgba(0,0,0,0), rgba(0,0,0,0)"
            height="80px"
            width="100px"
          ></v-img>
        </v-list-item-icon>

        <v-list-item-content class="item">
          {{ item.item.name }}<br />
          生産者：{{ item.item.seller.username }} <br />
          価格：{{ item.item.shop_price }}円 / 数量：{{ item.amount }}
        </v-list-item-content>
      </v-list-item>
    </v-list>
    <p class="submit">TOTAL PRICE : {{ orderInfo.total_price }}円</p>

    <v-divider></v-divider>

    <v-form ref="form" v-model="valid" :lazy-validation="lazy">
      <p></p>
      <p class="item">Address</p>

      <div v-if="!newAddress">
        <div v-if="!addressIsNull">
          <v-select
            v-model="orderInfo.address"
            item-text="label"
            item-value="value"
            :items="addressList"
            required
          ></v-select>
        </div>
      </div>
      <!-- 新しいアドレス -->
      <v-checkbox
        v-model="newAddress"
        label="New Address"
        :rules="this.addressIsNull ? newAddressRules : ''"
      ></v-checkbox>
      <div v-if="newAddress">
        <v-text-field
          v-model="newAddressInfo.first_name"
          :error-messages="errorMessages"
          label="First Name"
          :counter="10"
          :rules="nameRules"
          placeholder="John"
          required
        ></v-text-field>
        <v-text-field
          v-model="newAddressInfo.last_name"
          :error-messages="errorMessages"
          label="Last Name"
          :counter="10"
          :rules="nameRules"
          placeholder="Doe"
          required
        ></v-text-field>

        <v-text-field
          :rules="zipRules"
          v-model="newAddressInfo.zip"
          label="ZIP / Postal Code"
          required
          placeholder="79938"
        ></v-text-field>
        <v-text-field
          v-model="newAddressInfo.state"
          :rules="stateRules"
          label="State/Province/Region"
          required
          placeholder="TX"
        ></v-text-field>
        <v-text-field
          :rules="cityRules"
          v-model="newAddressInfo.city"
          label="City"
          placeholder="El Paso"
          required
        ></v-text-field>
        <v-text-field
          :rules="street1Rules"
          v-model="newAddressInfo.street_address1"
          label="Street_address1"
          placeholder="Snowy Rock Pl"
          counter="30"
          required
        ></v-text-field>
        <v-text-field
          :rules="street2Rules"
          v-model="newAddressInfo.street_address2"
          label="Street_address2"
          placeholder="East building 2F"
          counter="30"
          required
        ></v-text-field>
      </div>
      <br />
      <div class="item">Payment</div>
      <v-radio-group v-model="orderInfo.payment" :option="dateList" row>
        <v-radio label="代引き" value="0"></v-radio>
        <v-radio label="PayPay" value="1"></v-radio>
        <v-radio label="LinePay" value="2"></v-radio>
        <v-radio label="VISA" value="3"></v-radio>
      </v-radio-group>
      <div class="item">Delivery Date</div>

      <div class="delivery">
        <v-select
          v-model="orderInfo.delivery_date"
          :items="dateList"
          label="date"
          style="padding-right:60px;width:10px"
          required
        ></v-select>
        <v-select
          v-model="orderInfo.delivery_time"
          item-text="label"
          item-value="value"
          :items="timeList"
          label="time"
          style="width:5px"
          required
        ></v-select>
      </div>

      <br />
      <div class="submit">
        <v-spacer></v-spacer>
        <v-spacer></v-spacer>
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
  name: "ConfirmPurchase",
  data() {
    return {
      valid: false,
      nonFieldErrors: [],
      nameRules: [
        v => !!v || "this field is required",
        v => (v && v.length <= 10) || "Name must be less than 10 characters"
      ],
      zipRules: [
        v => !!v || "this field is required",
        v => (v && v.length <= 7) || "Zip must be less than 7 characters"
      ],
      stateRules: [v => !!v || "this field is required"],
      cityRules: [v => !!v || "this field is required"],
      street1Rules: [
        v => !!v || "This field is required",
        v =>
          (!!v && v.length <= 30) || "Address must be less than 30 characters"
      ],
      street2Rules: [
        v => v.length <= 30 || "Address must be less than 30 characters"
      ],
      newAddressRules: [v => !!v || "This field is required"],
      lazy: false,
      newAddress: false,
      addressList: [],
      dateList: ["最短"],
      timeList: [
        { value: "0", label: "最短" },
        { value: "1", label: "午前中" },
        { value: "2", label: "12:00 ~ 14:00" },
        { value: "3", label: "14:00 ~ 17:00" },
        { value: "4", label: "17:00 ~ 19:00" }
      ],
      orderInfo: {
        total_price: null,
        address: null,
        payment: "0",
        delivery_date: "最短",
        delivery_time: "0",
        order_detail: []
      },
      newAddressInfo: {
        first_name: null,
        last_name: null,
        zip: null,
        state: null,
        city: null,
        street_address1: null,
        street_address2: null,
        phone: null
      },
      loopEnd: false
    };
  },
  created() {
    let self = this;
    //ユーザー情報を取得
    self.getUserInfo();
    //①合計金額算出
    let total = 0;
    self.cartItems.forEach(item => {
      total += item.item.shop_price * item.amount;
    });
    self.orderInfo.total_price = total;

    //②お届け日の設定 ※本来はサーバー側で取得
    var now = new Date();
    now.setDate(now.getDate() + 3);
    //今日から3日後〜7日後をリストにつめる
    for (let index = 0; index < 8; index++) {
      var y = now.getFullYear();
      var m = now.getMonth() + 1;
      var d = now.getDate();
      if (m < 10) {
        m = "0" + m;
      }
      if (d < 10) {
        d = "0" + d;
      }
      //リストに追加
      self.dateList.push(y + "/" + m + "/" + d);
      now.setDate(now.getDate() + 1);
    }

    if (self.userInfo.address.length > 0) {
      //④以下アドレスがある場合
      self.userInfo.address.forEach(item => {
        self.addressList.push({
          value: item.id,
          label:
            item.last_name +
            item.first_name +
            "　〒" +
            item.zip +
            " " +
            item.state +
            item.city +
            item.street_address1 +
            (item.street_address2 ? item.street_address2 : "")
        });
      });
      //住所の初期値
      self.orderInfo.address = self.addressList[0].value;
    } else {
      //③アドレス新規追加チェックボックス初期値
      self.newAddress = true;
      return "";
    }
  },
  computed: {
    isLoggedIn() {
      return this.$store.getters.isLoggedIn;
    },
    userInfo() {
      return this.$store.getters.userInfo;
    },
    cartItems() {
      return this.$store.getters.cartItems;
    },
    cartItems_id() {
      return this.$store.getters.cartItems_id;
    },
    addressIsNull() {
      return this.userInfo.address.length < 1 ? true : false;
    }
  },
  methods: {
    ...mapActions(["getUserInfo"]),
    ...mapActions(["getOrderList"]),
    ...mapActions(["createOrder"]),
    ...mapActions(["createOrderDetail"]),
    ...mapActions(["deleteCartItems"]),
    ...mapActions(["createAddress"]),
    ...mapActions(["getCartItems"]),

    validate() {
      if (this.$refs.form.validate()) {
        this.snackbar = true;
      }
    },
    reset() {
      this.$refs.form.reset();
    },
    resetValidation() {
      this.$refs.form.resetValidation();
    },
    getApiError(obj) {
      return Object.keys(obj).map(function(key) {
        return obj[key][0];
      });
    },
    submit() {
      let self = this;
      if (this.newAddress) {
        //新規住所登録
        let addData = new FormData();
        addData.append("first_name", this.newAddressInfo.first_name);
        addData.append("last_name", this.newAddressInfo.last_name);
        addData.append("state", this.newAddressInfo.state);
        addData.append("city", this.newAddressInfo.city);
        addData.append("street_address1", this.newAddressInfo.street_address1);
        addData.append("street_address2", this.newAddressInfo.street_address2);
        addData.append("phone", this.newAddressInfo.phone);
        addData.append("zip", this.newAddressInfo.zip);
        addData.append("user", this.userInfo.user_id);
        //住所登録API
        this.createAddress(addData)
          .then(function(res) {
            self.orderInfo.address = res.id;
          })
          .then(function() {
            //注文履歴（詳細）登録
            // eslint-disable-next-line
            self.createOrderDetailPre(self).then(function(arr){
              //注文履歴登録
              self.orderInfo.user = self.userInfo.user_id;
              self.orderInfo.total_price = Number(self.orderInfo.total_price);
              //注文履歴作成API
              self
                .createOrder(self.orderInfo)
                .then(function() {
                  return new Promise(function(res) {
                    //カートアイテム削除API
                    self.cartItems.forEach(item => {
                      self.deleteCartItems(item.id);
                    });
                    res();
                  });
                })
                .then(function() {
                  self.getCartItems(self.userInfo.user_id).then(function() {
                    alert("商品購入完了しました!");
                    self.$router.push("/mypage");
                  });
                });
            });
          });
      } else {
        //既存の住所で購入
        //注文履歴（詳細）登録
        self
          .createOrderDetailPre(self)
          // eslint-disable-next-line
          .then(function(arr) {
            self.sleep(1);
            //注文履歴登録
            self.orderInfo.user = self.userInfo.user_id;
            self.orderInfo.total_price = Number(self.orderInfo.total_price);
            //注文履歴作成API
            self.createOrder(self.orderInfo);
          })
          .then(function() {
            return new Promise(function(res) {
              //カートアイテム削除API
              self.cartItems.forEach(item => {
                self.deleteCartItems(item.id);
              });
              res();
            });
          })
          .then(function() {
            self.getCartItems(self.userInfo.user_id).then(function() {
              alert("商品購入完了しました!");
              alert(self.orderInfo.order_detail.length);
              self.$router.push("/mypage");
            });
          });
      }
    },
    createOrderDetailPre(self) {
      // ループ処理の完了を受け取るPromise
      // eslint-disable-next-line
       return new Promise((resolve1, reject1) => {
        // ループ処理（再帰的に呼び出し）
        function loop(i) {
          // 非同期処理なのでPromiseを利用
          // eslint-disable-next-line
          return new Promise((resolve2, reject2) => {
            // 非同期処理部分
            let detailData = new FormData();
            detailData.append("item", self.cartItems[i].item.id);
            detailData.append("amount", self.cartItems[i].amount);
            detailData.append(
              "total_price",
              self.cartItems[i].item.shop_price * self.cartItems[i].amount
            );
            self
              .createOrderDetail(detailData)
              .then(function(res) {
                self.orderInfo.order_detail.push(res.id);
              })
              .then(function() {
                // resolveを呼び出し
                self.sleep(1);
                resolve2(i + 1);
              });
          }).then(function(count) {
            // ループを抜けるかどうかの判定
            alert("ループcount:" + count);
            if (count > self.cartItems.length - 1) {
              // 抜ける（外側のPromiseのresolve判定を実行）
              resolve1(self.orderInfo.order_detail);
            } else {
              // 再帰的に実行
              alert(count + "回目実行します");
              loop(count);
            }
          });
        }
        // 初回実行
        loop(0).then(function(res) {
          // eslint-disable-next-line
          return new Promise((resolve3, reject1) => {
            resolve3(res);
          });
        });
      });
    },

    sleep(second) {
      return new Promise(resolve => {
        setTimeout(() => {
          resolve();
        }, second * 1000);
      });
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
  -webkit-box-shadow: 0 0 200px rgba(255, 255, 255, 0.5),
    0 1px 2px rgba(0, 0, 0, 0.3);
  box-shadow: 0 0 200px rgba(255, 255, 255, 0.5), 0 1px 2px rgba(0, 0, 0, 0.3);
}

.submit {
  text-align: right;
}
.item {
  text-align: left;
}
.delivery {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}
</style>
