<script>
import axios from "axios";
let getURL =`http://localhost:5000/api/iso?id=`;
let updateURL = 'http://localhost:5000/api/iso';
let reportURL =`http://localhost:5000/api/SevenOne?id=`;

export default {
    /*prop contains id from ISO page, used for route params  */
    props:["id"],
    data() {
        return{
            iso: {
                iso_id:"",
                iso_company: ""
            },
            sevenOne: {
                iso_id: "",
                reseller_id: "",
                reseller_name: "",
                reseller_email: "",
                reseller_phone: ""
            },
            data:[],
            reportData:[],
            dataReady:false,
        }
            
    },
    /* Before mount we collect data from GET api based on id*/
    async mounted() {
        await axios
        /* Adds our route param, the ID of the ISO selected, to GET API */
            .get(getURL+this.$route.params.id
            )
            /* Takes API data and stores Table variables into Data variables */
            .then((resp) => {
                let data = resp.data[0];
                this.iso.iso_company = data.ISO_COMPANY;
                this.iso.iso_id = data.ISO_ID;
            });
        this.reportData = [];
        axios
            .get(reportURL+this.$route.params.id)
            .then((resp) => {
                this.reportData = resp.data;
                console.log(this.reportData)
            });
        this.dataReady = true;
    },
    /* Method to update ISO*/
    methods: {
        updateISO(){
            axios
            /* Uses full property, this.X, and not sub properties, this.X.X to run call */
            /* Runs call with all data collected in GET call */
            /*Needed to run this way due to ID being used in JSON for updates */
            .put(updateURL,this.iso)
            .then(() => {alert("ISO has been updated");
                    /* After Alert goes back to the main page for ISO */
                    window.history.go(-1);
        })
        }
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
      <div v-if="dataReady">
        <h1>Update {{ iso.iso_company }}</h1>
            
            <div>
            <!-- @submit.prevent stops the submit event from reloading the page-->
            <form @submit.prevent="updateISO">
                <!-- form field -->
                <div>
                    <label class="block">
                    <!-- asterisk to denote required field-->
                    <span style="color:#ff0000">* </span>
                    <span class="text-gray-700">ISO Company: </span>
                    <!-- Autofills input field based on data from beforeMount GET Call-->
                    <input
                        type="text"
                        placeholder
                        v-model="iso.iso_company"
                   
                    />
                    </label>
                <!-- submit button -->
                <div>
                    <button class="edit" type='submit'>Update</button>
                    <!--Go Back button-->
                    <!-- Router function goes to previous page-->
                    <button
                    type="reset"
                    class="delete"
                    @click="$router.go(-1)"
                    >Go back</button>
                </div>
                </div>
            </form>
            </div>
        <h3>Resellers Associated With {{ iso.iso_company }}</h3>
        <table class="table table-hover">
                    <!-- Table Head-->
                    <thead>
                      <tr>
                        <!--Table Head cells-->
                        <!-- Consider changing ISO Company ID to ISO Company if dropdown is implemented. Otherwise, leave as is.-->
                        <th scope="col">Reseller Name</th>
                        <th scope="col">Reseller Email</th>
                        <th scope="col">Reseller Phone Number</th>
                      </tr>
                    </thead>
                    <tbody>
                       <!-- Takes every entry stored in beginning pull request and loads into table rows -->
                      <tr v-for="item in reportData" :value="item.iso_company">
                        <td>{{ item.reseller_name }}</td>
                        <td>{{ item.reseller_email }}</td>
                        <td>{{ item.reseller_phone }}</td>
                      </tr>

                    </tbody>
                  </table>
      </div>
    </main>
</template>