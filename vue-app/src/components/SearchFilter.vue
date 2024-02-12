<template>
    <div>
        <input type="text" v-model="searchTerm" @input="search">
        <ul>
            <li v-for="item in filteredItems" :key="item.id"> {{ item.name }} </li>
        </ul>
    </div>
</template>

<script>
    import axios from 'axios';

    export default {
        data() {
            return {
                searchTerm: '',
                items: [],
                filteredItems: []
            };
        },
        methods: {
            async search() {
                try {
                    const response = await axios.get('api/search/', {
                        params: {
                            q: this.searchTerm
                        }
                    });
                    this.filteredItems = response.data;
                }
                catch (error) {
                    console.error("Error searching:", error)
                }
            }
        }
    }
</script>
