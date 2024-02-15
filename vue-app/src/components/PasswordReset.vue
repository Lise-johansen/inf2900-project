<template>
    <div>
        <input type="email" v-model="email" placeholder="Email">
        <button @click="passwordreset">Send Password Reset Email</button>
    </div>
</template>

<script>
import axios from '@/axios';

export default {
    data() {
        return {
            email: ''
        };
    },
    methods: {
        passwordreset() {
            axios.post('http://localhost:8000/api/send-password-reset-email/', { 
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
