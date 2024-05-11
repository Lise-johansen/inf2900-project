<template>
  <div class="card">
    <router-link :to="'/listing/' + listing.pk" class="card-content">
      <!-- You should use `listing.id` if that's what's being passed, or `listing.pk` if that's what's named in the prop -->
      <div class="card-details">
        <div class="item-name">{{ listing.fields.name }}</div>
        <!-- Make sure `listing.image` has the correct data -->
        <img :src="listing.fields.image" style="max-width: 100%;" :alt="listing.fields.name"/>
        <div class="item-data">
          <div class="item-price">{{ listing.fields.price_per_day }} kr/day</div>
          <div class="item-location">{{ listing.fields.location }}</div>
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
      required: true,
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
    color: var(--primary-color);
    cursor: pointer;
    display: none;
    align-items: none;
    justify-content: center;
    margin: 20px;
    padding: 20x;
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

  .item-data{
      text-align: left;
      display:flex;
      justify-content: space-between;
    }
  
  .card-details {
    text-align: left;
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
  