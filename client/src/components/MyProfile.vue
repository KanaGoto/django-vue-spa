<template>
  <div id="profile">
    <v-container class="pa-2" style="height:280px;">
      <v-row align="end" class="bg">
        <v-col align-self="start" class="pa-0" cols="12">
          <v-avatar class="profile" color="grey" size="164" tile>
            <v-img
              src="https://cdn.vuetifyjs.com/images/profiles/marcus.jpg"
              style="border:solid 1px padding:10px margin:10px"
            ></v-img>
          </v-avatar>
        </v-col>
        <v-col class="py-0">
          <v-list-item>
            <v-list-item-content>
              <v-list-item-title class="title">Marcus Obrien</v-list-item-title>
              <v-list-item-subtitle>Network Engineer</v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>
          <div class="text-right">
            <v-btn
              :loading="loading3"
              :disabled="loading3"
              color="green"
              class="ma-2 white--text"
              @click="loader = 'loading3'"
            >
              Edit Profile
              <v-icon right dark>mdi-account-circle</v-icon>
            </v-btn>
            <v-btn
              :loading="loading3"
              :disabled="loading3"
              color="blue-grey"
              class="ma-2 white--text"
              @click="loader = 'loading3'"
            >
              add new products
              <v-icon right dark>mdi-cloud-upload</v-icon>
            </v-btn>
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
          <v-col v-for="card in cards" :key="card.title" :cols="3">
            <v-card class="ma-3">
              <v-list-item>
                <v-list-item-content>
                  <v-list-item-title class="headline">{{
                    card.title
                  }}</v-list-item-title>
                </v-list-item-content>
              </v-list-item>

              <v-img
                :src="card.src"
                class="white--text align-end"
                gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
                height="200px"
              >
              </v-img>
              <v-card-text>
                dericious!
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
export default {
  data: () => ({
    offsetTop: 0,
    cards: [
      {
        title: "Orange",
        src: "https://cdn.vuetifyjs.com/images/cards/road.jpg",
        flex: 6
      },
      {
        title: "Apple",
        src: "https://cdn.vuetifyjs.com/images/cards/plane.jpg",
        flex: 6
      },
      {
        title: "Banana",
        src: "https://cdn.vuetifyjs.com/images/cards/road.jpg",
        flex: 6
      },
      {
        title: "Mango",
        src: "https://cdn.vuetifyjs.com/images/cards/plane.jpg",
        flex: 6
      }
    ]
  }),

  methods: {
    onScroll(e) {
      this.offsetTop = e.target.scrollTop;
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
