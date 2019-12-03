<template id="main">
  <v-ons-page>
    <v-ons-toolbar>
      <div class="center">{{ title }}</div>
    </v-ons-toolbar>

    <v-ons-tabbar
      swipeable
      position="auto"
      :tabs="tabs"
      :visible="true"
      :index.sync="activeIndex"
    >
    </v-ons-tabbar>
  </v-ons-page>
</template>

<script>
import Home from "@/components/Home.vue";
import Intro from "@/components/Intro.vue";
import News from "@/components/News.vue";
const home = {
  template: Home,
  props: ["myProp"]
};
const newsPage = {
  template: News
};
const IntroPage = {
  template: Intro
};

export default {
  name: "my-page",
  template: "#main",
  data() {
    return {
      activeIndex: 0,
      tabs: [
        {
          icon: this.md() ? null : "ion-home",
          label: "Home",
          page: home,
          props: {
            myProp: "This is a page prop!"
          },
          key: "home"
        },
        {
          icon: this.md() ? null : "ion-ios-bell",
          label: "News",
          page: newsPage,
          badge: 7,
          key: "newsPage"
        },
        {
          icon: this.md() ? null : "ion-ios-settings",
          label: "Settings",
          page: IntroPage,
          key: "IntroPage"
        }
      ]
    };
  },
  methods: {
    md() {
      return this.$ons.platform.isAndroid();
    }
  },
  computed: {
    title() {
      return this.tabs[this.activeIndex].label;
    }
  }
};
</script>
