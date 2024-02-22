<template>
    <div>
        <input type="text" v-model="searchTerm" @input="handleSearchChange">
        <ul v-if="!loading">
            <pre v-if="!loading">{{ jsonResult }}</pre>
        </ul>
        <div v-else class="loading-text">
            Searching...
        </div>
    </div>
</template>

<script>
    import { ref } from 'vue';
    import axios from 'axios';

    export default {
        setup() {
            const searchTerm = ref('');
            const loading = ref(false);
            const filteredItems = ref([]);
            let timeoutId = null;

            const fetchData = async () => {
                try {
                    // Maybe update the API endpoint URL , idk if this is the correct endpoint.
                    const response = await axios.get('/api/search', {
                        params: { q: searchTerm.value }
                    });
                    filteredItems.value = response.data;
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

            return { searchTerm, loading, filteredItems, handleSearchChange };
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
        border: 1px solid #ccc;
        border-radius: 99999999px;
        box-sizing: border-box;
    }

    .loading-text {
        font-family: 'louis_george_cafe', sans-serif;
        font-size: 20px;
        font-weight: bold;
        font-style: italic;
        color: #ffa500; /* Match the color of the gradient */
    }
    
</style>

