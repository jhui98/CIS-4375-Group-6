<script>
import axios from "axios";
export default {
  data() {
    return {
      iso: {
        iso_company: ""
      }
    }
  },
  methods: {
    /* method to handle form submission*/
    async submitForm() {
        let apiURL =`http://localhost:5000/api/iso`;
        axios
          /* sends POST request through axios to backend, alerts user of success, then reloads page through router */        
          .post(apiURL, this.iso)
          .then(() => {
            alert("ISO has been succesfully added.");
            this.$router.push("/iso");
            this.iso = {
              iso_company: "",
            };
          })
          .catch((error) => {
            console.log(error);
          });
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
    <main class="iso-page">
        <h1>HardwareType</h1>
        <br>
        <p>This is the ISO input form</p><br>
        <div>
          <!-- @submit.prevent stops the submit event from reloading the page-->
          <form @submit.prevent="submitForm">
              <!-- form field -->
              <div>
                <label class="block">
                  <!-- asterisk to denote required field-->
                  <span style="color:#ff0000">* </span>
                  <span class="text-gray-700">ISO Company: </span>
                  <input
                    type="text"
                    v-model="iso.iso_company"
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
                        <p> Header</p>

                        <table class="table table-hover">
                            <!-- Table Head-->
                            <thead>
                                <tr>
                                    <!--Table Head cells-->
                                    <th scope="col">ID</th>
                                    <th scope="col">Name</th>
                                    <th scope="col">Action</th>

                                </tr>
                            </thead>
                            <tbody>
                                <tr v-for="item, ISO_ID in isoData" :key="ISO_ID">
                                    <td> {{item.ISO_ID}} </td>
                                    <td> {{ item.ISO_COMPANY }} </td>
                                    <td> 
                                        <div class="btn-group" role="group">
                                            <button type="button" class="btn btn-info
                                            btn-sm">Update</button>
                                            <button type="button" class="btn btn-danger
                                            btn-sm" @click ="deleteISO(buttonid)">Delete</button>
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