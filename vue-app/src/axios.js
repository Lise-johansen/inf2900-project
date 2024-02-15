// axios.js

import axios from 'axios';

const axiosInstance = axios.create({
  baseURL: 'http://127.0.0.1:8000', // Use the domain Nginx forwards requests to
  withCredentials: true, // Ensure cookies are sent with cross-origin requests
});

export default axiosInstance;
