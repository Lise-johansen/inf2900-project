// axios.js

import axios from 'axios';


const axiosInstance = axios.create({
  baseURL: 'http://localhost:8000', // Replace with your Django backend URL
  withCredentials: true, // Make sure this option is set to true
});

export default axiosInstance;