<script>
let apiURL = `http://localhost:5000/api/reseller`;
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
      resellerData:[]
    }
  },
/* once axios is mounted, automatically sends get request to pull all resellers */
  mounted(){
    this.resellerData = [];
    axios.get(apiURL + '/all')
    /* array to store response data */
    .then((resp) => {
      /* takes response from get request and compiles it into array */
      this.resellerData = resp.data;
    });
  },
  methods: {
    /* method to handle form submission*/
    async submitForm() {       
        axios
          /* sends POST request through axios to backend, alerts user of success, then reloads page through router */
          .post(apiURL, this.reseller)
          .then(() => {
            alert("Reseller has been succesfully added.");
            window.location.reload();
          })
          .catch((error) => {
            console.log(error);
          });
    },
    /* method for deleting hardware type */
    deletereseller(resellerid) {
      if(confirm("Are you sure you want to permanently delete this Reseller? This cannot be undone.")){
      /* axios delete request, uses api URL and attaches id at end of it to specify what id to delete */ 
        axios.delete(apiURL+"?id=" + resellerid).then(() => {
          /* reloads window to show changes */
          window.location.reload();
        });
      }
    },
    /* method for routing to edit page */
    editreseller(reseller_id) {
      /* Activates on click of table property, routes to update page bases on name in index.js, params are the id of the item which is stored in id:  */
      this.$router.push({ name: "updatereseller", params: {id: reseller_id}})
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
    <main class="Resellers-page">
        <h1>Resellers</h1>
        <br>
        <p>This is the Reseller Input form</p><br>
        <div>
          <!-- @submit.prevent stops the submit event from reloading the page-->
          <form @submit.prevent="submitForm">
              <!-- form field -->
              <div>
                <label class="block">
                  <!-- asterisk to denote required field-->
                  <span style="color:#ff0000">* </span>
                  <span class="text-gray-700">Reseller Name (Required): </span>
                  <input
                    type="text"
                    v-model="reseller.reseller_name"
                    placeholder="Name"
                  />
                </label>
                <label class="block">
                  <!-- asterisk to denote required field-->
                  <span style="color:#ff0000"></span>
                  <span class="text-gray-700">Reseller Phone: </span>
                  <input
                    type="text"
                    v-model="reseller.reseller_phone"
                    placeholder="1234567890"
                  />
                </label>
                <label class="block">
                  <!-- asterisk to denote required field-->
                  <span style="color:#ff0000"></span>
                  <span class="text-gray-700">Reseller Email: </span>
                  <input
                    type="text"
                    v-model="reseller.reseller_email"
                    placeholder="reseller@email.com"
                  />
                </label>
                <label class="block">
                  <!-- This particular field may need to become a dropdown of existing ISO Companies, but I am not sure how to implement. Please advise.-->
                  <span style="color:#ff0000">* </span>
                  <span class="text-gray-700">ISO Company: </span>
                  <input
                    type="text"
                    v-model="reseller.iso_id"
                    placeholder="1"
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
                        <!-- Consider changing ISO Company ID to ISO Company if dropdown is implemented. Otherwise, leave as is.-->
                        <th scope="col">Name</th>
                        <th scope="col">Email</th>
                        <th scope="col">Phone Number</th>
                        <th scope="col">ISO Company ID</th>
                      </tr>
                    </thead>
                    <tbody>
                       <!-- Takes every entry stored in beginning pull request and loads into table rows -->
                      <tr v-for="item in resellerData" :key="item.reseller_id">
                        <td>{{ item.reseller_name }}</td>
                        <td>{{ item.reseller_email }}</td>
                        <td>{{ item.reseller_phone }}</td>
                        <td>{{ item.iso_id }}</td>
                        <!-- Adds click functionality to table rows, runs Edit function based on ID of row -->
                        <!-- Placed in TD due to runnig both edit and delete when in TD-->
                        <td>
                          <div class="btn-group" role="group">
                            <button type="button" class="btn btn-info btn-sm" 
                            @click="editreseller(item.reseller_id)">Update</button>
                            <button type="button" class="btn btn-danger
                            btn-sm" @click="deletereseller(item.reseller_id)">Delete</button>
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