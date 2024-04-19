<template>
    <div class="create-item-container">
        <h1 class="title">Create a New Listing</h1>
        <form @submit.prevent="createItem">
            <div class="form-group">
                <input type="text" id="title" v-model="title" placeholder="Short Title">
            </div>
            <div class="form-group">
                <textarea id="description" v-model="description" placeholder="Creative Description" rows="6"></textarea>
            </div>
            <div class="form-group">
                <input type="number" id="price_per_day" v-model="price_per_day" placeholder="Price per Day">
            </div>
            <div class="form-group">
                <input type="text" id="location" v-model="location" placeholder="Location">
            </div>
            <div class="form-group">
                <select id="category" v-model="category" class="custom-select">
                    <option value="" disabled>Select a Category</option>
                    <option v-for="category in categories" :key="category" :value="category">{{ category }}</option>
                </select>
            </div>
            <div class="form-group">
                <select id="condition" v-model="condition" class="custom-select">
                    <option value="" disabled>Select the Condition</option>
                    <option v-for="condition in conditions" :key="condition" :value="condition">{{ condition }}</option>
                </select>
            </div>
            <div class="form-group">
                <button type="submit" class="btn btn-primary">Create Item</button>
            </div>
        </form>
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
            image: null,
            condition: '',
            category: '',
            owner_id: '',
            imagePreview: null,
            imagePreviews: [],
            uploadedFileCount: 0,
            maxFiles: 2,
            // Define the available categories
            categories: ['Electronics', 'Furniture', 'Clothing', 'Books', 'Sports', 'Other'],
            conditions: ['New', 'Used', 'Refurbished']
        }
    },
    created() {
        // Call the method to redirect if the user is not logged in
        const token = this.getTokenFromCookies();
        if (token === 'undefined'){
            this.redirectIfLoggedIn();
        }
    },
    methods: {
        createItem() {
            // Create a new item
            // Send a POST request

            axios.post('create-item/', {
                name: this.title,
                description: this.description,
                price_per_day: this.price_per_day,
                location: this.location,
                availability: this.availability,
                image: this.image,
                condition: this.condition,
                category: this.category,
            })
                .then(() => {
                    // Handle successful creation
                    console.log('Item created successfully');
                    this.clearForm();
                })
                .catch(error => {
                    // Handle error
                    console.error('Error creating item:', error);
                });
        },
        redirectIfLoggedIn() {
            console.log('User is not logged in');
            // Token is not found in cookies (user is not logged in)
            if (confirm('You must be logged in to view this page.')) {
                this.$router.push('/login');
            }
        },
        // Get the token from the cookies
        getTokenFromCookies() {
            const cookies = document.cookie.split('; ');
            for (const cookie of cookies) {
                const [name, value] = cookie.split('=');
                if (name === 'token') {
                    return value;
                }
            }
            return null; // Token not found in cookies
        },

        handleFileUpload(event) {
            const files = event.target.files;

            // Iterate over each file and handle it individually
            for (let i = 0; i < files.length; i++) {
                if (this.uploadedFileCount >= this.maxFiles) {
                    console.error('Exceeded maximum number of allowed files');
                    return;
                }

                const file = files[i];
                const maxSize = 2 * 1024 * 1024; // 2 MB

                // Check if the file is an image
                if (file && file.type.startsWith('image/')) {
                    if (file.size > maxSize) {
                        console.error('File size exceeds 2MB:', file);
                        return;
                    }
                    const reader = new FileReader();

                    // Read the image file as a data URL
                    reader.readAsDataURL(file);

                    // Set up a listener for when the file has been loaded
                    reader.onload = () => {
                        // Store or process the image data as needed
                        // For example, you can store the data in an array or emit an event
                        this.imagePreviews.push(reader.result);
                    };

                    // Increment the uploaded file count
                    this.uploadedFileCount++;
                } else {
                    // Handle non-image files or display an error message
                    console.error('Invalid file:', file);
                }
            }
        },





        clearForm() {
            this.title = '';
            this.description = '';
            this.price_per_day = '';
            this.location = '';
            this.availability = true;
            this.image = '';
            this.condition = '';
            this.category = '';
            this.owner_id = '';

        }
    }
}
</script>

<style scoped>
.create-item-container {
    max-width: 800px;
    margin: 0 auto;
    align-items: center;
    justify-content: center;
}

.title {
    text-align: center;
    font-size: 2.5rem;
    margin-bottom: 30px;
}

.form-group {
    position: relative;
    flex: auto;
    margin-bottom: 20px;
    max-width: 100%;
}

input[type="text"],
input[type="number"],
textarea,
select {
    width: 100%;
    padding: 12px;
    border: 1px solid #ced4da;
    border-radius: 5px;
    box-sizing: border-box;
    font-size: 1rem;
}

textarea {
    resize: vertical;
}

.custom-select {
    appearance: none;
    -moz-appearance: none;
    -webkit-appearance: none;
    background-image: url('data:image/svg+xml;utf8,<svg fill="#000000" height="24" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg"><path d="M7 10l5 5 5-5z"/><path d="M0 0h24v24H0z" fill="none"/></svg>');
    background-repeat: no-repeat;
    background-position-x: calc(100% - 10px);
    background-position-y: center;
    padding-right: 30px;
}

button {
    width: 80%;
    padding: 12px;
    background-color: #007bff;
    color: #fff;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-size: 1rem;
    transition: background-color 0.3s ease;
}

button:hover {
    background-color: #0056b3;
}
</style>
