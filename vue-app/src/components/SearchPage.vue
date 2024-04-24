<template>
  <div>
    <SearchBox :initialSearchTerm="searchTerm" @search="handleSearch"/>
    <div class="spacing">
    </div>
    <ItemFilters @filter-change="handleFilterUpdate"/>
    <div class="spacing">
    </div>
    <div v-if="isLoading">Loading...</div>
    <div class="cards-container">
    <div class="card" v-for="item in filteredResults" :key="item.pk">
      <router-link :to="`/listing/${item.pk}`" class="card-link">
        <div class="card-image">
          <img :src="item.fields.imageUrl" alt="item.fields.name">
        </div>
        <div class="card-body">
          <h2 class="card-title">{{ item.fields.name }}</h2>
          <p class="card-location">{{ item.fields.location }}</p>
          <p class="card-price">{{ formatCurrency(item.fields.price_per_day) }}</p>
          <p class="card-dates">{{ item.fields.availableDates }}</p>
          <!-- You can add more item details here -->
        </div>
      </router-link>
    </div>
  </div>
    <div class="spacing"></div>
  </div>
</template>

<script>
import SearchBox from './SearchBox.vue';
import ItemFilters from './FilterComponent.vue';

export default {
  name: 'SearchPage',
  components: {
    SearchBox,
    ItemFilters,
    
  },

  data() {
    return {
      isLoading: false,
      searchResults: [],
      filteredResults: [],
      currentFilters: [],
      searchTerm: this.$route.query.q || '',
    };
  },
  
  mounted() {
    // Fetch all listings when the component is mounted and no search is performed
    if (!this.searchTerm) this.handleSearch('');
  },
  
  methods: {

    async handleSearch(searchTerm) {
      this.isLoading = true;
      try {
        const url = new URL('/api/search-page/', window.location.origin);
        url.searchParams.append('q', searchTerm);

        const response = await fetch(url);
        if (!response.ok) throw new Error('Failed to fetch');

        const data = await response.json();
        this.searchResults = JSON.parse(data); // Assume data is already in the correct format

        console.log('Current active filters:', this.currentFilters);
      
        // Initially set filteredResults to be the same as searchResults
        this.handleFilterUpdate(this.currentFilters);
      } catch (error) {
        console.error('Error fetching search results:', error);
      } finally {
        this.isLoading = false;
      }
    },

    formatCurrency(value) {
      const formatter = new Intl.NumberFormat('no-NB', {
        style: 'currency',
        currency: 'NOK',
      });
      return formatter.format(value);
    },

    handleFilterUpdate(filters) {
      // Update the current filters state and then apply these filters
      this.currentFilters = filters;
      this.applyFilters(filters);
    },

    applyFilters(filters) {
      // Start with all results
      let results = this.searchResults;

      // Log active filters
      console.log("Active filters before applying:", filters.filter(f => f.active).map(f => f.label));

      // Filter results if any filters are active
      const activeFilters = filters.filter(f => f.active);
      if (activeFilters.length) {
        results = this.searchResults.filter(item => {
          // Assumes item.fields.category is the category of the item
          // and filter.label is the label of the filter
          return activeFilters.some(filter => item.fields?.category === filter.label);
        });
      }

      // Update filteredResults to trigger the update in the template
      this.filteredResults = results;
    },
  },
  

  watch: {
    '$route.query.q': {
      immediate: true,
      handler(newVal) {
        if (newVal) this.handleSearch(newVal);
      },
    },
  },
};
</script>


<style scoped>
.cards-container {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
  justify-content: center;
}

.card {
  width: 20%; /* fixed width or use percentages for responsiveness */
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  overflow: hidden; /* Clip the children to the border radius */
}
.spacing {
  padding: 1em;
}

.card-link {
  text-decoration: none;
  color: inherit; /* Prevent color change on link */
}

.card-image img {
  width: 100%;
  height: auto;
  display: block; /* Remove extra space under the image */
}

.card-body {
  padding: 0.5rem;
}

.card-title {
  margin: 0.5rem 0;
  font-size: 1.25rem;
}

.card-location {
  margin: 0;
  color: #666;
  font-size: 1rem;
}

.card-price {
  margin: 0.5rem 0;
  font-weight: bold;
}

.card-dates {
  margin: 0;
  font-size: 0.875rem;
  color: #666;
}
</style>