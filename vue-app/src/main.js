import { createApp } from 'vue';
import App from './App.vue';
import VueRouter from 'vue-router';
import router from './router';

const app = createApp(App);

app.use(VueRouter);

  // Allow the user to log in as usual
  app.use(router).mount('#app');