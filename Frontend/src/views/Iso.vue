<script>
let apiURL =`http://localhost:5000/api/iso`;
import axios from "axios";
export default {
  data() {
    return {
      iso: {
        iso_id: "",
        iso_company: ""
      },
      isoData:[]
    }
  },
  /* once axios is mounted, automatically sends get request to pull all ISOs */
  mounted(){
    /* array to store response data */
    this.isoData = [];
    axios.get(apiURL + '/all')
      /* takes response from get request and compiles it into array */
      .then((resp) => {
        this.isoData = resp.data;
      });
    },
    methods: {
      /* method to handle form submission*/
      async submitForm() {
        axios
          /* sends POST request through axios to backend, alerts user of success, then reloads page through router */        
          .post(apiURL, this.iso)
          .then(() => {
            alert("ISO has been succesfully added.");
            /* reloads window to show changes */
            window.location.reload(); 
          })
          .catch((error) => {
            console.log(error);
          });
    },
    /* method for deleting iso */
    deleteISO(isoid) {
      if(confirm("Are you sure you want to permanently delete this ISO? This cannot be undone.")){
        /* axios delete request, uses api URL and attaches id at end of it to specify what id to delete */
        axios.delete(apiURL+"?id=" + isoid).then(() => {
          /* reloads window to show changes */
          window.location.reload();
        });
      }
    },
    /* method for routing to edit page */
    editISO(ISO_ID) {
      /* Activates on click of table property, routes to update page bases on name in index.js, params are the id of the item which is stored in id:  */
      this.$router.push({ name: "updateiso", params: {id: ISO_ID}})
    },
  },
}

</script>

<!--Styling of the ISO webpage-->
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
    <main class="iso-page">
        <h1>ISO</h1>
        <br>
        <div>
          <!-- @submit.prevent stops the submit event from reloading the page-->
          <form @submit.prevent="submitForm">
            <legend>Add New ISO Company</legend>
              <!-- form field -->
              <div class="form-group col-sm-2">
                <label class="form-label mt-4">
                  <!-- asterisk to denote required field-->
                  <span style="color:#ff0000">* </span>
                  <span class="text">ISO Company</span></label>
                  <div class="col-sm-10">
                    <input
                    type="text" class="form-control"
                    v-model="iso.iso_company"
                    placeholder="Name"/>
                  </div>
                  </div>
              <!-- submit button -->
              <div>
                <br>
                <button class="btn btn-info" type='submit'>Add ISO Company</button>
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
                      <h4>All Current ISOs</h4>
                      <br />
                        <table class="table table-hover">
                            <!-- Table Head-->
                            <thead>
                                <tr>
                                    <!--Table Head cells-->
                                    <th scope="col">Name</th>
                                    <th scope="col">Action</th>
                                </tr>
                            </thead>
                            <tbody>
                                <!-- Takes every entry stored in beginning pull request and loads into table rows -->
                                <tr v-for="item in isoData" :key="item.ISO_ID">
                                    <td> {{ item.ISO_COMPANY }} </td>
                                    <td> 
                                        <div class="btn-group" role="group">
                                            <!--Update Button-->
                                            <button
                                              type="button"
                                              class="btn btn-info btn-sm"
                                              @click="editISO(item.ISO_ID)"
                                            >
                                              Update
                                            </button>

                                            <!--Delete Button-->
                                            <button
                                              type="button"
                                              class="btn btn-danger btn-sm" 
                                              @click ="deleteISO(item.ISO_ID)"
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