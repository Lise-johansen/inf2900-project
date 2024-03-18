<template>
    <div v-if="userLoggedIn" class="contact-form">
    <h2 class='encouraging-text'>Your thoughts matter! We're here to listen and eager to hear from you. Feel free to share your ideas, questions, or any feedback you have.</h2>
    <div>
        <p><strong>Name:</strong> {{ user.firstName + ' ' + user.lastName }}</p>
    </div>
    <div>
        <p><strong>Email:</strong> {{ user.email }}</p>
    </div>
    <div>
        <label for="subject">Subject:</label>
        <textarea id="subject" v-model="subject" rows="1" cols="50" class="message-box"></textarea>
        <label for="message">Message:</label>
        <textarea id="message" v-model="message" rows="4" cols="50" class="message-box"></textarea>
    </div>
        <button @click="sendMessage">Send Message</button>
    </div>
    <div v-else>
        <p>Please log in first to contact us.</p>
        <router-link to="/login" class="login-link">Log In</router-link>
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
                    email: ''
                },
                userLoggedIn: false,
                message: ''
            };
        },
        mounted() {
        // Fetch user data upon component mount
            axios.get('dashboard/')
            .then(response => {
                this.user = response.data;
                this.userLoggedIn = true;
            })
            .catch(error => {
                console.error('Error fetching user data:', error);
            });
        },
        methods: {
            async sendMessage() {
                // Logic to send message
                console.log('Message sent:', this.message);
                console.log('User:', this.user);
                // You can implement the logic to send the message to the backend here
                // Include the user's information (this.user) in the request if needed
            }
        }
    };
</script>
  
<style scoped>
.contact-form {
        font-family: 'louis_george_cafe', sans-serif;
        max-width: 500px;
        margin: 0 auto;
        padding: 20px;
        border: 1px solid #ccc;
        border-radius: 5px;
        display: flex;
        flex-direction: column;
    }

    .contact-form h2 {
        margin-bottom: 10px;
    }

    .encouraging-text {
       font-size: x-large;
       margin-top: 0px;
    }

    .contact-form label {
        display: block;
        margin-top: 40px;
        margin-bottom: 5px;
        font-size: x-large;
    }

    #subject {
        width: 100%;
        height: auto; /* Allow height to adjust based on content */
        max-height: 30px; /* Limit the height to one line */
        border: 1px solid #ccc;
        border-radius: 5px;
        resize: none; /* Disable resizing */
        overflow: hidden; /* Hide overflow content */
    }
    
    .contact-form textarea {
        width: 100%;
        padding: 10px;
        border: 1px solid #ccc;
        border-radius: 5px;
        margin-bottom: 10px;
        font-family: 'monospace', sans-serif;
    }

    .contact-form button {
        font-family: 'louis_george_cafe', sans-serif;
        padding: 10px 20px;
        background-color: #007bff;
        color: #ffffff;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: large;
    }

    .contact-form button:hover {
        background-color: #0056b3;
    }

    div{
    display:flex;
    justify-content:center;
    align-items: center;
    flex-direction: column;
    }

    .message-box {
        max-width: 540px;
        height: 150px; /* Fixed height */
        border: 1px solid #ccc;
        border-radius: 5px;
        resize: none; /* Disable resizing */   
    }

    .login-link {
        color: #007bff;
        text-decoration: underline;
        cursor: pointer;
    }
</style>

  
  