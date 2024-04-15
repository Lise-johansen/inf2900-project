<template>
    <footer class="footer">
      <div class="footer-content">
        <ul>
          <li><router-link to="/about">About Us</router-link></li>
          <li class="spacer"></li>
          <li><router-link to="/contact">Contact Us</router-link></li>
        </ul>
      </div>
    </footer>
  </template>
  
  <script>
  export default {
    name: 'RentopiaFooter'
  }
  </script>
  
  <style scoped>
  /* Ensure the footer is positioned at the bottom of the viewport */
  .footer {
    position: relative;
    left: 0;
    bottom: 0;
    background: linear-gradient(to right, #ff5733, #ffa500, #4169e1);
    color: #fff;
    width: 100%;
    text-align: center;
    opacity: 0.7;
    box-shadow: 0px -10px 20px rgba(0, 0, 0, 0.3); /* Add shadow to the top */
    }
  
  /* Ensure the footer content is centered */
  .footer-content {
    max-width: 1200px;
    margin: 0 auto;
    font-family: 'louis_george_cafe', sans-serif;
    font-size: 1.5em;
  }
  
  .footer ul {
    list-style: none;
    padding: 0;
    margin: 0;
  }
  
  .footer ul li {
    display: inline;
    margin-right: 20px;
  }
  
  .footer ul li a {
    color: #fff;
    text-decoration: none;
  }
  
  .spacer {
    margin: 0 25px; /* Adjust the margin as needed */
  }
  </style>
  