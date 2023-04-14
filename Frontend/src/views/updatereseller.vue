<script>
import axios from "axios";
let getURL =`http://localhost:5000/api/reseller?id=`;
let updateURL = 'http://localhost:5000/api/reseller';
let dropURL =`http://localhost:5000/api/iso/all`;
let reportURL = `http://127.0.0.1:5000/api/SevenThree?id=`;
export default {
    /*prop contains id from the Reseller page, used for route params  */
    props:["id"],
    data() {
        return{
            reseller: {
                iso_id: "",
                reseller_email: "",
                reseller_id: "",
                reseller_name: "",
                reseller_phone: ""
            },
            isoData:[],
            reportData: []
        }
    },
    /* Before mount we collect data from GET api based on id*/
    async beforeMount() {
        await axios
        /* Adds our route param, the ID of the ISO selected, to GET API */
            .get(getURL+this.$route.params.id
            )
            /* Takes API data and stores Table variables into Data variables */
            .then((resp) => {
                let data = resp.data[0];
                this.reseller.reseller_id = data.reseller_id;
                this.reseller.reseller_name = data.reseller_name;
                this.reseller.reseller_email = data.reseller_email;
                this.reseller.reseller_phone = data.reseller_phone;
                this.reseller.iso_id = data.iso_id;
                console.log(data)
            }),
            this.isoData=[];

            await axios.get(dropURL)
            .then((resp) =>{
            this.isoData = resp.data;
            });
            this.reportData = [];
            axios
              .get(reportURL+this.$route.params.id)
              .then((resp) => {
                this.reportData = resp.data;
              });
    },
    methods: {
        updatereseller(){
            axios
            /* Uses full property, this.X, and not sub properties, this.X.X to run call */
            /* Runs call with all data collected in GET call */
            /*Needed to run this way due to ID being used in JSON for updates */
            .put(updateURL,this.reseller)
            .then(() => {alert("Reseller has been updated");
                    /* After Alert goes back to the main page for Reseller */
                    window.history.go(-1);
            })
        }
    }
    }
  



</script>

<!--Styling of the Reseller Update webpage-->
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

<template>
    <main>
        <h1>Reseller Operations</h1>
           <br /> 
        <div>
          <!-- @submit.prevent stops the submit event from reloading the page-->
          <form @submit.prevent="updatereseller">
            <legend>Update Reseller</legend>
              <!-- form field -->
              <div class="form-group col-sm-4">
                <label class="form-label mt-4">
                  <!-- asterisk to denote required field-->
                  <span style="color:#ff0000">* </span>
                  <span class="text">Reseller Name</span></label>
                  <div class="col-sm-6">
                  <input
                    type="text" class="form-control"
                    v-model="reseller.reseller_name"
                    placeholder="Name"
                  />
                </div>

              <div class="row">
                <div class="col-6">
                <label class="form-label mt-4">
                  <!-- asterisk to denote required field-->
                  <span style="color:#ff0000"></span>
                  <span class="text">Reseller Phone: </span></label>
                  <div class="col-sm-10">
                  <input
                    type="text" class="form-control"
                    v-model="reseller.reseller_phone"
                    placeholder="1234567890"
                  />
                  </div>
                </div>

                <div class="col-6">
                <label class="form-label mt-4">
                  <!-- asterisk to denote required field-->
                  <span style="color:#ff0000"></span>
                  <span class="text">Reseller Email:</span></label>
                  <div class="col-sm-10">
                  <input
                    type="text" class="form-control"
                    v-model="reseller.reseller_email"
                    placeholder="reseller@email.com"
                  />
                </div>
              </div>
            </div>
                <label class="form-label mt-4">
                  <!-- This particular field may need to become a dropdown of existing ISO Companies, but I am not sure how to implement. Please advise.-->
                  <span style="color:#ff0000">* </span>
                  <span class="text">ISO Company</span></label>
                  <div class="col-sm-6">
                    <select class="form-select" v-model="reseller.iso_id">
                      <option v-for="item in isoData" :key="item.ISO_ID" :value="item.ISO_ID">
                        {{ item.ISO_COMPANY }}
                      </option>
                    </select>
                </div>
              <!-- submit button -->
              <div>
            <br>
            <button type="submit" class="btn btn-info">Update Reseller</button>
            <!--Go Back button-->
            <!-- Router function goes to previous page-->
            <button 
            type="reset" 
            class="btn btn-danger ml-1" 
            @click="$router.go(-1)"
            >Go Back</button>
          </div>
            </div>
          </form>
        </div>
        <br>
        <br>
        <div class="jumbotron vertical center">
                <div class="container">
                    <div class="col-sm-12">
                        <hr/>
                        <h4>Merchants Associated With {{ reseller.reseller_name }}</h4>
                        <br>
                        <table class="table table-hover">
                            <!-- Table Head-->
                            <thead>
                                <tr>
                                    <!--Table Head cells-->
                                    <!-- Consider changing ISO Company ID to ISO Company if dropdown is implemented. Otherwise, leave as is.-->
                                    <th scope="col">Merchant Name</th>
                                    <th scope="col">Merchant Email</th>
                                    <th scope="col">Merchant Phone</th>
                                    <th scope="col">Merchant Address</th>
                                </tr>
                            </thead>
                            <tbody>
                                <!-- Takes every entry stored in beginning pull request and loads into table rows -->
                                <tr v-for="item in reportData" :value="item.MerchantID">
                                    <td>{{ item.MerchantName }}</td>
                                    <td>{{ item.MerchantEmail }}</td>
                                    <td>{{ item.MerchantPhone }}</td>
                                    <td>{{ item.MerchantAddress }}</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
    </main>
</template>