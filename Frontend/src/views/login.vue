<script>
import axios from "axios";
let loginURL = "https://localhost:5000/api/login"
export default {
   
   data() {
      return {
         login: {
            USERNAME: "",
            USER_PW: "",
         },
      };
   },

   beforeMount() {
      
   },

   methods: {
      doLogin() {
         if (this.emailLogin === "" || this.passwordLogin === "") {
            this.emptyFields = true;
         } else {
            alert("You are now logged in");
         }
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
                <div v-if="!registerActive" class="card login" v-bind:class="{ error: emptyFields }">
                   <h1>Sign In</h1>
                   <form class="form-group">
                      <input v-model="emailLogin" type="email" class="form-control" placeholder="Email" required>
                      <input v-model="passwordLogin" type="password" class="form-control" placeholder="Password" required>
                      <input type="submit" class="btn btn-primary" @click="doLogin">
                   </form>
                </div>
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
