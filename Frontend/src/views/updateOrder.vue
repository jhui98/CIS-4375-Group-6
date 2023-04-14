<script>
import axios from "axios";
let getURL = "http://localhost:5000/api/orders?id=";
let updateURL = "http://localhost:5000/api/orders";
let orderURL = "http://localhost:5000/api/detailsOrder?ORDER_NUMBER=";

export default {
  /*prop contains order_num from orders page, used for route params  */
  props: ["num"],
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
      /* Adds our route param, the ID of the order selected, to GET API */
      .get(orderURL + this.$route.params.num)
      /* Takes API data and stores Table variables into Data variables */
      .then((resp) => {
        this.orderData = resp.data;
        let data = resp.data[0];
        this.order.order_id = data.order_id;
        this.order.order_num = data.order_num;
      });
  },
  /* Method to update Order*/
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
  },
};
</script>
<template>
  <main>
    <div class="px-20 py-20"></div>
    <div class="jumbotron vertical center">
      <div class="container">
        <div class="col-sm-12">
          <hr />
          <h4>Hardware Associated With Order {{ $route.params.num }}</h4>
          <br />
          <table class="table table-hover">
            <!-- Table Head-->
            <thead>
              <tr>
                <!--Table Head cells-->
                <!-- Consider changing ISO Company ID to ISO Company if dropdown is implemented. Otherwise, leave as is.-->
                <th scope="col">Hardware Name</th>
                <th scope="col">Serial Number</th>
                <th scope="col">Order Date</th>
                <th scope="col">Ship Date</th>
                <th scope="col">Tracking Number</th>
                <th scope="col">Actions</th>
              </tr>
            </thead>
            <tbody>
              <!-- Takes every entry stored in beginning pull request and loads into table rows -->
              <tr v-for="item in orderData" :value="item.order_num">
                <td>{{ item.hardware_name }}</td>
                <td>{{ item.serial_number }}</td>
                <td>{{ item.order_date }}</td>
                <td>{{ item.ship_date }}</td>
                <td>{{ item.tracking_num }}</td>
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
    <div>
      <!--Go Back button-->
      <!-- Router function goes to previous page-->
      <button type="reset" class="btn btn-danger ml-1" @click="$router.go(-1)">
        Go back
      </button>
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
