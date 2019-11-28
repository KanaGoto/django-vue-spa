import axios from "axios";

import auth from "./auth";
import questions from "./questions";
//toDo
//import products from "./products";
//import product from "./product";

const client = axios.create({
  baseURL: "http://localhost:8000/api/"
});

/* apiを全て読み込む */
client.auth = auth(client);
client.questions = questions(client);
//toDo
//client.products = products(client);
//client.product = product(client);

// client.install = function(Vue) {
//   Object.defineProperty(Vue.prototype, "$request", {
//     get() {
//       return client;
//     }
//   });
//};

export default client;
