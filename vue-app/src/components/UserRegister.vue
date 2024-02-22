<template>
    <div>
        <h1>Register your profile!</h1>
        <form @submit.prevent="registerUser">
        <div class="form-group">
        <label for="first_name">First Name: </label>
        <input type="text" class="form-control" id="name" v-model="name"> 
        </div>
        <div class="form-group">
        <label for="last_name">Last Name: </label>
        <input type="text" class="form-control" id="last-name" v-model="last_name">
        </div>
        <div class="form-group">
        <label for="address">Address: </label>
        <input type="text" class="form-control" id="address" v-model="address">
        </div>
        <div class="form-group">
        <label for="phone">Phone Number: </label>
        <input type="text" class="form-control" id="phone" v-model="phone">
        </div>
        <div class="picture">
        <!-- Input field for selecting profile picture -->
        <input type="file" accept="image/*" @change="handleImageUpload">
        
        <!-- Display the selected profile picture -->
        <img v-if="profilePicture" :src="profilePicture" alt="Profile Picture" class="profile-picture">
        
        <!-- Button to upload the profile picture -->
        <button @click="uploadProfilePicture">Upload Profile Picture</button>
        </div>
        <button type="submit" class="btn btn-primary">Register</button>
        </form>
    </div>
</template>


<script>
import axiosInstance from '@/axios';

export default {
    data() {
        return {
            first_name: '',
            last_name: '',
            address: '',
            phone: '',
            bio: '',
            profilePicture: null, // Variable to store the selected profile picture
        }
    },
    methods: {
            // Event handler for selecting a profile picture
            handleImageUpload(event) {
        this.profilePicture = event.target.files[0];
    },
    uploadProfilePicture() {
        const formData = new FormData();
        formData.append('profilePicture', this.profilePicture);
        
        axiosInstance.post('upload-profile-picture/', formData)
        .then(response => {
            console.log(response);
            console.log('Profile picture uploaded successfully');
        })
        .catch(error => {
            console.error('Error uploading profile picture:', error);
        });
    },
        registerUser() {
            axiosInstance.post('userregister/', {
                first_name: this.first_name,
                last_name: this.last_name,
                address: this.address,
                phone: this.phone,
                bio: this.bio,
                profile_picture: this.profile_picture
            })
            .then(response => {
                console.log(response);
            })
            .catch(error => {
                console.log(error);
            })
        }
    }
}

</script>

<style scoped>
    h3 {
        color: blue;
    }
    .form-control {
        width: 25%;
        padding: .375rem .75rem;
        font-size: 1rem;
        line-height: 1.5;
        color: #495057;
        background-color: #fff;
        background-clip: padding-box;
        border: 1px solid #ced4da;
        border-radius: .25rem;
        transition: border-color .15s ease-in-out,box-shadow .15s ease-in-out;
    }
    .form-group {
        margin-bottom: 1rem;
    }
    .profile-picture {
    max-width: 200px; /* Adjust the maximum width as needed */
    max-height: 200px; /* Adjust the maximum height as needed */
    border-radius: 50%; /* Optional: Apply rounded corners to the image */
    }
    
</style>