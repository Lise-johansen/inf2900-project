<template>
  <div>
    <h1>Create Listing</h1>
    <form @submit.prevent="submitListing">
      <label for="title">Title:</label>
      <input type="text" id="title" v-model="title" required>
      
      <label for="description">Description:</label>
      <textarea id="description" v-model="description" required></textarea>
      
      <label for="price">Price:</label>
      <input type="number" id="price" v-model="price" required>
      
      <button type="submit">Submit</button>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      title: '',
      description: '',
      price: 0
    };
  },
  methods: {
    submitListing() {
      // Here you can handle the submission logic, e.g., send the data to a server
      console.log('Submitted listing:', {
        title: this.title,
        description: this.description,
        price: this.price
      });
    }
  }
};
</script>

<style scoped>
/* Add your custom styles here */
</style>
