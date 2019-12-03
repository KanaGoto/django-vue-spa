export default function(cli) {
  return {
    findAll(pageNo) {
      return cli.get(`reviews/?page=` + pageNo);
    },
    create(star, title, comment, prod, user) {
      const data = {
        star,
        title,
        comment,
        prod,
        user
      };
      return cli.post("reviews/", data);
    }
  };
}
