<template>
    <div class="about-us-container">
      <!-- Top middle picture -->
      <img class="about-us-image" src="@/assets/about_us.png" alt="About Us Image">
  
        <!-- Project vision -->
        <div class="project-vision">
            <h2>Project Vision</h2>
            <p>
            FOR outdoor enthusiasts and individuals with occasional needs <br>
            WHO seek an affordable and sustainable way to access specialized gear, <br>
            The Rentopia is a comprehensive online platform <br>
            THAT facilitates seamless renting and lending of various items, <br>
            UNLIKE traditional marketplaces such as Finn.no, <br>
            OUR PRODUCT prioritizes the shared economy, 
            offering a hassle-free and community-driven <br>
            experience for users to easily rent or rent out gear, <br>
            fostering a sense of accessibility, affordability, and environmental responsibility <br>
            </p>
        </div>
  
        <!-- Line separator -->
        <hr class="separator">
        <div class="developer-names">
            <h2>Developers</h2>
            <p></p>    
            <!-- Developer names -->
            <div class="developer-names">
                <ul class="developer-list">
                    <li>Adrian Dybdhal</li>
                    <li>Lise Johansen</li>
                    <li>Johansen Figenschou</li>
                    <li>Heine Lysfjord</li>
                    <li>Paal Brudevold</li>
                    <li>Haakon Solheim</li>
                </ul>
            </div>  
        </div>    
    </div>
</template>
  
<style scoped>
  .about-us-container {
    text-align: center;
    padding: 20px;
  }
  
  .about-us-image {
    max-width: 100%;
    margin-top: 20px;
  }
  
  .project-vision {
        margin-top: 20px;
        border: 1px solid #ccc;
    }

  .project-vision {
    margin-top: 20px;
  }
  
  .project-vision h2 {
    font-size: 24px;
  }
  
  .separator {
    margin: 20px 0;
    border: 1px solid #ccc;
  }
  
  .developer-names {
    margin-top: 20px;
  }
  
  .developer-names h2 {
    font-size: 24px;
  }
  
  .developer-names ul {
    list-style: none;
    padding: 0;
  }
  
  .developer-names li {
    font-size: 18px;
    margin-bottom: 10px;
  }
  </style>
  