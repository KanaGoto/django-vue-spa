<template>
  <div id="MyPage">
    <v-card>
      <v-row justify="center" align="center">
        <v-toolbar color="cyan" dark flat justify="center" align="center">
          <v-app-bar-nav-icon></v-app-bar-nav-icon>
          <v-toolbar-title>Your Dashboard</v-toolbar-title>
          <v-spacer></v-spacer>

          <v-btn icon>
            <v-icon>mdi-heart</v-icon>
          </v-btn>
          <v-btn icon>
            <v-icon @click.stop="drawer = !drawer">mdi-cart</v-icon>
          </v-btn>
          <v-tabs
            slot="extension"
            v-model="tabs"
            background-color="transparent"
            centered
          >
            <v-tab v-for="title in titles" :key="title"> {{ title }} </v-tab>
          </v-tabs>
        </v-toolbar>
      </v-row>

      <v-navigation-drawer v-model="drawer" absolute temporary right>
        <v-list-item>
          <v-list-item-content>
            <v-list-item-title>カート内の商品</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-divider></v-divider>
        <v-list dense>
          <v-list-item v-for="item in items" :key="item.title" link>
            <v-list-item-icon>
              <v-icon>{{ item.icon }}</v-icon>
            </v-list-item-icon>

            <v-list-item-content>
              <v-list-item-title>{{ item.title }}</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list>
      </v-navigation-drawer>
    </v-card>

    <v-tabs-items v-model="tabs">
      <v-tab-item>
        <home></home>
      </v-tab-item>
      <v-tab-item>
        <following></following>
      </v-tab-item>
      <v-tab-item>
        <my-profile></my-profile>
      </v-tab-item>
    </v-tabs-items>
  </div>
</template>

<script>
import MyProfile from "@/components/MyProfile.vue";
import Following from "@/components/Following.vue";
import Home from "@/components/Home.vue";
export default {
  name: "Mypage",
  components: {
    Home,
    MyProfile,
    Following
  },
  data() {
    return {
      titles: ["home", "following", "profile"],
      tabs: null,
      drawer: null,
      items: [
        { title: "Home", icon: "dashboard" },
        { title: "About", icon: "question_answer" }
      ],
      isLoggedIn: false
    };
  }
};
</script>
