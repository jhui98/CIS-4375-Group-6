<script>
let apiURL = `http://localhost:5000/api/hardware`;
let dropURL = `http://localhost:5000/api/hardware_type/all`;
import axios from "axios";
export default {
  data() {
    return {
      hardware: {
        hardware_id: "",
        hardware_name: "",
        model_number: "",
        htype_id: "",
      },
      hardware_type: {
        htype_id: "",
        htype_name: "",
      },
      hardwareData: [],
      htype_data: [],
    };
  },
  /* once axios is mounted, automatically sends get request to pull all hardwares */
  async mounted() {
    this.hardwareData = [];
    await axios
      .get(apiURL + "/all")
      /* array to store response data */
      .then((resp) => {
        /* takes response from get request and compiles it into array */
        this.hardwareData = resp.data;
      }),
      (this.htype_data = []);

    await axios.get(dropURL).then((resp) => {
      this.htype_data = resp.data;
    });
  },
  methods: {
    /* method to handle form submission*/
    async submitForm() {
      console.log(this.hardware);
      axios
        /* sends POST request through axios to backend, alerts user of success, then reloads page through router */
        .post(apiURL, this.hardware)
        .then(() => {
          alert("Hardware has been succesfully added.");
          window.location.reload();
        })
        .catch((error) => {
          console.log(error);
        });
    },
    /* method for deleting hardware type */
    deleteHardware(hardware_id) {
      if (
        confirm(
          "Are you sure you want to permanently delete this Hardware Type? This cannot be undone."
        )
      ) {
        /* axios delete request, uses api URL and attaches id at end of it to specify what id to delete */
        axios.delete(apiURL + "?id=" + hardware_id).then(() => {
          /* reloads window to show changes */
          window.location.reload();
        });
      }
    },
    /* method for routing to edit page */
    editHardware(hardware_id) {
      /* Activates on click of table property, routes to update page bases on name in index.js, params are the id of the item which is stored in id:  */
      this.$router.push({ name: "updatehardware", params: { id: hardware_id } });
    },
  },
};
</script>

<!--Styling of the Hardware webpage-->
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
</style>

<!--Structure of Hardware page-->
<template>
  <main class="home-page">
    <h1>Hardware Operations</h1>
    <br />
    <div>
      <!-- @submit.prevent stops the submit event from reloading the page-->
      <form @submit.prevent="submitForm">
        <legend>Register New Hardware</legend>
        <!-- form field -->
        <div class="form-group col-sm-2">
          <label class="form-label mt-4">
            <!-- asterisk to denote required field-->
            <span style="color: #ff0000">* </span>
            <span class="text">Hardware Name</span></label
          >
          <div class="col-sm-10">
            <input
              type="text"
              class="form-control"
              v-model="hardware.hardware_name"
              placeholder="Name"
              required
            />
          </div>
        </div>
        <!-- form field -->
        <div class="form-group col-sm-2">
          <label class="form-label mt-4">
            <!-- asterisk to denote required field-->
            <span style="color: #ff0000"> </span>
            <span class="text">Model Number</span></label
          >
          <div class="col-sm-10">
            <input
              type="text"
              class="form-control"
              v-model="hardware.model_number"
              placeholder="Model Number"
            />
          </div>
        </div>
        <!-- form field -->
        <div class="form-group col-sm-2">
          <label class="form-label mt-4">
            <!-- asterisk to denote required field-->
            <span style="color: #ff0000">* </span>
            <span class="text">Hardware Type</span></label
          >
          <div class="col-sm-10">
            <select class="form-select" v-model="hardware.htype_id" required>
              <option
                v-for="item in htype_data"
                :key="item.htype_id"
                :value="item.htype_id"
              >
                {{ item.htype_name }}
              </option>
            </select>
          </div>
        </div>
        <!-- submit button -->
        <div>
          <br />
          <button type="submit" class="btn btn-info">Add Hardware</button>
        </div>
      </form>
    </div>
    <br />
    <br />
    <div class="jumbotron vertical center">
      <div class="container">
        <div class="row">
          <div class="col-sm-12">
            <hr />
            <h4>All Current Hardware</h4>
            <br />
            <table class="table table-hover">
              <!-- Table Head-->
              <thead>
                <tr>
                  <!--Table Head cells-->
                  <th scope="col">Hardware Name</th>
                  <th scope="col">Model Number</th>
                  <th scope="col">Hardware Type</th>
                  <th scope="col">Action</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="item in hardwareData" :key="item.hardware_id">
                  <!--Do no show this to user-->
                  <!-- <td>{{ item.hardware_id }}</td> -->

                  <td>{{ item.hardware_name }}</td>
                  <td>{{ item.model_number }}</td>
                  <!-- Searches through all pulled hardware types and finds record that matches the item's hardware type id, then returns its name -->
                  <td>
                    {{ htype_data.find((i) => i.htype_id === item.htype_id).htype_name }}
                  </td>
                  <td>
                    <div class="btn-group" role="group">
                      <!--Update Button-->
                      <button
                        type="button"
                        class="btn btn-info btn-sm"
                        @click="editHardware(item.hardware_id)"
                      >
                        Update
                      </button>
                      <!--Delete Button-->
                      <button
                        type="button"
                        class="btn btn-danger btn-sm"
                        @click="deleteHardware(item.hardware_id)"
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
