<<<<<<< HEAD
<template>
	<div id="app">
		<header>
			<RentopiaHeader />
		</header>
		<router-view/>
	</div>
</template>
  
<script>
	import RentopiaHeader from './components/RentopiaHeader.vue';
  
	export default {
		name: 'App',
		components: { RentopiaHeader }
	};
</script>
  
<style>
	#app {
		font-family: Avenir, Helvetica, Arial, sans-serif;
		-webkit-font-smoothing: antialiased;
		-moz-osx-font-smoothing: grayscale;
		text-align: center;
		color: #2c3e50;
		margin: 0;
		padding: 0;
	}
</style> 
=======
/**
 * This is the main component that renders the matched route component.
 * It also imports the redirectToLogin component that we created earlier.
 * The template block of the App component contains the router-view element that renders the matched route component.
 * The script block of the App component imports the redirectToLogin component and registers it as a local component.
 * 
 */

<template>
  <div id="app">
    <header>
      <RentopiaHeader />
      <search-filter @filter="applyFilter" />
    </header>
    <router-view/> <!-- This will render the currently active route component (login or register) -->
  </div>
</template>


<script>
  import RentopiaHeader from './components/RentopiaHeader.vue';
  import SearchFilter from './components/SearchFilter.vue';
  
  export default {
    name: 'App',
    components: { RentopiaHeader, SearchFilter },
    data() {
      return {
        filteredItems: []
      };
    },
    methods:
    {
      applyFilter(filteredItems)
      {
        this.filteredItems = filteredItems;
      },
    },
  };  
</script>

<style>
  #app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin: 0;
    padding: 0;
  }
</style>
>>>>>>> 2ee7ca78f5fdced1e7a9f44d3c04b8ce53b0650e
