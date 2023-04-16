<script>
import axios from "axios";
let loginURL = "http://127.0.0.1:5000/api/login"
export default {
   data() {
      return {
         login: {
            username: "",
            user_pw: "",
         },
         loginresult: "",
      };
   },
   methods: {
      doLogin() {
         this.loginresult= "";
         let headervar = {
            headers: {
               "username": this.login.username,
               "password": this.login.user_pw
            },
         };
         
         axios.get(loginURL, headervar)
         .then((resp) => {
            this.loginresult = resp.data;
            if (this.loginresult=="SECURITY ERROR")
         {
            alert("SECURITY ERROR. Please try again.");
            window.location.reload();
         }
         
         if (this.loginresult=="TRUE")
         {
            alert("Login successful.");
            this.$router.push({ name: "home" });
         }



         });
      },
   },
};

</script>
<template>
<main>
<div id="app">

    <div class="login-page"> 
       <div class="container">
          <div class="row">
             <div class="col-lg-4 col-md-6 col-sm-8 mx-auto">
                   <h1>Sign In</h1>
                   <form class="form-group">
                      <input v-model="this.login.username" class="form-control" type="text" placeholder="Username" required>
                      <input v-model="this.login.user_pw" class="form-control" type="text" placeholder="Password" required>
                      <v-btn @click="doLogin()" class="btn btn-info">Login</v-btn>
                   </form>

                </div>
             </div>
          </div>
 
    </div>
 
 </div>
 </main>
</template>

<style>

.Hide {
   display:none;
   visibility:hidden;
}

p {
   line-height: 1rem;
}

.card {
   padding: 20px;
}

.form-group {
      margin-bottom: 20px;
}

.login-page {
   align-items: center;
   display: flex;
   height: 100vh;
}

.error {
   animation-name: errorShake;
   animation-duration: 0.3s;
}

@keyframes errorShake {
   0% {
      transform: translateX(-25px);
   }
   25% {
      transform: translateX(25px);
   }
   50% {
      transform: translateX(-25px);
   }
   75% {
      transform: translateX(25px);
   }
   100% {
      transform: translateX(0);
   }
}
</style>
