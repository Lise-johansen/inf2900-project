// import { createApp } from 'vue';
// import App from './App.vue';
// import router from './router';
// import axios from './axios';
// import csrf from './csrf';

// const app = createApp(App);

// app.use(router, axios, csrf).mount('#app');

import { createApp } from 'vue';
import App from './App.vue';
<<<<<<< HEAD
import router from './router';
import axiosInstance from './axios';
import { getCSRFToken } from './csrf';
=======
import VueRouter from 'vue-router';
import router from './router';
>>>>>>> localtest_johannes

const app = createApp(App);

// Use the router
app.use(router);

<<<<<<< HEAD
// Set up Axios as a global Vue plugin
app.config.globalProperties.$axios = axiosInstance;

// Set up CSRF token as a global Vue property
app.config.globalProperties.$csrfToken = getCSRFToken();

app.mount('#app');
=======
  // Allow the user to log in as usual
  app.use(router).mount('#app');
>>>>>>> localtest_johannes
