<template>
  <div class="user-dashboard">
    <input type="file" accept="image/*" @change="handleImageUpload">
    
    <!-- Display profile picture -->
    <img v-if="profilePicture" :src="profilePicture" alt="Profile Picture">

    <h2>Username: {{ user.username }}</h2>
    <p>Email: {{ user.email }}</p>
    <p>Address: {{ user.address }}</p>
    <p>Postal Code: {{ user.postal_code }}</p>
    
    <!-- Button to navigate to user's listings -->
    <router-link to="/listings" class="button-link">My Listings</router-link>
    <button @click="logout">Logout</button>

  </div>
</template>

<script>
import axiosInstance from '@/axios';

export default {
  data() {
    return {
      user: {
        username: '',
        email: '',
        address: '',
        postal_code: '',
        profile_picture: ''
      },
      profilePicture: null
    };
  },
  methods: {
    logout() {
      axiosInstance.get('logout/')
      .then(response => {
        document.cookie = `token=${response.data.token}`;
        document.cookie = `auth_user=${response.data.auth_user}`;
        console.log('auth_user:', document.cookie);
        console.log('Logged out successfully');
        this.$router.push('/');
      })
    },
  },
  mounted() {
    // Fetch user data upon component mount
    axiosInstance.get('dashboard/', { withCredentials: true })
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
</style> 