<template>
    <div>
        <h1 class="page-title">Listings</h1>
        <div class="listings-container">
        <div v-for="(listing, index) in displayedListings" :key="index" class="card" :style="{ marginRight: (index + 1) % 5 === 0 ? '0' : '10px' }">
            <router-link :to="'/listing/' + listing.id" class="card-content">
            <div class="card-details">
                <div class="item-name">{{ listing.name }}</div>
                <img :src="listing.image[0]" style="max-width: 100%;" :alt="listing.name" />
                <div class="card-footer">
                <div class="item-price">{{ listing.price_per_day }} kr/day</div>
                <div class="item-location">{{ listing.location }}</div>
                </div>
            </div>
            </router-link>
            <div class="button-container">
            <button @click="showConfirmationPopup(listing.id)" class="btn delete-btn">Delete Listing</button>
            <button @click="redirectToEditPage(listing.id)" class="btn edit-btn">Edit Listing</button>
            </div>
        </div>
        </div>

        <!-- Pagination -->
        <div class="pagination">
            <button @click="prevPage" :disabled="currentPage === 1">Previous</button>
            <span>{{ currentPage }}</span>
            <button @click="nextPage" :disabled="currentPage === totalPages">Next</button>
        </div>

        <!-- Confirmation Popup -->
        <div v-if="showConfirmation" class="popup">
            <div class="popup-content">
                <p class="error-message">Delete Listing?</p>
                <div class="button-container">
                    <button class="btn" @click="deleteListing"> Yes </button>
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
    </div>
</template>

<script>
    import axios from 'axios';

    export default {
    data() {
        return {
            listings: [],
            displayedListings: [],
            currentPage: 1,
            itemsPerPage: 20,
            showConfirmation: false,
            selectedListingId: null,
            errorMessage: '',
            showPopup: false,
        };
    },
    computed: {
        totalPages() {
            return Math.ceil(this.listings.length / this.itemsPerPage);
        },
    },
    methods: {
        async fetchListings() {
            try {
                const response = await axios.get('get-user-listings/');
                this.listings = response.data;
                this.updateDisplayedListings();
            } catch (error) {
                console.error('Error fetching listings:', error);
            }
        },
        updateDisplayedListings() {
            const startIndex = (this.currentPage - 1) * this.itemsPerPage;
            const endIndex = startIndex + this.itemsPerPage;
            this.displayedListings = this.listings.slice(startIndex, endIndex);
        },
        prevPage() {
            if (this.currentPage > 1) {
                this.currentPage -= 1;
                this.updateDisplayedListings();
            }
        },
        nextPage() {
            if (this.currentPage < this.totalPages) {
                this.currentPage += 1;
                this.updateDisplayedListings();
            }
        },
        deleteListing() {
            axios.delete('delete_item/' + this.selectedListingId)
            .then(() => {
                this.listings = this.listings.filter(listing => listing.id !== this.selectedListingId);
                this.updateDisplayedListings();
                this.hideConfirmationPopup();
            })
            .catch(error => {
                this.errorMessage = 'Error deleting listing: ' + error.message;
                this.showPopup = true;
            });
        },
        showConfirmationPopup(listingId) {
            this.selectedListingId = listingId;
            this.showConfirmation = true;
        },
        hideConfirmationPopup() {
            this.showConfirmation = false;
        },
        hidePopup() {
            this.errorMessage = '';
            this.showPopup = false;
        },
        redirectToEditPage(listingId) {
            const listingID = listingId;
            this.$router.push({ name: 'edit_listing', params: { id: listingID } });
        },
    },
    mounted() {
        this.fetchListings();
    },
};
</script>
  
  
<style scoped>
    .page-title {
        font-size: 3.5rem;
        background: linear-gradient(to right, #ff5733 0%, #ffa500 50%, #4169e1 100%);
        -webkit-text-fill-color: transparent; 
        -webkit-background-clip: text;
    }
    .pagination {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-top: 20px;
        margin-bottom: 20px;
    }

    .pagination button {
        cursor: pointer;
        padding: 0.5em 1em;
        margin: 0 5px;
        border: none;
        border-radius: 5px;
        background-color: #ff5733;
        color: white;
        font-size: 1rem;
        transition: background-color 0.3s ease;
    }

    .pagination button:hover {
        background-color: #ffa500;
    }

    .pagination button:disabled {
        background-color: lightgray;
        cursor: not-allowed;
    }

    .listings-container {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        max-width: 1800px; /* Maximum width of the container */
        margin: 0 auto; /* Center the container */
        min-height: 50vh; /* Set a minimum height equal to the viewport height */
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
        height: fit-content;
        padding: 10px;
        border: 3px solid grey;
        border-radius: 25px;
        transition: transform 250ms ease, color 250ms ease, border 250ms ease;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* optional, for a subtle shadow */
        max-width: 300px; 
        min-width: 300px;
        min-height: 300px;
        max-height: 300px;
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
        max-width: 300px;
        max-height: 150px;
        min-height: 150px;
        min-width: 150px;
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

    .button-container {
        display: flex;
        justify-content: space-between; /* Distribute space evenly between the buttons */
        margin-top: 10px;
        width: 100%;
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
    }

    .btn:hover {
        background: linear-gradient(to right, #ffa500 0, #ff5733 50%, #ffa500 100%);
    }

    .delete-btn {
        margin-right: auto; /* Push the delete button to the left */
    }

    .edit-btn {
        margin-left: auto; /* Push the edit button to the right */
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