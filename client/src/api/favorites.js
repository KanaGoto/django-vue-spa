export default function(cli) {
  return {
    findAll(pageNo) {
      return cli.get(`favorites/?page=` + pageNo);
    },
    findByUser(id) {
      return cli.get(`favorites/?user_id=${id}`);
    },
    create(prodInfo) {
      return cli.post("favorites/", prodInfo, {
        headers: {
          "content-type": "multipart/form-data"
        }
      });
    }
  };
}
