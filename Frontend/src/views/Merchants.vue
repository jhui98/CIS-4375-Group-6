<template>
    <main class="Merchants-page">
        <h1>Merchants</h1>
        <br>
        <p>This is the Merchants page</p>
        <br>

        <label class="block">
            <input
              type="text"
              class="w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
              placeholder="Enter Company name here"
              
            />
          </label>


        <hr class="mt-10 mb-10" />
    <!-- Display Found Data -->
    <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-x-6 gap-y-10">

      <div class="flex flex-col col-span-2">
        <table class="min-w-full shadow-md rounded">
          <thead class="bg-gray-50 text-xl">
            <tr>
              <th class="p-4 text-left">ISO Company Name</th>

            </tr>
          </thead>
          <tbody class="divide-y divide-gray-300">
            <!-- <tr v-for="(ISO, index) in isos" :key="index">
              <td class="p-2 text-left" v-text="iso.iso_company"></td>
            </tr> -->
          </tbody>
        </table>
      </div>
    </div>

    </main>
</template>

<!-- <script>
    new VUE({
        el: '#app',
        data: {
            isos: []
        },
        methods: {
            getISO() {
                const URL = "http://127.0.0.1:5000/api/iso/all";
                axios
                .get(URL)
                .then( res => {
                    this.isos = res.data.data;
                })
            }
        },
        mounted() {
            this.getISO();
        }
    })


</script> -->