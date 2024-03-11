// axios.js

import axios from 'axios';

const axiosInstance = axios.create({
  baseURL: 'http://localhost:8000/api/', // Use the domain Nginx forwards requests to
  withCredentials: true, // Ensure cookies are sent with cross-origin requests
});

export default axiosInstance;
