<template>
  <div class="wrapper">
    <div id="map"></div>
  </div>
</template>

<script>
import L from 'leaflet';
import 'leaflet/dist/leaflet.css';
import axios from 'axios';

export default {
  data() {
    return {
      latitude: null,
      longitude: null
    };
  },
  mounted() {
    this.getLocationCoordinates('8610, Norway');
  },
  methods: {
    async getLocationCoordinates(city) {
      const apiKey = '661d0b57ae725462506558qak8f7522';
      const apiURL = `https://geocode.maps.co/search?q=${city}&api_key=${apiKey}`;
    
        try {
          const response = await axios.get(apiURL, {withCredentials: false})
          // Extract latitude and longitude from the response

          this.latitude = response.data[0].lat;
          this.longitude = response.data[0].lon;

          // Initialize the map with the retrieved coordinates
          this.initializeMap(this.latitude, this.longitude);
        }
        catch{
          console.error('Error fetching location coordinates:');
        }
    },

    initializeMap(lat, lon) {
      // Initialize the map
      const map = L.map('map').setView([lat, lon], 13);

      // Add tile layer (using OpenStreetMap tiles)
      L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      }).addTo(map);

    }
  }
};
</script>

<style scoped>
.wrapper{
height: 100dvh;
display: flex;
border: 2px solid rgba(255,255,255,0.1);
justify-content: center;
align-items: center;
}
#map {
  border-radius: 5px;
  box-shadow: 0 0 10px rgba(8,7,16,0.6);
  height: 400px;
  width: 700px;
}
</style>

