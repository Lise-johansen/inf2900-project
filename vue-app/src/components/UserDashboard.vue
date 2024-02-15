<!-- UserDashboard.vue -->
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
    <!-- Profile picture input -->
    <router-link to="/listings" class="button-link">My Listings</router-link>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      // Initialize an empty user object
      user: {
        username: '',
        email: '',
        address: '',
        postal_code: '',
        profile_picture: ''
      }  
    };
  },
  mounted() {
    axios.get('http://localhost:8000/api/dashboard/', { withCredentials: true })
      .then(response => {
        this.user = response.data;
      })
      .catch(error => {
        console.error('Error fetching user data:', error);
      });
  },
  // handleImageUpload(event) {
      // const selectedFile = event.target.files[0];
      // You can perform additional checks on the selected file here
      
      // Display the selected image
      // this.profilePicture = URL.createObjectURL(selectedFile);
      
      // // Upload the image to the server (send selectedFile to the backend)
      // // Example:
      // const formData = new FormData();
      // formData.append('profilePicture', selectedFile);
      // axios.post('http://localhost:8000/api/upload-profile-picture/', formData)
      //   .then(response => {
      //     console.log('Profile picture uploaded successfully');
      //   })
      //   .catch(error => {
      //     this.errorMessage = 'Failed to upload profile picture';
      //     console.error('Error uploading profile picture:', error);
      //   });
    // }
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