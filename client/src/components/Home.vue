<template>
  <v-sheet id="scroll-area-2" class="overflow-y-auto" max-height="700">
    <v-container class="pa-2" style="height: 1300px;">
      <v-row dense>
        <v-col v-for="card in cards" :key="card.title" :cols="4">
          <v-card class="ma-3">
            <v-list-item>
              <v-list-item-avatar color="grey"></v-list-item-avatar>
              <v-list-item-content>
                <v-list-item-title class="headline">{{
                  card.title
                }}</v-list-item-title>
                <v-list-item-subtitle>by Kurt Wagner</v-list-item-subtitle>
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
                Add cart
              </v-btn>
              <v-spacer></v-spacer>
              <v-btn icon>
                <v-icon>mdi-heart</v-icon>
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
