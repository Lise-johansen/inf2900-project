<template>
  <div class="card">
    <router-link :to="'/listing/' + listing.id" class="card-content">
      <!-- You should use `listing.id` if that's what's being passed, or `listing.pk` if that's what's named in the prop -->
      <div class="card-details">
        <div class="item-name">{{ listing.name }}</div>
        <!-- Make sure `listing.image` has the correct data -->
        <img :src="listing.images" style="max-width: 100%;" :alt="listing.name"/>
        <div class="card-footer">
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
      listing_id: '',
      name: '',
      image: '',
      price_per_day: '',
      location: ''
      
    }
  },
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
    max-width: 300px; /* or whatever width you want */
    margin: 0 auto; /* to center the card */
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* optional, for a subtle shadow */
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
        min-width: 300px;
        height: 100%;
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
  </style>
  