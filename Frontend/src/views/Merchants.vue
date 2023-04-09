<script>
import axios from "axios";
// backend endpoint for list of all merchants
let apiURL = `http://127.0.0.1:5000/api/merchant`;
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
      },
      merchantData: [],
    };
  },
  /* once axios is mounted, automatically sends get request to pull all merchants */
  mounted() {
    /* array to store response data */
    this.merchantData = [];
    axios
      .get(apiURL + "/all")
      /* takes response from get request and compiles it into array */
      .then((resp) => {
        this.merchantData = resp.data;
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

<template>
  <main class="home-page">
    <h1>Merchants Operations</h1>
    <br />
    <h4 text-align="center">Register a New Merchant</h4>
    <div class="px-20 py-20">
      <!-- @submit.prevent stops the submit event from reloading the page-->
      <form @submit.prevent="submitForm">
        <!-- grid container -->
        <div class="row">
          <!--column 1 starts here-->
          <div class="column">
            <!-- form field -->
            <label class="block">
              <!-- asterisk to denote required field-->
              <span style="color: #ff0000">* </span>
              <span class="text-gray-700">Name: </span>
              <input type="text" v-model="merchant.merchant_name" placeholder="Name" />
            </label>
            <!-- form field -->
            <label class="block">
              <!-- asterisk to denote required field-->
              <span style="color: #ff0000">* </span>
              <span class="text-gray-700">Email: </span>
              <input
                type="email"
                v-model="merchant.merchant_email"
                placeholder="example@xyz.com"
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
                placeholder="(xxx)-xxx-xxxx"
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
                placeholder="Address"
              />
            </label>
            <label class="block">
              <span class="text-gray-700">Address 2: </span>
              <input
                type="text"
                v-model="merchant.merchant_address2"
                placeholder="Address"
              />
            </label>
            <label class="block">
              <!-- asterisk to denote required field-->
              <span style="color: #ff0000">* </span>
              <span class="text-gray-700">City: </span>
              <input type="text" v-model="merchant.merchant_city" placeholder="Houston" />
            </label>
          </div>

          <!--column 3 starts here-->
          <div class="column">
            <!-- form field -->
            <label class="block">
              <!-- asterisk to denote required field-->
              <span style="color: #ff0000">* </span>
              <span class="text-gray-700">State: </span>
              <input type="text" v-model="merchant.merchant_state" placeholder="TX" />
            </label>
            <label class="block">
              <!-- asterisk to denote required field-->
              <span style="color: #ff0000">* </span>
              <span class="text-gray-700">Zip code: </span>
              <input type="text" v-model="merchant.merchant_zip" placeholder="XXXXX" />
            </label>
            <label class="block">
              <span style="color: #ff0000">* </span>
              <span class="text-gray-700">Reseller: </span>
              <input
                type="text"
                v-model="merchant.reseller_id"
                placeholder="reseller ID - try dropdown later"
              />
            </label>
          </div>
        </div>
        <div class="row">
          <!-- submit button -->
          <div align="center">
            <button type="submit" class="add">Add Merchant</button>
          </div>
        </div>
      </form>
    </div>
    <br />
    <br />
    <h4>All Merchants with their details are listed below</h4>
    <div class="jumbotron vertical center">
      <div class="container">
        <div class="row">
          <div class="col-sm-12">
            <hr />
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
<style>
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
