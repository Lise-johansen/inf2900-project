<template>
  <div class="spacer">
  </div>
  
  <div class="search-box">
  <input
  type="text" 
  v-model="localSearchTerm" 
  @keydown.enter="onSearch" 
  placeholder="Search for items..."
  style="padding: 0.5em 0.5em;"
  >
  </div>
  
</template>

<script>
export default {
  props: {
    initialSearchTerm: String,
  },

  data() {
    return {
      localSearchTerm: this.initialSearchTerm || '',
    };
  },

  watch: {
    initialSearchTerm(newVal) {
      this.localSearchTerm = newVal || '';
    },
  },

  methods: {
    onSearch() {
      // Emit an event to the parent component with the current search term
      this.$emit('search', this.localSearchTerm);
    },
  },
};
</script>

<style scoped>
input  {
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
      outline: none;
  }
  input:focus {
      border-color: gray; /* Changes border color to gray on focus */
  }

  .search-box {
      margin-top: 10px;
      border-radius: 10px; /* Add border radius for smooth edges */
      overflow: hidden; /* Ensure that children don't overflow */
      box-shadow: 0 0 10px rgba(255, 255, 255, 0.2);
      width: 90%; /* Adjust the width as needed */
      max-width: 400px; /* Add a max-width for responsiveness */
      margin: 0 auto; /* Center the container horizontally */
  }

  .spacer {
      height: 30px; /* Set the height of the spacer */
  }
</style>