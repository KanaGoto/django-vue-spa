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
    <p class="submit">TOTAL PRICE : {{ orderInfo.totalPrice }}円</p>

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
            :rules="[v => !!v || 'address is required']"
            required
          ></v-select>
        </div>
      </div>
      <!-- 新しいアドレス -->
      <v-checkbox v-model="newAddress" label="New Address"></v-checkbox>
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
          :rules="streetRules"
          v-model="newAddressInfo.street_address1"
          label="Street_address1"
          placeholder="Snowy Rock Pl"
          counter="30"
          required
        ></v-text-field>
        <v-text-field
          :rules="streetRules"
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
          v-model="orderInfo.deliverydate"
          :items="dateList"
          label="date"
          style="padding-right:60px;width:10px"
          required
        ></v-select>
        <v-select
          v-model="orderInfo.deliverytime"
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
      streetRules: [
        v => !!v || "This field is required",
        v =>
          (!!v && v.length <= 30) || "Address must be less than 30 characters"
      ],
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
        totalPrice: null,
        address: null,
        payment: "0",
        deliverydate: "最短",
        deliverytime: "0",
        orderDetail: []
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
      }
    };
  },
  created() {
    //①合計金額算出
    let total = "";
    this.cartItems.forEach(item => {
      total += item.item.shop_price * item.amount;
    });
    this.orderInfo.totalPrice = total;

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
      this.dateList.push(y + "/" + m + "/" + d);
      now.setDate(now.getDate() + 1);
    }

    //③アドレス新規追加チェックボックス初期値
    if (this.addressList.length < 1) {
      this.newAddress = true;
      return "";
    }
    //④以下アドレスがある場合のみ
    this.userInfo.address.forEach(item => {
      this.addressList.push({
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
    this.orderInfo.address = this.addressList[0].value;
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
            self.createOrderDetailPre();
          })
          // eslint-disable-next-line
          .then(function(res) {
            //注文履歴登録
            let orderData = new FormData();
            orderData.append("user", self.userInfo.user_id);
            orderData.append("deliverydate", self.orderInfo.deliverydate);
            orderData.append("deliverytime", self.orderInfo.deliverytime);
            orderData.append("payment", self.orderInfo.payment);
            orderData.append("totalPrice", Number(self.orderInfo.totalPrice));
            orderData.append("address", self.orderInfo.address);
            for (var i = 0; i < self.orderInfo.orderDetail.length; i++) {
              orderData.append("order_detail[]", self.orderInfo.orderDetail[i]);
            }
            //注文履歴作成API
            self
              .createOrder(orderData)
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
      } else {
        //aaa
      }
    },
    createOrderDetailPre() {
      let self = this;
      // ループ処理の完了を受け取るPromise
      return new Promise(function(res) {
        // ループ処理（再帰的に呼び出し）
        function loop(i) {
          // 非同期処理なのでPromiseを利用
          return new Promise(function(resolve) {
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
                self.orderInfo.orderDetail.push(Number(res.id));
              })
              .then(function() {
                // resolveを呼び出し
                resolve(i + 1);
              });
          }).then(function(count) {
            // ループを抜けるかどうかの判定
            if (count > self.cartItems.length) {
              // 抜ける（外側のPromiseのresolve判定を実行）
              res("ok");
            } else {
              // 再帰的に実行
              loop(count);
            }
          });
        }
        // 初回実行
        loop(0);
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
