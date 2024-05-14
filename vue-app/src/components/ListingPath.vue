<template>
    <div class="listing-container">
        <ImageGallery :images="images_list" />  
            <div class="listing-details">
                <div class="flex-box">
                    <div class="title-price-container">
                        <h1 class="listing-title">{{ this.listing.name }}</h1>
                        <p class="listing-price"> {{ this.listing.price_per_day }}</p>
                    </div> 
                    <div class="condition-category-container">
                        <p class="condition"> Condition: {{ this.listing.condition }}</p>
                        <p class="category"> Category: {{ this.listing.category }}</p>
                    </div>
                </div>
                
                <div class="btn-wrapper" v-if="listing.owner !== user.username">
                    <button :disabled="isInFavourites(listing.id)" @click="addToFavourites" class="favorite-btn">
                        <span v-if="!isInFavourites(listing.id)">Add to Favourites</span>
                        <span v-else>Already in Favourites</span>
                    </button>    
                </div>
                
                <div class="btn-wrapper" v-if="listing.owner === this.user.username">
                    <button @click="redirectToEditPage" class="edit-btn">Edit Listing</button>
                </div>

                <div class="divider"></div>

                <div class="description-container">
                    <p class="description-title">Description:</p>
                    <p class="listing-description">{{ this.listing.description }}</p>
                </div>

                <div class="reverse-divider"></div>

            <div class="wrapper">
                <div class="calendar-container">
                    <div v-if="showCalendar">
                        <CalendarOrder @dates-selected="setDates" />
                        
                        <div class="selecteddates-container">
                            <p>Selected Dates:</p>
                            <div v-if="selectedDates && selectedDates[0] && selectedDates[1]" class="formatted-date">
                                <p>{{ formatDate(selectedDates) }}</p>
                            </div>
                        </div>
                        <div v-if="listing.owner !== this.user.username">
                            <button @click="orderListing" class="order-btn" :disabled="!selectedDates">Order Listing</button>
                        </div>
                    </div>
                </div>

                <div class="seller-container">
                    <div class="profilepicture-container">
                        <img :src="this.profilepicture" alt="Profile picture" class="profile-picture">
                    </div>
                    <p class="firstname"> Rent from: {{ listing.firstname }} </p>
                    <div v-if="listing.owner !== this.user.username">
                        <button class="profile-btn" @click="sendMessage">Send message</button>
                    </div>
                </div>
            </div>
            <div class="divider"></div>
    
            <div class="map-container">
                <h3>Location: {{ listing.postal_code }}, {{ listing.location }}</h3>
                <h3 class="address-details">For more accurate address details, please contact the seller directly.</h3>
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
import CalendarOrder from './CalendarOrder.vue';
import ImageGallery from './ImagesCarousel.vue';
import LeafletMap from './LeafletMap.vue';
import ListingCarousel from './SimilarListings.vue';

export default {
    data() {
        return {
            images_list: [],
            listing: {},
            favourites: [],
            profilepicture: '',
            category: null,
            condition: '',
            showCalendar: true,
            selectedDates: null,
            user: '',
            message_text: '',
        };
    },
    watch: {
        // Watch for changes in the route parameters
        '$route.params.id'(newId) {
            if (newId) {
                this.fetchListingData();
                location.reload()
            }
        }
    },

    mounted() {
        this.fetchListingData();
        this.fetchUser();
        this.fetchFavourites();
        this.CalendarOrder = CalendarOrder;
        window.scrollTo({ top: 0, });
    },
    methods: {
        formatDate(dates) {
            if (!dates || dates.length === 0) return 'No dates selected';
                const [start, end] = dates;
                const options = { day: '2-digit', month: '2-digit', year: 'numeric' };
                return `${new Date(start).toLocaleDateString('en-GB', options)} - ${new Date(end).toLocaleDateString('en-GB', options)}`;
        },
        setDates(dates) {
            this.selectedDates = dates;
        },
        orderListing() {
            if (this.selectedDates) {
                const [start, end] = this.selectedDates;
                const listingId = this.$route.params.id;
                axios.post(`/order-listing/${listingId}/`, {
                    listingId: this.listing.id,
                    startDate: start,
                    endDate: end
                }).then(response => {
                    this.selectedDates = null;
                    this.response = response.data;
                    alert('Listing ordered successfully!');
                    axios.get(`/get_listing/${listingId}/`)
                        .then(response => {
                            this.listing = response.data;
                        })
                        .catch(error => {
                            console.error('Error fetching listing data:', error);
                        });
                }).catch(error => {
                    console.error('Error ordering listing:', error);
                    alert('Failed to order listing.');
                });
            }
        },

        redirectToEditPage() {
            const listingID = this.$route.params.id;
            this.$router.push({ name: 'edit_listing', params: { id: listingID } });
        },

        fetchListingData() {
            const listingId = this.$route.params.id;
            axios.get(`get_listing/${listingId}/`)
                .then(response => {
                    this.listing = response.data;
                    this.images_list = this.listing.images;
                    this.profilepicture = this.listing.profilepicture;
                    this.category = this.listing.category;
                    this.condition = this.listing.condition;
                })
                .catch(error => {
                    console.error('Error fetching listing data:', error);
                });
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

        fetchUser() {
            // Fetch the user data from the server
            axios.get('get-user/')
                .then(response => {
                    // Update the user data based on the response
                    this.user = response.data;
                    console.log('User data:', this.user);
                })
                .catch(error => {
                    console.error('Error fetching user data:', error);
                });
        },

        // Open the mailbox to send a message to the owner of the listing
        sendMessage() {
            // Conversation ID is null by default
            this.conversation_id = null;

            // Image is null by default
            this.message_image = '';

            // Make a POST request to tell the server to start a conversation
            axios.post('send-messages/',
                {
                    item_id: this.listing.id,
                    sender_id: this.user.id,
                    receiver_id: this.listing.owner_id,
                    message: 'Hi, I am interested in your listing. Can we discuss further?',
                    image: this.message_image,
                    conversation_id: this.conversation_id,
                })

                .then(response => {
                    console.log('Success!:', response.data);
                    // Redirect to the mailbox page and attach the conversation ID
                    this.$router.push({ name: 'inbox', params: { id: response.data.conversation.id } });
                    // log the route
                    console.log('Route:', this.$route);
                })

                .catch(error => {
                    console.error('Error sending message!:', error);
                });
        }
    },

    components: {
        ImageGallery,
        LeafletMap,
        ListingCarousel,
        CalendarOrder,
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
        margin-top: 15px;
        margin-bottom: 20px; 
        border-radius: 15px;
    }

    .flex-box {
        display: flex;
        justify-content: space-between;
    }

    .title-price-container {
        display: flex;
        flex-direction: column;
    }
    .category-condition-container {
        display: flex;
        flex-direction: column;
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
        padding-bottom: 5px;
        text-align: left;
    }

    .listing-description {
        word-break: break-all;
        text-wrap: wrap;
    }

    .listing-title,
    .listing-price,
    .condition,
    .category {
        font-family: 'louis_george_cafe', sans-serif;
        font-weight: bolder;
        background: linear-gradient(to right, #ff5733, #ffa500, #4169e1);
        -webkit-text-fill-color: transparent;
        -webkit-background-clip: text;
    }
    .condition,
    .category {
        font-size: 25px;
        text-align: right;
        padding-top: 10px;
        padding-bottom: 10px,
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
        padding: 1em;
        background-color: #f9f9f9;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        border-radius: 15px;
    }

    .seller-container {
        flex-basis: 42%;
        padding: 1em;
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
        margin-bottom: 1em;
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
    .favorite-btn, .edit-btn, .order-btn {
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
    
    .favorite-btn:hover, .profile-btn:hover, .edit-btn:hover, .order-btn:hover {
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
    
    .calendar-order, .p-calendar {
    width: 100%;
    }

    .btn-wrapper {
        display: flex;
        gap: 10px; 
    }

    .selecteddates-container {
        Margin-top: 8px;
        border-radius: 5px;
        border: 1px solid #ccc;
        padding: 1em;
        display:flex;
        justify-content: space-between;
    }

    .formatted-date {
        text-align: right;
    }
    .map-container, .listing-carousel {
        font-family: 'louis_george_cafe', sans-serif;
    }
    .map-container {
        font-size: 25px;
    }

    .listing-carousel {
        font-size: 20px;
    }

    .address-details {
        font-size: 20px;
    }
</style>