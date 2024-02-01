// router.js
import { createRouter, createWebHistory } from 'vue-router';
import Login from './components/LoginPath.vue'; // Import your Login component
import Register from './components/RegisterPath.vue'; // Import your Register component

const routes = [
  {
    path: '/login',
    name: 'login',
    component: Login,
  },
  {
    path: '/register',
    name: 'register',
    component: Register,
  },
  // Other routes
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
