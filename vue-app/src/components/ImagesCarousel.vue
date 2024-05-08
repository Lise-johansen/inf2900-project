<template>
  <div class="image-gallery" @keydown="handleKeyDown">
    <button @click="prevImage" class="nav-button left">&lt;</button> <!-- Left arrow -->
    <img
      :src="currentImage"
      class="gallery-image"
      :alt="`Image ${currentIndex + 1}`"
      @click="toggleImageSize"
    />
    <button @click="nextImage" class="nav-button right">&gt;</button> <!-- Right arrow -->

    <div v-if="isImageExpanded" class="image-popup-overlay" @click="closeImagePopup">
      <button @click.stop="prevImage" class="nav-button popup-left">&lt;</button> <!-- Left arrow -->
      <img
        :src="currentImage"
        class="popup-image"
        :alt="`Image ${currentIndex + 1}`"
        @click="toggleImageSize"
      />
      <button @click.stop="nextImage" class="nav-button popup-right">&gt;</button> <!-- Right arrow -->

      <!-- Display for current image index in popup -->
      <div class="popup-image-display">
        {{ currentIndex + 1 }} / {{ images.length }}
      </div>
    </div>

    <!-- Display for current image index in main gallery -->
    <div v-else class="image-display">
      {{ currentIndex + 1 }} / {{ images.length }}
    </div>
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
        currentIndex: 0, // Initial index of the displayed image
        isImageExpanded: false
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
      },
      toggleImageSize() {
        this.isImageExpanded = !this.isImageExpanded; // Toggle the image size
      },
      closeImagePopup() {
        this.isImageExpanded = false; // Close the image popup
      },
      handleKeyDown(event) {
        if (event.key === 'ArrowLeft') {
          this.prevImage();
        } 
        else if (event.key === 'ArrowRight') {
          this.nextImage();
        }
        else {
          if (event.key === 'Escape') {
            this.closeImagePopup();
          }
        }
      }
    },

    mounted() {
      window.addEventListener('keydown', this.handleKeyDown); // Listen for keydown events
    },

    beforeUnmount() {
      document.removeEventListener('keydown', this.handleKeyDown);
    },
  }
</script>
  
<style scoped>
  .image-gallery {
    display: flex;
    justify-content: center;
    align-items: center;
    position: relative;
    width: 860px;
    height: 500px;
    margin: 20px auto;
    border-radius: 10px;
    background: linear-gradient(180deg, #ff58337a, #ffa60073, #4169e180);
  }
  
  .gallery-image {
    max-width: 100%; 
    display: block; 
    max-height: 500px;
    padding: 4em;
  }

  .gallery-image.expanded {
    width: 300%; /* Adjust the expanded width as desired */
    padding: 2em; /* Adjust the expanded padding as desired */
  }

  .nav-button {
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    background-color: rgba(0, 0, 0, 0.5);
    color: white;
    border: none;
    cursor: pointer;
    padding: 13px 15px 13px 15px;
    font-size: 25px;
    border-radius: 50%;
    line-height: 50px;
  }

  .nav-button:focus {
    outline: auto 5px;
  }

  .left {
    left: 5px;
  }
  
  .right {
    right: 5px;
  }

  .popup-left {
    left: 50px;
    background-color: rgba(139, 137, 137, 0.5);
    padding: 16px 18px 16px 18px;
    z-index: 2000;
  }

  .popup-right {
    right: 50px;
    background-color: rgba(139, 137, 137, 0.5);
    padding: 16px 18px 16px 18px;
    z-index: 2000;
  }

  .image-popup-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgb(0, 0, 0, 0.92);
    z-index: 2000;
  }

  .popup-image {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    max-width: 80%;
  }

  .image-display {
    font-family: 'louis_george_cafe', sans-serif;
    font-weight: bolder;
    position: absolute;
    bottom: 10px;
    color: rgb(255, 255, 255);
    font-size: 25px;
  }

  .popup-image-display {
    font-family: 'louis_george_cafe', sans-serif;
    font-weight: bolder;
    position: absolute;
    bottom: 10px;
    left: 50%;
    transform: translateX(-50%);
    color: rgb(255, 255, 255);
    font-size: 45px;
  }
</style>
  