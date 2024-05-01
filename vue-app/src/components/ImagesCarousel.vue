<template>
    <div class="image-gallery">
      <button @click="prevImage" class="nav-button left">&lt;</button> <!-- Left arrow -->
      <img
        :src="currentImage"
        class="gallery-image"
        :alt="`Image ${currentIndex + 1}`"
      />
      <button @click="nextImage" class="nav-button right">&gt;</button> <!-- Right arrow -->
    </div>
  </template>
  
  <script>
  export default {
    props: {
      images: {
        type: Array,
        required: true
      }
    },
    data() {
      return {
        currentIndex: 0 // Initial index of the displayed image
      };
    },
    computed: {
      currentImage() {
        return this.images[this.currentIndex]; // Returns the current image URL
      }
    },
    methods: {
      nextImage() {
        if (this.currentIndex < this.images.length - 1) {
          this.currentIndex++; // Move to the next image
        } else {
          this.currentIndex = 0; // Loop back to the first image
        }
      },
      prevImage() {
        if (this.currentIndex > 0) {
          this.currentIndex--; // Move to the previous image
        } else {
          this.currentIndex = this.images.length - 1; // Loop back to the last image
        }
      }
    }
  }
  </script>
  
  <style scoped>
  .image-gallery {
    position: relative;
    max-width: 600px; 
    margin: 20px auto;
  }
  
  .gallery-image {
    width: 100%; 
    display: block; 
    height: auto; 
  }
  
  .nav-button {
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    background-color: rgba(0, 0, 0, 0.5);
    color: white;
    border: none;
    cursor: pointer;
    padding: 10px;
    font-size: 24px;
  }
  
  .left {
    left: 10px;
  }
  
  .right {
    right: 10px;
  }
  </style>
  