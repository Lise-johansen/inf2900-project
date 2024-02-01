<template>
    <div>
      <input type="text" v-model="username" placeholder="Username">
      <input type="text" v-model="email" placeholder="Email">
      <input type="password" v-model="password" placeholder="Password">
      <button @click="register">Register</button>
      <router-link to="/login" class="button-link">Already registered? Login</router-link>
      <p v-if="errorMessage">{{ errorMessage }}</p>
    </div>
  </template>


<script>
import axios from 'axios';

export default {

    data() {
        return {
        username: '',
        password: '',
        email: '',
        errorMessage: ''
        };
    },

    methods: {
        register() {
        axios.post('http://localhost:8000/api/register/', {
            
            username: this.username,
            email: this.email,
            password: this.password
            })
            .then(response => {
              this.$router.push('/dashboard');
              console.log(response);
            })
            .catch(error =>  {
            this.errorMessage = 'Invalid username or password';
            console.error('Registration failed:', error.response.data.error);
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
