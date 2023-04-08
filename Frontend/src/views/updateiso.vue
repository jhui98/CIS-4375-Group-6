<script>
import axios from "axios";
let apiURL =`http://localhost:5000/api/iso?id=`;

export default {
    props:["id"],
    data() {
        return{
            iso: {
                iso_company: ""
            }
        }
            
    },
    beforeMount() {
        axios
            .get(apiURL+this.$route.params.id
            )
            
            .then((resp) => {
                let data = resp.data[0];
                this.iso.iso_company = data.ISO_COMPANY;
                console.log(data)
            });
    },
    methods: {
        updateISO(){
            axios
            .put(apiURL+this.$route.params.id)
            .then(() => alert("ISO has been updated"))
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
        <h1> this is the update page for ISOs</h1>

            <div>
            <!-- @submit.prevent stops the submit event from reloading the page-->
            <form @submit.prevent="updateISO">
                <!-- form field -->
                <div>
                    <label class="block">
                    <!-- asterisk to denote required field-->
                    <span style="color:#ff0000">* </span>
                    <span class="text-gray-700">ISO Company: </span>
                    <input
                        type="text"
                        placeholder
                        v-model="iso.iso_company"
                   
                    />
                    </label>
                <!-- submit button -->
                <div>
                    <button class="edit" type='submit'>Update</button>
                </div>
                </div>
            </form>
            </div>
    </main>
</template>