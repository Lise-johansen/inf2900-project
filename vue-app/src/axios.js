// axios.js

import axios from 'axios';

const axiosInstance = axios.create({
  baseURL: 'http://localhost:8080/api/', // Use the domain Nginx forwards requests to
  withCredentials: false, // Ensure cookies are sent with cross-origin requests
});

export default axiosInstance;
