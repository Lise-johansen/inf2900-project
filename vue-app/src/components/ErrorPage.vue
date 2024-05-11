<template>
    <div class="error-container">
        <h1 class="error-code">404</h1>
        <p class="error-message">Here at Rentopia you can rent anything ... Except hopes and dreams.</p>

        <!-- Display http cats 404 jpeg -->
        <img class="rentopia-logo" src="https://django.dybedahlserver.net/img/logo.fb06446f.png" alt="404" />
        
        <!-- Add a button to navigate back to the home page -->
        <router-link to="/" class="btn">Homepage</router-link>
    </div>
</template>
  
<style>
    /* Style for the error page container */
    .error-container {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        height: 70vh;
    }
    
    /* Style for the error code */
    .error-code {
        font-size: 4rem;
        color: #FF5722; 
        margin-bottom: 20px;
    }
    
    /* Style for the error message */
    .error-message {
        font-size: 1.5rem;
        color: #333;
    }

    /* Style for the button */
    .btn {
        display: inline-block;
        justify-content: center;
        padding: 10px 20px;
        font-family: 'louis_george_cafe', sans-serif;
        background-color: #ff5733;
        color: whitesmoke;
        text-decoration: none;
        border: none;
        border-radius: 4px;
        cursor: pointer;
        margin-top: 60px;
    }

    /* Scale the image */
    .rentopia-logo {
        margin-top: 20px;
        width: 300px;
        height: 300px;
        margin-bottom: -60px;
    }
</style>