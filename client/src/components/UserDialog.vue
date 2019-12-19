<template>
  <v-dialog v-model="dialogs.dialog" width="500">
    aaaaaaaaaaaaa aaaaaaaaaaaaaa
    <v-btn color="warning" @click="submit()">
      complete
    </v-btn>
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
  methods: {
    submit() {
      alert("ok");
    }
  },
  created() {}
};
</script>
