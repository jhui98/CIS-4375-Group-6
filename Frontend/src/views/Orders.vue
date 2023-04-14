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
      hardwareTable: [], // temporary array for added hardware
    };
  },
  /* once axios is mounted, automatically sends get request to pull all orders */
  async mounted() {
    /* array to store response data */
    this.orderData = [];
    await axios
      .get(ordersURL + "/all")
      /* takes response from get request and compiles it into array of orders */
      .then((resp) => {
        this.orderData = resp.data;

        //this.order.order_date = this.formattedDate(this.order.order_date); // double check date formatting later
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
    /* method to handle form submission*/
    async submitForm() {
      axios
        /* sends POST request through axios to backend, alerts user of success, then reloads page through router */
        .post(ordersURL, this.order)
        .then(() => {
          alert("order has been successfully added.");
          /* reloads window to show changes */
          hardwareTable.append(this.order);
          window.location.reload();
        })
        .catch((error) => {
          print(orderRecord);
          alert("An error occured:", error);
        });
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
  },
};
</script>

<template>
  <main class="home-page">
    <h1>Orders Operations</h1>
    <br />
    <div class="px-20 py-20">
      <div class="jumbotron vertical center">
        <!-- @submit.prevent stops the submit event from reloading the page-->
        <form @submit.prevent="submitForm">
          <!-- grid container -->
          <legend text-align="center">Register a New order</legend>
          <div class="row">
            <!--column 1 starts here-->
            <div class="column">
              <!-- form field -->
              <div class="form-group col-sm-2">
                <label class="form-label mt-4">
                  <!-- asterisk to denote required field-->
                  <span style="color: #ff0000">* </span>
                  <span class="text-gray-700">Order #: </span>
                  <input type="text" v-model="order.order_num" placeholder="12345" />
                </label>
              </div>
              <!-- form field - Merchant Dropdown-->
              <div class="form-group col-sm-2">
                <label class="form-label mt-4">
                  <span style="color: #ff0000">* </span>
                  <!-- asterisk to denote required field-->
                  <span class="text-gray-700">Merchant: </span>
                  <select v-model="order.merchant_id">
                    <option
                      v-for="item in merchantData"
                      :key="item.merchant_id"
                      :value="item.merchant_id"
                    >
                      {{ item.merchant_name }}
                    </option>
                  </select>
                </label>
              </div>
              <!-- form field - Merchant_ID from dropdown -->
              <label class="block">
                <input type="text" v-model="this.order.merchant_id" />
              </label>
              <br />
            </div>
            <!--column 2 starts here-->
            <div class="column">
              <!-- form field -->
              <div class="form-group col-sm-2">
                <label class="form-label mt-4">
                  <!-- asterisk to denote required field-->
                  <span style="color: #ff0000">* </span>
                  <span class="text-gray-700">Order Date: </span>
                  <input type="date" v-model="order.order_date" />
                </label>
              </div>

              <!-- form field - Hardware Dropdown-->
              <div class="form-group col-sm-2">
                <label class="form-label mt-4">
                  <span style="color: #ff0000">* </span>
                  <!-- asterisk to denote required field-->
                  <span class="text-gray-700">Hardware: </span>
                  <select v-model="this.order.hardware_id">
                    <option
                      v-for="item in hardwareData"
                      :key="item.hardware_id"
                      :value="item.hardware_id"
                    >
                      <!-- dropdown will show hardware name only -->
                      {{ item.hardware_name }}
                    </option>
                  </select>
                </label>
                <!-- form field - Hidden textbox to get dropdown selected hardware ID-->
                <label class="block">
                  <input type="text" v-model="this.order.hardware_id" />
                </label>
              </div>
              <!-- form field - serial number - Note sure we need this field when entering an order-->
              <!-- during the shipping process, sure but when adding order items - discuss with team -->
              <div class="form-group col-sm-2">
                <label class="form-label mt-4">
                  <span class="text-gray-700">Hardware Serial # </span>
                  <input type="text" v-model="this.hardware.serial_num" />
                </label>
              </div>
              <!-- submit button -->
              <div>
                <button type="submit" class="add">Add Order</button>
              </div>
            </div>
          </div>
          <br />
          <!-- make a take here to list hardware as they are added to an order -->
          <div class="col-sm-12">
            <hr />
            <br />
            <legend>List added hardware here as they come</legend>
            <table class="table table-hover">
              <!-- Table Head-->
              <thead>
                <tr>
                  <!--Table Head cells-->
                  <th scope="col">Hardware</th>
                  <th scope="col">Serial Number</th>
                  <th scope="col">Action</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="item in hardwareTable" :key="item.order_num">
                  <!--Do no show this to user-->
                  <!-- <td>{{ item.order_id }}</td> -->
                  <td>{{ item.hardware_name }}</td>
                  <td>{{ item.serial_num }}</td>
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
        </form>
      </div>
    </div>
    <!--   DO NOT TOUCHE ANYTHING BELOW THIS LINE - JONATHAN IS WORKING ON IT -->
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
                  <th scope="col">Action</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="item in groupbyData" :key="item.ORDER_ID">
                  <!--Do no show this to user-->
                  <!-- <td>{{ item.order_id }}</td> -->
                  <td>{{ item.ORDER_NUM }}</td>
                  <td>{{ item.ORDER_DATE }}</td>
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
  /* border-style: double; */
}

/* Clear floats after the columns */
.row:after {
  content: "";
  display: border-box;
  /* border-style: double; */
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
