<!-- UserDashboard.vue -->
<template>
    <div>
        <input type="text" v-model="username" placeholder="Username">
        <input type="text" v-model="email" placeholder="Email">
        <router-link to="/" class="button-link">Go to Home</router-link>
    </div>
  </template>
  
<script>


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