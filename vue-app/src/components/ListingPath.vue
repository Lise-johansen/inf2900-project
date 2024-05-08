<template>
    <div class="listing-container">
        <ImageGallery :images="images_list" />  
            <div class="listing-details">
                <h1 class="listing-title">{{ this.listing.name }}</h1>
                <p class="listing-price"> {{ this.listing.price_per_day }}</p>
                <button :disabled="isInFavourites(listing.id)" @click="addToFavourites" class="favorite-btn">
                    <span v-if="!isInFavourites(listing.id)">Add to Favourites</span>
                    <span v-else>Already in Favourites</span>
                </button>

                <div class="divider"></div>

                <div class="description-container">
                    <p class="description-title">Description:</p>
                    <p class="listing-description">{{ this.listing.description }}</p>
                </div>


                <div class="reverse-divider"></div>
            <div class="wrapper">
                <div class="calendar-container">
                    
                </div>
                <div class="seller-container">
                    <div class="profilepicture-container">
                        <img :src="this.profilepicture" alt="Profile picture" class="profile-picture">
                    </div>
                    <p class="firstname"> Rent from: {{ listing.firstname }} </p>

                    <button class="profile-btn">Send message</button>
            </div>
        </div>

        <div class="divider"></div>

        <div class="map-container">
            <h3>Location: {{ listing.postal_code }}, {{ listing.location }}</h3>
            <LeafletMap />
        </div>

        <div class="reverse-divider"></div>

        <div class="listing-carousel">
            <h2>Similar Listings</h2>
            <ListingCarousel :category= "this.category" />
        </div>
            </div>
            
    </div>
</template>

<script>
import axios from 'axios';
import ImageGallery from './ImagesCarousel.vue';
import LeafletMap from './LeafletMap.vue';
import ListingCarousel from './ListingCarousel.vue';

export default {
    data() {
        return {
            images_list: [],
            listing: {},
            favourites: [],
            profilepicture: '',
            category: null,
        };
    },

    mounted() {
        this.fetchListingData();
        this.fetchFavourites();
    },

    methods: {
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
                    this.profilepicture = this.listing.profilepicture;
                    this.category = this.listing.category;
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
        ImageGallery,
        LeafletMap,
        ListingCarousel,
    },

};
</script>

<style scoped>
    .listing-container {
        display: flex;
        flex-direction: column;
        width: 1000px;
        margin: 0 auto;
        padding-top: 30px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        margin-top: 10px;
        border-radius: 15px;
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
        padding-left: 70px;
        padding-right: 70px;
    }

    .listing-title,
    .listing-description {
        width: 100%;
        padding-bottom: 5px;
        text-align: left;
    }

    .listing-description {
        word-break: break-all;
        text-wrap: wrap;
    }

    .listing-title,
    .listing-price {
        font-family: 'louis_george_cafe', sans-serif;
        font-weight: bolder;
        background: linear-gradient(to right, #ff5733, #ffa500, #4169e1);
        -webkit-text-fill-color: transparent;
        -webkit-background-clip: text;

    }

    .listing-price {
        font-size: 25px;
        text-align: left; /* Center-align the price */
    }

    .listing-price::after {
        content: "kr per day"; /* Add currency symbol before the price */
        margin-right: 3px;
    }

    .listing-image {
        align-self: flex-start;
    }
    .description-title
    {
        font-family: 'louis_george_cafe', sans-serif;
        font-weight: bolder;
        font-size: 1.5rem;
        padding-bottom: 5px;
        text-align: left;
    }

    .wrapper {
        display: flex;
        justify-content: center;
        width: 100%;
        gap: 1em;
        margin-bottom: 20px
    }
    
    .calendar-container {
        flex-basis: 42%;
        background-color: #f9f9f9;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        border-radius: 15px;
    }

    .seller-container {
        padding: 20px;
        flex-basis: 42%;
        background-color: #f9f9f9;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        border-radius: 15px;
        display: flex;
        align-items: center;
        flex-direction: column;
        justify-content: center;
    }

    .profilepicture-container {
        display: flex;
        justify-content: center;
        align-items: center;
        overflow: hidden;
        box-sizing: border-box;
        border: 5px solid #ccc;
        border-radius: 50%;
        width: 150px;
        height: 150px;
    }

    .profile-picture {
        width: 150px;
        height: 150px;
    }

    .firstname {
        font-family: 'louis_george_cafe', sans-serif;
        font-weight: bolder;
        font-size: 1.5rem;
        background: linear-gradient(to right, #ff5733, #ffa500, #4169e1);
        -webkit-text-fill-color: transparent;
        -webkit-background-clip: text;
    }
    .profile-btn,
    .favorite-btn {
        margin-top: 10px;
        border-radius: 5px;
        cursor: pointer;
        padding: 1em 2em;
        border: none;
        font-family: 'louis_george_cafe', sans-serif;
        background-color: #ff5733;
        color: whitesmoke;
    }

    .favorite-btn{
        align-self: flex-start;
    }

    .favorite-btn:hover, .profile-btn:hover {
        background: linear-gradient(to right, #ffa500 0, #ff5733 50%, #ffa500 100%);
    }

    .divider {
        background: linear-gradient(to right, transparent, #ff5733, #ffa500, #4169e1, transparent);
    }
    .reverse-divider {
        background: linear-gradient(to left, transparent, #ff5733, #ffa500, #4169e1, transparent);
    }

    .divider, .reverse-divider {
        height: 3px; /* Adjust the height of the border */
        margin-top: 2em;
        margin-bottom: 2em;
        opacity: 0.8;
        width: 100%;
    }
    
</style>