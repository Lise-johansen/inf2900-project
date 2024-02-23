<template>
    <div>
        <h1 class="title">Create Item</h1> <!-- Fixed syntax error here -->
        <input type="text" v-model="title" placeholder="Title">
        <input type="text" v-model="description" placeholder="Description">
        <input type="text" v-model="price" placeholder="Price">
        <input type="text" v-model="location" placeholder="Location">
    </div>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            title: '',
            description: '',
            price_per_day: '',
            location: '',
            availability: true,
            image: '',
            owner_id: '',
            condition:'',
            category: '',
            location: '',
        }

    },
    methods:
    {
        createItem() {
            //
            axios.post(`/api/create-item/`)
                        .then(() => {
                            // Handle successful deletion
                            console.log("Item created successfully");
                        })
                        .catch(error => {
                            // Handle error
                            console.error("Error creating item:", error);
                        });
                }
            }
    }
</script>

<style>
    input[type="text"] {
        font-family: 'louis_george_cafe', sans-serif;
        font-size: 23px;
        font-weight: bold;
        background: linear-gradient(to right, #ff5733 0%, #ffa500 25%, #ffa500 50%, #4169e1 75%, #ff5733 100%);
        -webkit-text-fill-color: transparent;
        -webkit-background-clip: text;
        background-clip: text;
        width: 100%;
        max-width: 400px; /* Adjust as needed */
        padding: 1em .5em;
        border: 1px solid #ccc;
        border-radius: 99999999px;
        box-sizing: border-box;
    }
</style>