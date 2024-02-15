import { createRouter, createWebHistory } from 'vue-router';
import Login from './components/LoginPath.vue'; // Import your Login component
import Register from './components/RegisterPath.vue'; // Import your Register component
import UserDashboard from './components/UserDashboard.vue';
import IndexPath from './components/IndexPath.vue';
// import LogoutScript from './components/LogoutScript.vue';

const routes = [
  {
    path: '/',
    name: 'index',
    component: IndexPath,
  },
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
    path: '/dashboard',
    name: 'dashboard',
    component: UserDashboard,
    meta: { requiresAuth: false }, // Add this if authentication is required
  },
  // Other routes
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});


router.beforeEach((to, from, next) => {
  if (to.matched.some((record) => record.meta.requiresAuth)) {
    // Check if the user is authenticated here
    if (localStorage.getItem('jwt')) {
      next(); // Proceed to the route
    } else {
      next('/login'); // Redirect to the login page if not authenticated
    }
  } else {
    next(); // Proceed to the route
  }
});

export default router;
