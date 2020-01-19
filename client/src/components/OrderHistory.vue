<template>
  <div id="hidtory" class="con1">
    <div v-if="orderList.length > 0">
      <!-- timeline -->
      <v-timeline align-top dense class="no-shadows">
        <v-timeline-item
          v-for="(order, index) in orderList"
          :key="order.id"
          :color="colors[index].color"
        >
          <v-card
            :color="colors[index].color"
            style="width:680px;"
            class="no-shadows"
          >
            <v-card-title style="padding:1px 30px 1px">
              <h5 class="white--text font-weight-light small">
                ORDER No. {{ order.id }}
              </h5>
            </v-card-title>
            <v-card class="no-shadows">
              <v-expansion-panels class="no-shadows">
                <v-expansion-panel class="no-shadows">
                  <v-expansion-panel-header>
                    <div calss="fb">
                      <p style="font-size:13px">
                        【Delivery Date】 {{ order.delivery_date }}
                        {{ deliverytime[order.delivery_time] }} 【Payment】
                        {{ payment[order.payment] }}【Total】
                        {{ order.total_price }} 円
                      </p>

                      <p style="font-size:13px">
                        【Shipping Address】 {{ order.address.first_name }}
                        {{ order.address.last_name }}
                      </p>
                      <p style="font-size:13px">
                        〒{{ order.address.zip }} {{ order.address.state }}
                        {{ order.address.city }}
                        {{ order.address.street_address1 }}
                        {{ order.address.street_address2 }}
                      </p>
                      <p></p>
                    </div>
                  </v-expansion-panel-header>
                  <v-expansion-panel-content>
                    <div v-for="detail in order.order_detail" :key="detail.id">
                      <div style="padding:3px;font-size:13px">
                        <v-img
                          :src="detail.item.image"
                          width="100px"
                          class="fl"
                        />
                        <p style="margin:10px">
                          {{ detail.item.name }}
                        </p>
                        Quantity:
                        {{ detail.amount }}, Subtotal:
                        {{ detail.total_price }}円
                      </div>
                    </div>
                  </v-expansion-panel-content>
                </v-expansion-panel>
              </v-expansion-panels>
            </v-card>
          </v-card>
        </v-timeline-item>
      </v-timeline>
      <div style="padding-right:130px">
        <v-pagination
          v-model="currentPage"
          :length="totalPage"
          :total-visible="5"
          :click="$vuetify.goTo('#app', { duration: 0, offset: 0 })"
        ></v-pagination>
      </div>
      <v-fab-transition>
        <v-btn
          color="light-green darken-1"
          dark
          fab
          fixed
          bottom
          right
          v-show="showFab"
          @click="$vuetify.goTo('#app', { duration: 400, offset: 0 })"
        >
          <v-icon>keyboard_arrow_up</v-icon>
        </v-btn>
      </v-fab-transition>
      <br />
    </div>
    <div v-else></div>
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
          color: "teal lighten-1"
        },
        {
          color: "light-green lighten-1"
        },
        {
          color: "lime"
        },
        {
          color: "cyan accent-4"
        }
      ],
      showFab: false,
      currentPage: 1,
      totalPage: 1,
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
      ]
    };
  },
  created() {
    let self = this;
    this.getOrderList([this.userInfo.user_id, 1]).then(function(data) {
      self.totalPage = data.total_pages;
    });
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
  watch: {
    currentPage: function(newPageNo) {
      let self = this;
      this.getOrderList([this.userInfo.user_id, newPageNo]).then(function(
        data
      ) {
        self.totalPage = data.total_pages;
      });
    }
  },
  methods: {
    ...mapActions(["getOrderList"]),
    ...mapActions(["setCartItems_id"]),
    ...mapActions(["setFavorites_id"]),
    onScroll() {
      this.showFab = window.scrollY > 0;
    },
    pageNext() {
      this.pageNo += 1;
      this.$store.dispatch("getProducts", this.pageNo);
    }
  },
  mounted() {
    window.addEventListener("scroll", this.onScroll);
  },
  destroyed() {
    window.removeEventListener("scroll", this.onScroll);
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

.fb p {
  font-size: 3px;
}

.fl {
  float: left;
  margin-right: 10px;
}
.no-shadows {
  box-shadow: none !important;
}
.con1 {
  margin-left: 33%;
}

.con1 p {
  font-size: 17px;
}
</style>
