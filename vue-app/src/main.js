import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import axios from 'axios';
import PrimeVue from 'primevue/config';

axios.defaults.baseURL = 'http://localhost:8000/api/';
axios.defaults.withCredentials = true;
import 'primevue/resources/themes/lara-light-amber/theme.css'
const app = createApp(App);
app.use(PrimeVue);
app.use(router).mount('#app');
