import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import axios from 'axios';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import { library } from '@fortawesome/fontawesome-svg-core';
import { fas} from '@fortawesome/free-solid-svg-icons';

axios.defaults.baseURL = 'https://django.dybedahlserver.net/api/';
axios.defaults.withCredentials = true;

const app = createApp(App);

library.add(fas);


// Use router
app.use(router);

app.component('font-awesome-icon', FontAwesomeIcon)

// Mount the app
app.mount('#app');