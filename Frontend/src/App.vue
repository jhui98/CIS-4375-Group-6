<template>
  <div class="app">
      <Sidebar/>

      <RouterView/>

  </div>
</template>

<script setup>
import Sidebar from "./components/Sidebar.vue"




</script>



<style lang="scss">

:root {
	--primary: #5dee92;
	--primary-alt: #22c55e;
	--grey: #64748b;
	--dark: #010107;
	--dark-alt: #334155;
	--light: #f1f5f9;
	--sidebar-width: 300px;
}
* {
	margin: 0;
	padding: 0;
	box-sizing: border-box;
	font-family: 'Fira sans', sans-serif;
}
body {
	background: var(--light);
}
button {
	cursor: pointer;
	appearance: none;
	border: none;
	outline: none;
	background: none;
}

.app {
  display: flex;

  Main {
        flex: 1 1 0;
        padding: 2rem;

        @media (max-width: 786px) {
          padding-left: 6rem;
        }
  }
}
</style>
