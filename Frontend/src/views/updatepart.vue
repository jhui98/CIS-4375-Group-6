<script>
import axios from "axios";
let getURL = "http://localhost:5000/api/orders?id=";
let updateURL = "http://localhost:5000/api/orders";
let orderDetailsURL = "http://localhost:5000/api/detailsOrder?id=";
let orderDetailsURL = "http://localhost:5000/api/detailsOrder?id=";

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
  async beforeMount() {
    this.orderData = [];
    await axios
      /* Adds our route param, the ID of the Merchant selected, to GET API */
      .get(orderDetailsURL + this.$route.params.id)
      .get(orderDetailsURL + this.$route.params.id)
      /* Takes API data and stores Table variables into Data variables */
      .then((resp) => {
        let data = resp.data[0]
        this.detailsOrder.order_id = data.order_id;
        this.detailsOrder.hardware_name = data.hardware_name;
        this.detailsOrder.order_num = data.order_num;
        this.detailsOrder.order_date = data.order_date;
        this.detailsOrder.serial_number = data.serial_number;
        this.detailsOrder.tracking_num = data.tracking_num;
        this.detailsOrder.ship_date = data.ship_date;
      });
    await axios
      .get(getURL + this.$route.params.id)

      .then((resp) => {
        let datam = resp.data[0];
        this.order.order_id = datam.order_id;
        this.order.order_num = datam.order_num;
        this.order.order_date = datam.order_date;
        this.order.hardware_id = datam.hardware_id;
        this.order.serial_number = datam.serial_number;
        this.order.ship_date = datam.ship_date;
        this.order.tracking_num = datam.tracking_num;
        this.order.merchant_id = datam.merchant_id;
      });
  },
  /* Methods to update Order*/
  methods: {
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

        <legend text-align="center">Updating {{ detailsOrder.hardware_name }}</legend>
        <div class="row">
          <!--column 1 starts here-->
          <div class="column">
            <!-- form field -->
            <div class="form-group col-sm-2">
              <label class="form-label mt-4">
                <!-- asterisk to denote required field-->
                <span style="color: #ff0000">* </span>
                <span class="text-gray-700">Serial Number: </span>
                <input type="text" v-model="orderData.serial_number" />
              </label>
            </div>
            <!-- form field -->
            <div class="form-group col-sm-2">
              <label class="form-label mt-4">
                <!-- asterisk to denote required field-->
                <span style="color: #ff0000">* </span>
                <span class="text-gray-700">Tracking Number: </span>
                <input type="text" v-model="orderData.tracking_num" />
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
                <input type="date" v-model="orderData.ship_date" />
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
