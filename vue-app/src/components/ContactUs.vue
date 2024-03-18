<template>
    <div v-if="userLoggedIn" class="contact-form">
            <h1 class="form-title">Fill the form. <br/>It's easy.</h1>
        <div class="form-wrapper">
            <div class="form-container">
                <!-- <div class="credentials-container">
                <p><strong>Name:</strong> {{ user.firstName + ' ' + user.lastName }}</p>
                <p><strong>Email:</strong> {{ user.email }}</p>
                </div> -->
        
                <textarea id="subject" v-model="subject" rows="1" cols="50" class="message-box" placeholder="Subject"/>
                <textarea id="message" v-model="message" rows="4" cols="50" class="message-box" placeholder="Write your message..."/>
                <button @click="sendMessage" class="btn">Send Message</button>
            </div>

            <div class="encouraging-container">
            <h2 class="encouraging-title">Let's talk about everything.</h2>
            <h2 class='encouraging-text'> Your thoughts matter! We're here to listen and eager to hear from you. Feel free to share your ideas, questions, or any feedback you have.</h2> 
            </div>
        </div>
    </div>

    <div v-else>
        <router-link to="/login" class="login-link">Log In</router-link>
        <p>Please log in first to contact us.</p>
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
        width: 50%;
        margin: 0 auto;
        }
   .form-wrapper{
         display: flex;
    }
    .encouraging-title,
    .encouraging-text,
    .form-title{
        text-align: start;
    }

    .encouraging-title{
        align-self: flex-start;
        margin: 0;
        
    }
    .encouraging-text {
        font-family: 'louis_george_cafe', sans-serif;
    }
    .encouraging-title,
     .form-title{
        font-size: 3.5rem;
        background: linear-gradient(to right, #ff5733 0%, #ffa500 25%, #ffa500 50%, #4169e1 75%);
        -webkit-text-fill-color: transparent;
        -webkit-background-clip: text;
    }
    
    .form-container {
        display: flex;
        flex-direction: column;
        gap: 2em;
        border-right: 1px solid rgb(177, 175, 175);
        padding-right: 2em;
        flex-basis: 50%;
    }

    .message-box {
        resize: none;
        outline: none;
        font-size: 1rem;
        padding: 1em 0 1em 0; 
        border: none;
        border-bottom: 1px solid rgb(177, 175, 175);
        font-family: fantasy;
    }

    #message {
        min-height: 10em;
        resize: vertical;
    }

    .credentials-container {
        display: flex;
        gap: 2em;
        
    }

    .encouraging-container{
        flex-basis: 50%;
        display: flex;
        padding-left: 2em;
        flex-direction: column
    }

    .btn{
        padding: 1em 2em;
        align-self: flex-start;
        border: none;
        font-family: 'louis_george_cafe', sans-serif;
        background-color: #ff5733;
        color: whitesmoke;
    }

    .btn:hover{
        background: linear-gradient(to right,#ffa500 0, #ff5733 50%, #ffa500 100%);
    }

</style>

  
  