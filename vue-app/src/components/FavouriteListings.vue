<template>
    <h1 class="page-title">Favourites</h1>
    <div class="favourites-container">
        <div v-for="(favourite, index) in favourites" :key="index" class="card" :style="{ marginRight: (index + 1) % 5 === 0 ? '0' : '10px' }">
            <router-link :to="'/listing/' + favourite.id" class="card-content">
                <div class="card-details">
                    <div class="item-name">{{ favourite.name }}</div>
                    <img :src="favourite.image" style="max-width: 100%;" :alt="favourite.name" />
                    <div class="card-footer">
                        <div class="item-price">{{ favourite.price_per_day }} kr/day</div>
                        <div class="item-location">{{ favourite.location }}</div>
                    </div>
                </div>
            </router-link>
            <!-- Add a button to remove from favourites -->
            <button @click="showConfirmationPopup(favourite.id)" class="btn">Remove from Favourites</button>
        </div>
    </div>

    <!-- Confirmation Popup -->
    <div v-if="showConfirmation" class="popup">
        <div class="popup-content">
          <p class ="error-message">Remove Favourite?</p>
          <div class="button-container">
            <button class="btn" @click="removeFromFavourites"> Yes </button>
            <button class="btn" @click="hideConfirmationPopup"> No </button>
          </div>
        </div>
    </div>
      
    <!-- Error Popup -->
    <div v-if="showPopup" class="popup">
        <div class="popup-content">
            <p class="error-message">{{ errorMessage }}</p>
            <button @click="hidePopup">OK</button>
        </div>
    </div>

</template>

<script>
import axios from 'axios';
export default {
    props: {
        listing: {
        type: Object, // Define type for the prop
        default: () => ({}) // Set default value as an empty object
        }
    },

    data() {
        return {
        favourites: [], // Initialize favorites array
        showConfirmation: false,
        selectedFavouriteId: null
        };
    },

    async mounted() {
        try {
            const response = await axios.get('get-favourites/');
            this.favourites = response.data; // Assign fetched favorites to the favorites array
            console.log('Favourites:', this.favourites);
        } catch (error) {
            console.error('Error fetching favorites:', error);
        }
    },

    methods: {
        removeFromFavourites() {
            if (!this.selectedFavouriteId) {
                return; // No favourite selected
            }
            axios.delete(`remove-from-favourites/${this.selectedFavouriteId}/`)
            .then(response => {
                console.log('Removed from favourites:', response.data);
                // Update the favorites array by filtering out the removed listing
                this.favourites = this.favourites.filter(favourite => favourite.id !== this.selectedFavouriteId);
                // Reset selectedFavouriteId
                this.selectedFavouriteId = null;
            })
            .catch(error => {
                console.error('Error removing from favourites:', error);
            });
            this.hideConfirmationPopup();
        },
        showConfirmationPopup(favouriteId) {
            this.selectedFavouriteId = favouriteId;
            this.showConfirmation = true;
        },
        hideConfirmationPopup() {
            this.showConfirmation = false;
        },
        hidePopup() {
            this.errorMessage = '';
            this.showPopup = false;
        }
    }
};
</script>
  
<style scoped>
    .page-title {
        font-size: 3.5rem;
        background: linear-gradient(to right, #ff5733 0%, #ffa500 50%, #4169e1 100%);
        -webkit-text-fill-color: transparent; 
        -webkit-background-clip: text;
    }

    .favourites-container {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        max-width: 1800px; /* Maximum width of the container */
        margin: 0 auto; /* Center the container */
    }

    .card {
        color: var(--primary-color);
        cursor: pointer;
        display: flex;
        flex-direction: column;
        align-items: center;
        margin-top: 20px; /* Adjust spacing between rows */
        margin-left: 10px; /* Adjust spacing between cards */
        width: calc(20% - 20px); /* Set width for each card, considering margins */
        padding: 10px;
        border: 3px solid grey;
        border-radius: 25px;
        transition: transform 250ms ease, color 250ms ease, border 250ms ease;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* optional, for a subtle shadow */
    }

    .card-content {
        color: var(--primary-color);
        width: 100%;
        text-decoration: none;
    }

    .card-content:hover {
        color: var(--secondary-color);
    }

    .card-details {
        text-align: left;
    }

    img {
        border-radius: 25px;
        padding-top: 5px;
        padding-bottom: 5px;
        max-width: 100%;
    }

    .item-name {
        text-align: left;
        font-size: 20px;
        font-weight: bold;
    }

    .card:hover {
        color: var(--secondary-color);
        scale: 1.03;
        border: 3px solid var(--primary-color);
    }
    .btn {
        margin-top: 10px;
        cursor: pointer;
        padding: 1em 2em;
        margin-left: 10px;
        margin-right: 10px;
        border: none;
        font-family: 'louis_george_cafe', sans-serif;
        background-color: #ff5733;
        color: whitesmoke;
        align-self: center;
    }

    .btn:hover {
        background: linear-gradient(to right, #ffa500 0, #ff5733 50%, #ffa500 100%);
    }

    .popup {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(0, 0, 0, 0.5);
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .popup-content {
        background-color: white;
        padding: 20px 40px;
        border-radius: 5px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
    }

    .popup button {
        margin-top: 10px;
        font-size: 20px;
        padding: 10px;
    }
</style>