<script>
import axios from "axios";
let getURL = `http://localhost:5000/api/hardware_type?id=`;
let updateURL = "http://localhost:5000/api/hardware_type";
let reportURL = "http://localhost:5000/api/HardwareByType?id=";

export default {
  /*prop contains id from Hardware Type page, used for route params  */
  props: ["id"],
  data() {
    return {
      hardwaretype: {
        htype_id: "",
        htype_name: "",
      },
      sevenFour: {
        htype_id: "",
        hardware_name: "",
        model_number: "",
      },
      reportData: [],
    };
  },
  /* Before mount we collect data from GET api based on id*/
  async beforeMount() {
    await axios
      /* Adds our route param, the ID of the ISO selected, to GET API */
      .get(getURL + this.$route.params.id)
      /* Takes API data and stores Table variables into Data variables */
      .then((resp) => {
        let data = resp.data[0];
        this.hardwaretype.htype_name = data.htype_name;
        this.hardwaretype.htype_id = data.htype_id;
      });
    this.reportData = [];
    axios.get(reportURL + this.$route.params.id).then((resp) => {
      this.reportData = resp.data;
    });
    this.dataReady = true;
  },
  methods: {
    updateHTYPE() {
      axios
        /* Uses full property, this.X, and not sub properties, this.X.X to run call */
        /* Runs call with all data collected in GET call */
        /*Needed to run this way due to ID being used in JSON for updates */
        .put(updateURL, this.hardwaretype)
        .then(() => {
          alert("Hardware Type has been updated");
          /* After Alert goes back to the main page for Hardware Type */
          window.history.go(-1);
        });
    },
  },
};
</script>

<!--Styling of the Hardware Type Update webpage-->
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
    <h1>Hardware Type Operations</h1>
    <br />
    <div>
      <!-- @submit.prevent stops the submit event from reloading the page-->
      <form @submit.prevent="updateHTYPE">
        <legend>Update Hardware Type</legend>
        <!-- form field -->
        <div class="form-group col-sm-2">
          <label class="form-label mt-4">
            <!-- asterisk to denote required field-->
            <span style="color: #ff0000">* </span>
            <span class="text">Hardware Type Name </span></label
          >
          <div class="col-sm-10">
            <!-- Autofills input field based on data from beforeMount GET Call-->
            <input
              type="text"
              class="form-control"
              v-model="hardwaretype.htype_name"
              required
            />
          </div>
        </div>
        <!-- submit button -->
        <div>
          <br />
          <button class="btn btn-info" type="submit">Update Hardware Type</button>
          <!--Go Back button-->
          <!-- Router function goes to previous page-->
          <button type="reset" class="btn btn-danger ml-1" @click="$router.go(-1)">
            Go back
          </button>
        </div>
      </form>
    </div>
    <br />
    <br />
    <div class="jumbotron vertical center">
      <div class="container">
        <div class="col-sm-12">
          <hr />
          <h4>Hardware That Are {{ hardwaretype.htype_name }}s</h4>
          <br />
          <table class="table table-hover">
            <!-- Table Head-->
            <thead>
              <tr>
                <!--Table Head cells-->
                <!-- Consider changing ISO Company ID to ISO Company if dropdown is implemented. Otherwise, leave as is.-->
                <th scope="col">Hardware Name</th>
                <th scope="col">Model Number</th>
              </tr>
            </thead>
            <tbody>
              <!-- Takes every entry stored in beginning pull request and loads into table rows -->
              <tr v-for="item in reportData" :value="item.HARDWARE">
                <td>{{ item.HARDWARE }}</td>
                <td>{{ item.MODELNUMBER }}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </main>
</template>
