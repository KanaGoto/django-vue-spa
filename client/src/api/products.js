export default function(cli) {
  return {
    findAll(pageNo) {
      return cli.get(`products/?page=` + pageNo);
    },
    findById(id) {
      return cli.post(`products/${id}/`);
    },
    create(prodInfo) {
      return cli.post("products/", prodInfo);
    },
    category() {
      return cli.get("products/category/");
    }
  };
}
