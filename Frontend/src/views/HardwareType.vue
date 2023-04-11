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
    <main class="HardwareType-page">
        <h1>HardwareType</h1>
        <br>
        <p>This is the Hardware Type input form</p><br>
        <div>
          <!-- @submit.prevent stops the submit event from reloading the page-->
          <form @submit.prevent="submitForm">
              <!-- form field -->
              <div>
                <label class="block">
                  <!-- asterisk to denote required field-->
                  <span style="color:#ff0000">* </span>
                  <span class="text-gray-700">Hardware Type Name: </span>
                  <input
                    type="text"
                    v-model="hardwaretype.htype_name"
                    placeholder="Name"
                  />
                </label>
              <!-- submit button -->
              <div>
                <button class="add" type='submit'>Add</button>
              </div>
            </div>
          </form>
        </div>

        <div class="jumbotron vertical center">
          <div class="container">

              <div class="row">
                <div class="col-sm-12">
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