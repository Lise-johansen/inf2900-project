<template>
  <div class="background">
        <div class="shape"></div>
        <div class="shape"></div>
  </div>
  <form @submit.prevent="resetPassword">
    <div class="logo-container">
        <img src="@/assets/logo.png" alt="Company Logo" class="company-logo">
    </div>
    <input type="password" v-model="password" placeholder="New password..." id="password">
    <input type="password" v-model="confirmPassword" placeholder="Confirm new password..." id="confirm-password">
    <button type="submit"> Reset password </button>
  </form>
</template>
  
<script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        password: '',
        confirmPassword: ''
      };
    },
    methods: {
      resetPassword() {
        if (this.password !== this.confirmPassword) {
          alert('Passwords do not match');
          return;
        }

        const uidb64 = this.$route.params.uidb64;
        const token = this.$route.params.token;

        axios.post(`reset-password/${uidb64}/${token}/`, {
          new_password1: this.password, // Ensure both new_password1 and new_password2 are provided
          new_password2: this.confirmPassword
        })
        .then(() => {
          alert('Password reset successfully');
          // Optionally, redirect the user to another page
          this.$router.push('/login');
        })
        .catch((error) => {
          if (error && error.response && error.response.data && error.response.data.error) {
            alert('Error resetting password: ' + error.response.data.error); // Display error message from server
          } else {
            alert('Error resetting password: Unknown error'); // Display generic error message
          }
        });
      }
    }
  }
</script>
  
<style scoped>
   * {
    padding: 0;
    margin: 0;
    box-sizing: border-box;
  }
  
  body {
    background-color: #080710;
  }
  
  .background {
    width: 430px;
    height: 520px;
    position: absolute;
    transform: translate(-50%,-40%);
    left: 50%;
    top: 50%;
  }
  
  .background .shape {
    height: 200px;
    width: 200px;
    position: absolute;
    border-radius: 50%;
    opacity: 0.8;
  }
  
  .shape:first-child {
    background: linear-gradient(
      #1845ad,
      #23a2f6
    );
    left: -80px;
    top: -100px;
  }
  
  .shape:last-child {
    background: linear-gradient(
      to right,
      #ff512f,
      #f09819
    );
    right: -80px;
    bottom: -20px;
  }
  
  form {
    height: 450px;
    width: 400px;
    background-color: rgba(255,255,255,0.13);
    position: absolute;
    transform: translate(-50%,-50%);
    top: 50%;
    left: 50%;
    border-radius: 10px;
    backdrop-filter: blur(10px);
    border: 2px solid rgba(255,255,255,0.1);
    box-shadow: 0 0 40px rgba(8,7,16,0.6);
    padding: 50px 35px;
  }
  
  form * {
    font-family: 'Poppins', sans-serif;
    color: #ffffff;
    letter-spacing: 0.5px;
    outline: none;
    border: none;
  }
  
  form h3 {
    font-size: 35px;
    font-weight: bolder;
    line-height: 42px;
    text-align: center;
    font-family: 'louis_george_cafe', sans-serif;
    background: linear-gradient(to right, #ff5733, #ffa500, #4169e1);
    -webkit-text-fill-color: transparent;
    -webkit-background-clip: text;
  }

  .logo-container {
    position: relative; /* Set the container position to relative */
    height: 100px; /* Set a fixed height for the container */
    margin-top: -30px;
    
  }

  .company-logo {
    max-width: 120px; /* Set a maximum width for the image */
    height: auto; /* Allow the height to adjust proportionally */
  }

  input {
    display: block;
    height: 50px;
    width: 100%;
    background-color: rgba(255,255,255,0.07);
    border-radius: 3px;
    padding: 0 10px;
    margin-top: 8px;
    font-size: 14px;
    font-weight: 300;
  }

  #password, #confirm-password{
    font-family: 'louis_george_cafe', sans-serif;
    font-weight: bold;
    font-size: 1.5rem;
    padding: 1em .5em;
    border: 3px solid #a4a3a3;
    margin-top: 1.5em;
    border-radius: 99999999px;
    background: linear-gradient(to right, #ff5733, #ffa500, #4169e1);
    -webkit-text-fill-color: transparent;
    -webkit-background-clip: text;
  }

  button {
    font-family: 'louis_george_cafe', sans-serif;
    font-size: 30px;
    margin-top: 50px;
    width: 100%;
    background-color: #ffffff;
    color: #141414;
    padding: 15px 0;
    font-size: 18px;
    font-weight: 600;
    border-radius: 5px;
    cursor: pointer;
    box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    border: 3px solid #a4a3a3;
    background-color: rgb(241, 240, 240);
  }

  button:hover {
    background-color: #ffffff;
  }
</style>