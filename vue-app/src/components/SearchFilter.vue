<template>
    <div>
      <input type="text" v-model="searchTerm" @input="handleSearchChange">
      <ul v-if="!loading">
        <li v-for="item in filteredItems" :key="item.id">{{ item.name }}</li>
      </ul>
      <div v-else>
        Loading...
      </div>
    </div>
  </template>
  
  <script>
  import { ref } from 'vue';
  import axiosInstance from '@/axios';
  
  export default {
    setup() {
      const searchTerm = ref('');
      const loading = ref(false);
      const filteredItems = ref([]);
      let timeoutId = null;
  
      const fetchData = async () => {
        try {
          const response = await axiosInstance.get('search/', {
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
  