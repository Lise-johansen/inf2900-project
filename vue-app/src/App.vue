<template>
	<section class="background-section">
			<div class="air air1"></div>
			<div class="air air2"></div>
			<div class="air air3"></div>
			<div class="air air4"></div>
		</section>
		<RentopiaHeader />
		<main>
			<router-view/>
		</main>
		<RentopiaFooter/>
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

body, * {
margin: 0;
padding: 0;
}

	#app {
		display: flex;
		min-height: 100vh;
		flex-direction: column;
	}

	main{
		font-family: Avenir, Helvetica, Arial, sans-serif;
		-webkit-font-smoothing: antialiased;
		-moz-osx-font-smoothing: grayscale;
		text-align: center;
		color: #2c3e50;
		flex: 1;
	}
	
	section{
		position: relative;
		width: 100%;
		height: 100vh;
		background: #eeecec;
		overflow: hidden;
	}
	section .air{
		position: absolute;
		bottom: 0;
		left: 0;
		width: 100%;
		height: 100px;
		background: url(https://1.bp.blogspot.com/-xQUc-TovqDk/XdxogmMqIRI/AAAAAAAACvI/AizpnE509UMGBcTiLJ58BC6iViPYGYQfQCLcBGAsYHQ/s1600/wave.png);
		background-size: 1000px 100px
	}
	section .air.air1{
		animation: wave 30s linear infinite;
		z-index: 1000;
		opacity: 1;
		animation-delay: 0s;
		bottom: 0;
	}
	section .air.air2{
		animation: wave2 15s linear infinite;
		z-index: 999;
		opacity: 0.5;
		animation-delay: -5s;
		bottom: 10px;
	}
	section .air.air3{
		animation: wave 30s linear infinite;
		z-index: 998;
		opacity: 0.2;
		animation-delay: -2s;
		bottom: 15px;
	}
	section .air.air4{
		animation: wave2 5s linear infinite;
		z-index: 997;
		opacity: 0.7;
		animation-delay: -5s;
		bottom: 20px;
	}
	@keyframes wave{
	0%{
		background-position-x: 0px; 
	}
	100%{
		background-position-x: 1000px; 
	}
	}
	@keyframes wave2{
	0%{
		background-position-x: 0px; 
	}
	100%{
		background-position-x: -1000px; 
	}
	}
	.background-section {
		position: fixed; /* Position the background section */
		top: 0;
		left: 0;
		width: 100%;
		height: 100%;
		z-index: -1; /* Place it behind other content */
	}

</style> 