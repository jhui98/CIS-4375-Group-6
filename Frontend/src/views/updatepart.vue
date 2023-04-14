<script>
import axios from "axios";
let getURL = "http://localhost:5000/api/orders?id=";
let updateURL = "http://localhost:5000/api/orders";
let orderURL = "http://localhost:5000/api/detailsOrder?ORDER_NUMBER=";

export default {
  /*prop contains order_num from orders page, used for route params  */
  props: ["id"],
  data() {
    return {
      order: {
        order_id: "",
        order_num: "",
        order_date: "",
        hardware_id: "",
        serial_number: "",
        ship_date: "",
        tracking_num: "",
        merchant_id: "",
      },
      orderData: [],
      detailsOrder: {
        address: "",
        hardware_name: "",
        merchant_email: "",
        order_date: "",
        order_id: "",
        order_num: "",
        ship_date: "",
        tracking_num: "",
        serial_number: "",
      },
      detailsOrderData: [],
    };
  },
  /* Before mount we collect data from GET api based on id*/
  beforeMount() {
    this.orderData = [];
    axios
      /* Adds our route param, the ID of the Merchant selected, to GET API */
      .get(orderURL + this.$route.params.num)
      /* Takes API data and stores Table variables into Data variables */
      .then((resp) => {
        this.orderData = resp.data;
        let data = resp.data[0];
        this.order.order_id = data.order_id;
        this.order.hardware_id = data.order_id;
        this.order.order_num = data.order_num;

        //wakindo updates start here
        this.order.order_date = data.order_date;
        this.order.serial_number = data.serial_number;
        this.order.tracking_num = data.tracking_num;
        this.order.ship_date = data.ship_date;
      });
  },
  /* Methods to update Order*/
  methods: {
    deleteOrder(order_id) {
      if (
        confirm(
          "Are you sure you want to permanently delete this hardware? This cannot be undone."
        )
      ) {
        /* axios delete request, uses api URL and attaches id at end of it to specify what id to delete */
        axios.delete(getURL + order_id).then(() => {
          /* reloads window to show changes */
          window.location.reload();
        });
      }
    },
    /* method for routing to edit page */
    editOrder(order_id) {
      /* Activates on click of table property, routes to update page bases on name in index.js, params are the id of the item which is stored in id:  */
      this.$router.push({ name: "updatepart", params: { id: order_id } });
    },
    updatePart() {
      console.log(updateURL);
      axios
        /* Uses full property, this.X, and not sub properties, this.X.X to run call */
        /* Runs call with all data collected in GET call */
        /*Needed to run this way due to ID being used in JSON for updates */
        .put(updateURL, this.order)
        .then(() => {
          alert("Order has been updated!");
          /* After Alert goes back to the main page for Order */
          window.history.go(-1);
        });
    },
  },
};
</script>

<template>
  <main>
    <div>
      <h1>Order Operations</h1>
    </div>
    <br />

    <!-- wakindo updates start here -->
    <div class="jumbotron vertical center">
      <!-- @submit.prevent stops the submit event from reloading the page-->
      <form @submit.prevent="updatePart">
        <!-- grid container -->

        <legend text-align="center">Order Hardware Update</legend>
        <div class="row">
          <!--column 1 starts here-->
          <div class="column">
            <!-- form field -->
            <div class="form-group col-sm-2">
              <label class="form-label mt-4">
                <!-- asterisk to denote required field-->
                <span style="color: #ff0000">* </span>
                <span class="text-gray-700">Serial Number: </span>
                <input type="text" v-model="this.order.serial_number" />
              </label>
            </div>
            <!-- form field -->
            <div class="form-group col-sm-2">
              <label class="form-label mt-4">
                <!-- asterisk to denote required field-->
                <span style="color: #ff0000">* </span>
                <span class="text-gray-700">Tracking Number: </span>
                <input type="text" v-model="this.order.tracking_num" />
              </label>
            </div>

            <br />
          </div>
          <!--column 2 starts here-->
          <div class="column">
            <!-- form field -->
            <div class="form-group col-sm-2">
              <label class="form-label mt-4">
                <!-- asterisk to denote required field-->
                <span style="color: #ff0000">* </span>
                <span class="text-gray-700">Ship Date: </span>
                <input type="date" v-model="this.order.ship_date" />
              </label>
            </div>

            <!-- form field - Hardware Dropdown-->
            <div class="form-group col-sm-2">
              <label class="form-label mt-4">
                <span style="color: #ff0000">* </span>
                <!-- asterisk to denote required field-->
                <span class="text-gray-700">Hardware: </span>
                <input type="text" v-model="this.hardware_name" />
              </label>
              <!-- form field - Hidden textbox to get dropdown selected hardware ID-->
              <label class="block">
                <input type="hidden" v-model="this.order.hardware_id" />
              </label>
            </div>
            <br />
            <!-- submit button -->
            <button class="btn btn-info" type="submit">Update Order</button>
            <!--Go Back button-->
            <!-- Router function goes to previous page-->
            <button type="reset" class="btn btn-danger ml-1" @click="$router.go(-1)">
              Go Back
            </button>
          </div>
        </div>
      </form>
    </div>
  </main>
</template>

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
