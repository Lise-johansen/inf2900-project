<template>
  <div class="reserved-listing">
  <div class="card">
    <router-link :to="'/listing/' + listing.id" class="card-content">
      <!-- You should use `listing.id` if that's what's being passed, or `listing.pk` if that's what's named in the prop -->
      <div class="card-details">
        <div class="item-name">{{ listing.name }}</div>
        <div class="image-container">
            <img :src="listing.image" style="max-width: 100%;" :alt="listing.name"/>
        </div>
        <div class ="item-data">
            <div class="item-price">{{ listing.price_per_day}} kr/day</div>
            <div class="item-location">{{ listing.location}}</div>
        </div>
      </div>
    </router-link>
  </div>
  <div class="item-dates"> Renting Period: </div>
  <div class="item-dates"> From {{ formatDate(listing.start_date) }}   To   {{ formatDate(listing.end_date) }}</div>
  </div>
</template>

<script>

export default {
  props: {
    listing: {
      type: Object,
      required: true,
    }
  },
  methods: {
    formatDate(date) {
      return new Date(date).toLocaleDateString('en-GB');
    }
  },
}
</script>
  
  <style scoped>
  .cards-container {
    display: flex;
    flex-wrap: wrap; /* This ensures that cards will wrap onto the next line */
    justify-content: center; /* Adjust this to flex-start for left alignment if needed */
    gap: 1rem; /* Provides space between cards */
  }
  .card {
    font-family: 'louis_george_cafe', sans-serif;
    color: var(--primary-color);
    cursor: pointer;
    display: flex;
    align-items: none;
    justify-content: center;
    margin: 8px;
    padding: 10px;
    border: 3px solid grey;
    border-radius: 25px;
    transition: transform 250ms ease, color 250ms ease, border 250ms ease;
    max-width: 300px; 
    min-width: 300px;
    min-height: 300px;
    max-height: 300px;
    margin: 0 auto; /* to center the card */
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* optional, for a subtle shadow */
  }
  .item-data{
    margin: 10px;
    width: 250px;
    align-items: center;
    text-align: left;
    display:flex;
    justify-content: space-between;
  }
  .card-content {
    color: var(--primary-color);
    display: flex;
    align-items: center;
    justify-content: center;
    width: 100%;
    text-decoration: none;
  }
  
  .card-content:hover {
    color: var(--secondary-color);
  }

  .card-details {
    text-align: left;
  }
  
  .image-container {
        display: flex;
        justify-content: center;
    }

    img {
        border-radius: 25px;
        max-width: 300px;
        max-height: 220px;
        padding-top: 5px;
        padding-bottom: 5px;
    }
  
  .item-name {
    text-align: left;
    font-size: 20px;
    font-weight: bold;
  }

  .item-dates {
    background: linear-gradient(to right, #ff5733, #ffa500, #4169e1);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-top: 7px;
    font-size: 16px;
    font-weight: bold;
  }

  .reserved-listing:hover{
    color: var(--secondary-color);
    scale: 1.03;
    border: none;
  }

  .card:hover {
    color: var(--secondary-color);
    scale: 1.03;
    border: 3px solid var(--primary-color);
  } 

    .item-name{
        text-align: left;
        font-size: 20px;
        font-weight: bold;
    }
  </style>
  