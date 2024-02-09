// axios.js

import axios from 'axios';
import { getCSRFToken } from './csrf';

const axiosInstance = axios.create({
  baseURL: 'http://localhost:8000', // Replace with your Django backend URL
  withCredentials: true, // Make sure this option is set to true
});

axiosInstance.interceptors.request.use(
  config => {
    const csrfToken = getCSRFToken();
    if (csrfToken) {
      config.headers['X-CSRFToken'] = csrfToken;
    }
    return config;
  },
  error => {
    return Promise.reject(error);
  }
);

export default axiosInstance;
