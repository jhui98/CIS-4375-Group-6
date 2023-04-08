<template>
  <div class="create-service">
    <!-- header thing with styling to match other parts -->
    <h1 class="font-bold text-4xl text-red-700 tracking-widest text-center mt-10">
      {{ titleText }}
    </h1>
    <div class="px-10 pt-10"></div>
    <!-- form for the data name,description, status -->
    <form @submit.prevent="submitForm">
      <label class="text-2xl font-bold">
        Service Name:
        <input
          class="w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
          type="text"
          v-model="service.name"
          required
        />
        <!-- each part is required  -->
      </label>
      <label class="text-2xl font-bold">
        Description:
        <input
          class="w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
          type="text"
          v-model="service.description"
          required
        />
      </label>
      <label class="text-2xl font-bold">
        Active Status:
        <input
          class="rounded border-gray-300 text-indigo-600 shadow-sm focus:border-indigo-300 focus:ring focus:ring-offset-0 focus:ring-indigo-200 focus:ring-opacity-50"
          notchecked
          type="checkbox"
          v-model="service.active"
        />
      </label>
      <div class="button-group">
        <button class="submit-button bg-red-700 text-white rounded" type="submit">
          <!-- submit button! -->
          {{ buttonText }}
        </button>
        <!--- @wakindo: Guys, I just added a Go Back button here so user can go back to list of merchants when they are done adding new one(s) instead of doing an auto reload -->
        <button
          type="reset"
          class="border border-red-700 bg-white text-red-700 rounded"
          @click="$router.back()"
        >
          Go back
        </button>

        <button class="clear-button" type="button" @click="clearForm">Clear</button>
        <!-- a button to clear incase the person is to lazy to hit backspace -->
      </div>
    </form>
    <p v-if="showSuccessMessage" class="success-message">Service Successfully Added!</p>
  </div>
</template>

<script>
export default {
  props: {
    selectedService: {
      type: Object,
      default: null,
    },
    // prop to get the data to the list vue table data
  },
  data() {
    return {
      service: this.selectedService || {
        name: "",
        description: "",
        active: true,
      },
      showSuccessMessage: false,
      showUpdateMessage: false, // added variable for update message
    };
  },
  computed: {
    buttonText() {
      return this.selectedService ? "Update Entry" : "Create Service";
    },
    titleText() {
      return this.selectedService ? "Update Service" : "Create Service";
    },
  },

  // is it an update or creation?
  methods: {
    // what to do it u submit
    submitForm() {
      let createdServices = JSON.parse(localStorage.getItem("createdServices")) || [];
      if (this.selectedService) {
        createdServices[this.$route.params.index] = this.service;
        this.showUpdateMessage = true;
      } else {
        createdServices.push(this.service);
        this.showSuccessMessage = true;
        this.service = { name: "", description: "", active: true };
        setTimeout(() => {
          this.showSuccessMessage = false;
        }, 2000); // hide success message after 2 seconds
      }
      localStorage.setItem("createdServices", JSON.stringify(createdServices));
      if (this.selectedService) {
        this.$router.push({ name: "CreatedServicesList" });
      }
    },

    clearForm() {
      this.service = { name: "", description: "", active: true };
      this.showSuccessMessage = false;
      this.showUpdateMessage = false;
    },
  },
};
</script>

<style>
label {
  display: block;
  margin-bottom: 10px;
}

.create-service {
  max-width: 500px;
  margin: 0 auto;
}

.button-group {
  display: flex;
  justify-content: space-between;
}

.submit-button {
  color: #fff;
  padding: 8px 16px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.clear-button {
  background-color: #ccc;
  color: #000;
  padding: 8px 16px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.success-message {
  color: green;
  margin-top: 10px;
}
</style>
