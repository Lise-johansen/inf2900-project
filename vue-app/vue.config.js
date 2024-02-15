const { defineConfig } = require('@vue/cli-service')
module.exports = {
  transpileDependencies: [
    'axios', // Include axios
    'vue-router', // Include vue-router
    'csrf', // Include csrf
    // Add any other dependencies that need to be transpiled here
  ]
};

const { createProxyMiddleware } = require('http-proxy-middleware');

module.exports = {
  devServer: {
    proxy: {
      '/api': {
        target: 'http://127.0.0.1:8000', // Change this to your backend server URL
        changeOrigin: true,
        secure: false,
      },
    },
  },
};

