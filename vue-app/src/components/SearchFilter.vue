<template>
    <div>
        <input type="text" v-model="searchTerm" @input="handleSearchChange" placeholder="Search here!" class="search-input">
        <ul v-if="!loading">
            <li v-for="item in filteredItems" :key="item.pk" class="search-result">
                <router-link v-if="item.fields" :to="'/listings/' + item.pk">
                    {{ item.fields.name }}
                </router-link>
            </li>
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
            const filteredItems = ref([])
            let timeoutId = null;
            
            const fetchData = async () => {
                try {
                    const response = await axios.get('search/', {
                        params: { q: searchTerm.value }
                    });
                    filteredItems.value = JSON.parse(response.data)

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

    .search-input::placeholder {
        opacity: 0.4;
        font-style: italic;
    }

    .search-result {
        cursor: pointer;
        color:blue;
        text-decoration: underline;
        list-style: none;
        padding: 0;
        margin-bottom: 10px;
    }

    .search-result:hover {
        color: #ffa500;
    }
    
</style>

