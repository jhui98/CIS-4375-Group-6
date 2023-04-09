<script>
import axios from "axios";
let getURL = "http://localhost:5000/api/merchant?id=";
let updateURL = "http://localhost:5000/api/merchant";

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
      },
    };
  },
  /* Before mount we collect data from GET api based on id*/
  beforeMount() {
    axios
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

<style>
.edit {
  background-color: #4caf50; /* Green */
  border: none;
  color: white;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 12px;
  margin: 4px 2px;
  cursor: pointer;
}
.add {
  background-color: #008cba; /* Blue */
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
</style>

<template>
  <main>
    <h1>Merchants Operations</h1>
    <br />
    <h4 text-align="center">Update Merchant</h4>
    <div class="px-20 py-20">
      <!-- @submit.prevent stops the submit event from reloading the page-->
      <form @submit.prevent="updateMerchant">
        <!-- form field -->
        <div>
          <!-- grid container -->
          <div class="row">
            <!--column 1 starts here-->
            <div class="column">
              <!-- form field -->
              <label class="block">
                <!-- asterisk to denote required field-->
                <span style="color: #ff0000">* </span>
                <span class="text-gray-700">Name: </span>
                <input 
                    type="text" 
                    v-model="merchant.merchant_name" />
              </label>
              <!-- form field -->
              <label class="block">
                <!-- asterisk to denote required field-->
                <span style="color: #ff0000">* </span>
                <span class="text-gray-700">Email: </span>
                <input
                  type="email"
                  v-model="merchant.merchant_email"
                />
              </label>
              <!-- form field -->
              <label class="block">
                <span style="color: #ff0000">* </span>
                <span class="text-gray-700">Phone: </span>
                <input
                  type="text"
                  pattern="[0-9]{3}[0-9]{3}[0-9]{4}"
                  v-model="merchant.merchant_phone"
                />
              </label>
            </div>

            <!--column 2 starts here-->
            <div class="column">
              <!-- form field -->
              <label class="block">
                <!-- asterisk to denote required field-->
                <span style="color: #ff0000">* </span>
                <span class="text-gray-700">Address 1: </span>
                <input
                  type="text"
                  v-model="merchant.merchant_address1"
                />
              </label>
              <label class="block">
                <span class="text-gray-700">Address 2: </span>
                <input
                    type="text"
                    v-model="merchant.merchant_address2"
                />
              </label>
              <label class="block">
                <!-- asterisk to denote required field-->
                <span style="color: #ff0000">* </span>
                <span class="text-gray-700">City: </span>
                <input
                  type="text"
                  v-model="merchant.merchant_city"
                />
              </label>
            </div>

            <!--column 3 starts here-->
            <div class="column">
              <!-- form field -->
              <label class="block">
                <!-- asterisk to denote required field-->
                <span style="color: #ff0000">* </span>
                <span class="text-gray-700">State: </span>
                <input 
                    type="text" 
                    v-model="merchant.merchant_state" 
                />
              </label>
              <label class="block">
                <!-- asterisk to denote required field-->
                <span style="color: #ff0000">* </span>
                <span class="text-gray-700">Zip code: </span>
                <input 
                    type="text" 
                    v-model="merchant.merchant_zip" 
                />
              </label>
              <label class="block">
                <span style="color: #ff0000">* </span>
                <span class="text-gray-700">Reseller: </span>
                <input
                  type="text"
                  v-model="merchant.reseller_id"
                  
                />
              </label>
            </div>
          </div>
          <div class="row">
            <!-- submit button -->
            <button class="edit" type="submit">Save Changes</button>
            <!--Go Back button-->
            <!-- Router function goes to previous page-->
            <button type="reset" class="delete" @click="$router.go(-1)">Cancel</button>
          </div>
        </div>
      </form>
    </div>
  </main>
</template>
