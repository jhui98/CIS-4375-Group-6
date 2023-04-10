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

<template>
    <main>
      <h1>Hardwares Operations</h1>
      <br />
      <br/>
      <h4>Update Hardware</h4>
      <div class="px-20 py-20">
        <!-- @submit.prevent stops the submit event from reloading the page-->
          <form @submit.prevent="updatehardware">
            <!-- grid container -->
              <div class="row">
                  <!--column starts here-->
                  <div class="column">
                      <!-- form field -->
                      <label class="block">
                      <!-- asterisk to denote required field-->
                      <span style="color: #ff0000">* </span>
                      <span class="text-gray-700">Harware name: </span>
                      <input 
                          type="text" 
                          v-model="hardware.hardware_name" />
                      </label>
                      <!-- form field -->
                      <label class="block">
                      <!-- asterisk to denote required field-->
                      <span style="color: #ff0000">* </span>
                      <span class="text-gray-700">Model number: </span>
                      <input
                          type="text"
                          v-model="hardware.model_number"
                      />
                      </label>
                      <!-- form field -->
                      <label class="block">
                      <span style="color: #ff0000">* </span>
                      <span class="text-gray-700">Hardware ID: </span>
                      <input
                          type="text"
                          v-model="hardware.hardware_id"
                      />
                      </label>
                  </div>
                  <div align="center" border-style="solid">
                      <!-- submit button -->
                      <button class="edit" type="submit">Update</button>
                      <!--Go Back button-->
                      <!-- Router function goes to previous page-->
                      <button type="reset" class="delete" @click="$router.go(-1)">Cancel</button>
                  </div>
              </div>
          </form>
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