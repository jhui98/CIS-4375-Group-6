<script>
import axios from "axios";
// backend endpoint for list of all merchants
let apiURL = `http://127.0.0.1:5000/api/merchant`;
export default {
  data() {
    return {
      iso: {
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
  },
};
</script>

<template>
  <main class="home-page">
    <h1>Merchants Management</h1>
    <p>All Merchants with their details are listed below</p>
    <div class="jumbotron vertical center">
      <div class="container">
        <div class="row">
          <div class="col-sm-12">
            <hr />
            <br />
            <button type="button" class="btn btn-success btn-sm" v-b-modal.iso-modal>
              Add Merchant

              <router-link to="/addMerchant"> </router-link>
            </button>
            <br /><br />
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
                <tr v-for="(item, merchant_id) in merchantData" :key="item.merchant_id">
                  <!-- <tr v-for="item, ISO_ID in isoData" :key="item.ISO_ID"></tr> -->
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
                      <button type="button" class="btn btn-info btn-sm">Update</button>
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
