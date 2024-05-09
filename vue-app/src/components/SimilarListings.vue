<template>
    <div class="carousel-object">
        <div class="title-and-button">
            <h1 class="category-header">{{this.category}}</h1>
            <Button class= "refresh-button" icon="pi pi-refresh" rounded outlined @click="refreshListings"/>
        </div>
            <Carousel :value="listings" :orientation="horizontal" :circular="true" :numVisible="2" :numScroll="2" :responsiveOptions="responsiveOptions" v-model:page="page">
                <template #item="slotProps">
                    <router-link :to="'/listing/' + slotProps.data.id" class="carousel-item">
                        <div class="carousel-details">
                            <div class="item-name">{{ slotProps.data.name }}</div>
                            <img :src="slotProps.data.image" style="max-width: 100%;" :alt="slotProps.data.name"/>
                            <div class ="item-data">
                                <div class="item-price">{{ slotProps.data.price_per_day}} kr/day</div>
                                <div class="item-location">{{ slotProps.data.location}}</div>
                            </div>
                        </div>
                    </router-link>
                </template>
            </Carousel>
    </div>
</template>

<script>
import 'primeicons/primeicons.css'
import axios from 'axios';
import Carousel from 'primevue/carousel';
import Button from 'primevue/button';


export default {
    components: {
    Carousel, Button,
},
    props: {
        category: {
            type: String,
            required: true
        }

    },

    data() {
        return {
            listings: [],
            responsiveOptions: [
                {
                    breakpoint: '1106px',
                    numVisible: 2,
                    numScroll: 3
                },
                {
                    breakpoint: '850px',
                    numVisible: 2,
                    numScroll: 2
                },
                {
                    breakpoint: '600px',
                    numVisible: 1,
                    numScroll: 1,   
                }
            ],
            page: 0
        };
    },
    methods: {
        refreshListings() {
            axios.get('/get_items/' + this.category)
                .then(response => {
                    this.listings = response.data;
                    this.page = 0;
                })
                .catch(error => {
                    console.log(error);
                });
        },
    },

     watch: {
        category() {
            // When the category prop changes, fetch new listings
            this.refreshListings();
        }
    },

    created() {
        axios.get('/get_items/' + this.category)
            .then(response => {
                this.listings = response.data;
            })
            .catch(error => {
                console.log(error);
            });
    }
}
</script>

<style scoped>
    .refresh-button{
        scale:0.8;
        transition: transform 100ms ease;
        /* margin-right: 75px; */
    }

    .title-and-button{
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-left: 25px;
        margin-right: 25px;
        
    }

    .carousel-object{
        max-width: 1500px ;
        min-width: 20%;
        margin : 0 auto;
        margin-bottom: 40px;
    }

    .refresh-button:hover{
        animation: spinning 400ms linear infinite;
    }

    .category-header{
        font-family: 'louis_george_cafe', sans-serif;
        margin-top: 0;
        text-align: left;
        font-weight: bold;
        font-size: 28px;
        /* margin-left: 75px; */
        color: var(--primary-color);
        margin-bottom: 0;
    }

    .carousel-item{
        color: var(--primary-color);
        cursor: pointer;
        display:flex;
        align-items: center;
        justify-content: center;
        margin: 8px;
        margin-left: 45px;
        padding: 10px;
        border: 3px solid grey;
        border-radius: 25px;
        transition: transform 250ms ease, color 250ms ease, border 250ms ease; 
        max-width: 300px; /* or whatever width you want */
        min-width: 300px;
        min-height: 300px;
        max-height: 300px;
    }
    .item-data{
        text-align: left;
        display:flex;
        justify-content: space-between;
    }

    img{
        border-radius: 25px;
        padding-top: 5px;
        padding-bottom: 5px;
    }

    .item-name{
        text-align: left;
        font-size: 20px;
        font-weight: bold;
    }

    .carousel-item:hover{
        color: var(--secondary-color);
        scale: 1.02;
        border: 3px solid var(--primary-color); 

    }    
    @keyframes spinning {
        from {
            transform: rotate(0deg);
        }
        to {
            transform: rotate(360deg);
        }
    }
</style>