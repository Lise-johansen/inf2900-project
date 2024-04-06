<template>
    <div class="mailbox">
      <!-- Left side: Display list of conversations -->
      <div class="left-panel">
        <div class="inbox">
          <h3>Inbox</h3>
          <div v-if="filteredConversations.length === 0">No conversations</div>
          <div v-else>
            <div v-for="conversation in filteredConversations" :key="conversation.conversation.id" @click="openConversation(conversation)">
              <div class="conversation">
                <!-- Display the name of the other participant in the conversation -->
                <div class="participant">
                  {{ getParticipantName(conversation) }}
                </div>
                <!-- Display item id and date -->
                <div class="details">
                  Listing: {{ conversation.listing.name }}
                  <br>
                  Date: {{ formatDateString(conversation.created_at) }}
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
  
      <!-- Right side: Display selected conversation messages and input for new message -->
      <div class="right-panel">
        <div class="inbox">
          <div class="mail-details" v-if="selectedConversation">
            <h2> <router-link :to="'/listings/' + selectedConversation.listing.id" class="item-link">
                {{ selectedConversation.listing.name }}
            </router-link></h2>
            <div v-for="message in selectedConversation.messages" :key="message.id">
              <div class="message">
                <div class="sender">{{ message.sender.name }}</div>
                <div class="content">{{ message.message }}</div>
                <div class="date">{{ formatDateString(message.created_at) }}</div>
              </div>
            </div>
            <div class="input-box">
              <textarea v-model="newMessage" placeholder="Type your message..."></textarea>
              <button @click="sendMessage">Send</button>
            </div>
          </div>
        </div>
      </div>
  
      <!-- Popup for displaying error message -->
      <div v-if="showPopup" class="popup">
        <div class="popup-content">
          <p class="error-message">{{ errorMessage }}</p>
          <button @click="hidePopup">OK</button>
        </div>
      </div>
    </div>
</template>
  
<script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        conversations: [], // Array to store conversations with messages
        selectedConversation: null, // Object to store selected conversation
        newMessage: '', // New message input
        errorMessage: '', // Error message to display in popup
        showPopup: false // Flag to show/hide popup
      };
    },
    mounted() {
      // Fetch conversations with messages from API when component is mounted
      this.fetchConversations();
    },
    computed: {
        filteredConversations() {
            // Group conversations by conversation ID
            const groupedConversations = {};
            
            this.conversations.forEach(conversation => {
            const conversationId = conversation.conversation.id;
            if (!groupedConversations[conversationId]) {
                // Create a new array for this conversation ID if it doesn't exist
                groupedConversations[conversationId] = { ...conversation, messages: [] };
            }
            // Add the conversation messages to the corresponding array
            if (conversation.sender.name === "You" || conversation.receiver.name === "You") {
                groupedConversations[conversationId].messages.push(conversation);
            }
            });

            console.log("Grouped conversations:", groupedConversations);
            // Convert the grouped conversations object to an array
            return Object.values(groupedConversations);
        }
    },
    methods: {
      fetchConversations() {
        // Get the authentication token from cookies
        const token = this.getTokenFromCookies();
  
        // Make sure token is available
        if (!token) {
          // Handle error - user is not logged in
          this.errorMessage = 'Please login to view your inbox.';
          this.showPopup = true;
          return;
        }
  
        // Make API request to fetch conversations with messages
        axios.get('received-messages/', {
          headers: {
            Authorization: `Bearer ${token}`
          }
        })
        .then(response => {
          // Handle successful response
          const data = response.data;
          if (data && Array.isArray(data) && data.length > 0) {
            // Assign the received conversations directly
            this.conversations = data;
            console.log("Conversations with messages:", this.conversations);
          } else {
            // Handle unexpected response format
            console.error('Unexpected response format:', data);
          }
        })
        .catch(error => {
          // Handle error
          console.error('Error fetching conversations with messages:', error);
        });
      },
      openConversation(conversation) {
        // Set selectedConversation to the clicked conversation to display messages
        this.selectedConversation = conversation;
      },
      sendMessage() {
        // Get the authentication token from cookies
        const token = this.getTokenFromCookies();
        
        // Make sure token is available
        if (!token) {
          // Handle error - user is not logged in
          this.errorMessage = 'Please login to send a message.';
          this.showPopup = true;
          return;
        }
  
        // Make sure newMessage is not empty
        if (!this.newMessage) {
          this.errorMessage = 'Please enter a message.';
          this.showPopup = true;
          return;
        }
  
        // Make API request to send a message
        axios.post('send-messages/', {
          sender_id: this.selectedConversation.sender.id, // Assuming you have the sender's ID available
          receiver_id: this.selectedConversation.receiver.id, // Assuming you can access the recipient's ID
          message: this.newMessage,
          item_id: this.selectedConversation.listing.id, // Assuming you can access the ID of the listing (item)
          conversation_id: this.selectedConversation.conversation.id // Assuming you can access the conversation ID
        }, {
          headers: {
            Authorization: `Bearer ${token}`
          }
        })
        .then(response => {
          // Handle successful response
          console.log('Message sent:', response.data);
          // Clear the new message input
          this.newMessage = '';
        })
        .catch(error => {
          // Handle error
          console.error('Error sending message:', error);
        });
      },
      RedirectToLogin() {
        // Redirect to login page
        this.$router.push('/login');
      },
      isLoggedIn() {
        // Check if user is logged in by checking the token in cookies
        return this.getTokenFromCookies() !== null;
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
      hidePopup() {
        this.errorMessage = ''; // Clear the error message
        this.showPopup = false;
        this.RedirectToLogin();
      },
      formatDateString(dateString) {
        // Create a new Date object from the date string
        const date = new Date(dateString);
  
        // Format the date to a more readable format
        return date.toLocaleString();
      },
      getParticipantName(conversation) {
        // Return the name of the other participant in the conversation
        return conversation.sender.name === "You" ? conversation.receiver.name : conversation.sender.name;
      }
    }
  };
</script>
  
<style scoped>
    .mailbox {
        display: flex;
        justify-content: center;
        align-items: flex-start;
        height: calc(100vh - 200px); /* Adjust based on the height of the banner and footer */
    }

    .left-panel {
        max-width: 25%;
        transition: max-width 0.3s ease, margin-left 0.3s ease;
    }

    .right-panel {
        max-width: 75%; /* Adjusted to accommodate both mail details and input box */
        transition: max-width 0.3s ease, margin-right 0.3s ease;
    }

    .inbox {
        height: 100%;
        background-color: rgba(255, 255, 255, 0.13);
        border-radius: 30px;
        backdrop-filter: blur(10px);
        border: 2px solid rgba(255, 255, 255, 0.1);
        box-shadow: 0 0 40px rgba(8, 7, 16, 0.6);
        padding: 20px; /* Adjusted padding */
    }

    .inbox * {
        font-family: 'Poppins', sans-serif;
        color: #676767;
        letter-spacing: 0.5px;
        outline: none;
        border: none;
    }

    .inbox h3 {
        font-size: 35px;
        font-weight: bolder;
        line-height: 42px;
        text-align: center;
        font-family: 'louis_george_cafe', sans-serif;
        background: linear-gradient(to right, #ff5733, #ffa500, #4169e1);
        -webkit-text-fill-color: transparent;
        -webkit-background-clip: text;
    }

    .mail {
        cursor: pointer;
        margin-bottom: 20px;
        padding: 10px;
        border: 2px solid #ccc;
        border-radius: 10px;
        background-color: #f9f9f9;
        transition: background-color 0.3s ease;
    }

    .mail:hover {
        background-color: #e0e0e0;
    }

    .sender {
        font-weight: bold;
    }

    .date {
        margin-top: 5px;
        color: #888;
    }

    .mail-details {
        margin-top: 20px; /* Adjusted margin */
        padding: 20px;
        background-color: #f9f9f9;
        border: 2px solid #ccc;
        border-radius: 30px;
    }

    .mail-details h2 {
        font-size: 24px;
        font-weight: bold;
    }

    .message {
        margin-top: 10px;
    }

    .input-box {
        margin-top: 20px; /* Adjusted margin */
        display: flex;
    }

    textarea {
        flex: 1;
        resize: none;
        padding: 10px;
        border: 2px solid #ccc;
        border-radius: 5px;
    }

    button {
        padding: 10px 20px;
        margin-left: 10px;
        border: none;
        border-radius: 5px;
        background-color: #007bff;
        color: white;
        cursor: pointer;
    }

    button:hover {
        background-color: #0056b3;
    }

    .popup {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(0, 0, 0, 0.5);
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .popup-content {
        background-color: white;
        padding: 20px;
        border-radius: 5px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
    }

    .popup button {
        margin-top: 10px;
    }

    .error-message {
        font-family: 'louis_george_cafe', sans-serif;
        font-size: 20px;
        font-weight: bold;
        font-style: italic;
        padding: 10px;
        background: linear-gradient(to right, #ff5733, #ffa500, #4169e1);
        -webkit-text-fill-color: transparent;
        -webkit-background-clip: text;
    }

    .item-name {
        font-family: 'louis_george_cafe', sans-serif;
        font-weight: bold;
        font-size: 16px;
        padding-bottom: 5px;
        padding-top: 5px;
        list-style: none;
        margin-left: 0;
        padding-left: 0;
    }
</style>