<!-- UserDashboard.vue -->
<template>
  <div>
    <!-- Display user's username and email -->
    <div v-if="user.username && user.email">
      <input type="text" v-model="user.username" readonly>
      <input type="text" v-model="user.email" readonly>
      <router-link to="/" class="button-link">Go to Home</router-link>
      <RouterLink to="/logout" class="button-link">Logout</RouterLink>
    </div>
    <div v-else>
      <p>Loading user data...</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      user: {
        username: '',
        email: ''
      }  // Initialize an empty user object
    };
  },
  mounted() {
    alert(document.cookie);
    console.log(document.cookie);
    axios.get('http://localhost:8000/api/dashboard/', { withCredentials: true })
      .then(response => {
        this.user = response.data;
      })
      .catch(error => {
        console.error('Error fetching user data:', error);
      });
  }
}
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