<template>
  <div>
    <div class="background">
        <div class="shape"></div>
        <div class="shape"></div>
    </div>
    <form @submit.prevent="register">
      <h3>Just fill the form!</h3>
      <input placeholder="First name *" id="first-name" v-model="firstName" autocomplete="off" required>
      
      <input placeholder="Last name *" id="last-name" v-model="lastName" autocomplete="off" required>
      
      <input type="email" placeholder="Your email *" id="email" v-model="email" autocomplete="off" required>
      
      <input placeholder="Your address *" id="address" v-model="address" autocomplete="off" required>
      
      <input placeholder="Your phone number *" id="phone" v-model="phone" autocomplete="off" required>
      
      <span class="password-toggle" @mousedown="showPassword = true" @mouseup="showPassword = false"  @mouseleave="showPassword = false">

        <font-awesome-icon v-if="showPassword" icon="fa-solid fa-eye-slash"/>
        <font-awesome-icon v-else icon="fa-solid fa-eye"/>

      </span>

      <input placeholder="Your password *" id="password" v-model="password1" autocomplete="off" required :type="showPassword ? 'text' : 'password'">
      
      <input placeholder="Repeat your password" id="password-confirm" v-model="password2" autocomplete="off" :type="showPassword ? 'text' : 'password'">

      <label class="required-fields"><span>Required fields *</span></label>
      
      <button type="submit">Register</button>
    </form>

    <div v-if="showPopup" class="popup">
      <div class="popup-content">
        <p v-if="errorMessage">{{ errorMessage }}</p>
        <button @click="hidePopup">OK</button>
      </div>
    </div>
  </div>
</template>


<script>
import axios from 'axios';

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
        errorMessage: '',
        showPopup: false,
        isEmailValid: true,
        showPassword: false
      };
  },

  methods: {
    register() {
      if (!this.validateForm()) {
        this.showPopup = true;
        return;
      }
      else {
        axios.post('register/', {
          firstName: this.firstName,
          lastName: this.lastName,
          email: this.email,
          address: this.address,
          phone: this.phone,
          password1: this.password1,
          password2: this.password2,
        })
        .then(response => {
          // send email verification
          axios.post('send-email-verification/', {
            email: this.email
          })
          this.$router.push('dashboard/');
          console.log(response);
        })
        .catch(error =>  {
          this.errorMessage = error.response.data.error;
          console.log("Error:" + " " + this.errorMessage)
          this.showPopup = true; // Show the popup if there's an error
        });
      }  
    },

    validateForm() {
      if (!this.firstName || !this.lastName || !this.email || !this.address || !this.phone || !this.password1 || !this.password2) {
        this.errorMessage = 'Please fill in all the required fields.';
        return false;
      }

      if (!this.isValidEmail(this.email)) {
          this.errorMessage = 'Invalid email, please try again.';
          return false;
      }

      if (this.password1 !== this.password2) {
          this.errorMessage = 'Passwords do not match.';
          return false;
      }

      return true;
    },
    
    hidePopup() {
      this.showPopup = false; // Method to hide the popup
    },

    isValidEmail(email) {
      const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/; // This is a regex pattern for email validation.
      return emailPattern.test(email); // Return true if the email is valid, false otherwise
    },
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
    height: auto;
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
    padding: 15px 35px;
  }
  
  form input {
    font-family: 'Poppins', sans-serif;
    color: #000000;
    letter-spacing: 0.5px;
    outline: none;
    border: 3px;
    border-radius: 20px;
    background-color: rgba(224, 224, 224, 0.5); /* Background color with 50% opacity */

  }
  
  form h3 {
    margin-top: 0px;
    font-size: 35px;
    font-weight: bolder;
    line-height: 42px;
    text-align: center;
    font-family: 'louis_george_cafe', sans-serif;
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
    margin-top: 5px;
    font-size: 14px;
    font-weight: 300;
  }

  #password {
    /* stop the password from overlaying with the show password icon */
    padding-right: 32px;
  }

  .password-toggle {
    position: absolute;
    top: 363px;
    right: 45px;
    transform: translateY(-50%);
    cursor: pointer;
  }

  ::placeholder {
    color: black;
  }
  button {
    font-family: 'louis_george_cafe', sans-serif;
    font-size: 30px;
    margin-top: 10px;
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

  .error-message {
    font-family: 'louis_george_cafe', sans-serif;
    font-size: 50px;
    font-weight: bold;
    font-style: italic;
    padding: 10px;
    background: linear-gradient(to right, #ff5733, #ffa500, #4169e1);
    -webkit-text-fill-color: transparent;
    -webkit-background-clip: text;

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
    background-color:white;
    padding: 20px;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
  }

  .popup button {
    margin-top: 10px;
  }

  .required-fields {
    font-size: 12px;
  }
</style>
