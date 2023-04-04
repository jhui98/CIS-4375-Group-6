<template>
    <main class="Merchants-page">
        <h1>Merchants</h1>
        <br>
        <p>This is the Merchants page</p>
        <br>

        <label class="block">
            <p>Enter Company ID: 
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
    <!-- Display Found Data -->
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
              <tr v-for=" iso in isoData" :key="iso.ISO_ID">
                <td class="p-2 text-left" >{{ iso.id }}</td>
                <td class="p-2 text-left" >{{ iso.name }}</td>
              </tr>
          </tbody>
        </table>
      </div>



    </div>

    </main>
</template>


<script>

import axios from 'axios';

export default {
  data() {
    return {
      isoData: {},
      ISO_ID:[],
      ISO_COMPANY:[],
      loading: false,
      error: null,
    };
  },
    methods: {
      async fetchData() {
        try {
          this,error = null;
          this.loading = true;

          const url='http://127.0.0.1:5000/api/iso/all';
          const resp = await axios.get(url);

          this.isoData = resp.data;
          this.ISO_ID = resp.data.map((iso) =>iso.id);
          this.ISO_COMPANY = resp.data.map((iso) => iso.name);
        } catch (err){
          if (err.response) {
          // client received an error response (5xx, 4xx)
          this.error = {
            title: "Server Response",
            message: err.message,
          };
        } else if (err.request) {
          // client never received a response, or request never left
          this.error = {
            title: "Unable to Reach Server",
            message: err.message,
          };
        } else {
          // There's probably an error in your code
          this.error = {
            title: "Application Error",
            message: err.message,
          };
        }
        }
        this.loading = false;
      },
    },
    mounted () {
      this.fetchData();
    },
};
</script>