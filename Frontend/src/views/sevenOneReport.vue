<script>
import axios from "axios";
let getURL =`http://localhost:5000/api/SevenOne?id=`;

export default {
    /*prop contains id from the Reseller page, used for route params  */
    props:["id"],
    data() {
        return{
            sevenOne: {
                iso_company: "",
                reseller_email: "",
                reseller_id: "",
                reseller_name: "",
                reseller_phone: ""
            },
            reportData:[],
        }
    },
    /* Before mount we collect data from GET api based on id*/
    beforeMount() {
            this.reportData = [];
        /* Adds our route param, the ID of the ISO selected, to GET API */
            axios.get(getURL+this.$route.params.id
            )
            /* Takes API data and stores Table variables into Data variables */
            .then((resp) => {
                this.reportData = resp.data;
            });
    },
    methods: {
    }
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
  text-align: 
  center;
  text-decoration: none;
  display: inline-block;
  font-size: 12px;
  margin: 4px 2px;
  cursor: pointer;
}
</style>

<template>
    <main>
        <h1>Update Reseller</h1>
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
                        <th scope="col">Iso Company</th>
                        <th scope="col">Reseller Name</th>
                        <th scope="col">Reseller ID</th>
                        <th scope="col">Reseller Email</th>
                        <th scope="col">Reseller Phone Number</th>
                      </tr>
                    </thead>
                    <tbody>
                       <!-- Takes every entry stored in beginning pull request and loads into table rows -->
                      <tr v-for="item in reportData" :key="item.iso_company">
                        <td>{{ item.iso_company }}</td>
                        <td>{{ item.reseller_name }}</td>
                        <td>{{ item.reseller_id }}</td>
                        <td>{{ item.reseller_email }}</td>
                        <td>{{ item.reseller_phone }}</td>
                      </tr>

                    </tbody>
                  </table>

                </div>
              </div>

          </div>

        </div>
                <div>
                    <!-- Router function goes to previous page-->
                    <button type="reset" class="delete" @click="$router.go(-1)">Go back</button>
                </div>
    </main>
</template>