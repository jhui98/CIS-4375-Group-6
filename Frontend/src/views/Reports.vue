<script>
let ReportOneURL = `http://localhost:5000/api/SevenOne`;
let ReportTwoURL = `http://localhost:5000/api/SevenTwo`;
let ReportThreeURL = `http://localhost:5000/api/SevenThree`;
let ReportFourURL = `http://localhost:5000/api/HardwareByType`;
let ReportFiveURL = `http://localhost:5000/api/HardwareWithTypeName`;
let ReportSixURL = `http://localhost:5000/api/MerchantsResellerID`;
let ReportSevenURL = `http://localhost:5000/api/MerchantOrders`;
let ReportEightURL = `http://localhost:5000/api/ordersReport`;
let ReportNineURL = `http://localhost:5000/api/detailsOrder`;

let resellerURL = `http://localhost:5000/api/reseller`;
let hardwareURL = `http://localhost:5000/api/hardware`;
let htypeURL = `http://localhost:5000/api/hardware_type`;
let isoURL = `http://localhost:5000/api/iso`;
let merchantURL = `http://localhost:5000/api/merchant`;
let ordersURL = `http://localhost:5000/api/orders`;



import axios from "axios";
export default {
  data() {
    return {
      reseller: {
        iso_id: "",
        reseller_email: "",
        reseller_id: "",
        reseller_name: "",
        reseller_phone: ""
      },
      resellerData:[],
      dataReady: false,
      hardware: {
        hardware_id: "",
        hardware_name: "",
        model_number: "",
        htype_id: ""
      },
      hardwareData:[],
      iso: {
        iso_id: "",
        iso_company: ""
      },
      isoData:[],
      hardware_type: {
        htype_id: "",
        htype_name: ""
      },
      htypeData:[],
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
        reseller_id: ""
      },
      merchantData:[],
      orders: {
        order_id: "",
        order_num: "",
        serial_number: "",
        tracking_num: "",
        order_date: "",
        ship_date: "",
        hardware_id: "",
        merchant_id: ""
      },
      ordersData:[],
    }
  },
/* once axios is mounted, automatically sends get request to pull all isos */
 async mounted() {
    this.isoData = [];

    await axios.get(isoURL + '/all')
    /* array to store response data */
    .then((resp) => {
      /* takes response from get request and compiles it into array */
      this.isoData = resp.data;
    });

    this.resellerData = [];

    await axios.get(resellerURL + '/all')
    /* array to store response data */
    .then((resp) => {
      /* takes response from get request and compiles it into array */
      this.resellerData = resp.data;
    });

    this.hardwareData = [];

    await axios.get(hardwareURL + '/all')
    /* array to store response data */
    .then((resp) => {
      /* takes response from get request and compiles it into array */
      this.hardwareData = resp.data;
    });

    this.htypeData = [];
    
    await axios.get(htypeURL + '/all')
    /* array to store response data */
    .then((resp) => {
      /* takes response from get request and compiles it into array */
      this.htypeData = resp.data;
    });

    this.merchantData = [];

    await axios.get(merchantURL + '/all')
    /* array to store response data */
    .then((resp) => {
      /* takes response from get request and compiles it into array */
      this.merchantData = resp.data;
    });

    this.ordersData = [];

    await axios.get(ordersURL + '/all')
    /* array to store response data */
    .then((resp) => {
      /* takes response from get request and compiles it into array */
      this.ordersData = resp.data;
    });
    this.dataReady=true;

  },
  methods: {
    /* method for routing to edit page */
    sevenOneReport(iso_id) {
      this.$router.push({ name: "sevenOneReport", params: {id: iso_id}});
    },

  },
}
</script>

<style>
.edit {
  background-color: #4CAF50; /* Green */
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
  background-color: #008CBA; /* Blue */
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
  <div v-if="dataReady">
    <!--https://stackoverflow.com/questions/53513538/is-async-await-available-in-vue-js-mounted DataReady awaiting solution referenced-->
    <main class="Reports-page">
        <h1>Reports</h1>
        <br>

        <div class="jumbotron vertical center">
          <div class="container">
            <h3>Report 1</h3>

              <div class="row">
                <div class="col-sm-12">
                  <div>View Resellers of ISO Company: {{ selected }}</div>
                    <!-- Documentation for this v-model solution can be found here https://vuejs.org/guide/essentials/forms.html#select -->
                  <select class="btn btn-danger btn-sm" v-model="selected">
                    <option v-for="iso in isoData" :key="iso.ISO_ID" v-on:click="sevenOneReport(ISO_ID)">
                        {{ iso.ISO_COMPANY }}
                    </option>
                  </select>
                    

                  <h3>Report 2</h3>

                  

                  <h3>Report 3</h3>

                  

                  <h3>Report 4</h3>



                  <h3>Report 5</h3>

                  

                  <h3>Report 6</h3>

                  

                  <h3>Report 7</h3>



                  <h3>Report 8</h3>

                  

                  <h3>Report 9</h3>

                  

                </div>
              </div>

          </div>

        </div>
    </main>
  </div>
</template>