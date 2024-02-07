<template>
  <div>
    <input type="text" v-model="username" placeholder="Username">
    <input type="password" v-model="password" placeholder="Password">
    <button @click="login">Login</button>
    <router-link to="/register" class="button-link">Don't have an account? Register</router-link>
    <router-link to="/reset" class="button-link">Reset Password</router-link>
    <p v-if="errorMessage">{{ errorMessage }}</p>
  </div>
</template>

<script>
import axios from '@/axios';

export default {
  data() {
    return {
      username: '',
      password: '',
      errorMessage: ''
    };
  },
  methods: {
    login() {
      axios.post('http://localhost:8000/api/login/', {
          username: this.username,
          password: this.password
        })
        .then(response => {
          this.errorMessage = '';
          console.log(response);
        })
        .catch(error => {
          this.errorMessage = 'Invalid username or password';
          console.error('There was an error!', error);
        });
    },
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
