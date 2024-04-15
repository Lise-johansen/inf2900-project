<template>
  <div id="map"></div>
  <div>Latitude: {{ latitude }}</div>
  <div>Longitude: {{ longitude }}</div>
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
    this.getLocationCoordinates('Tromsø');
  },
  methods: {
    getLocationCoordinates(city) {
      const apiKey = '661d0b57ae725462506558qak8f7522';
      const apiURL = `https://geocode.maps.co/search?q=${encodeURIComponent(city)}&api_key=${apiKey}`;
  
      axios.get(apiURL)
        .then(response => {
          console.log('API Response:', response.data); // Log the response to inspect its structure
          // Extract latitude and longitude from the response
          const lat = response.data[0].lat;
          const lon = response.data[0].lon;

          this.latitude = lat;
          this.longitude = lon;

          // Initialize the map with the retrieved coordinates
          this.initializeMap(lat, lon);
        })
        .catch(error => {
          console.error('Error fetching location coordinates:', error);
        });
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
#map {
  height: 400px;
  width: 100%;
}
</style>

