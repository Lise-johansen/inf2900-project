import { createApp } from 'vue';
import App from './App.vue';
import router from './router.js'; // Import the router instance from router.js so the app redirects to other pages.

createApp(App).use(router).mount('#app');