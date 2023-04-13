<script>
import axios from "axios";
let getURL = "http://localhost:5000/api/orders?id=";
let updateURL = "http://localhost:5000/api/orders";
let orderURL = "http://localhost:5000/api/detailsOrder?ORDER_NUMBER="

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
      detailsOrderData:[],
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
        console.log(data);
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
      this.$router.push({ name: 'updatepart', params: { id: order_id } });
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
    <div>
        <h1> This is the Update Page for Part Orders. Input forms will go here and autofill.</h1>
    </div>   
    <div>
        <div>
            <br>
                      <!-- submit button -->
                      <button class="btn btn-info" type="submit">Update Hardware Order</button>
                      <!--Go Back button-->
                      <!-- Router function goes to previous page-->
                      <button 
                      type="reset" 
                      class="btn btn-danger ml-1" 
                      @click="$router.go(-1)"
                      >Go Back</button>
        </div>
    </div>  
  </main>
</template>
