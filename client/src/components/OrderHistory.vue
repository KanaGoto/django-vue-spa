<template>
  <div id="hidtory" style="margin-left:35%">
    <!-- timeline -->
    <v-timeline align-top dense>
      <v-timeline-item
        v-for="order in orderList"
        :key="order.id"
        :color="getColor()"
      >
        <v-card :color="cardColor" style="width:600px">
          <v-card-title>
            <v-float>
              <h3 class="white--text font-weight-light small">
                ORDER No. {{ order.id }}
              </h3>
            </v-float>
          </v-card-title>
          <v-card>
            <v-expansion-panels v-model="panel">
              <v-expansion-panel>
                <v-expansion-panel-header>
                  <div calss="fb">
                    <p>
                      Delivery Date: {{ order.delivery_date }}
                      {{ deliverytime[order.delivery_time] }}
                    </p>
                    <p>Payment: {{ payment[order.payment] }}</p>

                    <p>Total: {{ order.total_price }} 円</p>
                  </div>
                </v-expansion-panel-header>
                <v-expansion-panel-content>
                  <div v-for="detail in order.order_detail" :key="detail.id">
                    <p>
                      {{ detail.item.name }}
                      Quantitys:
                      {{ detail.amount }}
                      Subtotal: {{ detail.total_price }}
                      (Produced by
                      {{ detail.item.seller.username }})
                    </p>
                  </div>
                </v-expansion-panel-content>
              </v-expansion-panel>
            </v-expansion-panels>
          </v-card>
        </v-card>
      </v-timeline-item>
    </v-timeline>

    <!-- leftNavi -->
    <left-navi :isLoggedIn="isLoggedIn" :userInfo="userInfo"></left-navi>
  </div>
</template>

<script>
import LeftNavi from "./LeftNavi.vue";
import deliverytime from "../static/deliverytime.js";
import payment from "../static/payment.js";
import { mapActions } from "vuex";
export default {
  components: {
    LeftNavi: LeftNavi
  },
  data() {
    return {
      colors: [
        {
          color: "red lighten-2"
        },
        {
          color: "purple darken-1"
        },
        {
          color: "green lighten-1"
        },
        {
          color: "indigo"
        }
      ],
      colorCount: 0,
      cardColor: "",
      deliverytime: deliverytime,
      payment: payment,
      items: [
        {
          title: "My Account",
          icon: "mdi-image",
          link: "account"
        },
        {
          title: "Order History",
          icon: "mdi-view-dashboard",
          link: "orders"
        },
        { title: "About", icon: "mdi-help-box", link: "about" }
      ],
      titles: ["home", "following", "profile"],
      tabs: null,
      drawer: null,
      panel: false,
      cartdrawer: null,
      count: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    };
  },
  created() {
    this.getOrderList(this.userInfo.user_id);
  },
  computed: {
    isLoggedIn() {
      return this.$store.getters.isLoggedIn;
    },
    userInfo() {
      return this.$store.getters.userInfo;
    },
    orderList() {
      return this.$store.getters.orderList.results;
    },
    nextURL() {
      return this.$store.getters.orderList.next;
    },
    beforeURL() {
      return this.$store.getters.orderList.before;
    }
  },
  methods: {
    ...mapActions(["getOrderList"]),
    ...mapActions(["setCartItems_id"]),
    ...mapActions(["setFavorites_id"]),
    getColor() {
      let tmp = this.colors[this.colorCount].color;
      let loopNum = 0;
      if (loopNum != Number(this.orderList.length)) {
        if (this.colorCount == Number(this.colors.length - 1)) {
          this.colorCount = 0;
        } else {
          this.colorCount += 1;
        }
        this.cardColor = tmp;
        return tmp;
      } else {
        return "";
      }
    },
    onScroll(e) {
      this.offsetTop = e.target.scrollTop;
    },
    pageNext() {
      this.pageNo += 1;
      this.$store.dispatch("getProducts", this.pageNo);
    }
  }
};
</script>

<style scoped>
.timeline {
  text-align: left;
  margin: 50px;
}
.fb {
  /* floatを解除 */
  clear: both;
}
</style>
