export default function(cli) {
  /* eslint-disable */
  return {
    login(email, password) {
      const data = {
        email,
        password
      };
      return cli.post("login/", data);
    },
    verify(token) {
      return cli.post("auth/verify/", { token });
    }
  };
}
