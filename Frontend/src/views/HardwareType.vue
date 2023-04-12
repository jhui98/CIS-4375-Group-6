<script>
let apiURL = `http://localhost:5000/api/hardware_type`;
import axios from "axios";
export default {
  data() {
    return {
      hardwaretype: {
        htype_id: "",
        htype_name: ""
      },
      htData:[]
    }
  },
/* once axios is mounted, automatically sends get request to pull all hardware types */
  mounted(){
    this.htData = [];
    axios.get(apiURL + '/all')
    /* array to store response data */
    .then((resp) => {
      /* takes response from get request and compiles it into array */
      this.htData = resp.data;
    });
  },
  methods: {
    /* method to handle form submission*/
    async submitForm() {       
        axios
          /* sends POST request through axios to backend, alerts user of success, then reloads page through router */
          .post(apiURL, this.hardwaretype)
          .then(() => {
            alert("Hardware Type has been succesfully added.");
            window.location.reload();
          })
          .catch((error) => {
            console.log(error);
          });
    },
    /* method for deleting hardware type */
    deleteHtype(htypeid) {
      if(confirm("Are you sure you want to permanently delete this Hardware Type? This cannot be undone.")){
      /* axios delete request, uses api URL and attaches id at end of it to specify what id to delete */ 
        axios.delete(apiURL+"?id=" + htypeid).then(() => {
          /* reloads window to show changes */
          window.location.reload();
        });
      }
    },
    /* method for routing to edit page */
    editHTYPE(htype_id) {
      /* Activates on click of table property, routes to update page bases on name in index.js, params are the id of the item which is stored in id:  */
      this.$router.push({ name: "updatehtype", params: {id: htype_id}})
    },

  },
}

</script>

<!--Styling of the Hardware Type webpage-->
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

<template>
    <main class="HardwareType-page">
        <h1>Hardware Type</h1>
        <br>
        <div>
          <!-- @submit.prevent stops the submit event from reloading the page-->
          <form @submit.prevent="submitForm">
            <legend>Register New Hardware Type </legend>
              <!-- form field -->
              <div class="form-group col-sm-2">
                <label class="form-label mt-4">
                  <!-- asterisk to denote required field-->
                  <span style="color:#ff0000">* </span>
                  <span class="text">Hardware Type Name</span></label>
                    <div class="col-sm-10">
                    <input
                      type="text" class="form-control"
                      v-model="hardwaretype.htype_name"
                      placeholder="Name"/>
                    </div>
                    </div>
              <!-- submit button -->
              <div>
                <br>
                <button class="btn btn-info" type='submit'>Add Hardware Type</button>
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
                  <h4>All Current Hardware Types</h4>
                  <br />
                  <table class="table table-hover">
                    <!-- Table Head-->
                    <thead>
                      <tr>
                        <!--Table Head cells-->
                        <th scope="col">Hardware Type</th>
                        <th scope="col">Action</th>
                      </tr>
                    </thead>
                    <tbody>
                       <!-- Takes every entry stored in beginning pull request and loads into table rows -->
                      <tr v-for="item in htData" :key="item.htype_id">
                        <!-- Adds click functionality to table rows, runs Edit function based on ID of row -->
                        <!-- Placed in TD due to runnig both edit and delete when in TD-->
                        <td @click="editHTYPE(item.htype_id)">{{ item.htype_name }}</td>
                        <td>
                          <div class="btn-group" role="group">
                            <button type="button" class="btn btn-info btn-sm" 
                            @click="editHTYPE(item.htype_id)">Update</button>
                            <button type="button" class="btn btn-danger
                            btn-sm" @click="deleteHtype(item.htype_id)">Delete</button>
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