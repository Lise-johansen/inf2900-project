<template>
    <div>
        <h1 class="title">Create Item</h1>
        <input type="text" v-model="title" placeholder="Title">
        <input type="text" v-model="description" placeholder="Description">
        <input type="text" v-model="price_per_day" placeholder="Price">
        <input type="text" v-model="location" placeholder="Location">
    </div>
    <div>
        <button @click="createItem">Create Item</button>
    </div>
</template>

<script>
    import axios from 'axios';

    export default {
        data() {
            return {
                title: '',
                description: '',
                price_per_day: '',
                location: '',
                availability: true,
                image: '',
                condition:'',
                category: '',
                owner_id: '',
            }
        },
        created() {
            // Call the method to redirect if the user is not logged in
            this.redirectIfLoggedIn();
        },
        methods: {
            createItem() {
                // Create a new item
                
                // Get the user ID from the cookies
                const user_id = this.getUserIDFromCookies();

                // Send a POST request
                axios.post('create-item/', {
                    title: this.title,
                    description: this.description,
                    price_per_day: this.price_per_day,
                    location: this.location,
                    availability: this.availability,
                    image: this.image,
                    owner_id: user_id,
                    condition: this.condition,
                    category: this.category,
                }
                )
                .then(() => {
                    // document.cookie = `token=${response.data.token}`;
                    // Handle successful creation
                    console.log('Item created successfully');
                })
                .catch(error => {
                    // Handle error
                    console.error('Error creating item:', error);
                });
            },
            redirectIfLoggedIn() {
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
            getTokenFromCookies() {
                const cookies = document.cookie.split('; ');
                for (const cookie of cookies) {
                    const [name, value] = cookie.split('=');
                    if (name === 'token') {
                    return value;
                    }
                }
                return null; // Token not found in cookies
                },
            // Get the user ID from the cookies
            getUserIDFromCookies() {
                const cookies = document.cookie.split('; ');
                for (const cookie of cookies) {
                    const [name, value] = cookie.split('=');
                    if (name === 'id') {
                    return value;
                    }
                }
                return null; // User ID not found in cookies
                }
        }
    }
</script>

<style>
    input[type="text"] {
        font-family: 'louis_george_cafe', sans-serif;
        font-size: 23px;
        font-weight: bold;
        background: linear-gradient(to right, #ff5733 0%, #ffa500 25%, #ffa500 50%, #4169e1 75%, #ff5733 100%);
        -webkit-text-fill-color: transparent;
        -webkit-background-clip: text;
        background-clip: text;
        width: 100%;
        max-width: 400px; /* Adjust as needed */
        padding: 1em .5em;
        border: 1px solid #ccc;
        border-radius: 99999999px;
        box-sizing: border-box;
    }
</style>