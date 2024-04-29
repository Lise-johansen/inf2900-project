<template>
    <div class="card">
      <router-link :to="'/listing/' + listing.id" class="card-content">
        <div class="card-details">
          <div class="item-name">{{ listing.name }}</div>
          <img :src="listing.image" style="max-width: 100%;" :alt="listing.name"/>
          <div class="card-data">
            <div class="item-price">{{ listing.price_per_day }} kr/day</div>
            <div class="item-location">{{ listing.location }}</div>
          </div>
        </div>
      </router-link>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      listing: {
        type: Object,
        required: true
      }
    }
  }
  </script>
  
  <style scoped>
  .card {
    color: var(--primary-color);
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 8px;
    padding: 10px;
    border: 3px solid grey;
    border-radius: 25px;
    transition: transform 250ms ease, color 250ms ease, border 250ms ease;
  }
  
  .card-content {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 100%;
    text-decoration: none;
  }
  
  .card-details {
    text-align: left;
  }
  
  .card-data {
    display: flex;
    justify-content: space-between;
  }
  
  img {
    border-radius: 25px;
    padding-top: 5px;
    padding-bottom: 5px;
  }
  
  .item-name {
    text-align: left;
    font-size: 20px;
    font-weight: bold;
  }
  
  .card:hover {
    color: var(--secondary-color);
    scale: 1.03;
    border: 3px solid var(--primary-color);
  }
  </style>
  