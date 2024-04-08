/**
 * The template block of the IndexPath component.
 * This component represents the main template of the IndexPath component.
 */

 <template>
	<div>
		<h1 class="headline">Find your next rental below:</h1>
		<search-filter @filter="applyFilter" />
		<SmallListing v-for="item in filteredItems" :key="item.id" :imageUrl="item.imageUrl" :title="item.title" :location="item.location" />
	</div>
    <div>
		<input type="number" v-model="inputNumber" placeholder="Enter a number" />
		<button @click="handleButtonClick">Submit</button>
	</div>    
</template>

<script>
	import SearchFilter from './SearchFilter.vue';
	import SmallListing from './SmallListing.vue';
    import axios from 'axios';


	export default {
		name: 'App',
		components: { SearchFilter, SmallListing },
		data() {
			return {
				filteredItems: [],
                inputNumber: null
			};
		},
        created() {
            // Call the method to redirect if the user is not logged in
            this.redirectIfLoggedIn();
        },
		methods: {
			applyFilter(filteredItems) {
				this.filteredItems = filteredItems;
			},
            handleButtonClick(){
                axios.delete(`http://localhost:8080/api/delete_item/${this.inputNumber}`)
                .then(response => {
                    console.log(response);
                })
                .catch(error => {
                    console.log(error);
                }); 
            },
            redirectIfLoggedIn() {
                // Redirect to login page if user is not logged in
                console.log('Checking if user is logged in...');
                const token = this.getTokenFromCookies();
                if (token === 'undefined') {
                    // Token is not found in cookies (user is not logged in)
                    if (confirm('You must be logged in to view this page.')) {
                        this.$router.push('/login'); 
                    }
                }
            },
            // Get the token from the cookies
            getTokenFromCookies() {
                const cookies = document.cookie.split('; ');
                for (const cookie of cookies) {
                    const [name, value] = cookie.split('=');
                    if (name === 'token') {
                    return value;
                    }
                }
                return null; // Token not found in cookies
                }
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