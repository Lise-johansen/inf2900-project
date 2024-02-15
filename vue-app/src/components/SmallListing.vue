<template>
    <div class="listing">
        <img :src="imageUrl" alt="Listing Image">
        <div class="listing-details">
            <h2>
                {{ title }}
            </h2>
            <p>
                {{ location }}
            </p>
        </div>
    </div>
</template>

<script>
    export default {
        props: {
            imageUrl: String,
            title: String,
            location: String
        }
    };
</script>

<style scoped>
    .listing {
        display: flex;
        flex-direction: column;
        align-items: center;
        width: 200px; /* Adjust width as needed */
        height: 250px; /* Adjust height as needed */
        padding: 10px;
        border: 1px solid #ccc;
        border-radius: 10px;
        margin: 10px;
    }
    .listing img {
        width: 100%;
        height: 60%; /* Adjust image height as needed */
        object-fit: cover;
        border-radius: 8px;
    }
    .listing-details {
        margin-top: 10px;
        text-align: center;
    }
    .listing-details h2 {
        font-size: 1.2em;
        margin-bottom: 5px;
    }
    .listing-details p {
        font-size: 1em;
        color: #666;
    }
</style>
