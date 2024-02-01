<!-- UserDashboard.vue -->
<template>
    <div>
      <h1>Welcome to Your Dashboard, {{ username }}</h1>
      <!-- Add dashboard content here -->
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        username: '', // You can retrieve the username from the user's authentication information
      };
    },
  };
  </script>
  