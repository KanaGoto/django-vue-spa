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
    },
    userRegister(userInfo){
      return cli.post("users/register/", userInfo);
    },
    getUserInfo(){
      return cli.get("users/info/");
    },
    createAddress(data){
      return cli.post("users/address/", data);
    }
  };
}
