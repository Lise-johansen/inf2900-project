<template>
    <div class="carousel-object">
        <div class="title-and-button">
            <h1 class="category-header">{{this.category}}</h1>
            <Button class= "refresh-button" icon="pi pi-refresh" rounded outlined/>
        </div>
            <Carousel :value="listings" :orientation="horizontal" :circular="true" :numVisible="4" :numScroll="2" :responsiveOptions="responsiveOptions">
                <template #item="slotProps">
                    <div class="carousel-item">
                        <div class="carousel-details">
                            <div class="item-name">{{ slotProps.data.name }}</div>
                            <img :src="'https://via.placeholder.com/210'" :alt="slotProps.data.name"/>
                            <div class ="item-data">
                                <div class="item-price">{{ slotProps.data.price_per_day}} kr/day</div>
                                <div class="item-location">{{ slotProps.data.location}}</div>
                            </div>
                        </div>
                    </div>
                </template>
            </Carousel>
    </div>
</template>

<script>
import 'primeicons/primeicons.css';
import axios from 'axios';
import Carousel from 'primevue/carousel';
import Button from 'primevue/button';


export default {
    components: {
        Carousel, Button
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
                    numVisible: 3,
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
            ]
        };
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

<style>
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
        max-width: 1200px ;
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
        padding: 10px;
        border: 3px solid grey;
        border-radius: 25px;
        transition: transform 250ms ease, color 250ms ease, border 250ms ease; 
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
        scale: 1.03;
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