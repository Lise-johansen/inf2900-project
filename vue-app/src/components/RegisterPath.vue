<template>
  <div>
    <input type="text" v-model="username" placeholder="Username">
    <input type="text" v-model="email" placeholder="Email">
    <div>
      <!-- Password input with toggle visibility checkbox -->
      <input :type="showPassword1 ? 'text' : 'password'" v-model="password1" placeholder="Password">
      <input type="checkbox" v-model="showPassword1"> Show Password
    </div>
    <div>
      <!-- Repeat password input with toggle visibility checkbox -->
      <input :type="showPassword2 ? 'text' : 'password'" v-model="password2" placeholder="Repeat Password">
      <input type="checkbox" v-model="showPassword2"> Show Password
    </div>
    <button @click="register">Register</button>
    <router-link to="/login" class="button-link">Already registered? Login</router-link>
    <p v-if="errorMessage">{{ errorMessage }}</p>
  </div>
</template>



<script>
import axios from '@/axios';

export default {
    data() {
      return {
        username: '',
        email: '',
        password1: '',
        password2: '',
        showPassword1: false,
        showPassword2: false,
        errorMessage: ''
      };
    },
    methods: {
        register() {
          if (this.password1 !== this.password2) {
            this.errorMessage = 'Passwords do not match';
            return; // Exit the method early if passwords don't match
          }
          axios.post('http://localhost:8000/api/register/', {
            username: this.username,
            email: this.email,
            password1: this.password1,
            password2: this.password2
            })
            .then(response => {
              this.$router.push('/dashboard');
              console.log(response);
            })
            .catch(error =>  {
                this.errorMessage = error.response.data.error;
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
