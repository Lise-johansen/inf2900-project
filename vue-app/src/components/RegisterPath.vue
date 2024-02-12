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
import axios from '@/axios';

export default {
    data() {
        return {
        username: '',
        password: '',
        email: '',
        errorMessage: '',
        errorEmail: '',
        errorUsernameExists: '',
        errorEmailExists: ''
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
                if (error.response) {
                    const data = error.response.data;
                    if (data.error_email) {
                        this.errorEmail = data.error_email;
                        this.errorMessage = this.errorEmail
                    }
                    if (data.error_username_exists) {
                        this.errorUsernameExists = data.error_username_exists;
                        this.errorMessage = this.errorUsernameExists
                    }
                    if (data.error_email_exists) {
                        this.errorEmailExists = data.error_email_exists;
                        this.errorMessage = this.errorEmailExists
                    }
                } else {
                    this.errorMessage = 'Registration failed. Please try again later.';
                    console.error('Registration failed:', error);
                }
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
