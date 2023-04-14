<script>
import axios from "axios";
let getURL = "http://localhost:5000/api/hardware?id=";
let updateURL = "http://localhost:5000/api/hardware";
let dropURL = `http://localhost:5000/api/hardware_type/all`;
let reportURL = `http://127.0.0.1:5000/api/HardwareWithTypeName`;

export default {
  /*prop contains id from hardware page, used for route params  */
  props: ["id"],
  data() {
    return {
        hardware: {
        hardware_id: "",
        hardware_name: "",
        model_number: "",
        htype_id: "",
        htype_name: ""
      },
      hwData:[],
      reportData:[]
    };
  },
  /* Before mount we collect data from GET api based on id*/
  async beforeMount() {
    await axios
      /* Adds our route param, the ID of the Hardware selected, to GET API */
      .get(getURL + this.$route.params.id)
      /* Takes API data and stores Table variables into Data variables */
      .then((resp) => {
        let data = resp.data[0];
        this.hardware.hardware_id = data.hardware_id;
        this.hardware.hardware_name = data.hardware_name;
        this.hardware.model_number = data.model_number;
        this.hardware.htype_id = data.htype_id;

        console.log(data);
      }),
      this.hwData = [];
      await axios
      .get(dropURL)

      .then((resp) =>
        this.hwData = resp.data);
      this.reportData = [];
      await axios
      .get(reportURL)
      .then((resp) =>{
        this.reportData = resp.data;
      });
    this.dataReady = true;
  },
  /* Method to update Hardware*/
  methods: {
    updatehardware() {
      axios
        /* Uses full property, this.X, and not sub properties, this.X.X to run call */
        /* Runs call with all data collected in GET call */
        /*Needed to run this way due to ID being used in JSON for updates */
        .put(updateURL, this.hardware)
        .then(() => {
          alert("Hardware has been updated!");
          /* After Alert goes back to the main page for hardware */
          window.history.go(-1);
        });
    },
  },
};
</script>

<!--Styling of the Hardware Update webpage-->
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
      <h1>Hardware Operations</h1>
      <br />
      <div>
        <!-- @submit.prevent stops the submit event from reloading the page-->
          <form @submit.prevent="updatehardware">
            <legend>Update Hardware</legend>
              <!-- form field -->
                      <div class="form-group col-sm-2">
                      <label class="form-label mt-4">
                      <!-- asterisk to denote required field-->
                      <span style="color: #ff0000">* </span>
                      <span class="text">Hardware Name</span></label>
                      <div class="col-sm-10">
                        <input 
                            type="text" class="form-control"
                            placeholder
                            v-model="hardware.hardware_name"
                            />
                        </div>
                        </div>
                        <!--Form Field-->
                        <div class="form-group col-sm-2">
                        <label class="form-label mt-4">
                        <!-- asterisk to denote required field-->
                        <span style="color: #ff0000">* </span>
                        <span class="text">Model Number</span></label>
                        <div>
                        <input
                            type="text" class="form-control"
                            placeholder
                            v-model="hardware.model_number"
                        />
                      </div>
                      </div>
                      <!--Form Field-->
                      <div class="form-group col-sm-2">
                      <label class="form-label mt-4">
                        <span style="color: #ff0000">* </span>
                        <span class="text">Hardware Type </span></label>
                        <div class="col-sm-10">
                          <select class="form-select" v-model="hardware.htype_id">
                            <option v-for="item in hwData" :key="item.htype_id" :value="item.htype_id">
                              {{ item.htype_name}}
                            </option>
                          </select>
                        </div>
                      </div>
                  <div>
                    <br>
                      <!-- submit button -->
                      <button class="btn btn-info" type="submit">Update Hardware</button>
                      <!--Go Back button-->
                      <!-- Router function goes to previous page-->
                      <button 
                      type="reset" 
                      class="btn btn-danger ml-1" 
                      @click="$router.go(-1)"
                      >Go Back</button>
                  </div>
              
          </form>
      </div>
      <br>
      <br>
      <div class="jumbotron vertical center">
                <div class="container">
                    <div class="col-sm-12">
                        <hr/>
                        <h4>All Current Hardware</h4>
                        <br>
                        <table class="table table-hover">
                            <!-- Table Head-->
                            <thead>
                                <tr>
                                    <!--Table Head cells-->
                                    <!-- Consider changing ISO Company ID to ISO Company if dropdown is implemented. Otherwise, leave as is.-->
                                    <th scope="col">Hardware</th>
                                    <th scope="col">Model Number</th>
                                    <th scope="col">Hardware Type</th>
                                </tr>
                            </thead>
                            <tbody>
                                <!-- Takes every entry stored in beginning pull request and loads into table rows -->
                                <tr v-for="item in reportData" :value="item.HARDWARE">
                                    <td>{{ item.HARDWARE }}</td>
                                    <td>{{ item.MODELNUMBER }}</td>
                                    <td>{{ item.TYPE }}</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
    </main>
  </template>

