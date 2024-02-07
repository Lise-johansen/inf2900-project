<template>
    <div class="header-container">
        <h1 class="logo" @click="redirectToHomepage">Rentopia</h1>
        <div class="company-logo" @click="redirectToHomepage">
            <img src="@/assets/cloud.png" alt="Company Logo">
        </div>
        <div class="login-icon" @click="redirectToLogin">
            <img src="@/assets/login.png" alt="Login Icon">
        </div>
        <div class="tagline">
                <p>Own less, explore more. Rent your next adventure with Rentopia.</p>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'RentopiaHeader',
        methods: {
            redirectToLogin() {
            // Implement redirectToLogin method to handle navigation to login page
            this.$router.push('/login');
            },
            redirectToHomepage() {
            this.$router.push('/');
            }
        }
    }
</script>

<style scoped>
        .logo {
            font-family: 'louis_george_cafe', sans-serif;
            text-align: center;
            color: #5373d4;
            cursor: pointer;
        }

        .header-container {
            display: flex;
            align-items: center;
        }

        .company-logo {
            display: inline-block; /* Ensure the icon is treated as a block element */
            margin: 0 5px;
            cursor: pointer;
        }
        
        .company-logo img {
            max-width: 50px; /* Set a maximum width for the image */
            height: auto; /* Allow the height to adjust proportionally */
            margin-right: 200px;
        }

        .tagline p {
            font-family: 'louis_george_cafe', sans-serif;
            font-size: 21px;
            font-weight: bold;
            color: #2e468e;
            text-align: center;
        }

        .login-icon {
            display: inline-block; /* Ensure the icon is treated as a block element */
            position: fixed;
            top: 10px;
            right: 10px;
            cursor: pointer;
        }

        .login-icon img {
            max-width: 50px; /* Set a maximum width for the image */
            height: auto; /* Allow the height to adjust proportionally */
        }

        @font-face {
            font-family: 'louis_george_cafe';
            src: url('@/assets/louis_george_cafe.ttf') format('truetype');
            font-weight: normal;
            font-style: normal;
        }

        @font-face {
            font-family: 'cotton_cloud';
            src: url('@/assets/Cotton_Cloud.ttf') format('truetype');
            font-weight: normal;
            font-style: normal;
        }

</style>