<script>
export default {
  data() {
    return {
      message: ''
    }
  }
}
</script>

<style>
.edit {
  background-color: #4CAF50; /* Green */
}
.add {
  background-color: #008CBA; /* Blue */
}
.delete {
  background-color: #f44336; /* Red */
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