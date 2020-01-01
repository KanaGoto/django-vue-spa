<template>
  <v-timeline align-top dense>
    <v-timeline-item
      v-for="order in orderList"
      :key="order.id"
      :color="getColor()"
    >
      <v-card :color="cardColor" style="width:600px">
        <v-card-title>
          <h3 class="white--text font-weight-light small">
            ORDER No. {{ order.id }}
          </h3>
        </v-card-title>
        <v-card>
          <v-expansion-panels v-model="panel">
            <v-expansion-panel>
              <v-expansion-panel-header>
                <p>受注日時: {{ order.add_time }}</p>
                <p>
                  お届け日時: {{ order.delivery_date }}
                  {{ order.delivery_time }}
                </p>
                <p>PAYMENT: {{ order.payment }}</p>
                <p>TOTAL PRICE: {{ order.total_price }}</p>
              </v-expansion-panel-header>
              <v-expansion-panel-content>
                Some content
              </v-expansion-panel-content>
            </v-expansion-panel>
          </v-expansion-panels>
        </v-card>
      </v-card>
    </v-timeline-item>
  </v-timeline>
</template>

<script>
import { mapActions } from "vuex";
export default {
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
      cardColor: ""
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
</style>
