// axios.js

import axios from 'axios';

const axiosInstance = axios.create({
  baseURL: 'https://django.dybedahlserver.net/api/', // Use the domain Nginx forwards requests to
  withCredentials: false, // Ensure cookies are sent with cross-origin requests
});

export default axiosInstance;
