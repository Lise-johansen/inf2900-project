/**
 * @fileoverview This file contains the router configuration for the Vue application.
 * It defines the routes and their corresponding components.
 * @module router
 */

import { createRouter, createWebHistory } from 'vue-router';
import IndexPath from '@/components/IndexPath.vue'; // Ensure correct import
import Login from '@/components/LoginPath.vue'; // Ensure correct import

/**
 * The routes for the application.
 * Each route consists of a path, name, and component.
 * @type {Array}
 */
const routes = [
  {
    path: '/',
    name: 'Home',
    component: IndexPath,
  },
  {
    path: '/login',
    name: 'Login',
    component: Login,
  },
  // other routes...
];

/**
 * The router instance for the application.
 * It uses the web history mode and the defined routes.
 * @type {Object}
 */
const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
