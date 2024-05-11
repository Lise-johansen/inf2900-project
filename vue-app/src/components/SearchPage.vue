<template>
  <div>
    <SearchBox :initialSearchTerm="searchTerm" @search="handleSearch"/>
    <div class="spacing"></div>
      <ItemFilters @filter-change="handleFilterUpdate"/>
    <div class="spacing"></div>
      <div v-if="isLoading">Loading...</div>
        <div class="cards-container">
          <div v-for="listing in filteredResults" :key="listing">
            <!-- write out all information from the listing -->
            <ListingCard :listing="listing.data"  />
          <div class="spacing"></div>
        </div>
      </div>
    <div class="spacing"></div>
  </div>
</template>

<script>
import SearchBox from './SearchBox.vue';
import ItemFilters from './FilterComponent.vue';
import ListingCard from './SearchPageCard.vue';


export default {
  name: 'SearchPage',
  components: {
    SearchBox,
    ItemFilters,
    ListingCard,
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

        // const data = await response.json();
        this.searchResults = await response.json();
      
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

        // Filter results if any filters are active
        const activeFilters = filters.filter(f => f.active);
        if (activeFilters.length) {
            results = this.searchResults.filter(item => {
                // Here you can add additional filter logic as necessary
                return activeFilters.some(filter => item.fields?.category === filter.label);
            });
        }

        // Map results to include the id and the full item
        this.filteredResults = results.map(item => {
            return {
                id: item.pk,   // Assuming 'pk' is the identifier used, adjust as needed
                data: item     // Pass the entire item object
            };
        });
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
  min-width:600px;
  flex-wrap: wrap;
  gap: 3rem;
  justify-content: center;
}


.card {
    color: var(--primary-color);
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 30px;
    padding: 10px;
    border: 3px solid grey;
    border-radius: 25px;
    transition: transform 250ms ease, color 250ms ease, border 250ms ease;
    max-width: 300px; /* or whatever width you want */
    min-width: 300px;
    min-height: 300px;
    max-height: 300px;
    margin: 0 auto; /* to center the card */
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* optional, for a subtle shadow */
  }
  img {
    border-radius: 25px;
    max-width: 300px;
    max-height: 300px;
    padding-top: 5px;
    padding-bottom: 5px;
  }
.spacing {
  padding: 1em;
}

</style>