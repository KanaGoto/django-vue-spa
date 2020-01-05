export default function(cli) {
  return {
    findAll(pageNo) {
      return cli.get(`products/?page=` + pageNo);
    },
    findByUser(id) {
      return cli.get(`products/users/?user_id=${id}`);
    },
    findById(id) {
      return cli.post(`products/${id}/`);
    },
    create(prodInfo) {
      return cli.post("products/", prodInfo, {
        headers: {
          "content-type": "multipart/form-data"
        }
      });
    },
    category() {
      return cli.get("products/category/");
    }
  };
}
