<script>
import axios from "axios";
let getURL =`http://localhost:5000/api/reseller?id=`;
let updateURL = 'http://localhost:5000/api/reseller';

export default {
    /*prop contains id from the Reseller page, used for route params  */
    props:["id"],
    data() {
        return{
            reseller: {
                iso_id: "",
                reseller_email: "",
                reseller_id: "",
                reseller_name: "",
                reseller_phone: ""
            }
        }
    },
    /* Before mount we collect data from GET api based on id*/
    beforeMount() {
        axios
        /* Adds our route param, the ID of the ISO selected, to GET API */
            .get(getURL+this.$route.params.id
            )
            /* Takes API data and stores Table variables into Data variables */
            .then((resp) => {
                let data = resp.data[0];
                this.reseller.reseller_id = data.reseller_id;
                this.reseller.reseller_name = data.reseller_name;
                this.reseller.reseller_email = data.reseller_email;
                this.reseller.reseller_phone = data.reseller_phone;
                this.reseller.iso_id = data.iso_id;
                console.log(data)
            });
    },
    methods: {
        updatereseller(){
            axios
            /* Uses full property, this.X, and not sub properties, this.X.X to run call */
            /* Runs call with all data collected in GET call */
            /*Needed to run this way due to ID being used in JSON for updates */
            .put(updateURL,this.reseller)
            .then(() => {alert("Reseller has been updated");
                    /* After Alert goes back to the main page for Reseller */
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
        <h1>Update Reseller</h1>
            
            <div>
            <!-- @submit.prevent stops the submit event from reloading the page-->
            <form @submit.prevent="updatereseller">
                <!-- form field -->
                <div>
                    <label class="block">
                    <!-- asterisk to denote required field-->
                    <span style="color:#ff0000">* </span>
                    <span class="text-gray-700">Name: </span>
                    <!-- Autofills input field based on data from beforeMount GET Call-->
                    <input
                        type="text"
                        placeholder
                        v-model="reseller.reseller_name"
                   
                    />
                    </label>
                    <label class="block">
                    <!-- asterisk to denote required field-->
                    <span style="color:#ff0000">* </span>
                    <span class="text-gray-700">Email: </span>
                    <!-- Autofills input field based on data from beforeMount GET Call-->
                    <input
                        type="text"
                        placeholder
                        v-model="reseller.reseller_email"
                   
                    />
                    </label>
                    <label class="block">
                    <!-- asterisk to denote required field-->
                    <span style="color:#ff0000">* </span>
                    <span class="text-gray-700">Phone Number: </span>
                    <!-- Autofills input field based on data from beforeMount GET Call-->
                    <input
                        type="text"
                        placeholder
                        v-model="reseller.reseller_phone"
                   
                    />
                    </label>
                    <label class="block">
                    <!-- asterisk to denote required field-->
                    <span style="color:#ff0000">* </span>
                    <span class="text-gray-700">ISO Company ID: </span>
                    <!-- Autofills input field based on data from beforeMount GET Call-->
                    <input
                        type="text"
                        placeholder
                        v-model="reseller.iso_id"
                   
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
    </main>
</template>