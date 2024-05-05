<template>
    <div>
        <div class="spacer">
            <!-- Add a spacer to push the content below the header -->
        </div>
        <input type="text" 
        v-model="searchTerm" 
        @input="handleSearchChange" 
        placeholder="Search here!" 
        class="search-input" 
        @keyup.enter="redirectToSearchPage"
        style="padding: 0.5em 0.5em;">
        <div v-if="searchTerm.length === 0">
            <!-- Just so that the no result text doesn't show up before the user has written anything. -->
        </div>
        <div v-else>
            <div v-if="!loading && filteredItems.length > 0" class="results-container">
                <!-- Loop through each unique category -->
                <ul class="search-results">
                    <li v-for="category in uniqueCategories" :key="category">
                        <!-- Display the category name -->
                        <div class="item-category">{{ category }}</div>
                        <!-- Display the items under this category -->
                        <ul class="item-name">
                            <li v-for="item in filteredItemsByCategory(category)" :key="item.pk" class="item-name">
                                <!-- Display the item name as a clickable link -->
                                <router-link :to="'/listings/' + item.pk" class="item-link">
                                    {{ item.fields.name }}
                                </router-link>
                            </li>
                        </ul>
                    </li>
                </ul>
            </div>
            <div v-else-if="!loading && filteredItems.length === 0" class="no-results">No results found</div>
            <div v-else class="loading-text">Searching...</div>
        </div>
    </div>
</template>



<script>
    import { ref, computed } from 'vue';
    import axios from 'axios';

    export default {
        methods: {
            redirectToSearchPage() {
                if (this.searchTerm) {
                    this.$router.push({ name: 'searchPage', query: { q: this.searchTerm } });
                } else {
                // If there's no searchTerm, just go to the search page without any query
                    this.$router.push('/search-page/');
                }
            },
        },

        setup() {
            const searchTerm = ref('');
            const loading = ref(false);
            const filteredItems = ref([]);
            let timeoutId = null;

            const fetchData = async () => {
                try {
                    const response = await axios.get('search/', {
                        params: { q: searchTerm.value }
                    });
                    filteredItems.value = JSON.parse(response.data);

                } catch (err) {
                    console.error(`Something went wrong: ${err}`);
                } finally {
                    loading.value = false;
                }
            };

            const handleSearchChange = () => {
                clearTimeout(timeoutId);
                loading.value = true;
                timeoutId = setTimeout(fetchData, 1000);
            };

            const filteredItemsByCategory = (category) => {
                return filteredItems.value.filter(item => {
                    return item.fields.category === category && item.fields.name.toLowerCase().includes(searchTerm.value.toLowerCase());
                });
            };

            // Compute unique categories from filtered items
            const uniqueCategories = computed(() => {
                const categories = new Set();
                filteredItems.value.forEach(item => {
                    categories.add(item.fields.category);
                });
                return Array.from(categories);
            });

            return { searchTerm, loading, filteredItems, handleSearchChange, filteredItemsByCategory, uniqueCategories };
        }
    };
</script>


<style scoped>
    /* Add your styles here */
    input[type="text"] {
        font-family: 'louis_george_cafe', sans-serif;
        font-size: 23px;
        font-weight: bold;
        background: linear-gradient(to right, #ff5733 0%, #ffa500 25%, #ffa500 50%, #4169e1 75%, #ff5733 100%);
        -webkit-text-fill-color: transparent;
		-webkit-background-clip: text;
        width: 100%;
        max-width: 400px; /* Adjust as needed */
        padding: 1em .5em;
        border: 3px solid #ccc;
        border-radius: 99999999px;
        box-sizing: border-box;
    }
    .results-container {
        margin-top: 10px;
        border-radius: 10px; /* Add border radius for smooth edges */
        overflow: hidden; /* Ensure that children don't overflow */
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
        width: 90%; /* Adjust the width as needed */
        max-width: 400px; /* Add a max-width for responsiveness */
        margin: 0 auto; /* Center the container horizontally */
    }

    .loading-text {
        font-family: 'louis_george_cafe', sans-serif;
        font-size: 20px;
        font-weight: bold;
        font-style: italic;
        padding: 10px;
        color: #ffa500; /* Match the color of the gradient */
    }

    .search-input::placeholder {
        opacity: 0.4;
        font-style: italic;
    }

    .no-results {
        font-family: 'louis_george_cafe', sans-serif;
        font-size: 20px;
        font-weight: bold;
        font-style: italic;
        padding: 10px;
        color: red; /* Match the color of the gradient */
    }

    .item-name {
        font-family: 'louis_george_cafe', sans-serif;
        font-weight: bold;
        font-size: 16px;
        padding-bottom: 5px;
        padding-top: 5px;
        list-style: none;
        margin-left: 0;
        padding-left: 0;
    }

    .item-category {
        font-family: 'louis_george_cafe', sans-serif;
        font-style: bold; 
        font-size: 18px;
        padding-top: 5px;
        padding-bottom: 5px;
        border-bottom: 2px dashed #ebe0e0;
        text-align: left; /* Align text to the left */
        margin-left: 0; /* Remove any left margin */
        padding-left: 0; /* Remove any left padding */
        box-sizing: border-box; /* Ensure padding and border are included in width */
    }

    .item-category:last-child {
        border-bottom: none;
    }
    .spacer {
        height: 30px; /* Set the height of the spacer */
    }
</style>

