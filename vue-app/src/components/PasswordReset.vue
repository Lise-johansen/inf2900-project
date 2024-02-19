<template>
    <div>
        <input type="email" v-model="email" placeholder="Email">
        <button @click="passwordreset">Send Password Reset Email</button>
    </div>
</template>

<script>
import axiosInstance from '@/axios';


export default {
    data() {
        return {
            email: ''
        };
    },
    methods: {
        passwordreset() {
            axiosInstance.post('send-password-reset-email/', { 
                email: this.email 
            })
            .then(() => {
                alert('Password reset email sent');
            })
            .catch(() => {
                alert('Error sending password reset email');
            });
        }
    }
};
</script>
