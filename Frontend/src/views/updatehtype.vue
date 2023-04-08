<script>
import axios from "axios";
let getURL =`http://localhost:5000/api/hardware_type?id=`;
let updateURL = 'http://localhost:5000/api/hardware_type';

export default {
    /*prop contains id from Hardware Type page, used for route params  */
    props:["id"],
    data() {
        return{
            hardwaretype: {
                htype_id: "",
                htype_name: ""
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
                this.hardwaretype.htype_name = data.htype_name;
                this.hardwaretype.htype_id = data.htype_id;
                console.log(data)
            });
    },
    methods: {
        updateHTYPE(){
            axios
            /* Uses full property, this.X, and not sub properties, this.X.X to run call */
            /* Runs call with all data collected in GET call */
            /*Needed to run this way due to ID being used in JSON for updates */
            .put(updateURL,this.hardwaretype)
            .then(() => {alert("Hardware Type has been updated");
                    /* After Alert goes back to the main page for Hardware Type */
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
        <h1> this is the update page for Hardware Types</h1>
            
            <div>
            <!-- @submit.prevent stops the submit event from reloading the page-->
            <form @submit.prevent="updateHTYPE">
                <!-- form field -->
                <div>
                    <label class="block">
                    <!-- asterisk to denote required field-->
                    <span style="color:#ff0000">* </span>
                    <span class="text-gray-700">Hardware Type: </span>
                    <!-- Autofills input field based on data from beforeMount GET Call-->
                    <input
                        type="text"
                        placeholder
                        v-model="hardwaretype.htype_name"
                   
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