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
