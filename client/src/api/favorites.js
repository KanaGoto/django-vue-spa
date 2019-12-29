export default function(cli) {
  return {
    // findAll(pageNo) {
    //   return cli.get(`favorites/?page=` + pageNo);
    // },
    findByUser(id) {
      return cli.get(`favorites/?user_id=${id}`);
    },
    add(data) {
      return cli.post("favorites/", data);
    },
    delete(id) {
      return cli.delete(`favorites/delete/${id}`);
    }
  };
}
