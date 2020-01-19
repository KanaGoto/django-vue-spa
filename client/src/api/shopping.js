export default function(cli) {
  return {
    findByUser(user_id) {
      return cli.get(`shopping/cart?user_id=${user_id}`);
    },
    add(data) {
      return cli.post(`shopping/cart/`, data);
    },
    update(id, data) {
      return cli.put(`shopping/cart/update/${id}/`, data);
    },
    delete(id) {
      return cli.delete(`shopping/cart/delete/${id}/`);
    },
    orderList(user_id, pageNo) {
      return cli.get(
        `shopping/orders?user_id=${user_id}&page=${pageNo}&ordering=-id`
      );
    },
    createOrder(data) {
      return cli.post(`shopping/orders/`, data);
    },
    createOrderDetail(data) {
      return cli.post(`shopping/orders/detail/`, data);
    }
  };
}
