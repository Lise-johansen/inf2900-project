
/**
 * This is the main component that renders the matched route component.
 * It also imports the redirectToLogin component that we created earlier.
 * The template block of the App component contains the router-view element that renders the matched route component.
 * The script block of the App component imports the redirectToLogin component and registers it as a local component.
 * 
 */

<template>
  <div id="app">
    <router-view/> <!-- This will render the currently active route component (login or register) -->
  </div>
</template>


<script>
export default {
  name: 'App',
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
