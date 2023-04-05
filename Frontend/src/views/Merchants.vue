<script>
import axios from "axios";
export default {
  data() {
    return {
      isoData: []
    }
  },
  mounted() {
    /* sends GET request through axios to recieve data from ISO table */   
    axios.get(`http://localhost:5000/api/iso/all`)
        /* Holds data in variable isoData, used to fill in table */        
        .then(response => this.isoData = response.data)
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
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 12px;
  margin: 4px 2px;
  cursor: pointer;
}

</style>

<template>
    <main class="Merchants-page">
        <h1>Merchants</h1>
        <br>
        <p>This is the Merchants page</p>
        <br>

        <label class="block">
            <p>Enter Company ID: {{ message }}
                <input
                    v-model="message"
                type="text"
                class="w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
                placeholder="Enter Company name here"
                
                />
            </p>
            <button class="add" type='submit'>Add</button>
            <button class="edit" type='submit'>Edit</button>
            <button class="delete" type='submit'>Delete</button>
          </label>


        <hr class="mt-10 mb-10" />
 
     Display Found Data
    <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-x-6 gap-y-10">

      <div class="flex flex-col col-span-2">
        <table class="min-w-full shadow-md rounded">
          <thead class="bg-gray-50 text-xl">
            <tr>
                <th class="p-4 text-left">ISO ID</th>
                <th class="p-4 text-left">ISO Company Name</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-gray-300">
            <tr v-for="item in isoData" :key="item.ISO_ID">
              <td class="p-2 text-left" > {{ item.ISO_ID }}</td>
              <td class="p-2 text-left" > {{ item.ISO_COMPANY }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    </main>
</template>