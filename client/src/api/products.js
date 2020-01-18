export default function(cli) {
  return {
    findAll(pageNo) {
      return cli.get(`products/?page=` + pageNo);
    },
    findByUser(pageNo, userId) {
      return cli.get(`products/users/?user_id=${userId}&page=${pageNo}`);
    },
    findById(id) {
      return cli.get(`products/retrieve/${id}/`);
    },
    create(prodInfo) {
      return cli.post("products/", prodInfo, {
        headers: {
          "content-type": "multipart/form-data"
        }
      });
    },
    update(id, prodInfo) {
      return cli.put(`products/retrieve/${id}/`, prodInfo, {
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
