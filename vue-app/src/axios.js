// axios.js

import axios from 'axios';

const axiosInstance = axios.create({
  baseURL: 'http://django.dybedahlserver.net/api/', // Use the domain Nginx forwards requests to
  withCredentials: true, // Ensure cookies are sent with cross-origin requests
});

export default axiosInstance;
