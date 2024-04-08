<template>
  <div class="about-us">
    <h1 class="page-title animated-fade-in">Who are we?</h1>
    <div class="about-content">
      <p class="about-text divider">
        <strong>Our team:</strong><br>
        We are a group of passionate computer science students from UiT, the Arctic University of Norway, 
        working together on a project for our INF-2900 course. Our team consists of six members:
        Adrian Dybdal, Haakon Solheim, Heine Lysfjord, Johannes Figenschou, Lise Johansen, and Paal Brudevold.
      </p>
      <p class="about-text">
        <strong>Our mission:</strong><br>
        Here at Rentopia, Our mission is to provide an affordable and sustainable solution for accessing a wide range of items through our comprehensive online platform.
        Unlike traditional marketplaces, Rentopia prioritizes the shared economy. We believe in fostering a sense of accessibility, 
        affordability, and environmental responsibility in everything we do. Our platform facilitates seamless renting and lending experiences, 
        connecting users in a community-driven environment. Whether you're looking to rent or rent out gear, 
        we strive to offer a hassle-free experience that empowers our users to explore the outdoors while minimizing their environmental impact.
        Join us at Rentopia and embark on your next adventure with confidence!
      </p>
    </div>
  </div>
</template>

<script>
  export default {
    name: "AboutUs",
  };
</script>

<style scoped>
  .about-us {
    width: 70%;
    margin: 0 auto;
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

  .page-title {
    font-size: 3.5rem;
    background: linear-gradient(to right, #ff5733 0%, #ffa500 25%, #4169e1 75%);
    -webkit-text-fill-color: transparent; 
    -webkit-background-clip: text;
  }

  .about-content {
    display: flex;
    justify-content: center;
    margin-top: 2rem;
    min-width: 50%; /* Set a minimum width for the container */
  }

  .about-text {
    font-family: 'louis_george_cafe', sans-serif;
    font-weight: bold;
    font-size: 1.5rem;
    line-height: 1.6;
    text-align: justify;
    padding: 1em;
    text-justify: inter-word;
    flex-basis: 60%;
    overflow-wrap: anywhere
  }

  .about-text strong {
    background: linear-gradient(to right, #ff5733 0%, #ffa500 25%, #4169e1 75%);
    -webkit-text-fill-color: transparent; 
    -webkit-background-clip: text;
    animation: fadeIn 4s ease forwards;
  }
  .divider {
    border-right: 1px solid grey;
  }
</style>
