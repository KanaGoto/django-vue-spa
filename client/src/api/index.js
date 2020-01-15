import axios from "axios";

import auth from "./auth";
import products from "./products";
import reviews from "./reviews";
import shopping from "./shopping";
import favorites from "./favorites";

const client = axios.create({
  baseURL: "http://localhost:8000/"
});

/* apiを全て読み込む */
client.auth = auth(client);
client.products = products(client);
client.favorites = favorites(client);
client.reviews = reviews(client);
client.shopping = shopping(client);

export default client;
