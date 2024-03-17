<template>
    <div class="search-container">
      <input type="text" v-model="searchTerm" @input="handleSearchChange" placeholder="Search here!" class="search-input">
      <span class="search-icon">&#128269;</span>
      <div v-if="searchTerm.length === 0"></div>
      <div v-else>
        <div v-if="!loading && filteredItems.length > 0" class="results-container">
          <ul class="search-results">
            <li v-for="category in uniqueCategories" :key="category" class="item-category">
              <div>{{ category }}</div>
              <ul>
                <li v-for="item in filteredItemsByCategory(category)" :key="item.pk" class="item-name">
                  <router-link :to="'/listings/' + item.pk" class="item-link">{{ item.fields.name }}</router-link>
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
    setup() {
      const searchTerm = ref('');
      const loading = ref(false);
      const filteredItems = ref([]);
      let timeoutId = null;
  
      const fetchData = async () => {
        try {
          const response = await axios.get('search/', { params: { q: searchTerm.value } });
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
  
      const uniqueCategories = computed(() => {
        const categories = new Set();
        filteredItems.value.forEach(item => {
          categories.add(item.fields.category);
        });
        return Array.from(categories);
      });
  
      return { searchTerm, loading, filteredItems, handleSearchChange, filteredItemsByCategory, uniqueCategories};
    }
  };
  </script>
  
  <style scoped>
  /* Add your styles here */
  .search-container {
    position: relative;
    margin-top: 20px;
  }
  
  .search-input {
    font-family: 'louis_george_cafe', sans-serif;
    font-size: 23px;
    font-weight: bold;
    background: linear-gradient(to right, #ff5733 0%, #ffa500 25%, #ffa500 50%, #4169e1 75%, #ff5733 100%);
    -webkit-background-clip: text; /* Apply gradient to text */
    width: 100%;
    max-width: 400px;
    padding: 1em .5em;
    border: 1px solid #ccc;
    border-radius: 99999999px;
    box-sizing: border-box;
    padding-right: 50px; /* Adjust the padding to accommodate the icon */
  }
  
  .search-input::placeholder {
    opacity: 0.4;
    font-style: italic;
  }
  
  .search-icon {
    position: absolute;
    top: 50%;
    right: 15px; /* Adjust the distance from the right side */
    transform: translateY(-50%);
    color: #888;
  }
  
  .results-container {
    margin-top: 10px;
    border-radius: 10px;
    overflow: hidden;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
    width: 90%;
    max-width: 400px;
    margin: 0 auto;
  }
  
  .loading-text {
    color: #ffa500;
  }
  
  .no-results {
    color: red;
  }

  .loading-text, .no-results {
    font-family: 'louis_george_cafe', sans-serif;
    font-size: 20px;
    font-weight: bold;
    font-style: italic;
    padding: 10px;
  }

  .item-name {
    font-family: 'louis_george_cafe', sans-serif;
    font-weight: bold;
    font-size: 16px;
    list-style: none;
    text-align: left;
  }
  
  .item-category {
    font-family: 'louis_george_cafe', sans-serif;
    font-style: bold;
    font-size: 18px;
    border-bottom: 2px dashed #ebe0e0;
  }

.item-name, .item-category {
    text-align:left;
    padding-top: 5px;
    padding-bottom: 5px;
}

  .item-category:last-child {
    border-bottom: none;
  }
  </style>
  