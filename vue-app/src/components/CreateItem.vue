<template>
    <div class="create-item-container">
        <h1 class="title">Create a New Listing</h1>
        <form @submit.prevent="createItem">
            <div class="form-group">
                <input type="text" id="title" v-model="title" placeholder="Short Title (max 100 characters)" :maxlength="maxTitleLength" @input="handleTitleInput">
            </div>
            <div class="form-group">
                <textarea id="description" v-model="description" placeholder="Creative Description (max 2000 characters)" rows="6" :maxlength="maxTextLength" @input="handleDescInput"></textarea>
                <p>{{ remainingCharacters }} characters remaining</p>
            </div>
            <div class="form-group">
                <input type="text" id="price_per_day" v-model="price_per_day" placeholder="Price per Day" @input="handlePrice">
            </div>
            <div class="form-group">
                <input type="text" id="location" v-model="location" placeholder="Location">
            </div>
            <div class="form-group">
                <input type="text" id="postal_code" v-model="postal_code" placeholder="Postal code" :maxlength="maxPostalLength" @input="handlePostalCode">
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
            <!-- Upload Images to the listing -->
            <div class="form-group">
                <input type="file" ref="fileInput" @change="handleFileUpload" multiple>
                <!-- Iterate and display the images in the preview -->
                <div v-for="(imagePreview, index) in imagePreviews" :key="index">
                    <img :src="imagePreview" alt="Image Preview" style="margin-top: 10px;">
                </div>
            </div>
            <div class="form-group">
                <button type="submit" class="btn btn-primary">Create Item</button>
            </div>
        </form>
    </div>

    <!-- Popup for displaying various info -->
    <div v-if="showPopup" class="popup">
        <div class="popup-content">
          <p>{{ popupMessage }}</p>
          <button @click="hidePopup">OK</button>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import Cookies from 'js-cookie';

export default {
    data() {
        return {
            title: '',
            description: '',
            price_per_day: '',
            location: '',
            postal_code: '',
            availability: true,
            image: [],
            condition: '',
            category: '',
            owner_id: '',
            imagePreview: null,
            imagePreviews: [],
            uploadedFileCount: 0,
            maxFiles: 5,
            // Change size if needed
            maxSizeInBytes: 2 * 1024 * 1024, // 2MB
            // Define the available categories
            categories: ['Summer', 'Winter', 'Tools', 'Electronics', 'Clothing', 'Furniture', 'Sports Equipment', 'Books', 'Other'],
            conditions: ['New', 'Used', 'Refurbished'],
            maxTextLength: 2000,
            maxTitleLength: 100,
            maxPostalLength: 4  ,
            showPopup: false,
            popupMessage: ''
        }
    },
    computed: {
        remainingCharacters() {
            return this.maxTextLength - this.description.length;
        }
    },

    beforeRouteEnter(to, from, next) {
        // Check if the user is logged in
        const token = Cookies.get('token');
        if (token) {
            next();
        } else {
            alert('You must be logged in to create a listing');
            next('/login');
        }
    },

    methods: {
        createItem() {
            // Check for missing fields
            if (!this.title || !this.description || !this.price_per_day || !this.location || !this.postal_code || !this.category || !this.condition || this.image.length === 0) {
                this.showPopup = true;
                this.popupMessage = 'Please fill in all required fields.';
                return;
            }

            // Create an object to store item data
            const itemData = {
                name: this.title,
                description: this.description,
                price_per_day: this.price_per_day,
                location: this.location,
                postal_code: this.postal_code,
                availability: this.availability,
                condition: this.condition,
                category: this.category,
                images: this.image,
            };

            // Send a POST request with itemData as JSON
            axios.post('create-item/', itemData)
                .then(() => {
                    // Handle successful creation
                    console.log('Item created successfully');
                    this.clearForm();
                    this.showPopup = true;
                    this.popupMessage = 'Item created successfully!';
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
        hidePopup() {
            this.showPopup = false;
            this.popupMessage = '';
        },
        handleFileUpload(event) {
                const files = event.target.files;

                
                // Iterate over each file and handle it individually
                for (let i = 0; i < files.length; i++) {
                    const file = files[i];
                    
                    // Check if the number of files exceeds the maximum allowed
                    if (files.length + this.uploadedFileCount > this.maxFiles) {
                        this.showPopup = true; // Display the popup
                        this.popupMessage = `You can only upload a maximum of ${this.maxFiles} files.`;
                        event.target.value = '';
                        return; // Stop further processing
                    }
    
                    if (file.size > this.maxSizeInBytes) {
                        this.showPopup = true; // Display the popup
                        this.popupMessage = 'File size exceeds the limit (2MB). Please choose a smaller file.';
                        // Clear the file input to allow the user to select a different file
                        event.target.value = '';
                        return;
                    }

                    // Check if the file type is allowed (png, jpeg, jpg)
                    const allowedTypes = ['image/png', 'image/jpeg', 'image/jpg'];
                    if (!allowedTypes.includes(file.type)) {
                        this.showPopup = true; // Display the popup
                        this.popupMessage = 'Only PNG, JPEG, or JPG files are allowed for upload.';
                        event.target.value = '';
                        return; // Stop further processing
                    }
                    if (file) {
                        // Create a new FileReader instance for each file
                        const reader = new FileReader();
                        
                        // Setup an onloadend event handler for each reader
                        reader.onloadend = () => {
                            const imageData = reader.result;
                            
                            // Add each image data to the imagePreviews array separately
                            this.imagePreviews.push(imageData);

                            // Increment the uploadedFileCount
                            this.uploadedFileCount++;
                            
                            // Add the image data to the image array
                            this.image.push(imageData);

                        };
                        
                        // Read the current file as a data URL
                        reader.readAsDataURL(file);
                    }
                }
        },

        clearForm() {
            this.title = '';
            this.description = '';
            this.price_per_day = '';
            this.location = '';
            this.postal_code = '';
            this.availability = true;
            this.image = '';
            this.condition = '';
            this.category = '';
            this.owner_id = '';
            this.imagePreview = null;
            this.imagePreviews = [];
            this.uploadedFileCount = 0;
        },
        handleDescInput() {
            // Ensure text does not exceed the maximum length
            if (this.description.length > this.maxTextLength) {
                this.description = this.description.slice(0, this.maxTextLength);
            }
        },
        handleTitleInput() {
            // Ensure text does not exceed the maximum length
            if (this.title.length > this.maxTitleLength) {
                this.title = this.title.slice(0, this.maxTitleLength);
            }
        },
        handlePrice(event) {
            // Use a regular expression to allow only integers
            this.price_per_day = event.target.value.replace(/\D/g, '');
        },
        handlePostalCode(event) {
            // Use a regular expression to allow only integers
            this.postal_code = event.target.value.replace(/\D/g, '');
        },
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
/* Add custom styles for the popup */
.popup {
    position: fixed;
    top: 50%; /* Adjust as needed */
    left: 50%; /* Adjust as needed */
    transform: translate(-50%, -50%);
    background-color: #ffffff;
    border: 1px solid #ced4da;
    border-radius: 5px;
    padding: 20px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.popup-content {
    text-align: center;
}

.popup button {
    margin-top: 10px;
    padding: 8px 20px;
    background-color: #007bff;
    color: #ffffff;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-size: 1rem;
    transition: background-color 0.3s ease;
}

.popup button:hover {
    background-color: #0056b3;
}
</style>