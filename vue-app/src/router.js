// router.js
import { createRouter, createWebHistory } from 'vue-router';
import Login from './components/LoginPath.vue'; // Import your Login component
import Register from './components/RegisterPath.vue'; // Import your Register component
import PasswordReset from './components/PasswordReset.vue'; // Import Password Reset component
import UserDashboard from './components/UserDashboard.vue';
import IndexPath from './components/IndexPath.vue';
import PasswordResetForm from './components/PasswordResetForm.vue'; // Import Password Reset Form component
import VerifyEmail from './components/VerifyEmail.vue'; // Import Verify Email component
// import Listing from '.components/Listing.vue'; // Import Listing component
import AboutUs from './components/AboutUs.vue'; // Import About Us component
import ContactUs from './components/ContactUs.vue'; // Import Contact Us component
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
    path: '/reset',
    name: 'reset',
    component: PasswordReset,
  },
  {
    path: '/reset-password/:uidb64/:token',
    name: 'resetform',
    component: PasswordResetForm,
  },
  {
    path: '/reset',
    name: 'reset',
    component: PasswordReset,
  },
  {
    path: '/reset-password/:uidb64/:token',
    name: 'resetform',
    component: PasswordResetForm,
  },
  {
    path: '/dashboard',
    name: 'dashboard',
    component: UserDashboard,
    meta: { requiresAuth: false }, // Add this if authentication is required
  },
  {
    path: '/verify-email',
    name: 'verifyemail',
    component: VerifyEmail,
  },
  // {
  //   path: '/listings/:id',
  //   name: 'listings',
  //   component: Listings,
  // },
  {
    path: '/about',
    name: 'about',
    component: AboutUs,
  },
  {
    path: '/contact',
    name: 'contact',
    component: ContactUs,
  }
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
