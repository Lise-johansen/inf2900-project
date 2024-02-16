
<script>
import axiosInstance from 'axios';

export default {
    methods: {
        logout() {
            axiosInstance.get('logout/')
                .then(response => {
                    // Clear the token and user_auth cookies
                    document.cookie = `token=${'undefined'}`;
                    document.cookie = `user_auth=${'undefined'}`; 
                    document.cookie = `user_id=${'undefined'}`;
                    console.log(response);
                    this.user = response.data;
                    this.$router.push('/');
                })
                .catch(error => {
                    console.error('Error logging out:', error);
                });
            },
    },
};
</script>
