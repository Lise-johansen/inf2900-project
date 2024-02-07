// router.js
import { createRouter, createWebHistory } from 'vue-router';
import Login from './components/LoginPath.vue'; // Import your Login component
import Register from './components/RegisterPath.vue'; // Import your Register component
import PasswordReset from './components/PasswordReset.vue'; // Import Password Reset component

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
  {
    path: '/reset',
    name: 'reset',
    component: PasswordReset
  }
  // Other routes
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
