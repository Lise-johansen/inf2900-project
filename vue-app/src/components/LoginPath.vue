<template>
  <div>
    <input type="text" v-model="username" placeholder="Username">
    <input type="password" v-model="password" placeholder="Password">
    <button @click="login">Login</button>
    <router-link to="/register" class="button-link">Don't have an account? Register</router-link>
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
  /*
   * Methods block of the Login component.
   * it contains the login method that sends a POST request to the /login endpoint of the backend.
   * The login method is called when the user clicks the Login button.
   * The login method sends the username and password to the backend.
   * If the username and password are correct, the backend returns a 200 OK response.
   *  */
  methods: {
    login() {
      axios.post('http://localhost:8000/api/login/', {
          username: this.username,
          password: this.password,
        })
        .then(response => {
          console.log(response);
          axios.get('http://localhost:8000/api/dashboard/', {
            headers: {
              Authorization: `Bearer ${response.data.access}`
            }
          })
          this.$router.push('/dashboard');
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
