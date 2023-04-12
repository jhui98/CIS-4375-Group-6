<script>
import axios from "axios";
let getURL = "http://localhost:5000/api/hardware?id=";
let updateURL = "http://localhost:5000/api/hardware";

export default {
  /*prop contains id from hardware page, used for route params  */
  props: ["id"],
  data() {
    return {
        hardware: {
        hardware_id: "",
        hardware_name: "",
        model_number: "",
        htype_id: ""
      },
    };
  },
  /* Before mount we collect data from GET api based on id*/
  beforeMount() {
    axios
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
      });
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
      <h1>Hardwares Operations</h1>
      <br />
      <div>
        <!-- @submit.prevent stops the submit event from reloading the page-->
          <form @submit.prevent="updatehardware">
              <!-- form field -->
              <div class="form-group col-sm-2">
                      <label class="form-label mt-4">
                      <!-- asterisk to denote required field-->
                      <span style="color: #ff0000">* </span>
                      <span class="text">Harware Name</span></label>
                      <div class="col-sm-10">
                        <input 
                            type="text" class="form-control"
                            placeholder
                            v-model="hardware.hardware_name"
                            />
                          <br>
                        <!-- asterisk to denote required field-->
                        <span style="color: #ff0000">* </span>
                        <span class="text">Model number</span>
                        <input
                            type="text" class="form-control"
                            placeholder
                            v-model="hardware.model_number"
                        />
                          <br>
                        <span style="color: #ff0000">* </span>
                        <span class="text">Hardware ID: </span>
                        <input
                            type="text" class="form-control"
                            placeholder
                            v-model="hardware.hardware_id"
                        />
                      </div>
                  <div>
                    <br>
                      <!-- submit button -->
                      <button class="btn btn-info" type="submit">Update</button>
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
    </main>
  </template>

