<!-- <template>
    <div>
        <input v-model="name" type="text" placeholder="Name">
        <input v-model="description" type="text" placeholder="Description">
        <input v-model="price_per_day" type="number" placeholder="Price per day">
        <input v-model="location" type="text" placeholder="Location">
        <input v-model="category" type="text" placeholder="Category">
        <button @click="updateListing">Update</button>
        <input v-model="inputNumber" type="number" placeholder="ID">
    </div>
</template>

<script>
import axios from 'axios';

export default {
    name: 'EditListing',
    data() {
        return {
            name: '',
            description: '',
            price_per_day: '',
            location: '',
            category: '',
            inputNumber: '',
        };
    },

    created() {
        // Call the method to redirect if the user is not logged in
        this.redirectIfLoggedIn();
    },

    methods: {
        updateListing() 
        {
            const data = {
                name: this.name,
                description: this.description,
                price_per_day: this.price_per_day,
                location: this.location,
                category: this.category
            };
                
            axios.put(`http://localhost:8080/api/edit_listing/${this.inputNumber}/`, data)
                .then(response => {
                    console.log(response);
                })
                .catch(error => {
                    console.log(error);
                });        
        },

        redirectIfLoggedIn()
        {
            // Redirect to login page if user is not logged in
            console.log('Checking if user is logged in...');
            const token = this.getTokenFromCookies();
            if (token === 'undefined') {
                // Token is not found in cookies (user is not logged in)
                if (confirm('You must be logged in to view this page.')) {
                    this.$router.push('/login'); 
                }
            }
        },

        // Get the token from the cookies
        getTokenFromCookies() 
        {
            const cookies = document.cookie.split('; ');
            for (const cookie of cookies) {
                const [name, value] = cookie.split('=');
                if (name === 'token') {
                return value;
                }
            }
            return null; // Token not found in cookies
        }
    }
};
</script>

<style scoped>
/*Your component styles go here */
</style> -->

<!-- 
<template>
    <div class="contact-form">
      <h1 class="form-title">Update Listing</h1>
      <div class="form-wrapper">
        <div class="form-container">
          <input v-model="name" type="text" placeholder="Name" class="message-box">
          <input v-model="description" type="text" placeholder="Description" class="message-box">
          <input v-model="price_per_day" type="number" placeholder="Price per day" class="message-box">
          <input v-model="location" type="text" placeholder="Location" class="message-box">
          <input v-model="category" type="text" placeholder="Category" class="message-box">
          <button @click="updateListing" class="btn">Update</button>
          <input v-model="inputNumber" type="number" placeholder="ID" class="message-box">
        </div>
  
        <div class="encouraging-container">
          <h2 class="encouraging-title">Let's update your listing.</h2>
          <h2 class="encouraging-text">Make the necessary changes to your listing and click the update button to save the changes.</h2>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    name: 'EditListing',
    data() {
      return {
        name: '',
        description: '',
        price_per_day: '',
        location: '',
        category: '',
        inputNumber: '',
      };
    },
  
    methods: {
      updateListing() {
        const data = {
          name: this.name,
          description: this.description,
          price_per_day: this.price_per_day,
          location: this.location,
          category: this.category
        };
  
        axios.put(`http://localhost:8080/api/edit_listing/${this.inputNumber}/`, data)
          .then(response => {
            console.log(response);
          })
          .catch(error => {
            console.log(error);
          });
      },
    }
  };
  </script>
  
  <style scoped>
  .contact-form {
    width: 50%;
    margin: 0 auto;
  }
  
  .form-wrapper {
    display: flex;
  }
  
  .form-container {
    display: flex;
    flex-direction: column;
    gap: 2em;
    padding-right: 2em;
    flex-basis: 50%;
  }
  
  .message-box {
    resize: none;
    outline: none;
    font-size: 1rem;
    padding: 1em 0 1em 0;
    border: none;
    border-bottom: 1px solid rgb(177, 175, 175);
  }
  
  .btn {
    padding: 1em 2em;
    align-self: flex-start;
    border: none;
    font-family: 'louis_george_cafe', sans-serif;
    background-color: #ff5733;
    color: whitesmoke;
  }
  
  .btn:hover {
    background: linear-gradient(to right,#ffa500 0, #ff5733 50%, #ffa500 100%);
  }
  
  .encouraging-container {
    flex-basis: 50%;
    display: flex;
    padding-left: 2em;
    flex-direction: column;
  }
  
  .encouraging-title,
  .encouraging-text,
  .form-title {
    text-align: start;
    opacity: 0;
    animation: fadeIn 1.5s ease forwards;
  }
  
  .encouraging-title {
    align-self: flex-start;
    margin: 0;
    opacity: 0;
    animation: fadeIn 1.5s ease forwards;
    animation-delay: 0.5s;
  }
  
  .encouraging-text {
    font-family: 'louis_george_cafe', sans-serif;
    opacity: 0;
    animation: fadeIn 1.5s ease forwards;
    animation-delay: 1.5s;
  }
  
  @keyframes fadeIn {
    from {
      opacity: 0;
    }
    to {
      opacity: 1;
    }
  }
  </style>
   -->

<template>
    <div v-if="userLoggedIn" class="contact-form">
        <h1 class="form-title">Update Listing</h1>
        <div class="form-wrapper">
            <div class="form-container">
                <div class="input-container">
                    <input v-model="name" type="text" placeholder="Name" class="input-field" />
                </div>
                <div class="description-container">
                    <textarea id="description" v-model="description" placeholder="Write a creative description"
                        rows="10" :cols="45"></textarea>
                </div>
                <div class="input-container">
                    <input v-model="price_per_day" type="number" placeholder="Price per day" class="input-field" />
                </div>
                <div class="input-container">
                    <input v-model="location" type="text" placeholder="Location" class="input-field" />
                </div>
                <div class="input-container">
                    <input v-model="category" type="text" placeholder="Category" class="input-field" />
                </div>
                <div class="button-container">
                    <button @click="updateListing" class="btn">Update</button>
                    <!-- <input v-model="inputNumber" type="number" placeholder="ID" class="input-field" disabled /> -->
                </div>
            </div>

            <div class="encouraging-container">
                <h2 class="encouraging-title">Let's update your listing.</h2>
                <h2 class="encouraging-text">
                    Make the necessary changes to your listing and click the update button
                    to save the changes.
                </h2>
            </div>
        </div>
    </div>

    <div v-else>
        <div class="login-container">
            <h2 class="encouraging-title login-title animated-fade-in">Please log in first to update your listing.</h2>
            <router-link to="/login" class="login-btn btn">Log In</router-link>
        </div>
    </div>
</template>

<script>
import axios from "axios";

export default {
    name: "EditListing",
    data() {
        return {
            name: "",
            description: "",
            price_per_day: "",
            location: "",
            category: "",
            inputNumber: "",
            userLoggedIn: false
        };
    },
    computed: {
        namePlaceholder() {
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
        categoryPlaceholder() {
            return this.category ? this.category : 'Category';
        }
    },

    created() {
        this.checkLoggedIn();
        this.fetchListingDetails();
    },

    methods: {
        updateListing() {
            const data = {
                name: this.name,
                description: this.description,
                price_per_day: this.price_per_day,
                location: this.location,
                category: this.category,
            };

            // Update the listing based on the ID
            this.updateListingData(data);
        },

        async updateListingData(data) {
            try {
                const response = await axios.put(`edit_listing/${this.inputNumber}/`, data);
                console.log(response);
            }
            catch (error) {
                console.error('Error updating listing:', error);
            }
        },

        checkLoggedIn() {
            const token = this.getTokenFromCookies();
            if (token) {
                this.userLoggedIn = true;
            }
            else {
                this.redirectToLogin();
            }
        },

        redirectToLogin() {
            if (confirm("You must be logged in to view this page.")) {
                this.$router.push("/login");
            }
        },

        getTokenFromCookies() {
            const cookies = document.cookie.split('; ');
            for (const cookie of cookies) {
                const [name, value] = cookie.split('=');
                if (name === 'token') {
                    return value;
                }
            }
            return null;
        },

        async fetchListingDetails() {
            const ListingID = this.$route.params.id;
            try {
                const response = await axios.get(`get_listing/${ListingID}/`);
                document.cookie = `token=${response.data.token}`;

                const listingData = response.data;

                // Update the data fields with the fetched listing data
                this.name = listingData.name || '';
                this.description = listingData.description || '';
                this.price_per_day = listingData.price_per_day || '';
                this.location = listingData.location || '';
                this.category = listingData.category || '';

                console.log('Listing data:', listingData);
            }
            catch (error) {
                console.error('Error fetching listing data:', error);
            }
        },
    }
};
</script>


<style scoped>
.contact-form {
    width: 50%;
    margin: 0 auto;
    padding-top: 30px;
}

.form-title {
    padding-bottom: 20px;
}

.form-wrapper {
    display: flex;
    flex-direction: row;
    gap: 2em;
    padding-top: 10px;
}

.form-container {
    display: flex;
    flex-direction: column;
    gap: 2em;
}

.input-container {
    display: flex;
    flex-direction: column;
}

.input-field {
    resize: none;
    outline: none;
    font-size: 1rem;
    padding: 1em 0 1em 0;
    border: none;
    border-bottom: 1px solid rgb(177, 175, 175);
    font-family: 'louis_george_cafe', sans-serif;
}

.btn {
    padding: 1em 2em;
    align-self: flex-start;
    border: none;
    font-family: 'louis_george_cafe', sans-serif;
    background-color: #ff5733;
    color: whitesmoke;
}

.btn:hover {
    background: linear-gradient(to right, #ffa500 0, #ff5733 50%, #ffa500 100%);
}

.encouraging-container {
    display: flex;
    flex-direction: column;
    padding-left: 80px;
}

.encouraging-title,
.encouraging-text,
.form-title {
    text-align: start;
    opacity: 0;
    animation: fadeIn 1.5s ease forwards;
}

.encouraging-title {
    align-self: flex-start;
    margin: 0;
    opacity: 0;
    animation: fadeIn 1.5s ease forwards;
    animation-delay: 0.5s;


}

.button-container {
    padding-bottom: 10px;
    transform: translate(350px, -75px);
    /* right and down */

}

.encouraging-text {
    font-family: 'louis_george_cafe', sans-serif;
    opacity: 0;
    animation: fadeIn 1.5s ease forwards;
    flex-direction: column;
}

@keyframes fadeIn {
    from {
        opacity: 0;
    }

    to {
        opacity: 1;
    }
}
</style>
