export default function(cli) {
  /* eslint-disable */
  return {
    login(email, password) {
      alert("直前"+email)
      const data = {
        email,
        password
      };
      return cli.post("login/", data);
    },
    verify(token) {
      return cli.post("auth/verify/", { token });
    },
    userRegister(userInfo){
      return cli.post("users/register/", userInfo);
    }
  };
}
