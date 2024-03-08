<template>
	<div id="app">
		<header>
			<RentopiaHeader />
		</header>
		<footer>
			<RentopiaFooter />
		</footer>
		<router-view/>
	</div>
</template>
  
<script>
	import RentopiaHeader from './components/RentopiaHeader.vue';
	import RentopiaFooter from './components/RentopiaFooter.vue';
	export default {
		name: 'App',
		components: { RentopiaHeader, RentopiaFooter}
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