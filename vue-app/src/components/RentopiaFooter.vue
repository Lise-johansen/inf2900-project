<template>
    <footer class="footer">
        <div class="footer-content">
            <ul>
                <router-link to="/about">About Us</router-link>
                <span class="spacer"></span>
                <router-link to="/contact">Contact Us</router-link>
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
    .footer {
        background: linear-gradient(to right, #ff5733, #ffa500, #4169e1);
        color: #fff;
        padding: 20px 0;
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        text-align: center;
        opacity: 0.8;
        z-index: 1;
        box-shadow: 0px -10px 20px rgba(0, 0, 0, 0.3); /* Add shadow to the top */
    }

    .footer-content {
        max-width: 1200px;
        margin: 0 auto;
        opacity: 1;
        font-family: 'louis_george_cafe', sans-serif;
    }

    .footer ul {
        list-style: none;
        padding: 0;
        margin: 0;
        bottom: 0;
        width: 100%;
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