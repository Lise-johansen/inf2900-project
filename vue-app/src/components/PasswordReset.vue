<template>
    <div>
      <div class="background">
          <div class="shape"></div>
          <div class="shape"></div>
      </div>
      <form @submit.prevent="reset">
        <div class="logo-container">
          <img src="@/assets/logo.png" alt="Company Logo" class="company-logo">
        </div>
            <p class="reset-body">Please enter your email address. You will receive an email with instructions on resetting your password.</p>
          <input type="email" placeholder="Your email..." id="username" v-model="email">
          <div class="invalid-feedback" v-if="emailError">{{ emailError }}</div>
          <button @click="passwordreset" :disabled="isSubmitting">Reset password</button>

      </form>
      <div v-if="showPopup" class="popup">
        <div class="popup-content">
          <p>Incorrect email. Please try again.</p>
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
                email: '',
                emailError: '',
                isSubmitting: false
            };
        },
        methods: {
            validateForm() {
                this.emailError = '';
                if (!this.email) {
                    this.emailError = 'Email is required';
                    return false;
                } else if (!this.isValidEmail(this.email)) {
                    this.emailError = 'Please enter a valid email address';
                    return false;
                }
                return true;
            },
            isValidEmail(email) {
                // Basic email validation
                return /\S+@\S+\.\S+/.test(email);
            },
            passwordreset() {
                if (!this.validateForm()) {
                    return;
                }
                this.isSubmitting = true;
                axios.post('send-password-reset-email/', { 
                    email: this.email 
                })
                .then(() => {
                    alert('Password reset email sent');
                    // Reset email input field
                    this.email = '';
                    // Display success message
                    this.emailSent = true;
                })
                .catch(error => {
                    if (error.response) {
                        // The request was made and the server responded with a status code
                        // that falls out of the range of 2xx
                        if (error.response.status === 400) {
                            this.errorMessage = 'User not found';
                        } else {
                            this.errorMessage = 'Error sending password reset email';
                        }
                    } else if (error.request) {
                        // The request was made but no response was received
                        this.errorMessage = 'No response from server';
                    } else {
                        // Something happened in setting up the request that triggered an Error
                        this.errorMessage = 'Request failed';
                    }
                    // Display the error message to the user
                    alert(this.errorMessage);
                })
                .finally(() => {
                    this.isSubmitting = false;
                });
            },
            showRetryPopup() {
                this.showPopup = true;
            },
            hidePopup() {
                this.errorMessage = ''; // Clear the error message
                this.showPopup = false;
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
  
  label {
    display: block;
    margin-top: 30px;
    font-size: 16px;
    font-weight: 500;
    background: linear-gradient(to right, #ff5733, #ffa500, #4169e1);
    -webkit-text-fill-color: transparent;
    -webkit-background-clip: text;
  }

  p {
    font-family: 'louis_george_cafe', sans-serif;
    font-size: 20px;
    font-weight: bold;
    margin-top: 20px;
    margin-bottom: 20px;
    text-align: center;
    color: #333232;
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

  .logo-container {
    position: relative; /* Set the container position to relative */
    height: 100px; /* Set a fixed height for the container */
    margin-top: -30px;
    
  }

  .company-logo {
    max-width: 120px; /* Set a maximum width for the image */
    height: auto; /* Allow the height to adjust proportionally */
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
    background-color: white;
    padding: 20px;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
  }

  .popup button {
    margin-top: 10px;
  }

  .invalid-feedback {
    color: red;
    font-size: 25px;
    margin-top: 5px;
    font-family: 'louis_george_cafe', sans-serif;
    font-weight: bold;
    opacity: 70%;
  }
</style>

