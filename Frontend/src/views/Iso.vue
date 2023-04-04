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
    </main>
</template>