<template>
  <div class="mt-4 ml-4">
    <v-badge>
      <template v-slot:badge>
        <span>2</span>
      </template>
      <v-icon>
        shopping_cart
      </v-icon>
    </v-badge>
  </div>
</template>

<script>
export default {
  data() {
    return {
      messages: 0,
      show: false
    };
  }
};
</script>
