import { createApp } from 'vue';
import App from './App.vue';
import VueRouter from 'vue-router'

import router from './router'

const app = createApp(App);

app.use(VueRouter);

app.use(router).mount('#app');
