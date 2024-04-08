import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import axios from 'axios';

// axios.defaults.baseURL = 'https://django.dybedahlserver.net/api/';
axios.defaults.baseURL = 'http://localhost:8000/api/';

axios.defaults.withCredentials = true;

const app = createApp(App);

app.use(router).mount('#app');
