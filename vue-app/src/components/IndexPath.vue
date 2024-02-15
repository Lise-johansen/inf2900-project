
/**
 * The template block of the IndexPath component.
 * This component represents the main template of the IndexPath component.
 */

<template>
        <div>
                <h1>Welcome to the Index Page</h1>
        <button @click="redirectToLogin">Go to Login</button>
        </div>
</template>

/**
 * The script block of the IndexPath component.
 * This component represents the main script of the IndexPath component.
 * It contains the redirectToLogin method that redirects the user to the login page.
 */

<script>
export default {
        methods: {
                redirectToLogin() {
                        this.$router.push('/login');
                }
        }
}
</script>



<style scoped>
h3 {
    margin: 40px 0 0;
}
ul {
    list-style-type: none;
    padding: 0;
}
li {
    display: inline-block;
    margin: 0 10px;
}
a {
    color: #42b983;
}
</style>
