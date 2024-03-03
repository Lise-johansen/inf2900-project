<template>
  <div>
    <input type="text" v-model="username" placeholder="Username">
    <input type="password" v-model="password" placeholder="Password">

    <button @click="login">Login</button>
    <router-link to="/register" class="button-link">Don't have an account? Register</router-link>
    <router-link to="/reset" class="button-link">Reset Password</router-link>
    <router-link to="/reset" class="button-link">Reset Password</router-link>
    <p v-if="errorMessage">{{ errorMessage }}</p>
  </div>
</template>

<script>
import axiosInstance from '@/axios';

export default {
  data() {
    return {
      username: '',
      password: '',
      errorMessage: ''
    };
  },
  created() {
    // Call the method to redirect if the user is already logged in
    this.redirectIfLoggedIn();
  },
  methods: {
    login() {
      // Token and auth_user are not present, proceed with login
      axiosInstance.post('login/', {
        username: this.username,
        password: this.password
      })
      .then(response => {
        document.cookie = `token=${response.data.token}`;
        document.cookie = `auth_user=${response.data.auth_user}`;
        this.$router.push('/dashboard');
      })
      .catch(error => {
        console.log("Login failed!");
        this.errorMessage = 'Invalid username or password';
        console.error('There was an error!', error);
      });
    },
    redirectIfLoggedIn() {
      const token = this.getTokenFromCookies();
      if (token != 'undefined') {
        this.$router.push('/dashboard');
      }
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
    },
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
