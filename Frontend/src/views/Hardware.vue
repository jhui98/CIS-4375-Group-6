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