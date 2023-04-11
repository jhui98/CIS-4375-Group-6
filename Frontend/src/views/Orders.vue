<script>
import axios from "axios";
// backend endpoint for list of all orders
let apiURL = `http://127.0.0.1:5000/api/orders`;
//let apiHardwareURL = `http://127.0.0.1:5000/api/hardware`;
//let apiMerchantURL = `http://127.0.0.1:5000/api/hardware`;

export default {
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
      hardwareData: [], // will hold all added items to order
    };
  },
  /* once axios is mounted, automatically sends get request to pull all orders */
  mounted() {
    /* array to store response data */
    this.orderData = [];
    axios
      .get(apiURL + "/all")
      /* takes response from get request and compiles it into array */
      .then((resp) => {
        this.orderData = resp.data;
      });
  },
  methods: {
    /* method to handle form submission*/
    async submitForm() {
      axios
        /* sends POST request through axios to backend, alerts user of success, then reloads page through router */
        .post(apiURL, this.order)
        .then(() => {
          alert("order has been successfully added.");
          /* reloads window to show changes */
          window.location.reload();
        })
        .catch((error) => {
          console.log(error);
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
        axios.delete(apiURL + "?id=" + order_id).then(() => {
          /* reloads window to show changes */
          window.location.reload();
        });
      }
    },
    /* method for routing to edit page */
    editOrder(order_id) {
      /* Activates on click of table property, routes to update page bases on name in index.js, params are the id of the item which is stored in id:  */
      this.$router.push({ name: "updateOrder", params: { id: order_id } });
    },
  },
};
</script>

<template>
  <main class="home-page">
    <h1>Orders Operations</h1>
    <br />
    <h4 text-align="center">Register a New order</h4>
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
              <span class="text-gray-700">Order #: </span>
              <input
                type="text"
                v-model="order.order_num"
                placeholder="12345"
                pattern="[0-9]{3}[0-9]{3}[0-9]{4}"
              />
            </label>
            <br />
            <!-- form field -->
            <label class="block">
              <!-- asterisk to denote required field-->
              <span style="color: #ff0000">* </span>
              <span class="text-gray-700">Merchant: </span>
              <input
                type="text"
                v-model="order.merchant_id"
                placeholder="dropdown menu later"
              />
            </label>
            <br />
          </div>

          <!--column 2 starts here-->
          <div class="column">
            <!-- form field -->
            <label class="block">
              <!-- asterisk to denote required field-->
              <span style="color: #ff0000">* </span>
              <span class="text-gray-700">Order Date: </span>
              <input
                type="date"
                v-model="order.order_date"
                placeholder="example@xyz.com"
              />
            </label>
            <br />
            <!-- form field -->
            <label class="block">
              <!-- asterisk to denote required field-->
              <span style="color: #ff0000">* </span>
              <span class="text-gray-700">Phone # </span>
              <input
                type="text"
                v-model="merchant.merchant_phone"
                placeholder="1234567890"
              />
            </label>
          </div>
        </div>

        <div class="jumbotron vertical center">
          <div class="container"></div>
        </div>

        <div class="row">
          <!-- submit button -->
          <div align="center">
            <label class="block">
              <span class="text-gray-700">Hardware: </span>
              <input
                type="text"
                v-model="order.hardware_id"
                placeholder="Dropdown menu"
              />
            </label>
            <button type="submit" class="add">Add order</button>
          </div>
        </div>
      </form>
    </div>
    <br />
    <br />
    <h4>All orders with their details are listed below</h4>
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
                  <th scope="col">Ship Date</th>
                  <th scope="col">Merchant</th>
                  <th scope="col">Action</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="item in orderData" :key="item.order_id">
                  <!--Do no show this to user-->
                  <!-- <td>{{ item.order_id }}</td> -->
                  <td>{{ item.order_num }}</td>
                  <td>{{ item.order_date }}</td>
                  <td>{{ item.ship_date }}</td>
                  <td>{{ item.merchant_id }}</td>
                  <td>
                    <div class="btn-group" role="group">
                      <!--Update Button-->
                      <button
                        type="button"
                        class="btn btn-info btn-sm"
                        @click="editOrder(item.order_id)"
                      >
                        Update
                      </button>
                      <!--Delete Button-->
                      <button
                        type="button"
                        class="btn btn-danger btn-sm"
                        @click="deleteOrder(item.order_id)"
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
