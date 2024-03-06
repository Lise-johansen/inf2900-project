<template>
    <div class="user-dashboard">
    <input type="file" accept="image/*" @change="handleImageUpload">
    
    <!-- Display profile picture -->
    <img v-if="profilePicture" :src="profilePicture" alt="Profile Picture">
    
    <!-- Display checkmark icon if user is verified -->
    <svg v-if="user.verified" class="verified-icon" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">
        <!-- Include SVG path for the checkmark icon -->
        <path fill="blue" d="M9 16.2L4.8 12l-1.4 1.4L9 19 21 7l-1.4-1.4L9 16.2z"/>
    </svg>
    
    <p>First Name: {{ user.firstName }}</p>
    <p>Last Name: {{ user.lastName }}</p>
    <p>Email: {{ user.email }}</p>
    <p>Address: {{ user.address }}</p>
    <p>Phone Number: {{ user.phone }}</p>
    
    <!-- Button to navigate to user's listings -->
    <router-link to="/listings" class="button-link">My Listings</router-link>
    <button @click="logout">Logout</button>
    </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      user: {
        firstName: '',
        lastName: '',
        email: '',
        phone: '',
        address: '',
        profile_picture: '',
        verified: false,
      },
      profilePicture: null
    };
  },
  methods: {
    logout() {
      axios.get('logout/')
      .then(response => {
        document.cookie = `token=${response.data.token}`;
        document.cookie = `auth_user=${response.data.auth_user}`;
        this.$router.push('/');
      })
    },
  },
  mounted() {
    // Fetch user data upon component mount
    axios.get('dashboard/')
      .then(response => {
        this.user = response.data;
      })
      .catch(error => {
        console.error('Error fetching user data:', error);
      });
  }
};
</script>

  <style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
.button-link {
    display: inline-block;
    padding: 10px 20px;
    background-color: #007bff;
    color: #ffffff;
    text-decoration: none;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}
.button-link:hover {
    background-color: #0056b3;
}
.verified-icon {
  width: 24px; /* Adjust size as needed */
  height: 24px; /* Adjust size as needed */
  fill: rgb(0, 197, 219); /* Change color as needed */
  margin-left: 5px; /* Adjust margin as needed */
}
</style> 