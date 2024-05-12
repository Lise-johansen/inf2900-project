<template>
	<div>
		<div class="eyecandy-container">
			<h1 class="eyecandy-title css-selector">Rentopia: Where you can turn your unused items into someone else's next adventure!</h1>
			<h2 class="eyecandy-description">From camping gear to party supplies, let your belongings earn their keep while giving others memorable experiences.</h2>
		</div>
		<search-filter @filter="applyFilter" />
		
		<div class="reverse-divider"></div>

		<IndexFilters />
		<div class="spacing"></div>
        <FilterButtons />
        <ListingCarousel category="Furniture"/>
        <ListingCarousel category="Books"/>
        <ListingCarousel category="Clothing"/>    
		<ListingCarousel category="Electronics"/>
		<ListingCarousel category="Tools"/>
    </div>
</template>

<script>
	import SearchFilter from './SearchFilter.vue';
	import SmallListing from './SmallListing.vue';
    import ListingCarousel from './ListingCarousel.vue';
	import IndexFilters from './IndexFilters.vue';


	export default {
		name: 'App',
		components: { SearchFilter, SmallListing, ListingCarousel, IndexFilters},
		data() {
			return {
				filteredItems: [],
			};
		},
		methods: {
			applyFilter(filteredItems) {
				this.filteredItems = filteredItems;
			},
		},
	};
</script>

<style scoped>

	.spacing {
		padding: 1em;
	}
	ul {
		list-style-type: none;
		padding: 0;
	}

	li {
		display: inline-block;
		margin: 0 10px;
	}

	a {
		color: #42b983;
	}

	@font-face {
		font-family: 'louis_george_cafe';
		src: url('@/assets/louis_george_cafe.ttf') format('truetype');
		font-weight: normal;
		font-style: normal;
	}

	@font-face {
		font-family: 'louis_george_cafe';
		src: url('@/assets/louis_george_cafe.ttf') format('truetype');
		font-weight: normal;
		font-style: normal;
	}

	.eyecandy-container {
		justify-content: center;
		align-items: center;
		margin-top: 50px;
	}
	.eyecandy-title {
        align-self: flex-start;
        margin: 0;
		font-family: 'louis_george_cafe', sans-serif;
		font-size: 2.5rem;
		font-weight: 1500;
    }

	.eyecandy-description {
        font-family: 'louis_george_cafe', sans-serif;
        opacity: 0;
        animation: fadeIn 1.5s ease forwards;
        animation-delay: 1.5s; /* Add a delay of 2 seconds */
		/* cursive */
		font-size: 1.5rem;
		font-style: italic;
    }

	.divider {
        background: linear-gradient(to right, transparent, #ff5733, #ffa500, #4169e1, transparent);
    }
    
    .reverse-divider {
        background: linear-gradient(to left, transparent, #ff5733, #ffa500, #4169e1, transparent);
    }

    .divider, .reverse-divider {
        height: 3px; /* Adjust the height of the border */
        margin-top: 2em;
        margin-bottom: 2em;
        opacity: 0.8;
        width: 100%;
    }
	
    .animated-fade-in {
        opacity: 0;
        animation: fadeIn 1.5s ease forwards;
    }

    @keyframes fadeIn {
        from {
            opacity: 0;
        }
        to {
            opacity: 1;
        }
    }

	.css-selector {
		background: linear-gradient(200deg, #f75342, #f7bb42, #4276f7);
		background-size: 600% 600%;

		-webkit-animation: AnimationName 20s ease infinite;
		-moz-animation: AnimationName 20s ease infinite;
		animation: AnimationName 20s ease infinite;
		-webkit-background-clip: text;
		-webkit-text-fill-color: transparent;
	}

	@-webkit-keyframes AnimationName {
		0%{background-position:0% 50%}
		50%{background-position:100% 50%}
		100%{background-position:0% 50%}
	}
	@-moz-keyframes AnimationName {
		0%{background-position:0% 50%}
		50%{background-position:100% 50%}
		100%{background-position:0% 50%}
	}
	@keyframes AnimationName {
		0%{background-position:0% 50%}
		50%{background-position:100% 50%}
		100%{background-position:0% 50%}
	}
</style>