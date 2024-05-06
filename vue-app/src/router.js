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
import DeleteListing from './components/DeleteListing.vue'; // Import Delete Listing component
import ContactUs from './components/ContactUs.vue'; // Import Contact Us component
// import LogoutScript from './components/LogoutScript.vue';
import EditListing from './components/EditListing.vue'; // Import Edit Listing component
import CreateItem from './components/CreateItem.vue';
import MyAccount from './components/MyAccount.vue';
import SearchPage from './components/SearchPage.vue';
import PrivacyPolicy from './components/PrivacyPolicy.vue';
import MailBox from './components/MailBox.vue';
import ListingPath from './components/ListingPath.vue';
import ErrorPage from './components/ErrorPage.vue';
import LeafletMap from './components/LeafletMap.vue';
import FavouriteListings from './components/FavouriteListings.vue';


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
  {
    path: '/create-listing',
    name: 'create-listing',
    component: CreateItem
  },
  {
    path: '/about',
    name: 'about',
    component: AboutUs,
  },
  {
    path: '/EditListing',
    name: 'EditListing',
    component: EditListing,
  },
  {
    path: '/delete',
    name: 'delete',
    component: DeleteListing,
  },
  {
    path: '/contact',
    name: 'contact',
    component: ContactUs,
  },
  {
    path: '/inbox',
    name: 'inbox',
    component: MailBox,
  },
  {
    path: '/my-account',
    name: 'my-account',
    component: MyAccount,
  },
  {
    path: '/search-page/', // Ensure this matches the path used in navigation
    name: 'searchPage',
    component: SearchPage,
  },
  {
    path: '/privacy-policy',
    name: 'privacy-policy',
    component: PrivacyPolicy,
  },
  {
    path: '/listing/:id/', // Ensure this matches the path used in navigation
    name: 'listingPage',
    component: ListingPath,
  },
  {
    path: '/ordered-listings/',
    name: 'ordered-listings',
    component: UserDashboard,
  },
  {
    path: '/order-listing/',
    name: 'order-listing',
    component: ListingPath,
  },
  {
    path: '/reserved-dates/',
    name: 'reserved-dates',
    component: ListingPath,
  },
  {
    path: '/map',
    name: 'map',
    component: LeafletMap,
  },
  {
    path: '/favourites',
    name: 'favourites',
    component: FavouriteListings,
  },
  // Other routes

  // Wildcard route to catch any requests to a page that does not exist.
  // This should be the last route in the array
  {
    path: '/:catchAll(.*)',
    name: 'error',
    component: ErrorPage,
  }
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
