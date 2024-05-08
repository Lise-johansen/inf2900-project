<template>
  <div class="user-dashboard">
    <!-- Verify Email banner -->
    <verification-banner v-if="!user.verified || !isDismissed"/>
    
    <div class="flex-container">
      <div class="profilepicture-container">
        <div class="profile-picture-outline"></div>
          <img v-if="profilePicture" :src="profilePicture" alt="Avatar" class="profile-picture">
      </div>
      
      <div class="user-info">
        <p class="Realname">{{ user.firstName + " " + user.lastName}}</p>
        <p>{{ user.email }}</p>
        <p>{{ user.address }}</p>
        <p>{{ user.phone }}</p>
        <div v-if="user.verified" class="verified">
          <p>Verified</p> 
          <svg class="verified-icon" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">
            <path fill="blue" d="M9 16.2L4.8 12l-1.4 1.4L9 19 21 7l-1.4-1.4L9 16.2z"/>
          </svg>
        </div>
      </div>
    </div>


      <div class="divider"></div>

      <div class="button-grid">
        <router-link to="/listings" class="button-link">My listings</router-link>
        <router-link to="/favourites" class="button-link">My favorites</router-link>
        <router-link to="/my-account" class="button-link">My account</router-link>
        <router-link to="/privacy-policy" class="button-link">Privacy policy</router-link>
      </div>
      
      <button class="logout-button" @click="logout">Logout</button>

    <div class="divider"></div>

    <div class="Realname">Reserved Listings:</div>
    <div class="spacing"></div>
    <div class="listing-card">
    <div v-for="listing in orderedListings" :key="listing">
      <ListingCard :listing="listing"  />
      <div class="spacing"></div>
    </div>
    </div>
    <div class="divider"></div>
    </div>
</template>


<script>
  import axios from 'axios';
  import ListingCard from './ReservedListing.vue'
  import VerificationBanner from './VerifyEmail.vue';


  export default {
    data() {
      return {
        user: {
          firstName: '',
          lastName: '',
          email: '',
          phone: '',
          address: '',
          profilePicture: '',
          verified: false,
        },
        orderedListings: [], // Make this a top-level data property
        profilePicture: null,
      };
    },
    components: {
      ListingCard, VerificationBanner
    },

    created() {
      // Check if the banner is dismissed from local storage
      const dismissed = localStorage.getItem('verificationBannerDismissed');
      this.isDismissed = dismissed === 'true';
    },

    methods: {
      logout() {
        axios.get('logout/')
        .then(response => {
            this.$router.push('/');
            alert(response.data.message);
          })
      },
      
      getTokenFromCookies() {
        const cookies = document.cookie.split('; ');
        for (const cookie of cookies) {
          const [name, value] = cookie.split('=');
          if (name === 'token') {
            return value;
          }
        }
        return null; // Token not found in cookies
      }
    },

    mounted() {
        // Fetch user data upon component mount
        axios.get('dashboard/')
        .then(response => {
            this.user = response.data;
            console.log('User data:', this.user);
            this.profilePicture = response.data.profilePicture;
            axios.get('ordered-listings/')
              .then(response => {
                  this.orderedListings = response.data;
              })
              .catch(error => {
                  console.error('Error fetching ordered listings:', error);
              });
        })
        .catch(error => {
            console.error('Error fetching user data:', error);
        });
    }
  };
</script>


<style scoped>
  .verified {
    display: flex;
    align-items: center;
  }
  
  .verified p {
    margin-left: 20px;
  }

  .verified-icon {
    width: 24px;
    height: 24px;
    fill: blue;
  }
  
  .user-dashboard {
    max-width: 1200px;
    margin: 0 auto;
  }

  .flex-container {
    display: flex;
    align-items: center;
  }
  .listing-card { /* Assuming .listing-card is the class used in ListingCard component */
    display: flex;
    flex-wrap: wrap;
    justify-content: space-around; /* Changes from flex-start to space-around for better spacing */
    align-items: flex-start; /* Keeps items aligned at the top */
    gap: 20px; /* Manage the spacing between cards */
    padding: 20px 0; /* Adds padding to the top and bottom for better visual separation from other elements */
}

  p {
    margin-left: 20px;
  }

  .Realname {
    font-family: 'louis_george_cafe', sans-serif;
    font-size: 2em;
    font-weight: bold;
    margin-top: 20px;
    background: linear-gradient(to right, #ff5733, #ffa500, #4169e1);
    -webkit-text-fill-color: transparent;
    -webkit-background-clip: text;
  }

  .profilepicture-container, .profile-picture-outline, .profile-picture {
    width: 200px;
    height: 200px;
    margin-top: 20px;
  }

  .profilepicture-container {
    display: flex;
    justify-content: left;
    align-items: center;
    position: relative;
  }

  .profile-picture-outline {
    border: 5px solid #ccc;
    position: absolute;
  }

  .profile-picture, .profile-picture-outline {
    margin-bottom: 20px;
    border-radius: 50%;
    object-fit: cover;
    object-position: center;
  }

  .profile-picture {
    padding: 2px;
  }

  .user-info {
    text-align: left;
  }
  
  .divider {
    height: 3px; /* Adjust the height of the border */
    margin-top: 20px;
    margin-bottom: 2em;
    background: linear-gradient(to left, transparent, #ff5733, #ffa500, #4169e1, transparent);
    opacity: 0.8;
    width: 75em;
  }

  .button-container {
    margin-top: 20px;
  }

  .button-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr); /* Two columns with equal spacing */
    grid-gap: 2em; 
  }

  .button-link, .logout-button {
      display: inline-block;
      justify-content: center;
      padding: 10px 20px;
      font-family: 'louis_george_cafe', sans-serif;
      background-color: #ff5733;
      color: whitesmoke;
      text-decoration: none;
      border: none;
      border-radius: 4px;
      cursor: pointer;
  }

  .button-link:hover, .logout-button:hover {
    background: linear-gradient(to right,#ffa500 0, #ff5733 50%, #ffa500 100%);
  }

  .logout-button {
    font-size: 1em;
    margin-top: 2em;
  }

  .spacing {
  padding: 1em;
  }

</style> 