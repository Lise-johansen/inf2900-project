<template>
  <div>
    <div class="background">
        <div class="shape"></div>
        <div class="shape"></div>
    </div>
    <form @submit.prevent="login">
        <h3 class="login-title animated-fade-in"> Login Here </h3>

        <label for="username"> Username </label>
        <input type="username" placeholder="Enter your email here..." id="username" v-model="username">
 
        <label for="password"> Password </label>
        <input type="password" placeholder="Enter your password here..." id="password" v-model="password">

        <button type="submit"> Log In </button>
        <div class="register-and-reset">
            <router-link to="/register" class="button-link"> Register here </router-link>
        <div class="spacer"></div>
            <router-link to="/reset" class="button-link">Reset Password </router-link>
        </div>
    </form>

    <p v-if="errorMessage">{{ errorMessage }}</p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      username: '',
      password: '',
      errorMessage: ''
    };
  },
  created() {
    // Call the method to redirect if the user is already logged in
    this.redirectIfLoggedIn();
  },
  methods: {
    login() {
      // Token and auth_user are not present, proceed with login
      axios.post('login/', {
        username: this.username,
        password: this.password
      })
      .then(response => {
        document.cookie = `token=${response.data.token}`;
        document.cookie = `auth_user=${response.data.auth_user}`;
        // emit login event
        this.$emit('login');
        this.$router.push('/dashboard');
      })
      .catch(error => {
        this.errorMessage = 'Invalid username or password';
        // Log the error to the console if not in test mode
        if (process.env.NODE_ENV !== 'test') {
          console.log("Login failed!");
          console.error(error);
        }
      });
    },
    redirectIfLoggedIn() {
      const token = this.getTokenFromCookies();
      if (token != 'undefined') {
        this.$router.push('/dashboard');
      }
    },
    getTokenFromCookies() {
      const cookies = document.cookie.split('; ');
      for (const cookie of cookies) {
        const [name, value] = cookie.split('=');
        if (name === 'token') {
          return value;
        }
      }
      return null; // Token not found in cookies
    },
  }
};
</script>

<style scoped>
  * {
    padding: 0;
    margin: 0;
    box-sizing: border-box;
  }
  body {
    background-color: #080710;
  }
  .background {
    width: 430px;
    height: 520px;
    position: absolute;
    transform: translate(-50%,-50%);
    left: 50%;
    top: 50%;
  }
  .background .shape {
    height: 200px;
    width: 200px;
    position: absolute;
    border-radius: 50%;
  }
  .shape:first-child {
    background: linear-gradient(
      #1845ad,
      #23a2f6
    );
    left: -80px;
    top: -80px;
  }
  .shape:last-child {
    background: linear-gradient(
      to right,
      #ff512f,
      #f09819
    );
    right: -30px;
    bottom: -80px;
  }
  form {
    height: 520px;
    width: 400px;
    background-color: rgba(255,255,255,0.13);
    position: absolute;
    transform: translate(-50%,-50%);
    top: 50%;
    left: 50%;
    border-radius: 10px;
    backdrop-filter: blur(10px);
    border: 2px solid rgba(255,255,255,0.1);
    box-shadow: 0 0 40px rgba(8,7,16,0.6);
    padding: 50px 35px;
  }
  form * {
    font-family: 'Poppins', sans-serif;
    color: #ffffff;
    letter-spacing: 0.5px;
    outline: none;
    border: none;
  }
  form h3 {
    font-size: 32px;
    font-weight: 500;
    line-height: 42px;
    text-align: center;
    font-family: 'louis_george_cafe', sans-serif;
    background: linear-gradient(to right, #ff5733, #ffa500, #4169e1);
    -webkit-text-fill-color: transparent;
    -webkit-background-clip: text;
    font-weight: bolder;
  }
  label {
    display: block;
    margin-top: 30px;
    font-size: 16px;
    font-weight: 500;
    background: linear-gradient(to right, #ff5733, #ffa500, #4169e1);
    -webkit-text-fill-color: transparent;
    -webkit-background-clip: text;
  }
  input {
    display: block;
    height: 50px;
    width: 100%;
    background-color: rgba(255,255,255,0.07);
    border-radius: 3px;
    padding: 0 10px;
    margin-top: 8px;
    font-size: 14px;
    font-weight: 300;
  }
  ::placeholder {
    color: #e5e5e5;
  }
  button {
    margin-top: 50px;
    width: 100%;
    background-color: #ffffff;
    color: #080710;
    padding: 15px 0;
    font-size: 18px;
    font-weight: 600;
    border-radius: 5px;
    cursor: pointer;
  }
  .register-and-reset {
    margin-top: 30px;
    display: flex;
  }
  .register-and-reset div {
    background: red;
    width: 150px;
    border-radius: 3px;
    padding: 5px 10px 10px 5px;
    background-color: rgba(255,255,255,0.27);
    color: #eaf0fb;
    text-align: center;
  }
  .register-and-reset div:hover {
    background-color: rgba(255,255,255,0.47);
  }
  .button-link {
    background: linear-gradient(to right, #ff5733, #ffa500, #4169e1);
    -webkit-text-fill-color: transparent;
    -webkit-background-clip: text;
  }

  #username, #password {
    font-family: 'louis_george_cafe', sans-serif;
    background: linear-gradient(to right, #ff5733, #ffa500, #4169e1);
    -webkit-text-fill-color: transparent;
    -webkit-background-clip: text;
    padding: 1em .5em;
    border: 3px solid #a4a3a3;
    border-radius: 99999999px;
  }

  .animated-fade-in {
    opacity: 0;
    animation: fadeIn 1.5s ease forwards;
  }

  @keyframes fadeIn {
    from {
      opacity: 0;
    }
    to {
      opacity: 1;
    }
  }
  .spacer {
    flex: 1;
  }
</style>
