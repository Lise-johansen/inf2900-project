<template>
    <div class="error-container">
      <h1 class="error-code">404</h1>
      <p class="error-message">Here at Rentopia you can rent anything ... Except hopes and dreams.</p>

      <!-- Add a button to navigate back to the home page -->
    <router-link to="/" class="btn btn-primary">Homepage</router-link>

    <!-- Display http cats 404 jpeg -->
    <img class="http-cat" src="https://http.cat/images/404.jpg" alt="404" />
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
    color: #FF5722; /* Adjust the color as needed */
    margin-bottom: 20px;
  }
  
  /* Style for the error message */
  .error-message {
    font-size: 1.5rem;
    color: #333; /* Adjust the color as needed */
  }

    /* Style for the button */
    .btn {
        text-size-adjust: 100%;
        text-align: center;
        cursor: pointer;
        size: 300px;
    }

    /* Scale the image */
    .http-cat {
        margin-top: 20px;
        width: 500px;
        height: 400px;
        margin-bottom: -60px;
    }
  </style>
  