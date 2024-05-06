<template>
  <div v-if="isVisible" class="verification-container">
    <div v-if="isLoading" class="verification-loading">
      <p>Verifying your email address...</p>
    </div>
    <div v-if="verificationSuccess" class="verification-success">
      <p>Email verified successfully!</p>
    </div>
    <div v-if="verificationError" class="verification-error">
      <p>{{ verificationError }}</p>
      <button @click="retryVerification" class="btn">Retry</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      isVisible: false,
      isLoading: true,
      verificationError: null,
      verificationSuccess: false
    };
  },
  mounted() {
    // Start the verification process when the component is mounted
    this.isVisible = true;
    this.verifyEmail();
  },
  beforeUnmount() {
    // Stop the verification process when the component is destroyed
    this.isVisible = false;
  },
  methods: {
    verifyEmail() {
      const token = this.$route.query.token; // Get token from URL parameters
      
      if (token) {
        axios.get(`verify-email/?token=${token}`)
          .then(response => {
            console.log(response);
            this.isLoading = false;
            this.verificationSuccess = true; // Set verification success flag
          })
          .catch(error => {
            console.error(error);
            this.isLoading = false;
            this.verificationError = 'Error verifying email. Please try again.'
          });
        } else {
        // No token present, stop the verification process
        this.isLoading = false;
        this.verificationError = 'Email not verified! Please check your email for the verification link or retry.';
      }
    },
    retryVerification() {
      // Reset states and retry verification
      this.isLoading = true;
      this.verificationError = null;
      this.verifyEmail();
    }
  }
}
</script>

<style scoped>
.verification-container {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 20px;
}

.verification-loading,
.verification-success,
.verification-error {
  padding: 20px;
  text-align: center;
  border-radius: 8px;
  font-family: 'louis_george_cafe', sans-serif;
}

.verification-loading {
  background-color: #ff5733;
  color: #fff;
  width: 100%;
}

.verification-success {
  background-color: #dff0d8;
  color: #58ad5a;
  width: 100%;
}

.verification-error {
  background-color: #f2dede;
  color: #a94442;
  width: 100;
}
.btn {
      display: inline-block;
      justify-content: center;
      padding: 10px 20px;
      font-family: 'louis_george_cafe', sans-serif;
      background-color: #ff5733;
      color: whitesmoke;
      text-decoration: none;
      border: none;
      border-radius: 4px;
      cursor: pointer;
      margin-top: 10px;
  }

  .btn:hover {
    background: linear-gradient(to right,#ffa500 0, #ff5733 50%, #ffa500 100%);
  }
</style>
