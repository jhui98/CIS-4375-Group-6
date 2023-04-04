<script>
import axios from "axios";
export default {
  data() {
    return {
      hardwaretype: {
        htype_name: ""
      }
    }
  },
  methods: {
    async handleSubmitForm() {
        let apiURL =`http://localhost:5000/api/hardware_type`;
        axios
          .post(apiURL, this.hardwaretype)
          .then(() => {
            alert("Hardware Type has been succesfully added.");
            this.$router.push("/hardwaretype");
            this.hardwareType = {
              htype_name: "",
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
    <main class="HardwareType-page">
        <h1>HardwareType</h1>
        <br>
        <p>This is the Hardware Type input form</p><br>
        <div>
          <!-- @submit.prevent stops the submit event from reloading the page-->
          <form @submit.prevent="handleSubmitForm">
              <!-- form field -->
              <div>
                <label class="block">
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
    </main>
</template>