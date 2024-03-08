<template>
    <div>
      <input type="password" v-model="password" placeholder="New Password">
      <input type="password" v-model="confirmPassword" placeholder="Confirm New Password">
      <button @click="resetPassword">Reset Password</button>
    </div>
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
  