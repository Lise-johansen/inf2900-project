<template>
  <div class="filter-box">
    <div class="filter-option" v-for="(filter, index) in filters" :key="filter.label" :class="{ 'active': filter.active }" @click="redirectWithFilter(filter.label, index)">
      <!-- Apply the fa-icon class to the icon -->
      <font-awesome-icon class="fa-icon" :icon="['fas', filter.icon]" />
      {{ filter.label }}
    </div>
  </div>
</template>
  
  <script>
  import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
  
  export default {
    name: 'IndexFilters',
    components: {
      FontAwesomeIcon
    },
    data() {
        return {
          filters: [
            { label: 'Sports Equipment', icon: 'futbol', active: false },
            { label: 'Books', icon: 'book', active: false },
            { label: 'Electronics', icon: 'laptop', active: false },
            { label: 'Clothing', icon: 'tshirt', active: false },
            { label: 'Furniture', icon: 'couch', active: false },
            { label: 'Tools', icon: 'tools', active: false },
            { label: 'Toys', icon: 'robot', active: false },
            { label: 'Instruments', icon: 'guitar', active: false},
            { label: 'Town Square', icon: 'tree-city', active: false },
            { label: 'Winter', icon: 'snowflake', active: false},
            { label: 'Summer', icon: 'umbrella-beach', active: false}
          ],
          searchTerm:'',
        };
    },
    methods: {
      redirectWithFilter(filterLabel) {
        this.$router.push({ path: '/search-page/', query: { filter: filterLabel } });
      },
      applyInitialFiltersAndSearch() {
        const filterFromQuery = this.$route.query.filter;
        const searchTermFromQuery = this.$route.query.q;

        if (filterFromQuery) {
        const filterIndex = this.filters.findIndex(filter => filter.label === filterFromQuery);
        if (filterIndex !== -1) {
            this.toggleFilter(filterIndex);
        }
        }

        if (searchTermFromQuery) {
        this.searchTerm = searchTermFromQuery; // Assuming `searchTerm` is a data property
        this.handleSearch(searchTermFromQuery); // Assuming `handleSearch` is a method to perform the search
        }
    },
    }
  };
  </script>
  
  <style scoped>
 .filter-box {
    display: flex;
    flex-wrap: wrap;
    gap: 10px; /* adjust spacing between filter options */
    padding: 10px 10px;
    border: 3px solid #ccc;
    border-radius: 20px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    width: 700px;
    margin: 0 auto;
}

.filter-option {
  padding: 10px; /* adjust padding for filter options */
  border: 1px solid #d3d3d3; /* border color */
  display: flex;
  max-width: 1200px; /* maximum width for the filter options */
  border-radius: 20px; /* rounded corners for filter options */
  user-select: none; /* prevent text selection */
  cursor: pointer; /* change mouse cursor on hover */
  margin: 0 auto; /* Center the container horizontally */
}

.fa-icon {
  margin-right: 5px; /* adjust spacing between icon and text */
}

.filter-option.active {
  background-color: #a8a8a8; /* active filter background color */
  color: white; /* active filter text color */
  margin: 0 auto; /* Center the container horizontally */
}
  </style>
  