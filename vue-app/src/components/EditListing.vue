<template>
    <div class="edit-container">
        <h1 class="title">Edit your listing here!</h1>
        <div class="form-wrapper">
            <div class="form-container">
                <div class="input-container">
                    <input type="text" id="name" v-model="name" placeholder="Title" :maxlength="maxTitleLength" @input="handleTitleInput">
                </div>

                <div class="description-container">
                    <textarea id="description" v-model="description" placeholder="Description" rows="6" :maxlength="maxTextLength" @input="handleDescInput"></textarea>
                    <p class="remainingchars">{{ remainingCharacters }} characters remaining</p>
                </div>

                <div class="input-container">
                    <input type="text" id="price_per_day" v-model="price_per_day" placeholder="Price per day" @input="handlePrice">

                    <input v-model="location" type="text" placeholder="Location" class="input-field" />

                    <input type="text" id="postal_code" v-model="postal_code" placeholder="Postal code" :maxlength="maxPostalLength" @input="handlePostalCode">

                    <select id="category" v-model="category" class="custom-select">
                        <option value="" disabled>Select a category</option>
                        <option v-for="category in categories" :key="category" :value="category">{{ category }}</option>
                    </select>

                    <select id="condition" v-model="condition" class="custom-select">
                        <option value="" disabled>Select the condition</option>
                        <option v-for="condition in conditions" :key="condition" :value="condition">{{ condition }}</option>
                    </select>
                </div>
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

                <button @click="updateListing" class="btn">Update</button>
        </div>

    </div>
</template>

<script>
import axios from "axios";
import Cookies from "js-cookie";

export default {
    name: "EditListing",
    data() {
        return {
            name: "",
            description: "",
            price_per_day: "",
            location: "",
            postal_code: "",
            category: "",
            condition: "",
            categories: ['Summer', 'Winter', 'Tools', 'Electronics', 'Clothing', 'Furniture', 'Sports Equipment', 'Books', 'Other'],
            conditions: ['New', 'Used', 'Refurbished'],
            inputNumber: "",
            image: [],
            currentIndex: 0,
            imagePreview: null,
            imagePreviews: [],
            maxFiles: 5,
            maxSizeInBytes: 2 * 1024 * 1024, // 2MB
            maxPostalLength: 4,
            maxTitleLength: 50,
            userLoggedIn: false,
            maxTextLength: 2000,
        };
    },
    computed: {
        titlePlaceholder() {
            return this.name ? this.name : 'Name';
        },
        descriptionPlaceholder() {
            return this.description ? this.description : 'Write a creative description';
        },
        pricePlaceholder() {
            return this.price_per_day ? this.price_per_day : 'Price per day';
        },
        locationPlaceholder() {
            return this.location ? this.location : 'Location';
        },
        postalcodePlaceholder() {
            return this.postal_code ? this.postal_code : 'Postal Code';
        },
        categoryPlaceholder() {
            return this.category ? this.category : 'Category';
        },
        conditionPlaceholder() {
            return this.condition ? this.condition : 'Condition';
        },
        remainingCharacters() {
            return this.maxTextLength - this.description.length;
        },
    },

    beforeRouteEnter(to, from, next) {
        if (Cookies.get('token')) {
            axios.get(`verify-user/`, {
                params: { 
                    item_id: to.params.id 
                } 
            })
            .then(response => {
                // User is authorized, proceed to the route
                console.log('User verified:', response.data);
                next();
            })
            .catch(error => {
                // User is not authorized, redirect to login
                console.error('Error verifying user:', error);
                next('/listing/' + to.params.id);
            });
        } else {
            // No token found, redirect to login
            next('/login');
        }
    },

    created() {
        this.fetchListingDetails();
    },

    methods: {
        updateListing() {
            const data = {
                name: this.name,
                description: this.description,
                price_per_day: this.price_per_day,
                location: this.location,
                postal_code: this.postal_code,
                category: this.category,
                condition: this.condition,
                image: this.imagePreviews,
            };

            // Update the listing based on the ID
            this.updateListingData(data);
        },

        async updateListingData(data) {
            const ListingID = this.$route.params.id;
            try {

                console.log(data);

                const response = await axios.put(`edit_listing/${ListingID}/`, data);
                console.log(response);
                this.$router.push(`/listing/${ListingID}`)
            } catch (error) {
                console.error('Error updating listing:', error); // you are the problem here.
            }
        },

        async fetchListingDetails() {
            const ListingID = this.$route.params.id;
            if (ListingID) {
                try {
                    const response = await axios.get(`get_listing/${ListingID}/`);
                    const listingData = response.data;

                    this.name = listingData.name || '';
                    this.description = listingData.description || '';
                    this.price_per_day = listingData.price_per_day || '';
                    this.location = listingData.location || '';
                    this.category = listingData.category || '';
                    this.condition = listingData.condition || '';
                    this.postal_code = listingData.postal_code || '';
                    this.imagePreviews = listingData.images || [];
                    
                    console.log('Listing data:', listingData);
                } catch (error) {
                    console.error('Error fetching listing data:', error);
                }
            } else {
                console.error('Listing ID is undefined');
            }
        },

        handleDescInput() {
            // Ensure text does not exceed the maximum length
            if (this.description.length > this.maxTextLength) {
                this.description = this.description.slice(0, this.maxTextLength);
            }
        },

        handleTitleInput() {
            // Ensure text does not exceed the maximum length
            if (this.name.length > this.maxTitleLength) {
                this.name = this.name.slice(0, this.maxTitleLength);
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
                            
                            console.log("Updated imagePreviews:", this.imagePreviews);
                            
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
    }
};
</script>

<style scoped>
.edit-container {
    max-width: 800px;
    margin: 0 auto;
    padding-top: 30px;
    border: 1px solid #ced4da;
    border-radius: 5px;
    padding: 20px;
    box-shadow: 0px 0px 6px rgba(0, 0, 0, 0.2);
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

.form-wrapper {
    gap: 2em;
}

.form-container {
    display: flex;
    flex-direction: column;
    gap: 2em;
}

.input-container {
    display: flex;
    flex-direction: column;
    gap: 1em;
}

.input-field {
    resize: none;
    outline: none;
    font-size: 1.4rem;
    padding: 1em 0 1em 0;
    border: none;
    border-bottom: 1px solid rgb(177, 175, 175);
    font-family: 'louis_george_cafe', sans-serif;
}

.btn {
    padding: 1em 2em;
    width: 50%;
    justify-content: center;
    align-items: center;
    border: none;
    border-radius: 5px;
    font-family: 'louis_george_cafe', sans-serif;
    font-size: 1.2rem;
    background-color: #ff5733;
    color: whitesmoke;
    margin-left: auto;
    margin-right: auto;
    margin-top: 20px;
}

.btn:hover {
    background: linear-gradient(to right, #ffa500 0, #ff5733 50%, #ffa500 100%);
}

.btn-container {
    padding-bottom: 10px;
}

custom-select {
    font-family: 'louis_george_cafe', sans-serif;
}

.description-container textarea {
    resize: vertical;
}

.remainingchars {
    font-family: 'louis_george_cafe', sans-serif;
    font-size: 1.5em;
    margin-top: 15px;
}

.input-container, .description-container {
    position: relative;
    flex: auto;
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
    margin-bottom: 20px;
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

.image-title {
    font-family: 'louis_george_cafe', sans-serif;
    font-size: 1.5em;
    margin-top: 30px;
    margin-bottom: 12px;
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

</style>
