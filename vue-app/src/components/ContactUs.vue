<template>
    <div v-if="userLoggedIn" class="contact-form">
            <h1 class="form-title">Fill the form. <br/>It's easy.</h1>
        <div class="form-wrapper">
            <div class="form-container">        
                <textarea id="subject" v-model="subject" rows="1" cols="50" class="message-box" placeholder="Subject"/>
                <textarea id="message" v-model="message" rows="4" cols="50" class="message-box" placeholder="Write your message..."/>
                <button @click="sendMessage" class="btn">Send Message</button>
            </div>

            <div class="encouraging-container">
                <h2 class="encouraging-title">Let's talk about everything.</h2>
                <h2 class="encouraging-text"> Your thoughts matter! We're here to listen and eager to hear from you. Feel free to share your ideas, questions, or any feedback you have.</h2> 
            </div>
        </div>
    </div>  

    <div v-else>
        <div class="login-container">
            <h2 class="encouraging-title login-title animated-fade-in">Please log in first to contact us.</h2>
            <router-link to="/login" class="login-btn btn">Log In</router-link>
        </div>
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
                message: '',
                subject: ''
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
                // Create message object
                const message = {
                    subject: this.subject,
                    message: this.message,
                    user: this.user
                };

                try {
                    // Send message to the server
                    const response = await axios.post('contact_us_message/', message);

                    console.log('Message sent:', response.data);

                    alert('Message sent successfully: ' + response.data.message);
                    
                    // Clear form fields
                    this.subject = '';
                    this.message = '';
                    
                }
                catch (error) {
                    console.error('Error sending message:', error);
                    alert('Error sending message: ' + error.response.data.error);
                }
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
        opacity: 0;
        animation: fadeIn 1.5s ease forwards;
    }

    .encouraging-title{
        align-self: flex-start;
        margin: 0;
        opacity: 0;
        animation: fadeIn 1.5s ease forwards;
        animation-delay: 0.5s; /* Add a delay of 2 seconds */
        
    }
    .encouraging-text {
        font-family: 'louis_george_cafe', sans-serif;
        opacity: 0;
        animation: fadeIn 1.5s ease forwards;
        animation-delay: 1.5s; /* Add a delay of 2 seconds */
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

    .encouraging-container {
        flex-basis: 50%;
        display: flex;
        padding-left: 2em;
        flex-direction: column
    }

    .btn {
        text-decoration: none;
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

    .login-container {
        margin-top: 2em;
    }

    .login-title {
        text-align: center;
        margin-bottom: 1em  ;
    }

    .animated-fade-in {
        opacity: 0;
        animation: fadeIn 1.5s ease forwards;
    }

    @keyframes fadeIn {
        from {
            opacity: 0;
        }
        to {
            opacity: 1;
        }
    }
</style>

  
  