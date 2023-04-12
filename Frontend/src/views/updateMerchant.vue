<script>
import axios from "axios";
let getURL = "http://localhost:5000/api/merchant?id=";
let updateURL = "http://localhost:5000/api/merchant";
let resellerURL = `http://127.0.0.1:5000/api/reseller/all`;
export default {
  /*prop contains id from merchant page, used for route params  */
  props: ["id"],
  data() {
    return {
      merchant: {
        merchant_id: "",
        merchant_name: "",
        merchant_address1: "",
        merchant_address2: "",
        merchant_city: "",
        merchant_state: "",
        merchant_zip: "",
        merchant_email: "",
        merchant_phone: "",
        reseller_name: "",
        reseller_id: ""
      },
      resellerData: []
    };
  },
  /* Before mount we collect data from GET api based on id*/
  async beforeMount() {
    await axios
      /* Adds our route param, the ID of the Merchant selected, to GET API */
      .get(getURL + this.$route.params.id)
      /* Takes API data and stores Table variables into Data variables */
      .then((resp) => {
        let data = resp.data[0];
        this.merchant.merchant_id = data.merchant_id;
        this.merchant.merchant_name = data.merchant_name;
        this.merchant.merchant_email = data.merchant_email;
        this.merchant.merchant_phone = data.merchant_phone;
        this.merchant.merchant_address1 = data.merchant_address1;
        this.merchant.merchant_address2 = data.merchant_address2;
        this.merchant.merchant_city = data.merchant_city;
        this.merchant.merchant_state = data.merchant_state;
        this.merchant.merchant_zip = data.merchant_zip;
        this.merchant.reseller_id = data.reseller_id;

        console.log(data);
      }),
      /* array to store response data */
      this.resellerData = [];
       await axios
      .get(resellerURL)
      /* takes response from get request and compiles it into array */
      .then((resp) => {
        this.resellerData = resp.data;
        console.log(this.resellerData);
      });
  },
  /* Method to update Merchant*/
  methods: {
    updateMerchant() {
      axios
        /* Uses full property, this.X, and not sub properties, this.X.X to run call */
        /* Runs call with all data collected in GET call */
        /*Needed to run this way due to ID being used in JSON for updates */
        .put(updateURL, this.merchant)
        .then(() => {
          alert("Merchant has been updated!");
          /* After Alert goes back to the main page for Merchant */
          window.history.go(-1);
        });
    },
  },
};
</script>

<!--Styling of the Merchant Update webpage-->
<style>
@import "bootswatch/dist/flatly/bootstrap.min.css";

* {
  box-sizing: border-box;
}

.column {
  float: left;
  width: 33.33%;
  height: 100px;
  border-style: double;
}

/* Clear floats after the columns */
.row:after {
  content: "";
  display: border-box;
  clear: both;
}
.delete {
  background-color: #f44336; /* Red */
  border: none;
  color: white;
  padding: 15px 25px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 12px;
  margin: 4px 2px;
  cursor: pointer;
}
.ml-1 {
  margin-left: 10px;
}
</style>

<template>
  <main>
    <h1>Merchants Operations</h1>
    <br />
      <form @submit.prevent="updateMerchant">
      <legend>Update Merchant</legend>
      <div class="form-group col-sm-6">
        <div class="row">

          <div class="col-12">
            <label class="form-label mt-4">
                  <!-- asterisk to denote required field-->
                  <span style="color:#ff0000">* </span>
                  <span class="text">Merchant Name</span></label>
                <div class="col-sm-9">
                  <input
                type="text" class="form-control"
                v-model="merchant.merchant_name"
                placeholder="Merchant name"
              /> 
            </div>  
          </div>

        </div>
        <div class="row">

          <div class="col-6">
            <label class="form-label mt-4">
                  <!-- asterisk to denote required field-->
                  <span style="color:#ff0000">* </span>
                  <span class="text">Phone Number</span></label>
                <div class="col-sm-6">
                  <input
                type="text" class="form-control"
                v-model="merchant.merchant_phone"
                placeholder="(xxx)-xxx-xxxx"
              /> 
            </div>  
          </div>

          <div class="col-6">
            <label class="form-label mt-4">
                  <!-- asterisk to denote required field-->
                  <span style="color:#ff0000">* </span>
                  <span class="text">Email</span></label>
                <div class="col-sm-10">
                  <input
                type="text" class="form-control"
                v-model="merchant.merchant_email"
                placeholder="example@xyz.com"
              /> 
            </div>  
          </div>

        </div>
        <div class="row">
          <div class="col-6">
            <label class="form-label mt-4">
                  <!-- asterisk to denote required field-->
                  <span style="color:#ff0000">* </span>
                  <span class="text">Address Line 1</span></label>
                <div class="col-sm-10">
                  <input
                type="text" class="form-control"
                v-model="merchant.merchant_address1"
                placeholder="Address 1"
              /> 
            </div>  
          </div>
          <div class="col-6">
            <label class="form-label mt-4">
                  <!-- asterisk to denote required field-->
                  <span style="color:#ff0000"> </span>
                  <span class="text">Address Line 2</span></label>
                <div class="col-sm-10">
                  <input
                type="text" class="form-control"
                v-model="merchant.merchant_address2"
                placeholder="Address 2"
              /> 
            </div>  
          </div>
        </div>
        <div class="row">
          <div class="col-4">
            <label class="form-label mt-4">
                  <!-- asterisk to denote required field-->
                  <span style="color:#ff0000">*  </span>
                  <span class="text">City</span></label>
                <div class="col-sm-10">
                  <input
                type="text" class="form-control"
                v-model="merchant.merchant_city"
                placeholder="Houston"
              /> 
            </div>  
          </div>
          <div class="col-4">
            <label class="form-label mt-4">
                  <!-- asterisk to denote required field-->
                  <span style="color:#ff0000">*  </span>
                  <span class="text">State</span></label>
                <div class="col-sm-10">
                  <input
                type="text" class="form-control"
                v-model="merchant.merchant_state"
                placeholder="Texas"
              /> 
            </div>  
          </div>
          <div class="col-4">
            <label class="form-label mt-4">
                  <!-- asterisk to denote required field-->
                  <span style="color:#ff0000">*  </span>
                  <span class="text">Zip Code</span></label>
                <div class="col-sm-10">
                  <input
                type="text" class="form-control"
                v-model="merchant.merchant_zip"
                placeholder="XXXXX"
              /> 
            </div>  
          </div>
        </div>
          <div class="col-4">
            <label class="form-label mt-4">
                  <!-- asterisk to denote required field-->
                  <span style="color:#ff0000">*  </span>
                  <span class="text">Reseller</span></label>
                <div class="col-sm-10">
                  <select class="form-select" v-model="merchant.reseller_id">
                    <option v-for="item in resellerData" :key="item.reseller_id" :value="item.reseller_id">
                      {{ item.reseller_name }}
                    </option>
                  </select> 
            </div>  
          </div> 
          <!--Submit Button-->
          <div>
            <br>
            <button type="submit" class="btn btn-info">Update Merchant</button>
            <!--Go Back button-->
            <!-- Router function goes to previous page-->
            <button 
            type="reset" 
            class="btn btn-danger ml-1" 
            @click="$router.go(-1)"
            >Go Back</button>
          </div>
          
    
        
        </div>
      </form>



    
  </main>
</template>
