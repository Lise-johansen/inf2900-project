// router.js
import { createRouter, createWebHistory } from 'vue-router';
import Login from './components/LoginPath.vue'; // Import your Login component
import Register from './components/RegisterPath.vue'; // Import your Register component
import UserDashboard from './components/UserDashboard.vue';
import IndexPath from './components/IndexPath.vue';

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
    children:[
      {
        path: '/dashboard',
        name: 'UserDashboard',
        component: UserDashboard,
        meta: { requiresAuth: false }, // Add this if authentication is required
      },
    ]
  },

  {
    path: '/register',
    name: 'register',
    component: Register,
    children:[
      {
        path: '/dashboard',
        name: 'UserDashboard',
        component: UserDashboard,
        meta: { requiresAuth: false }, // Add this if authentication is required
      },
    ]
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
