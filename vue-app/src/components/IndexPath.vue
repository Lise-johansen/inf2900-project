/**
 * The template block of the IndexPath component.
 * This component represents the main template of the IndexPath component.
 */

 <template>
	<div>
        <h1 class="headline">Find your next rental below:</h1>
		<search-filter @filter="applyFilter" />
		<SmallListing v-for="item in filteredItems" :key="item.id" :imageUrl="item.imageUrl" :title="item.title" :location="item.location" />
        <FilterButtons />
        <ListingCarousel />
        <ListingCarousel />
        <ListingCarousel />
        <ListingCarousel />
        <ListingCarousel />
    
    </div>
</template>

<script>
	import SearchFilter from './SearchFilter.vue';
	import SmallListing from './SmallListing.vue';
    import FilterButtons from './FilterButtons.vue';
    import ListingCarousel from './ListingCarousel.vue';


	export default {
		name: 'App',
		components: { SearchFilter, SmallListing, FilterButtons, ListingCarousel},
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
	.headline {
		font-family: 'louis_george_cafe', sans-serif;
		text-align: center;
		background: linear-gradient(to right, #ff5733, #ffa500, #4169e1);
		-webkit-text-fill-color: transparent;
		-webkit-background-clip: text;
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

</style>

