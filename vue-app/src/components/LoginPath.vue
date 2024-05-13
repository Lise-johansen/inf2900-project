<template>
  <div>
    <div class="background">
        <div class="shape"></div>
        <div class="shape"></div>
    </div>
    <form @submit.prevent="login">
      <div class="logo-container">
        <img src="@/assets/logo.png" alt="Company Logo" class="company-logo">
      </div>
        <input type="username" placeholder="Your email..." id="username" v-model="username">
        <div class="password-input-container">
          <span class="password-toggle" @mousedown="showPassword = true" @mouseup="showPassword = false"  @mouseleave="showPassword = false">

            <font-awesome-icon v-if="showPassword" icon="fa-solid fa-eye-slash"/>
            <font-awesome-icon v-else icon="fa-solid fa-eye"/>

          </span>

          <input placeholder="Your password..." id="password" v-model="password" :type="showPassword ? 'text' : 'password'">
        </div>

        <button type="submit" class="submit-button"> Log in </button>

        <div class="register-and-reset">
            <button class="button-link" @click="redirectToRegister"> Register here </button>
            <button class="button-link" @click="redirectToReset"> Reset password </button>
        </div>
    </form>

    <div v-if="showPopup" class="popup">
      <div class="popup-content">
        <p class="error-message">{{ errorMessage }}</p>
        <button class="popup-button" @click="hidePopup">OK</button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      username: '',
      password: '',
      errorMessage: '',
      showPopup: false,
      showPassword: false
    };
  },
  created() {
    // Call the method to redirect if the user is already logged in
    this.redirectIfLoggedIn();
  },
  methods: {
    login() {
      // Token and auth_user are not present, proceed with login
      axios.post('login/', {
        username: this.username,
        password: this.password
      })
      .then(response => {
        document.cookie = `token=${response.data.token}`;
        document.cookie = `auth_user=${response.data.auth_user}`;
        // emit login event
        this.$emit('login');
        this.$router.push('/dashboard');
      })
      .catch(error => {
        this.errorMessage = 'Invalid username or password. Please try again.';
        // Log the error to the console if not in test mode
        if (process.env.NODE_ENV !== 'test') {
          console.log("Login failed!");
          console.error(error);
        }
      });
    },
    redirectIfLoggedIn() {
      const token = this.getTokenFromCookies();
      if (token != null && token !== 'undefined') {
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
    redirectToRegister() {
      this.$router.push('/register');
    },
    redirectToReset() {
      this.$router.push('/reset');
    },
    showRetryPopup() {
      this.showPopup = true;
    },
    hidePopup() {
      this.errorMessage = ''; // Clear the error message
      this.showPopup = false;
    },
  },

  watch: {
      errorMessage(newValue) {
        if (newValue) {
          this.showRetryPopup();
        }
      }
    }
};
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
    transform: translate(-50%,-50%);
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
    top: -80px;
  }
  
  .shape:last-child {
    background: linear-gradient(
      to right,
      #ff512f,
      #f09819
    );
    right: -30px;
    bottom: -80px;
  }
  
  form {
    height: 520px;
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
    color: #000000;
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
  
  label {
    display: block;
    margin-top: 30px;
    font-size: 16px;
    font-weight: 500;
    background: linear-gradient(to right, #ff5733, #ffa500, #4169e1);
    -webkit-text-fill-color: transparent;
    -webkit-background-clip: text;
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
  .password-input-container {
    position: relative;
  }

  .password-toggle {
    position: absolute;
    top: 50%;
    right: 10px;
    transform: translateY(-50%);
    cursor: pointer;
  }

  .submit-button, .button-link, .popup-button {
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

  .submit-button:hover,
  .button-link:hover,
  .popup-button:hover{
    background-color: #ffffff;
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

  .register-and-reset { 
    display: flex;
    gap: 15px;
    margin-top: -35px;
  }
  
  #username, #password {
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

  #password {
    /* stop the password from overlaying with the show password icon */
    padding-right: 30px;
  }

  .error-message {
    font-family: 'louis_george_cafe', sans-serif;
    font-size: 30px;
    font-weight: bold;
    padding: 10px;
  }

  .popup {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .popup-content {
    background-color: white;
    padding: 20px;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
  }

  .popup button {
    margin-top: 10px;
    font-size: 20px;
    padding: 10px;
  }
</style>
