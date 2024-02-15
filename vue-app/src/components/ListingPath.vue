<template>
    <div class="listing-container">
      <div class="listing-content">
        <img class="listing-image" src="@/assets/skiutstyr.jpg" alt="Listing Image">
        <div class="listing-details">
          <div class="listing-title">
            <h1 class="Title">Skiutstyr</h1>
          </div>
          <div class="listing-description">
            <h1 class="Description">Add description here</h1>
          </div>
          <div class="rating-container" @click="scrollToRating">

            <!-- Use the StarRating component to display the rating -->
            <star-rating :rating="rating" :editable="false" />
          </div>
        </div>
      </div>
      <div id="more-ratings-section" class="more-ratings-section">

        <!-- Content for more ratings from other users goes here -->
        <h2>More Ratings from Other Users</h2>
        <star-rating :rating="4.2" :editable="false" />
        <star-rating :rating="3.8" :editable="false" />
        <star-rating :rating="4.0" :editable="false" />
        <!-- Add more user ratings as needed -->
      </div>
    </div>
  </template>
  
  <script>
  import StarRating from './StarRating.vue';
  
  export default {
    data() {
      return {
        rating: 3.5, // Initial rating for the listing
        userRating: 0, // User's editable rating
      };
    },
    methods: {
      scrollToRating() {
        // Scroll to the rating section using smooth behavior
        document.getElementById('rating-section').scrollIntoView({ behavior: 'smooth' });
      },
      updateUserRating(rating) {
        // Update the user's editable rating
        this.userRating = rating;
      },
    },
    components: {
      StarRating,
    },
  };
  </script>
  
  <style scoped>
  .listing-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: flex-end;
  }
  /* Shift all compunted to the lest */
  .listing-content {
    display: flex;
    width: 90%;
  }
  
  /* Image size */
  .listing-image {
    max-width: 35%; /* Adjust the width as needed */
    height: auto;
  }
  /* Text container */
  .listing-details {
    flex: 1;
    padding: 30px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }
  
  /* Shift conntent to the left */
  .listing-title,
  .listing-description {
    width: 100%;
    padding-bottom: 20px;
  }
  /* Listing image cotainer */
  .listing-image {
    align-self: flex-start; /* Align to the start (left) of the flex container */
  }
  
  /* Container for the listing rating (sum/#)*/
  .rating-container {
    cursor: pointer;
    margin-top: 20px;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
    text-align: center;
  }
  
  /* Styling for the section containing more rating*/
  .more-ratings-section {
    padding: 15px;
    border: 1px solid #ccc;
    border-radius: 5px;
    margin-top: 100px;
    opacity: 0.95;
    transition: opacity 0.5s ease; /* Smooth transition effect */
  }
  
  .visible {
    opacity: 1;
  }
  </style>
  