import { createApp } from 'vue';
import App from './App.vue';
import router from './router';

const app = createApp(App);

// Allow the user to log in as usual
app.use(router).mount('#app');