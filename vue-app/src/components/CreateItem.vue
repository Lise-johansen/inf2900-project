<template>
    <div class="create-item-container">
        <h1 class="title">Create your listing here!</h1>
        <form @submit.prevent="createItem">
            <div class="form-group">
                <input type="text" id="title" v-model="title" placeholder="Title" :maxlength="maxTitleLength" @input="handleTitleInput">
            </div>
            <div class="form-group">
                <textarea id="description" v-model="description" placeholder="Description" rows="6" :maxlength="maxTextLength" @input="handleDescInput"></textarea>
                <p class="remainingchars">{{ remainingCharacters }} characters remaining</p>
            </div>
            <div class="form-group">
                <input type="text" id="price_per_day" v-model="price_per_day" placeholder="Price per day" @input="handlePrice">
            </div>
            <div class="form-group">
                <input type="text" id="location" v-model="location" placeholder="City">
            </div>
            <div class="form-group">
                <input type="text" id="postal_code" v-model="postal_code" placeholder="Postal code" :maxlength="maxPostalLength" @input="handlePostalCode">
            </div>
            <div class="form-group">
                <select id="category" v-model="category" class="custom-select">
                    <option value="" disabled>Select a category</option>
                    <option v-for="category in categories" :key="category" :value="category">{{ category }}</option>
                </select>
            </div>
            <div class="form-group">
                <select id="condition" v-model="condition" class="custom-select">
                    <option value="" disabled>Select the condition</option>
                    <option v-for="condition in conditions" :key="condition" :value="condition">{{ condition }}</option>
                </select>
            </div>

            <div class="image-title">Choose the images you would like to use for your listing below:</div>
            <div class="image-container">
                <div class="form-group">
                    <input id="fileInput" type="file" ref="fileInput" @change="handleFileUpload" multiple>
                    <label for="fileInput" class="custom-file-upload">
                        <i class="pi pi-upload" style="font-size: 2rem; margin-bottom: 5px; margin-top: 5px;"></i>
                    </label>
                </div>
                <div class="image-gallery" v-if="imagePreviews.length > 0">
                    <div class="preview-container">
                        <div class="image-wrapper" v-for="(imagePreview, index) in imagePreviews" :key="index" v-show="currentIndex == index">
                            <img :src="imagePreview" alt="Image Preview" class="gallery-image">
                            <button type="button" @click="removeImage(index)" class="remove-button"><i class="pi pi-times-circle" style="font-size: 2rem;"></i></button>
                        </div>
                        <div class="nav-container">
                            <button class="nav-btn" type="button" @click="handleNavigation('prev')" :disabled="currentIndex === 0">Previous</button>
                            <button class="nav-btn" type="button" @click="handleNavigation('next')" :disabled="currentIndex === imagePreviews.length - 1">Next</button>
                        </div>
                    </div>
                </div>
                <div v-else>
                    No images uploaded.
                </div>
            </div>

            <div class="form-group">
                <button type="submit" class="post-btn">Post listing</button>
            </div>
            <p class="slogan">You're one step away from finding the perfect match with Rentopia!</p>
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
import 'primeicons/primeicons.css'

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
            currentIndex: 0,
            imagePreview: null,
            imagePreviews: [],
            uploadedFileCount: 0,
            maxFiles: 5,
            // Change size if needed
            maxSizeInBytes: 5 * 1024 * 1024, // 5MB
            // Define the available categories
            categories: ['Sports Equipment', 'Books', 'Electronics', 'Clothing', 'Furniture', 'Tools', 'Toys', 'Instruments', 'Town Square', 'Winter', 'Summer'],
            conditions: ['New', 'Used', 'Refurbished'],
            maxTextLength: 2000,
            maxTitleLength: 100,
            maxPostalLength: 4,
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
                    this.showPopup = true;
                    this.popupMessage = 'Error creating listing. Please try again.';
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

                this.currentIndex = 0;
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
                        this.popupMessage = 'File size exceeds the limit (5MB). Please choose a smaller file.';
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

        removeImage(index) {
            // Remove the image preview and corresponding image data from arrays
            this.imagePreviews.splice(index, 1);
            this.image.splice(index, 1);
            this.uploadedFileCount--;
            this.prevImage();
        },

        handleNavigation(action) {
            if (action === 'prev') {
                this.prevImage();
            } else if (action === 'next') {
                this.nextImage();
            }
        },

        prevImage() {
            if (this.currentIndex > 0) {
                this.currentIndex--;
            }
        },

        nextImage() {
            if (this.currentIndex < this.imagePreviews.length - 1) {
                this.currentIndex++;
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
    },
    components : {
    }
}
</script>

<style scoped>
.create-item-container {
    max-width: 800px;
    margin: 0 auto;
    align-items: center;
    justify-content: center;
    border: 1px solid #ced4da;
    border-radius: 5px;
    box-shadow: 0px 0px 6px rgba(0, 0, 0, 0.2);
    padding: 20px;
    margin-top: 20px;
    margin-bottom: 20px;
}

.title {
    text-align: center;
    font-size: 2.5rem;
    font-weight: bold;
    margin-bottom: 30px;
    font-family: 'louis_george_cafe', sans-serif;
    background: linear-gradient(to right, #ffa500 0, #ff5733 50%, #ffa500 100%);
    -webkit-text-fill-color: transparent;
    -webkit-background-clip: text;
}

.form-group {
    position: relative;
    flex: auto;
    margin-bottom: 20px;
    max-width: 100%;
}

input[type="text"], input[type="number"], textarea {
    outline: none;
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
    font-size: 1.5rem;
    font-family: 'louis_george_cafe', sans-serif;
}

textarea {
    resize: vertical;
}

.custom-select {
    appearance: true;
    -moz-appearance: none;
    -webkit-appearance: none;
    background-image: url('data:image/svg+xml;utf8,<svg fill="#000000" height="24" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg"><path d="M7 10l5 5 5-5z"/><path d="M0 0h24v24H0z" fill="none"/></svg>');
    background-repeat: no-repeat;
    background-position-x: calc(100% - 10px);
    background-position-y: center;
    padding-right: 30px;
}

.preview-container{
    width: 600px;
}

.nav-container{
    display: flex;
    gap: 10px;
}

.nav-btn, .post-btn {
    width: 50%;
    padding: 15px;
    border: none;
    color: #fff;
    border-radius: 5px;
    font-size: 1.2rem;
    margin-top: 20px;
    cursor: pointer;
    font-family: 'louis_george_cafe', sans-serif;
    background-color: #ff5733;
    color: whitesmoke;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
}
 
.nav-btn:hover, .post-btn:hover {
    background: linear-gradient(to right, #ffa500 0, #ff5733 50%, #ffa500 100%);
}

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
    font-family: 'louis_george_cafe', sans-serif;
    font-size: 1.5em;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.8);
}

.popup-content {
    text-align: center;
}

.remainingchars {
    font-family: 'louis_george_cafe', sans-serif;
    font-size: 1.5em;
    margin-top: 15px;
}

.image-title {
    font-family: 'louis_george_cafe', sans-serif;
    font-size: 1.5em;
    margin-top: 30px;
    margin-bottom: 12px;
}
.popup button {
    margin-top: 10px;
    padding: 8px 20px;
    background-color: #ff5733;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-size: 1rem;
    transition: background-color 0.3s ease;
    font-family: 'louis_george_cafe', sans-serif;
    font-size: 0.7em;
    color: whitesmoke;
}

.popup button:hover {
    background: linear-gradient(to right, #ffa500 0, #ff5733 50%, #ffa500 100%);
}
.slogan {
    font-size: 1.5rem;
    font-weight: bold;
    font-family: 'louis_george_cafe', sans-serif;
    background: linear-gradient(to right, #ff5733 0%, #ffa500 25%, #ffa500 50%, #4169e1 75%);
    -webkit-text-fill-color: transparent;
    -webkit-background-clip: text;
    padding-top: 20px;
}

.image-container {
    display: flex;
    flex-direction: column; /* Align items vertically */
    justify-content: center; /* Center items vertically */
    align-items: center; /* Center items horizontally */
    background: rgba(255, 255, 255, 0.2);
    border-radius: 5px;
    padding: 10px;
    padding-bottom: 30px;
    padding-top: 30px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.custom-file-upload {
    display: inline-block;
    padding: 10px 20px;
    cursor: pointer;
    background-color: #ff5733;
    color: #fff;
    border-radius: 50%; /* Make it circular */
    width: 100px; /* Adjust width as needed */
    height: 100px; /* Adjust height as needed */
    line-height: 100px; /* Center the text vertically */
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.4);
}

.form-group input[type="file"] {
    display: none;
}

.remove-button {
    top: -30px;
    right: -20px;
    position: absolute;
    background: none;
    cursor: pointer;
    border: none;
    border-radius: 50%;
    font-size: 1rem;
    z-index: 1; /* Ensure it's above the image */
}

.remove-button:hover {
    transform: scale(1.2,1.2);
    transition: transform 1s ease;
}

.image-gallery {
    max-width: 100%;
}

.image-wrapper {
    position: relative;
    max-width: 600px; /* Adjust as needed */
}

.gallery-image {
    display: block; /* Ensures the image behaves as a block element */
    margin: 0 auto; /* Centers the image horizontally */
    width: 100%; /* Makes the image fill its container */
    max-height: 600px; /* Adjust the maximum height as needed */
    height: auto; /* Allows the image to maintain its aspect ratio */
    max-width: 100%; /* Ensures the image does not exceed its container */
}

</style>