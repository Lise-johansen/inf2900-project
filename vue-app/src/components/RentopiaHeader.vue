<template>
    <header class="header-container">
        <div class='logo-container'>
            <h1 class="logo" @click="redirectToHomepage">Rentopia</h1>
            <div class="company-logo" @click="redirectToHomepage">
                <img src="@/assets/logo.png" alt="Company Logo">
            </div>
        </div>

            <div class="tagline">
                <p>Own less, explore more.</p>
            </div>

        <div class='icon-container'>
            <div class="newlisting-icon" @click="redirectToNewListing">
                <img src="@/assets/addlisting.png" alt="New Listing Icon">
            </div>
            <div class="inbox-icon" @click="redirectToInbox">
                <img src="@/assets/inbox.png" alt="Inbox Icon">
            </div>
            <div class="login-icon" @click="redirectToLogin">
                <img src="@/assets/login.png" alt="Login Icon">
            </div>
        </div>
    </header>
    <div class="header-border"></div>
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
            },
            redirectToInbox() {
            this.$router.push('/inbox');
            },
            redirectToNewListing() {
            this.$router.push('/create-listing');
            }
        }
    }
</script>

<style scoped>
        .logo {
            font-family: 'louis_george_cafe', sans-serif;
            text-align: center;
            background: linear-gradient(to right, #ff5733, #ffa500, #4169e1);
            -webkit-text-fill-color: transparent;
            -webkit-background-clip: text;
            cursor: pointer;
        }

        .header-container {
            display: flex;
            align-items: center;
            justify-content: space-between;
            height: 60px;
            z-index: 1;
        }

        .logo-container,
        .icon-container {
            display: flex;
            align-items: center;
            width: 200px;
        }

        .company-logo {
            display: block; /* Ensure the icon is treated as a block element */
            cursor: pointer;
        }
        
        .company-logo img {
            max-width: 45px; /* Set a maximum width for the image */
            height: auto; /* Allow the height to adjust proportionally */
        }

        .tagline p {
            font-family: 'louis_george_cafe', sans-serif;
            font-size: 21px;
            font-weight: bold;
            background: linear-gradient(to right, #ff5733, #ffa500, #4169e1);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-size: 300% 300%;
            animation : AnimationName 6s ease infinite;
        }
        
        .icon-container {
            justify-content: flex-end;
        }

        .login-icon,
        .inbox-icon,
        .newlisting-icon {
            display: block; /* Ensure the icon is treated as a block element */
            cursor: pointer;
        }

        .login-icon img,
        .inbox-icon img,
        .newlisting-icon img{
            max-width: 50px; /* Set a maximum width for the image */
            height: auto; /* Allow the height to adjust proportionally */
            transition: transform 1s ease;
        }

        .login-icon:hover img,
        .inbox-icon:hover img,
        .newlisting-icon:hover img{
            transform: scale(1.2,1.2);
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

        .header-border {
            height: 3px; /* Adjust the height of the border */
            background: linear-gradient(to right, #ff5733, #ffa500, #4169e1);
            opacity: 0.4;
            width: 100%; /* Make the border span the entire width of the page */
        }
        
        @media (max-width: 600px) {
            .tagline {
                display: none;
            }
        }

</style>