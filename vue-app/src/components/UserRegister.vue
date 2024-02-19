<template>
    <div>
        <h1>User Register</h1>
        <form @submit.prevent="registerUser">
        <div class="form-group">
        <label for="name">Name</label>
        <input type="text" class="form-control" id="name" v-model="name"> 
        </div>
        <div class="form-group">
        <label for="address">Address</label>
        <input type="text" class="form-control" id="address" v-model="address">
        </div>
        <div class="form-group">
        <label for="phone">Phone Number</label>
        <input type="text" class="form-control" id="phone" v-model="phone">
        </div>
        <div class="form-group">
        <label for="bio">Bio</label>
        <input type="text" class="form-control" id="bio" v-model="bio">
        </div>
        <div class="form-group">
        <label for="profile_picture">Profile Picture</label>
        <input type="file" class="form-control" id="profile_picture" v-on:change="profile_picture">
        </div>
        <button type="submit" class="btn btn-primary">Register</button>
        </form>
    </div>
</template>


<script>
import axios from 'axios';

export default {
    data() {
        return {
            name: '',
            address: '',
            phone: '',
            bio: '',
            profile_picture: '',
        }
    },
    methods: {
        registerUser() {
            axios.post('http://localhost:8000/api/userregister/', {
                name: this.name,
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