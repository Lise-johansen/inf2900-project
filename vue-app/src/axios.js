// axios.js

import axios from 'axios';

// Create Axios instance
const axiosInstance = axios.create({
  baseURL: 'http://localhost:8000', // Replace with your Django backend URL
});

// Add a request interceptor to dynamically add CSRF token to outgoing requests
axiosInstance.interceptors.request.use(config => {
  // Fetch CSRF token from Django
  const csrfToken = document.cookie
    .split('; ')
    .find(row => row.startsWith('csrftoken='))
    ?.split('=')[1];

  // Add CSRF token to request headers
  if (csrfToken) {
    config.headers['X-CSRFToken'] = csrfToken;
  }

  return config;
}, error => {
  // Handle request error
  return Promise.reject(error);
});

export default axiosInstance;
