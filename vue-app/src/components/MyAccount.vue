<template>
  <div class="my-account">
      <div class="input-container">
        <h3>Feel free to change your account information here!</h3>
        <h4>First name:</h4>
        <input v-model="user.firstName" placeholder="First name..." class="input-field"/>
        <h4>Last name:</h4>
        <input v-model="user.lastName" placeholder="Last name..." class="input-field"/>
        <h4>Address:</h4>
        <input v-model="user.address" placeholder="Address..." class="input-field"/>
        <h4>Phone number:</h4>
        <input v-model="user.phone" placeholder="Phone number..." class="input-field" @input="validatePhone"/>

        <div class="spacer"></div>

        <button class="button-link" @click="redirectToReset"> Reset password? </button>
        <button class="button-link" @click="deleteAccount"> Delete your account?</button>
        <button class="button-link" @click="saveChanges"> Save changes </button>
      </div>
      <div v-if="showPopup" class="popup">
      <div class="popup-content">
        <p class="error-message">{{ errorMessage }}</p>
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
        user: {
            firstName: '',
            lastName: '',
            email: '',
            phone: '',
            address: '',
            profilepicture: '',
            verified: false,
        },
        profilePicture: null,
        showPopup: false,
        errorMessage: '',
        illegalSymbolsPattern: /[^\d\s+]/,
        };
    },

    methods: {
        logout() {
        axios.get('logout/')
        .then(response => {
            document.cookie = `token=${response.data.token}`;
            document.cookie = `auth_user=${response.data.auth_user}`;
            this.$router.push('/');
        })
        },
        
        validatePhone(event) {
          const inputValue = event.target.value;
          if (this.illegalSymbolsPattern.test(inputValue)) {
            this.showPopup = true;
            this.errorMessage = 'Phone number can only contain numbers.';
            this.user.phone = ''
          }
        },

        handleImageUpload(event) {
            const file = event.target.files[0];
            if (file) {
                const reader = new FileReader();
                reader.readAsDataURL(file);
                reader.onload = () => {
                    this.profilePicture = reader.result;
                };
            }
        },
        
        saveChanges() {
          // Check if any of the required fields are empty
          if (!this.user.firstName || !this.user.lastName || !this.user.address || !this.user.phone) {
            this.errorMessage = 'Please fill out all the fields.';
            this.showPopup = true;
            return; // Exit the function early if validation fails
          }
          
          // Prepare the user data to be sent to the server.
          const userData = {
            first_name: this.user.firstName,
            last_name: this.user.lastName,
            address: this.user.address,
            phone: this.user.phone,
          };

          axios.put('update_user/', userData)
          .then(response => {
            console.log('Changes saved successfully:', response);
            this.showPopup = true;
            this.errorMessage = 'Changes saved successfully!';
          })
          .catch(error => {
            console.error('Error updating user information:', error);
          });
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

    mounted() {
        // Fetch user data upon component mount
        axios.get('dashboard/')
        .then(response => {
            this.user = response.data;
        })
        .catch(error => {
            console.error('Error fetching user data:', error);
        });
    }
  };
</script>

<style scoped>
  .verified-icon {
    width: 24px; /* Adjust size as needed */
    height: 24px; /* Adjust size as needed */
    fill: rgb(0, 197, 219); /* Change color as needed */
    margin-left: 5px; /* Adjust margin as needed */
  }
  
  .my-account {
    max-width: 1200px;
    margin: 0 auto;
  }

  .flex-container {
    display: flex;
    align-items: center;
  }

  p {
    margin-left: 20px;
  }

  h3 {
    font-family: 'louis_george_cafe', sans-serif;
    font-weight: bold;
    font-size: 1.6em;
    margin-bottom: 20px;
    background: linear-gradient(to right, #ff5733, #ffa500, #4169e1);
    -webkit-text-fill-color: transparent;
    -webkit-background-clip: text;
  }

  h4 {
    font-family: 'louis_george_cafe', sans-serif;
    font-weight: bold;
    font-size: 1.2em;
    margin-top: 10px;
    text-align: left;
  }

  .Realname {
    font-family: 'louis_george_cafe', sans-serif;
    font-size: 2em;
    font-weight: bold;
    margin-top: 20px;
    background: linear-gradient(to right, #ff5733, #ffa500, #4169e1);
    -webkit-text-fill-color: transparent;
    -webkit-background-clip: text;
  }

  .profilepicture-container, .profile-picture {
    width: 150px;
    height: 150px;
    margin-top: 20px;
  }

  .profilepicture-container {
    display: flex;
    justify-content: left;
    align-items: center;
  }

  .profile-picture {
    margin-bottom: 20px;
    border-radius: 50%;
    object-fit: cover;
    object-position: center;
    overflow: hidden;
    border: 2px solid #ccc;
    box-sizing: border-box;
  }
  
  .user-info {
    text-align: left;
  }

  .divider {
    height: 3px; /* Adjust the height of the border */
    margin-top: 20px;
    margin-bottom: 2em;
    background: linear-gradient(to left, transparent, #ff5733, #ffa500, #4169e1, transparent);
    opacity: 0.8;
    width: 75em;
  }

  .input-field {
    display: block;
    height: 50px;
    width: 96%;
    background-color: rgba(255,255,255,0.07);
    border-radius: 3px;
    padding: 0 10px;
    margin-top: 8px;
    font-size: 20px;
    font-weight: 300;
    outline: none;
  }

  .input-container {
    height: 600px;
    width: 600px;
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

  .button-link {
    font-family: 'louis_george_cafe', sans-serif;
    font-size: 30px;
    width: 100%;
    background-color: #ffffff;
    margin-top: 8px;
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

  .button-link:hover {
    background-color: #ffffff;
  }

  .spacer {
    height: 18px;
  }

  .error-message {
    margin-left: 0px;
    font-family: 'louis_george_cafe', sans-serif;
    font-size: 30px;
    font-weight: bold;
    align-content: center;
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
    padding: 20px 40px;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
  }

  .popup button {
    margin-top: 10px;
    font-size: 20px;
    padding: 10px;
  }
</style> 