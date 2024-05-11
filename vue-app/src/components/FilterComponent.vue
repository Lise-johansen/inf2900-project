<template>
  <div class="filter-box">
    <div 
      class="filter-option" 
      v-for="(filter, index) in filters" 
      :key="filter.label" 
      :class="{ 'active': filter.active }" 
      @click="toggleFilter(index), filterRoute(filter.label)" 
    >
      <!-- Display the icon associated with the filter -->
      <font-awesome-icon :icon="['fas', filter.icon]" />
      {{ filter.label }}
    </div>
  </div>
</template>

<script>
export default {
    name: 'ItemFilters',
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
        };
    },
    

    methods: {
      toggleFilter(clickedIndex) {
        // Determine the new active state for the clicked filter
        // It should be activated if it was not already active; otherwise, it should be deactivated
        const shouldBeActive = !this.filters[clickedIndex].active;

        // First, deactivate all filters
        this.filters.forEach(filter => {
          filter.active = false;
        });

        // Then, set the active state of the clicked filter based on shouldBeActive
        this.filters[clickedIndex].active = shouldBeActive;

        // Emit the updated filters array to the parent component
        this.$emit('filter-change', this.filters);
        console.log('Current active component filters:', this.filters);
      },
      filterRoute(filterLabel) {
        this.$router.push({ path: '/search-page/', query: { filter: filterLabel } });
      },
    },

    mounted() {
    const filterFromQuery = this.$route.query.filter;
    if (filterFromQuery) {
      const filterIndex = this.filters.findIndex(filter => filter.label === filterFromQuery);
      if (filterIndex !== -1) {
        this.toggleFilter(filterIndex);
      }
    }
  },
};



</script>

<style scoped>
.filter-box {
  display: flex;
  flex-wrap: wrap;
  gap: 10px; /* adjust spacing between filter options */
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

.filter-option.active {
  background-color: #a8a8a8; /* active filter background color */
  color: white; /* active filter text color */
  margin: 0 auto; /* Center the container horizontally */
}
</style>
