<template>
    <div>
        <input type="email" v-model="email" placeholder="Email" :class="{ 'is-invalid': emailError }">
        <div class="invalid-feedback" v-if="emailError">{{ emailError }}</div>
        <button @click="passwordreset" :disabled="isSubmitting">Send Password Reset Email</button>
    </div>
</template>

<script>
import axiosInstance from '@/axios';


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
            axiosInstance.post('send-password-reset-email/', { 
                email: this.email 
            })
            .then(() => {
                alert('Password reset email sent');
                // Reset email input field
                this.email = '';
                // Display success message
                this.emailSent = true;
                // Redirect to login page
                this.$router.push('/login');
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
        }
    }
};
</script>

<style>
.is-invalid {
    border: 1px solid red; /* Add red border for invalid input */
}
.invalid-feedback {
    color: red; /* Style error message text */
}
</style>
