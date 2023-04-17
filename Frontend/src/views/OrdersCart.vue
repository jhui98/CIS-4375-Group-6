<script>
import axios from "axios";
let ordersURL = `http://127.0.0.1:5000/api/orders`;
let merchantURL = `http://127.0.0.1:5000/api/merchant`;
let hardwareURL = `http://127.0.0.1:5000/api/hardware`;

export default {
  /*prop contains id from hardware page, used for route params  */
  props: ["id","date","merchants"],
  data() {
    return {
      orders: {
        order_num: Number,
        serial_number: "",
        tracking_num: "",
        order_date: Date,
        ship_date: "",
        hardware_id: "",
        merchant_id: Number,
      },
      iterateArray: [],
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
      orderDate: "",
      orderNum: "",
      orderMerchant: "",
    };
  },
  /* Before mount we collect data from GET api based on id*/
  async beforeMount() {
    this.iterateArray = [];
    this.hardwareData = [];
    this.merchantData = [];
    this.orderDate = this.$route.params.date;
    this.orderNum = this.$route.params.id;
    this.orderMerchant = this.$route.params.merchants;

    await axios.get(hardwareURL + "/all").then((resp) => {
      this.hardwareData = resp.data;
      console.log(this.hardwareData);
    });

      /* takes response from get request and compiles it into array of hardwares */
    await axios.get(merchantURL + "/all").then((resp) => {
      this.merchantData = resp.data;
      console.log(this.merchantData);
    });
  },
  /* Method to update Hardware*/
  methods: {
    addtoCart(hardware_id) {
      if (hardware_id == "")
        {
          
        }
       else {
        let appendArray = {
            order_num: this.orderNum,
            serial_number: this.orders.serial_number,
            tracking_num: this.orders.tracking_num,
            order_date: this.orderDate,
            ship_date: this.orders.tracking_num,
            hardware_id: hardware_id,
            merchant_id: this.orderMerchant
        };
        this.iterateArray.push(appendArray);
        console.log(this.iterateArray);
      }
    },

    async completeOrder() {
        const postArray = this.iterateArray;
        if (
        confirm(
          "Are you sure you want to submit the order?"
            )
        )
        {
        for (let x = 0; x < postArray.length; x++)
        {
        await axios
        .post(ordersURL,postArray[x]);
        }
    }
        alert("Order(s) have been successfully added.");
        this.$router.go(-1);
    },

    deletefromCart(index) {
        this.iterateArray.splice(index, 1);
    },
  },
};
</script>

<template>
    <main >
      <h1>Cart for Order {{ this.$route.params.id }}</h1>
      <br />
  
      <form required>
        <legend>Add Hardware To Cart</legend>
        <div class="form-group col-sm-6">
          <div class="row">
            <div class="col-6">
              <label class="form-label mt-4">
                <!-- asterisk to denote required field-->
                <span style="color: #ff0000">*</span>
                <span class="text">Hardware</span></label
              >
              <div class="col-sm-10">
                <select name="hardware" class="form-control" v-model="orders.hardware_id" required>
                  <option
                    name="Hardware"
                    v-for="item in hardwareData"
                    :key="item.hardware_id"
                    :value="item.hardware_id"
                  >
                    {{ item.hardware_name }}
                  </option>
                </select>
              </div>
            </div>
          </div>
          <br><br>
          <div class="col-6">
              <div class="col-sm-10">
                <v-btn @click="addtoCart(this.orders.hardware_id)" type="submit" class="btn btn-info">
                    Add To Cart
                </v-btn>
              </div>
            </div>
  
          <!--Submit Button-->
          <div>
            <br />
            <v-btn @click="completeOrder()" type="submit" class="btn btn-primary">Submit Order</v-btn>
          </div>
        </div>
      </form>
      <br>

      <table class="table table-hover">
              <!-- Table Head-->
              <thead>
                <legend>Cart Items</legend>
                <tr>
                  <!--Table Head cells-->
                  <th scope="col">Hardware</th>
                  <th scope="col">Actions</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="(item,index) in iterateArray" :key="index">
                  <!--Do no show this to user-->
                  <!-- <td>{{ item.order_id }}</td> -->
                  <td>{{ 
                    this.hardwareData.find((i) => i.hardware_id === item.hardware_id).hardware_name
                  }}</td>                  
                  <td>
                    <div class="btn-group" role="group">
                      <!--Delete Button-->
                      <button
                        type="button"
                        class="btn btn-danger btn-sm"
                        @click="deletefromCart(index)"
                      >
                        Delete
                      </button>
                    </div>
                  </td>
                </tr>
              </tbody>
            </table>
    </main>
</template>

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
.ml-1 {
  margin-left: 10px;
}
</style>

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