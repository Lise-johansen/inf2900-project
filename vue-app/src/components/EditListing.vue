<template>
    <div>
        <input v-model="name" type="text" placeholder="Name">
        <input v-model="description" type="text" placeholder="Description">
        <input v-model="price_per_day" type="number" placeholder="Price per day">
        <input v-model="location" type="text" placeholder="Location">
        <input v-model="category" type="text" placeholder="Category">
        <button @click="updateListing">Update</button>
        <input v-model="inputNumber" type="number" placeholder="ID">
    </div>
</template>

<script>
import axios from 'axios';

export default {
    name: 'EditListing',
    data() {
        return {
            name: '',
            description: '',
            price_per_day: '',
            location: '',
            category: '',
            inputNumber: '',
        };
    },

    created() {
        // Call the method to redirect if the user is not logged in
        this.redirectIfLoggedIn();
    },

    methods: {
        updateListing() 
        {
            const data = {
                name: this.name,
                description: this.description,
                price_per_day: this.price_per_day,
                location: this.location,
                category: this.category
            };
                
            axios.put(`http://localhost:8080/api/edit_listing/${this.inputNumber}/`, data)
                .then(response => {
                    console.log(response);
                })
                .catch(error => {
                    console.log(error);
                });        
        },

        redirectIfLoggedIn()
        {
            // Redirect to login page if user is not logged in
            console.log('Checking if user is logged in...');
            const token = this.getTokenFromCookies();
            if (token === 'undefined') {
                // Token is not found in cookies (user is not logged in)
                if (confirm('You must be logged in to view this page.')) {
                    this.$router.push('/login'); 
                }
            }
        },

        // Get the token from the cookies
        getTokenFromCookies() 
        {
            const cookies = document.cookie.split('; ');
            for (const cookie of cookies) {
                const [name, value] = cookie.split('=');
                if (name === 'token') {
                return value;
                }
            }
            return null; // Token not found in cookies
        }
    }
};
</script>

<style scoped>
/*Your component styles go here */
</style>