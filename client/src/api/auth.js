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
    logout(){
      return cli.get("logout/");
    },
    verify(token) {
      return cli.post("auth/verify/", { token });
    },
    getUserInfo(){
      return cli.get("users/info/");
    },
    userRegister(userInfo){
      return cli.post("users/register/", userInfo);
    },
    userUpdate(userInfo){
      return cli.put("users/update/", userInfo);
    },
    createAddress(data){
      return cli.post("users/address/", data);
    }
  };
}
