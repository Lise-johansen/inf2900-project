<template>
    <div class="listing-container">
        <header class="listing-header">
        <!-- Use the Galleria component to display the images -->
        <ImageGallery :images="images_list" />  
        <!-- <img :src="images" :alt="listing.name" :class="listing-image"> -->
            <div class="listing-details">
                <h1 class="listing-title">{{ this.listing.name }}</h1>
                <div class="rating-container" @click="scrollToRating">
                    <!-- Use the StarRating component to display the rating -->
                    <star-rating :rating="rating" :editable="false" />
                </div>
                <p class="listing-description">{{ this.listing.description }}</p>

                <!-- Add the listing to favourites -->
                <!-- Check if the item already is in favourites -->
                <button :disabled="isInFavourites(listing.id)" @click="addToFavourites" class="btn">
                    <span v-if="!isInFavourites(listing.id)">Add to Favourites</span>
                    <span v-else>Already in Favourites</span>
                </button>
            </div>
        </header>

        <div class="map-container">
            <h3>Location: {{ listing.postal_code }}, {{ listing.location }}</h3>
            <LeafletMap />
        </div>

        <div class="new-rating-container">
            <star-rating v-model="newRating" :editable="true" />
            <textarea v-model="newDescription" placeholder="Add a new review (max 150 characters)"
                class="message-box"></textarea>
            <button @click="addNewRating" class="btn">Add Rating</button>
        </div>
        
        <section id="more-ratings-section" class="more-ratings-section-container">
            <!-- Container for existing additional ratings -->
            <div v-for="(item, index) in additionalRatings" :key="index" class="additional-rating-container">
                <star-rating :rating="item.rating" :editable="false" />
                <p class="additional-description">{{ item.description }}</p>
            </div>
        </section>
        <section class="add-rating-section">
            <!-- Container for adding a new rating -->
        </section>
    </div>
</template>

<script>
import axios from 'axios';
import StarRating from './StarRating.vue';
import ImageGallery from './ImagesCarousel.vue';
import LeafletMap from './LeafletMap.vue';
// import Rating from 'primevue/rating';

export default {
    data() {
        return {
            images_list: [],
            // Empty listing object to be populated with data
            listing: {},

            rating: 0, // Initial rating for the listing
            additionalRatings: [
                { rating: 4.2, description: 'Description 1 (max 150 characters)' },
                { rating: 3.8, description: 'Description 2 (max 150 characters)' },
                // Add more ratings and descriptions as needed
            ],
            newRating: 0, // New rating to be added
            newDescription: '', // New description to be added
            favourites: [],
        };
    },

    mounted() {
        this.fetchListingData();
        this.fetchFavourites();
    },

    methods: {
        scrollToRating() {
            // Scroll to the rating section using smooth behavior
            // You can customize this behavior based on your needs
        },
        addNewRating() {
            // Add a new rating and description to the list
            if (this.newRating > 0 && this.newDescription.length <= 150) {
                this.additionalRatings.push({
                    rating: this.newRating,
                    description: this.newDescription,
                });

                // Reset new rating and description
                this.newRating = 0;
                this.newDescription = '';
            }
        },
        fetchListingData() {
            // Fetch listing data from the server
            const ListingID = this.$route.params.id;
            axios.get(`get_listing/${ListingID}/`)
                .then(response => {
                    // Update the listing data based on the response
                    this.listing = response.data;
                    console.log('Listing data:', this.listing);

                    // Format the image URLs for Galleria
                    this.images_list = (this.listing.images);
                    console.log('Images:', this.images);
                })
                .catch(error => {
                    console.error('Error fetching listing data:', error);
                })
        },
        addToFavourites() {
            // get the listing ID and user ID
            const ListingID = this.$route.params.id;

            // Make a POST request to add the listing to favourites
            axios.post('add-favourites/', {
                    listing_id: ListingID,
                })
                .then(response => {
                    // Show message for successful addition
                    console.log('Added to favourites:', response.data);
                    alert('Added to favourites!');
                    // Update the favourites array
                    this.fetchFavourites();
                })
                .catch(error => {
                    console.error('Error adding to favourites:', error.response.data.error);
                    console.log('Error adding to favourites:', error.response.data.error);
                    // Show the error message from the server
                    alert(error.response.data.error);
                });
        },
        fetchFavourites() {
            // Fetch the user's favourite listings
            axios.get('get-favourites/')
                .then(response => {
                    // Update the favourites array based on the response
                    this.favourites = response.data;
                    console.log('Favorites:', this.favourites);
                })
                .catch(error => {
                    console.error('Error fetching favourites:', error);
                });
        },
        isInFavourites(listingId) {
            // Check if the listingId exists in the favourites array
            return this.favourites.some(favorite => favorite.id === listingId);
        },

    },

    components: {
        StarRating,
        ImageGallery,
        LeafletMap,
    },

};
</script>

<style scoped>
.listing-container {
    width: 50%;
    margin: 0 auto;
    padding-top: 30px;
}

.listing-header {
    display: flex;
}

.listing-image {
    max-width: 40%;
    height: auto;
}

.listing-details {
    flex: 1;
    display: flex;
    flex-direction: column;
    padding-left: 20px;
}

.listing-title,
.listing-description {
    width: 100%;
    padding-bottom: 5px;
    text-align: left;
    /* Aligning text to the left */
}

.listing-image {
    align-self: flex-start;
}

.rating-container {
    cursor: pointer;
    margin-top: 20px;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
    text-align: flex-start;
}

.more-ratings-section-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-top: 20px;
}

.additional-rating-container {
    margin-top: 10px;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
    text-align: center;
}

.add-rating-section {
    display: flex;
    justify-content: center;
    align-items: center;
    margin-top: 20px;
}

.new-rating-container {
    margin-top: 10px;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
    text-align: center;
}

.message-box {
    width: 100%;
    margin-top: 10px;
    resize: none;
    outline: none;
    font-size: 1rem;
    padding: 1em 0;
    border: none;
    border-bottom: 1px solid #ccc;
    font-family: 'louis_george_cafe', sans-serif;
    /* Applying the font from contact-us page */
}

.btn {
    margin-top: 10px;
    cursor: pointer;
    padding: 1em 2em;
    align-self: flex-start;
    border: none;
    font-family: 'louis_george_cafe', sans-serif;
    background-color: #ff5733;
    color: whitesmoke;
}

.btn:hover {
    background: linear-gradient(to right, #ffa500 0, #ff5733 50%, #ffa500 100%);
}
</style>