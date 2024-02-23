
<template>
    <div class="register-container">
      <h1>Register</h1>
      <form @submit.prevent="registerUser">
        <!-- First Name -->
        <div class="form-group">
          <label for="firstName">First Name:</label>
          <input type="text" class="form-control" id="first-name" v-model="firstName">
        </div>
        <!-- Last Name -->
        <div class="form-group">
          <label for="lastName">Last Name:</label>
          <input type="text" class="form-control" id="last-name" v-model="lastName">
        </div>
        <!-- Email -->
        <div class="form-group">
          <label for="email">Email:</label>
          <input type="email" class="form-control" id="email" v-model="email">
        </div>
        <!-- Address -->
        <div class="form-group">
          <label for="address">Address:</label>
          <input type="text" class="form-control" id="address" v-model="address">
        </div>
        <!-- Phone Number -->
        <div class="form-group">
          <label for="phone">Phone Number:</label>
          <input type="text" class="form-control" id="phone" v-model="phoneNumber">
        </div>
        <!-- Password -->
        <div class="form-group">
          <label for="password">Password:</label>
          <input type="password" class="form-control" id="password" v-model="password1">
        </div>
        <!-- Password 2 -->
        <div class="form-group">
          <label for="password">Repeat Password:</label>
          <input type="password" class="form-control" id="password" v-model="password2">
        </div>
        <!-- Submit Button -->
        <button @click="register">Register</button>
      </form>
    </div>
  </template>
  
  <script>
  
  import axiosInstance from '@/axios';
  
  export default {
    data() {
      return {
          firstName: '',
          lastName: '',
          email: '',
          address: '',
          phone:'',
          password1: '',
          password2: '',
          password: '',
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
            else 
                this. password = this.password1
                axiosInstance.post('register/', {
                firstName: this.firstName,
                lastName: this.lastName,
                email: this.email,
                address: this.address,
                phone: this.phoneNumber,
                password1: this.password1,
                password2: this.password2
            })
            .then(response => {
                this.$router.push('dashboard/');
                console.log(response);
            })
            .catch(error =>  {
                  alert(this.phoneNumber)
                  this.errorMessage = error.response.data.error;
            });  
          },
      },
    }
  </script>
  
  <style scoped>
      h3 {
          color: blue;
      }
      .form-control {
          width: 25%;
          padding: .375rem .75rem;
          font-size: 1rem;
          line-height: 1.5;
          color: #495057;
          background-color: #fff;
          background-clip: padding-box;
          border: 1px solid #ced4da;
          border-radius: .25rem;
          transition: border-color .15s ease-in-out,box-shadow .15s ease-in-out;
      }
      .form-group {
          margin-bottom: 1rem;
      }
      
  </style>