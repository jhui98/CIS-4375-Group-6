<script>
var app = new Vue({
   el: "#app",
   
   data: {
      registerActive: false,
      emailLogin: "",
      passwordLogin: "",
      emailReg: "",
      passwordReg: "",
      confirmReg: "",
      emptyFields: false
   },
   
   methods: {
      doLogin() {
         if (this.emailLogin === "" || this.passwordLogin === "") {
            this.emptyFields = true;
         } else {
            alert("You are now logged in");
         }
      },
      
      doRegister() {
         if (this.emailReg === "" || this.passwordReg === "" || this.confirmReg === "") {
            this.emptyFields = true;
         } else {
            alert("You are now registered");
         }
      }
   }
});
</script>

<template>
<div id="app">

    <div class="login-page">
       <transition name="fade">
          <div v-if="!registerActive" class="wallpaper-login"></div>
       </transition>
       <div class="wallpaper-register"></div>
 
       <div class="container">
          <div class="row">
             <div class="col-lg-4 col-md-6 col-sm-8 mx-auto">
                <div v-if="!registerActive" class="card login" v-bind:class="{ error: emptyFields }">
                   <h1>Sign In</h1>
                   <form class="form-group">
                      <input v-model="emailLogin" type="email" class="form-control" placeholder="Email" required>
                      <input v-model="passwordLogin" type="password" class="form-control" placeholder="Password" required>
                      <input type="submit" class="btn btn-primary" @click="doLogin">
                      <p>Don't have an account? <a href="#" @click="registerActive = !registerActive, emptyFields = false">Sign up here</a>
                      </p>
                      <p><a href="#">Forgot your password?</a></p>
                   </form>
                </div>
 
                <div v-else class="card register" v-bind:class="{ error: emptyFields }">
                   <h1>Sign Up</h1>
                   <form class="form-group">
                      <input v-model="emailReg" type="email" class="form-control" placeholder="Email" required>
                      <input v-model="passwordReg" type="password" class="form-control" placeholder="Password" required>
                      <input v-model="confirmReg" type="password" class="form-control" placeholder="Confirm Password" required>
                      <input type="submit" class="btn btn-primary" @click="doRegister">
                      <p>Already have an account? <a href="#" @click="registerActive = !registerActive, emptyFields = false">Sign in here</a>
                      </p>
                   </form>
                </div>
             </div>
          </div>
 
       </div>
    </div>
 
 </div>
 </template>

<style>
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
