<script>
import axios from "axios";
// backend endpoint for list of all merchants
let apiURL = `http://127.0.0.1:5000/api/merchant`;
let resellerURL = `http://127.0.0.1:5000/api/reseller/all`;
export default {
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
      merchantData: [],
      resellerData: []
    };
  },
  /* once axios is mounted, automatically sends get request to pull all merchants */
  async mounted() {
    /* array to store response data */
    this.merchantData = [];
    await axios
      .get(apiURL + "/all")
      /* takes response from get request and compiles it into array */
      .then((resp) => {
        this.merchantData = resp.data;
      }),
      this.resellerData = [];

      await axios.get(resellerURL)
      .then((resp) => {
        this.resellerData = resp.data;
      });
  },
  methods: {
    /* method to handle form submission*/
    async submitForm() {
      axios
        /* sends POST request through axios to backend, alerts user of success, then reloads page through router */
        .post(apiURL, this.merchant)
        .then(() => {
          alert("Merchant has been successfully added.");
          /* reloads window to show changes */
          window.location.reload();
        })
        .catch((error) => {
          console.log(error);
        });
    },
    /* method for deleting iso */
    deleteMerchant(merchant_id) {
      if (
        confirm(
          "Are you sure you want to permanently delete this merchant? This cannot be undone."
        )
      ) {
        /* axios delete request, uses api URL and attaches id at end of it to specify what id to delete */
        axios.delete(apiURL + "?id=" + merchant_id).then(() => {
          /* reloads window to show changes */
          window.location.reload();
        });
      }
    },
    /* method for routing to edit page */
    editMerchant(merchant_id) {
      /* Activates on click of table property, routes to update page bases on name in index.js, params are the id of the item which is stored in id:  */
      this.$router.push({ name: "updateMerchant", params: { id: merchant_id } });
    },
  },
};
</script>

<!--Styling of the Merchant webpage-->
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
</style>

<template>
  <main class="home-page">
    <h1>Merchants Operations</h1>
    <br />
    <div>
      <form @submit.prevent="submitForm">
      <legend>Register New Merchant</legend>
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
            <button type="submit" class="btn btn-info">Add Merchant</button>
          </div>
          
    
        
        </div>
      </form>



    </div>
    <br />
    <br />
    <div class="jumbotron vertical center">
      <div class="container">
        <div class="row">
          <div class="col-sm-12">
            <hr />
            <h4>All Current Merchants</h4>
            <br />
            <table class="table table-hover">
              <!-- Table Head-->
              <thead>
                <tr>
                  <!--Table Head cells-->
                  <th scope="col">Name</th>
                  <th scope="col">Address 1</th>
                  <th scope="col">Address 2</th>
                  <th scope="col">City</th>
                  <th scope="col">State</th>
                  <th scope="col">Zip code</th>
                  <th scope="col">Email</th>
                  <th scope="col">Phone #</th>
                  <th scope="col">Reseller</th>
                  <th scope="col">Action</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="item in merchantData" :key="item.merchant_id">
                  <!--Do no show this to user-->
                  <!-- <td>{{ item.merchant_id }}</td> -->

                  <td>{{ item.merchant_name }}</td>
                  <td>{{ item.merchant_address1 }}</td>
                  <td>{{ item.merchant_address2 }}</td>
                  <td>{{ item.merchant_city }}</td>
                  <td>{{ item.merchant_state }}</td>
                  <td>{{ item.merchant_zip }}</td>
                  <td>{{ item.merchant_email }}</td>
                  <td>{{ item.merchant_phone }}</td>
                  <td>{{ item.reseller_name }}</td>
                  <td>
                    <div class="btn-group" role="group">
                      <!--Update Button-->
                      <button
                        type="button"
                        class="btn btn-info btn-sm"
                        @click="editMerchant(item.merchant_id)"
                      >
                        Update
                      </button>
                      <!--Delete Button-->
                      <button
                        type="button"
                        class="btn btn-danger btn-sm"
                        @click="deleteMerchant(item.merchant_id)"
                      >
                        Delete
                      </button>
                    </div>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  </main>
</template>


