/**
 * The template block of the IndexPath component.
 * This component represents the main template of the IndexPath component.
 */

<template>
	<div>
		<search-filter @filter="applyFilter" />
		<h1></h1>
		<SmallListing v-for="item in filteredItems" :key="item.id" :imageUrl="item.imageUrl" :title="item.title" :location="item.location" />
	</div>
</template>

/**
 * The script block of the IndexPath component.
 * This component represents the main script of the IndexPath component.
 * It contains the redirectToLogin method that redirects the user to the login page.
 */

<script>
	import SearchFilter from './SearchFilter.vue';
	import SmallListing from './SmallListing.vue';
	
	export default {
		name: 'App',
		components: { SearchFilter, SmallListing },
		data() {
			return {
				filteredItems: []
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

        h3 {
        margin: 40px 0 0;
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


        h3 {
        margin: 40px 0 0;
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

</style>
