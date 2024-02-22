<template>
    <div>
      <p>Verifying your email address...</p>
      <p v-if="verificationError">{{ verificationError }}</p>
    </div>
  </template>
  
  <script>
  import axiosInstance from '@/axios';
  
  export default {
    data() {
      return {
        verificationError: null
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
            // Handle successful verification (e.g., redirect to dashboard)
            this.$router.push('/dashboard');
          })
          .catch(error => {
            this.verificationError = error.response.data.message;
          });
      }
    }
  }
  </script>
  