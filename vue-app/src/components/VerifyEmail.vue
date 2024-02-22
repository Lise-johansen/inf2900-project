<template>
    <div>
      <p>Verifying your email address...</p>
      <p v-if="verificationError">{{ verificationError }}</p>
      <p v-if="verificationSuccess">Email verified successfully!</p>
    </div>
  </template>
  
  <script>
  import axiosInstance from '@/axios';
  
  export default {
    data() {
      return {
        verificationError: null,
        verificationSuccess: false
      };
    },
    created() {
      this.verifyEmail();
    },
    methods: {
      verifyEmail() {
        const token = this.$route.query.token; // Get token from URL parameters
        axiosInstance.get(`verify-email/?token=${token}`)
          .then(response => {
            console.log(response);
            this.verificationSuccess = true; // Set verification success flag
          })
          .catch(error => {
            this.verificationError = error.response.data.message;
          });
      }
    }
  }
  </script>
  