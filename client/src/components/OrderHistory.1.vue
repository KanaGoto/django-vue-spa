<template>
  <v-timeline dense>
    <span v-for="order in orderList" :key="order.id">
      <v-timeline-item color="green lighten-2 mb-12" small>
        <v-card style="width:600px">
          <v-card-title class="green lighten-2">
            <v-icon dark size="42" class="mr-4">
              mdi-magnify
            </v-icon>
            <h2 class="display-15 white--text font-weight-light small">
              ORDER No. {{ order.id }}
            </h2>
          </v-card-title>
          <v-container>
            <v-row>
              <v-col cols="12" md="10">
                <p>受注日時: {{ order.add_time }}</p>
                <p>
                  お届け日時: {{ order.delivery_date }}
                  {{ order.delivery_time }}
                </p>
                <p>PAYMENT: {{ order.payment }}</p>
                <p>TOTAL PRICE: {{ order.total_price }}</p>
              </v-col>
              <v-col class="hidden-sm-and-down text-right" md="2">
                <v-icon size="64">mdi-calendar-text</v-icon>
              </v-col>
              <v-expansion-panels v-model="panel">
                <v-expansion-panel>
                  <v-expansion-panel-header>Panel 1</v-expansion-panel-header>
                  <v-expansion-panel-content>
                    Some content
                  </v-expansion-panel-content>
                </v-expansion-panel>
              </v-expansion-panels>
            </v-row>
          </v-container>
        </v-card>
      </v-timeline-item>
    </span>
  </v-timeline>
</template>

<script>
import { mapActions } from "vuex";
export default {
  data() {
    return {
      products: []
    };
  },
  created() {
    this.getOrderList(this.userInfo.user_id);
  },
  computed: {
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
</style>
