<template>
    <div class="star-rating">
      <span v-for="i in 5" :key="i" @click="setRating(i)" :class="{ 'filled': i <= currentRating }">&#9733;</span>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      rating: {
        type: Number,
        default: 0,
      },
      editable: {
        type: Boolean,
        default: false,
      },
    },
    data() {
      return {
        currentRating: this.rating,
      };
    },
    methods: {
      setRating(rating) {
        if (this.editable) {
          this.currentRating = rating;
          this.$emit('update:rating', this.currentRating);
        }
      },
    },
  };
  </script>
  
  <style scoped>
  .star-rating {
    font-size: 24px;
    color: #ffd700; /* Gold color for stars */
    cursor: pointer;
  }
  
  .filled {
    color: #ffd700; /* Gold color for filled stars */
  }
  </style>
  