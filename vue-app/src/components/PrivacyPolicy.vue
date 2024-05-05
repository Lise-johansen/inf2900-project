<template>
 <div class="pp-container">
    <div class="background">
        <div class="shape"></div>
        <div class="shape"></div>
    </div>
    <div class="form">
        <div class="title">Privacy Policy</div>
        <div class="date">Effective date: April 14, 2024</div>
        <p> We understand that privacy is important to our users. This Privacy Policy outlines the types of personal information we receive and collect when you use our services, as well as some of the steps we take to safeguard your information.</p>
    
        <h3>Information Collection and Use</h3>
        <p>We do not collect any personally identifiable information about you unless you voluntarily provide it to us. The information you provide is used solely to fulfill your specific request and will not be shared with any third parties. </p>
    
        <h3>Log Data</h3>
        <p>Like many other websites and services, we collect information that your browser sends whenever you visit our site. This may include information such as your IP address, browser type, browser version, pages of our site that you visit, the time and date of your visit, and other statistics.</p>
    
        <h3>Cookies</h3>
        <p>We use cookies to store information about visitors' preferences, to record user-specific information on which pages the user accesses or visits, and to customize web page content based on visitors' browser type or other information that the visitor sends via their browser.</p>
    
        <h3>Security</h3>
        <p>We are committed to ensuring that your information is secure. In order to prevent unauthorized access or disclosure, we have put in place suitable physical, electronic, and managerial procedures to safeguard and secure the information we collect online.</p>
    
        <h3>Changes to This Privacy Policy</h3>
        <p>We may update this Privacy Policy from time to time. We encourage you to review this Privacy Policy periodically for any changes.</p>
    
        <h3>Contact Us</h3>
        <p>If you have any questions about this Privacy Policy, please contact us through the link in the footer.</p>
    </div>
 </div>
</template>
  
<script>

</script>

<style scoped>
    .pp-container {
    margin: 0 auto;
    padding: 20px;
    max-width: 50%;
    }
    
    .title {
    font-size: 3em;
    font-weight: bolder;
    }

    .date {
        margin-bottom: 20px;
        font-style: italic;
        font-size: 1.2em;
    }

    h3 {
    margin-top: 30px;
    font-size: 1.5em;
    align-content: left;
    }

    p {
        font-size: 1.2em;
    }

    p, .date {
        font-family: 'louis_george_cafe', sans-serif;
    }

    .form {
    height: auto;
    width: 750px;
    background-color: rgba(255,255,255,0.13);
    position: absolute;
    transform: translate(-50%,-50%);
    top: 50%;
    left: 50%;
    border-radius: 10px;
    backdrop-filter: blur(10px);
    border: 2px solid rgba(255,255,255,0.1);
    box-shadow: 0 0 40px rgba(8,7,16,0.6);
    padding: 50px 35px;
  }

  .background {
    width: 430px;
    height: 520px;
    position: absolute;
    transform: translate(-50%,-50%);
    left: 50%;
    top: 50%;
  }
  
  .background .shape {
    height: 275px;
    width: 275px;
    position: absolute;
    border-radius: 50%;
    opacity: 0.8;
  }
  
  .shape:first-child {
    background: linear-gradient(
      #1845ad,
      #23a2f6
    );
    left: -325px;
    top: -280px;
  }
  
  .shape:last-child {
    background: linear-gradient(
      to right,
      #ff512f,
      #f09819
    );
    right: -325px;
    bottom: -280px;
  }
</style>

  