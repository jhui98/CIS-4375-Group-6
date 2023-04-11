<script>
import axios from "axios";
let getURL = "http://localhost:5000/api/orders?id=";
let updateURL = "http://localhost:5000/api/orders";

export default {
  /*prop contains id from merchant page, used for route params  */
  props: ["id"],
  data() {
    return {
      order: {
        order_id: "",
        order_num: "",
        order_date: "",
        hardware_id: "",
        serial_num: "",
        ship_date: "",
        tracking_num: "",
        merchant_id: "",
      },
      orderData: [],
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
        this.order.order_id = data.order_id;
        this.order.order_num = data.order_num;
        this.order.hardware_id = data.hardware_id;
        this.order.serial_num = data.serial_num;
        this.order.ship_date = data.ship_date;
        this.order.tracking_num = data.tracking_num;
        this.order.merchant_id = data.merchant_id;

        console.log(data);
      });
  },
  /* Method to update Order*/
  methods: {
    updateMerchant() {
      axios
        /* Uses full property, this.X, and not sub properties, this.X.X to run call */
        /* Runs call with all data collected in GET call */
        /*Needed to run this way due to ID being used in JSON for updates */
        .put(updateURL, this.order)
        .then(() => {
          alert("Order has been updated!");
          /* After Alert goes back to the main page for Orders */
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
    <h1>Orders Operations</h1>
    <br />
    <br />
    <h4>Update Order</h4>
    <div class="px-20 py-20"></div>
  </main>
</template>
