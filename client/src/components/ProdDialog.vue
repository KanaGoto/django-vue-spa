<template>
  <v-dialog v-model="dialogs.dialog" width="500">
    <v-card>
      <v-card class="ma-3">
        <v-list-item>
          <v-list-item-avatar color="grey"></v-list-item-avatar>
          <v-list-item-content>
            <v-list-item-title class="headline">
              {{ dialogs.prod.name }}</v-list-item-title
            >
            <v-list-item-subtitle>
              by {{ dialogs.prod.seller.username }}
            </v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>
        <v-img
          :src="dialogs.prod.image"
          class="white--text align-end"
          gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.1)"
          height="200px"
        >
        </v-img>
        <v-card-text>
          <p>price : {{ dialogs.prod.shop_price }}円</p>
          <br />
          {{ dialogs.prod.brief }}
        </v-card-text>
        <v-divider></v-divider>

        <v-card-actions>
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
    </v-card>
  </v-dialog>
</template>

<script>
export default {
  props: ["dialogs"],
  data() {
    return {
      prod_detail: []
    };
  },
  created() {}
};
</script>
