<script>
import axios from "axios";
import { DateTime } from "luxon";
// base endpoint for orders
let ordersURL = `http://127.0.0.1:5000/api/orders`;
// base endpoint for  merchant
let merchantURL = `http://127.0.0.1:5000/api/merchant`;
// base endpoint for hardware
let hardwareURL = `http://127.0.0.1:5000/api/hardware`;

export default {
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
      orderData: [], // array for order data
      hardware: {
        hardware_id: "",
        hardware_name: "",
        model_number: "",
        htype_id: "",
      },
      hardwareData: [], // array  for hardware data
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
      groupby: {
        order_id: "",
        order_num: "",
        order_date: "",
        hardware_id: "",
        serial_number: "",
        ship_date: "",
        tracking_num: "",
        merchant_id: "",
      },
      groupbyData: [], // array  for merchant data
    };
  },

  async mounted() {
    this.orderData = [];
    /* array to store response data */
    await axios
      .get(ordersURL + "/all")
      /* takes response from get request and compiles it into array of orders */
      .then((resp) => {
        this.orderData = resp.data;
        this.order.order_date = this.formattedDate(this.order.order_date);
      }),
      /* takes response from get request and compiles it into array of hardwares */
      (this.hardwareData = []);
    await axios.get(hardwareURL + "/all").then((resp) => {
      this.hardwareData = resp.data;
    }),
      /* takes response from get request and compiles it into array of hardwares */
      (this.merchantData = []);
    await axios.get(merchantURL + "/all").then((resp) => {
      this.merchantData = resp.data;
    });

    this.groupbyData = [];
    await axios.get(ordersURL + "/groupby").then((resp) => {
      this.groupbyData = resp.data;
    });
  },
  methods: {
    // better formatted date, converts UTC to local time
    // from CIS 4339 Project SP23 - in "eventDetails.vue"
    formattedDate(datetimeDB) {
      const dt = DateTime.fromISO(datetimeDB, {
        zone: "utc",
      });
      return dt.setZone(DateTime.now().zoneName, { keepLocalTime: true }).toISODate();
    },
    dateOnly(date){
      return date.substr(0, 16)
    }, 
    /* method for deleting iso */
    deleteOrder(order_id) {
      if (
        confirm(
          "Are you sure you want to permanently delete this order? This cannot be undone."
        )
      ) {
        /* axios delete request, uses api URL and attaches id at end of it to specify what id to delete */
        axios.delete(ordersURL + "?num=" + order_id).then(() => {
          /* reloads window to show changes */
          window.location.reload();
        });
      }
    },
    /* method for routing to edit page */
    editOrder(order_num) {
      /* Activates on click of table property, routes to update page bases on name in index.js, params are the id of the item which is stored in id:  */
      this.$router.push({ name: "updateOrder", params: { num: order_num } });
    },

    startOrder(order_num, order_date) {
      this.$router.push({ name: "OrdersCart", params: { id: order_num, date: order_date} });
    },
  },
};
</script>

<!--Styling of the Hardware webpage-->
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
    <h1>Orders Operations</h1>
    <br />

    <form>
      <legend>Register a New Order</legend>
      <div class="form-group col-sm-6">
        <div class="row">
          <div class="col-6">
            <label class="form-label mt-4">
              <!-- asterisk to denote required field-->
              <span style="color: #ff0000">* </span>
              <span class="text">Order Number</span></label
            >
            <div class="col-sm-6">
              <input
                type="number"
                class="form-control"
                v-model="order.order_num"
                placeholder="12345"
                required
              />
            </div>
          </div>

          <div class="col-6">
            <label class="form-label mt-4">
              <!-- asterisk to denote required field-->
              <span style="color: #ff0000">* </span>
              <span class="text">Order Date</span></label
            >
            <div class="col-sm-10">
              <input
                type="date"
                class="form-control"
                v-model="order.order_date"
                required
              />
            </div>
          </div>
        </div>
        <!--Start Order Button Button-->
        <div>
          <br />
          <button @click="startOrder(order.order_num, order.order_date)" 
            type="button" class="btn btn-info">
            Start New Order
          </button>
        </div>
      </div>
    </form>

    <br />
    <br />

    <h4>All Orders are listed below</h4>
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
                  <th scope="col">Order #</th>
                  <th scope="col">Order Date</th>
                  <th scope="col">Merchant</th>
                  <th scope="col">Actions</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="item in groupbyData" :key="item.ORDER_ID">
                  <!--Do no show this to user-->
                  <!-- <td>{{ item.order_id }}</td> -->
                  <td>{{ item.ORDER_NUM }}</td>
                  <td>{{ dateOnly(item.ORDER_DATE) }}</td>
                  <!-- Searches through all pulled merchants and finds record that matches the item's merchant_id, then returns its name - Thanks Zach :) -->
                  <td>
                    {{
                      merchantData.find((i) => i.merchant_id === item.MERCHANT_ID)
                        .merchant_name
                    }}
                  </td>
                  <td>
                    <div class="btn-group" role="group">
                      <!--Update Button-->
                      <button
                        type="button"
                        class="btn btn-info btn-sm"
                        @click="editOrder(item.ORDER_NUM)"
                      >
                        Update
                      </button>
                      <!--Delete Button-->
                      <button
                        type="button"
                        class="btn btn-danger btn-sm"
                        @click="deleteOrder(item.ORDER_NUM)"
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
  width: auto;
  height: auto;
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
