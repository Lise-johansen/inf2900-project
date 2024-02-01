
/**
 * This is the main component that renders the matched route component.
 * It also imports the redirectToLogin component that we created earlier.
 * The template block of the App component contains the router-view element that renders the matched route component.
 * The script block of the App component imports the redirectToLogin component and registers it as a local component.
 * 
 */

<template>
  <div id="app">
    <router-view></router-view> <!-- This renders the matched route component -->
  </div>
</template>


<script>
import redirectToLogin from '@/components/IndexPath.vue'; // Adjust the path based on your project structure


export default {
  name: 'App',
  components: {
    // eslint-disable-next-line vue/no-unused-components
    redirectToLogin,
    
  }
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

