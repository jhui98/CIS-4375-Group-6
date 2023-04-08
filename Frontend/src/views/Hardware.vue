<script>
let apiURL = `http://localhost:5000/api/hardware`;
import axios from "axios";
export default {
  data() {
    return {
      hardwaretype: {
        hardware_id: "",
        hardware_name: "",
        model_number: "",
        htype_id: ""
      },
      hardwareData:[]
    }
  },
  /* once axios is mounted, automatically sends get request to pull all hardware */
  mounted(){
    this.hardwareData = [];
    axios.get(apiURL + '/all')
    /* array to store response data */
    .then((resp) => {
      /* takes response from get request and compiles it into array */
      this.hardwareData = resp.data;
    });
  },
  methods: {
    /* method to handle form submission*/
    async submitForm() {       
        axios
          /* sends POST request through axios to backend, alerts user of success, then reloads page through router */
          .post(apiURL, this.hardware)
          .then(() => {
            alert("Hardware has been succesfully added.");
            window.location.reload();
          })
          .catch((error) => {
            console.log(error);
          });
    },
    /* method for deleting hardware type */
    deleteHtype(hardwareid) {
      if(confirm("Are you sure you want to permanently delete this Hardware Type? This cannot be undone.")){
      /* axios delete request, uses api URL and attaches id at end of it to specify what id to delete */ 
        axios.delete(apiURL+"?id=" + hardwareid).then(() => {
          /* reloads window to show changes */
          window.location.reload();
        });
      }
    },
    /* method for routing to edit page */
    editHTYPE(hardware_id) {
      /* Activates on click of table property, routes to update page bases on name in index.js, params are the id of the item which is stored in id:  */
      this.$router.push({ name: "updatehardware", params: {id: hardware_id}})
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
    <main class="Hardware-page">
        <h1>Hardware</h1>
        <br>
        <p>This is the Hardware page</p>
        <br>
        <p>Enter a Hardware ID: {{ message }}
        <input v-model="message" placeholder="Hardware ID" /></p>
        <br>
        <button class="add" type='submit'>Add</button>
        <button class="edit" type='submit'>Edit</button>
        <button class="delete" type='submit'>Delete</button>
    </main>
</template>
