const items = [
  { id: 1, name: "商品A", price: 100, content: "とってもおいしい" },
  { id: 2, name: "商品B", price: 200, content: "パーティ用" },
  { id: 3, name: "商品C", price: 300, content: "とっても珍しい" },
  { id: 4, name: "商品D", price: 400, content: "期間限定" },
  { id: 5, name: "商品E", price: 500, content: "安い" },
  { id: 6, name: "商品F", price: 600, content: "お高い" }
];

export default {
  fetch() {
    return items;
  },
  find(id) {
    return items.find(el => el.id === id);
  },
  asyncFind(id, callback) {
    setTimeout(() => {
      callback(items.find(el => el.id === id));
    }, 1000);
  }
};
// export default function(cli) {
//   return {
//     fetch() {
//       //仮
//       return cli.get("products/");
//     },
//     find(id) {
//       //仮
//       return cli.post(`products/${id}/`);
//     },
//     asyncFind(id, callback) {
//       setTimeout(() => {
//         callback(items.find(el => el.id === id));
//       }, 1000);
//     }
//   };
