<template>
  <div class="mailbox">
    <!-- Left side: Display list of conversations -->
    <div class="left-panel">
      <div class="inbox">
        <h3>Inbox</h3>
        <div v-if="filteredConversations.length === 0">No conversations</div>
        <div v-else>
          <div class="conversation-box">
            <div v-for="conversation in filteredConversations" :key="conversation.id" @click="openConversation(conversation)">
              <div class="conversation-details">
                <!-- Display the name of the other participant in the conversation -->
                <div class="participant">
                  {{ getParticipantName(conversation) }}
                </div>
                <!-- Display item id and date -->
                <div class="details">
                  Listing: {{ conversation.item.name }}
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Right side: Display selected conversation messages and input for new message -->
    <div :class="{ 'right-panel': true, 'active': showRightPanel }">
      <div class="message-box">
      <div v-if="selectedConversation">
        <router-link :to="'/listings/' + selectedConversation.item.id" class="item-link">
        <h2> {{ selectedConversation.item.name }} </h2></router-link>
          <div class="mail-details" v-if="selectedConversation">
            <div class="mail-box"  ref="messageContainer">
              <div v-for="message in selectedConversation.messages" :key="message.id">
                <div class="message">
                  <!-- Check if there are messages -->
                  <div v-if="selectedConversation.messages.length !== 0">
                    <div v-if="message.sender.name === 'You'">
                      <div class="date-sender" v-if="message.created_at">{{ formatDateString(message.created_at) }}</div>                  
                      <div class="sender">{{ message.sender.name }}
                        <div class="message-content-sender">{{ message.message }}</div>
                      </div>
                    </div>
                    <div v-else>
                      <div class="date-receiver" v-if="message.created_at">{{ formatDateString(message.created_at) }}</div>   
                      <div class="receiver">{{ message.sender.name }}
                        <div class="message-content-receiver">{{ message.message }}</div>
                      </div>
                    </div>
                    
                  </div>
                  <div v-else>
                    <p class="error-message">{{ errorMessage }}</p>
                  </div>
                </div>
              </div>
            </div>
            <div class="input-box">
              <textarea v-model="newMessage" placeholder="Type your message..."></textarea>
              <button @click="sendMessage">Send</button>
            </div>
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
        showPopup: false, // Flag to show/hide popup
        showRightPanel: false
      };
    },

    created() {
      // Check if logged in
      const token = this.loginCheck();
      
      // Redirect to login page if not logged in
      if (!token) {
        this.errorMessage = 'Please login to view your inbox.';
        this.showPopup = true;
        return;
      }
    },

    mounted() {
      // Fetch conversations when component is mounted
      this.fetchConversations();
    },
    computed: {
        filteredConversations() {
            // Group conversations by conversation ID
            const groupedConversations = {};
            
            this.conversations.forEach(conversation => {
            const conversationId = conversation.id;
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
      scrollToBottom() {
        // Get the message container element using $refs
        const messageContainer = this.$refs.messageContainer;

        // Scroll the message container to the bottom
        messageContainer.scrollTop = messageContainer.scrollHeight;
      },

      fetchConversations() {
        
        // Get the authentication token from cookies
        const token = this.loginCheck();

        // Make API request to fetch conversations with messages
        axios.get('get-conversations/', {
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

            // Update selectedConversation to reflect the first conversation (if available)
            if (!this.selectedConversation && this.conversations.length > 0) {
              this.selectedConversation = this.conversations[0];
            }

          } else {
            // Handle unexpected response format
            console.error('Unexpected response format:', data);
          }

          // Trigger vue component update
          this.$forceUpdate();
        })
        .catch(error => {
          // Handle error
          console.error('Error fetching conversations with messages:', error);
        });
      },

      openConversation(conversation) {
        // Set selectedConversation to the clicked conversation to display messages
        this.selectedConversation = conversation;
        this.showRightPanel = true;
        console.log("Selected conversation:", this.selectedConversation);
        this.fetchMessages(conversation.id);
      },

      fetchMessages(conversation_id){
        
        // Get the authentication token from cookies
        const token = this.loginCheck();
  
        // Make API request to fetch messages for the selected conversation
        axios.get(`get-messages/`, {
          params: {
            conversation_id: conversation_id
          },
          headers: {
            Authorization: `Bearer ${token}`
          }
        })
        .then(response => {
          // Handle successful response
          const data = response.data;
          if (data && Array.isArray(data) && data.length > 0) {
            // Assign the received messages to the selected conversation
            this.selectedConversation.messages = data;
            console.log("Messages for conversation:", this.selectedConversation.messages);

            // Scroll to the bottom after messages have been fetched
            this.$nextTick(() => {
                this.scrollToBottom();
            });

          } else {
            // Handle unexpected response format
            console.error('Unexpected response format:', data);
          }
        })
        .catch(error => {
          // Handle error
          console.error('Error fetching messages:', error);
          this.errorMessage = 'Error fetching messages.';
        });
      },

      sendMessage() {
        // Get the authentication token from cookies
        const token = this.loginCheck();
  
        // Make sure newMessage is not empty
        if (!this.newMessage) {
          this.errorMessage = 'Please enter a message.';
          this.showPopup = true;
          return;
        }
  
        // Make API request to send a message
        axios.post('send-messages/', {
          sender_id: this.selectedConversation.sender.id,
          receiver_id: this.selectedConversation.receiver.id,
          message: this.newMessage,
          item_id: this.selectedConversation.item.id,
          conversation_id: this.selectedConversation.id
        }, 
        {
          headers: {
            Authorization: `Bearer ${token}`
          }
        })
        .then(response => {
          // Handle successful response
          console.log('Message sent:', response.data);
          
          // Append the new message to the selected conversation
          this.selectedConversation.messages.push({
            sender: { name: "You" },
            message: this.newMessage,
            created_at: response.data.created_at
          });
          
          // Clear the new message input
          this.newMessage = '';

          // Scroll to the bottom after sending the message
          this.$nextTick(() => {
            this.scrollToBottom();
          });
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
      },

      loginCheck() {
        // Get the authentication token from cookies
        const token = this.getTokenFromCookies();

        // Make sure token is available
        if (!token) {
          // Handle error - user is not logged in
          this.errorMessage = 'Please login to view your inbox.';
          this.showPopup = true;
          return null;
        }
        return token;
      }
    }
  };
</script>
  
<style scoped>
    .mailbox {
      display: flex;
      justify-content: center;
      align-items: flex-start;
    }

    .left-panel {
      margin-left: 0%;
      margin-right: 5px;
      margin-top: 20px;
      width: 15%;
      transition: max-width 0.3s ease, margin-left 0.3s ease;
      box-shadow: 0 1px 10px rgba(0, 0, 0, 0.1);
      padding: 20px;
      border-radius: 30px;
      backdrop-filter: blur(10px);
      overflow: auto;
    }

    .right-panel {
      width: 0%;
      overflow: hidden;
      overflow-y: auto;
      transition: max-width 0.3s ease, margin-left 0.3s ease;
    }

    .right-panel.active {
      margin-top: 20px;
      margin-right: 0; /* Reset margin-right */
      margin-left: 0; /* Reset margin-left */
      width: 40%; /* Adjusted width when panel is active */
      margin-right: 0; /* Reset margin-right */
      box-shadow: 0 1px 10px rgba(0, 0, 0, 0.1);
      padding: 20px;
      border-radius: 30px;
      backdrop-filter: blur(10px);
    }

    .inbox {
      height: 100%;
      max-width: 800px;
      border: 1px solid rgba(255, 255, 255, 0.1);
    }

    /* Add animation for right panel opening */
    .right-panel {
      animation: slideInRight 0.3s forwards;
    }

    @keyframes slideInRight {
      from {
        transform: translateX(100%);
        opacity: 0;
      }
      to {
        transform: translateX(0);
        opacity: 100;
      }
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

    .message-box {
      border: 1px solid rgba(255, 255, 255, 0.1);
    }

    .message-box * {
      font-family: 'Poppins', sans-serif;
      color: #676767;
      letter-spacing: 0.5px;
      outline: none;
      border: none;
    }

    .message-box h2 {
      font-size: 30px;
      font-weight: bolder;
      line-height: 42px;
      text-align: center;
      font-family: 'louis_george_cafe', sans-serif;
      background: linear-gradient(to right, #ff5733, #ffa500, #4169e1);
      -webkit-text-fill-color: transparent;
      -webkit-background-clip: text;
    }
    
    .mail-details h2 {
        font-size: 24px;
        font-weight: bold;
    }

    .mail-details {
      max-width: 100%;
    }

    .sender, .receiver {
      font-family: 'Poppins', sans-serif;
      display: inline-block;
      position: relative;
      font-display: swap;
      padding: 10px;
      border-radius: 20px;
      word-wrap: break-word;
      margin-bottom: 5px;
    }

    .sender::after, .receiver::after {
      display: inline-block;
      width: 0;
      height: 0;
      border-top: 8px solid transparent;
      border-bottom: 8px solid transparent;
      position: absolute;
    }

    .sender {
      background-color: #007bff;
      color: #fff;
      text-align: right;
      float: right;
    }

    .sender::after {
      border-left: 8px solid #007bff;
      right: -15px;
      top: 50%;
      transform: translateY(-50%);
    }

    .message-content-sender {
      background-color: #007bff;
      color: #fff;
      text-align: right;
      margin-left: auto;
    }

    .receiver {
      background-color: #868686;
      color: #fff;
      text-align: left;
      float: left;
    }

    .receiver::after {
      border-right: 8px solid #868686;
      left: -15px;
      top: 50%;
      transform: translateY(-50%);
    }

    .message-content-receiver {
      color: #fff;
      text-align: left;
      margin-right: auto;
    }

    .date-sender {
      margin-bottom: 5px;
      margin-right: 5px;
      color: #888;
      font-size: 12px;
      text-align: right;
    }

    .date-receiver {
      margin-bottom: 5px;
      margin-right: 5px;
      color: #888;
      font-size: 12px;
      text-align: left;
    }

    .message {
      display: flex;
      flex-direction: column;
      margin-top: 20px;
      border-radius: 20px;
      overflow-wrap: break-word;
      padding: 15px;
    }

    .mail-box {
      margin-top: 20px;
      max-width: 100%;
      padding: 20px;
      background-color: #f9f9f9;
      border: 2px solid #ccc;
      border-radius: 10px;
      max-height: calc(100vh - 450px);
      overflow-y: scroll;
    }

    .conversation-details {
      margin-bottom: 10px;
      padding: 15px;
      border-radius: 10px;
      background-color: #f0f0f0;
      transition: background-color 0.3s ease;
    }

    .conversation-box {
      margin-top: 10px;
      max-width: 100%;
      padding: 20px;
      background-color: #f9f9f9;
      border: 2px solid #ccc;
      border-radius: 10px;
      max-height: calc(100vh - 450px);
      overflow-y: scroll;
    }

    .conversation-details:hover {
        background-color: #e0e0e0;
    }


    .input-box {
      margin-top: 20px;
      padding: 20px;
      background-color: #f9f9f9;
      border: 2px solid #ccc;
      border-radius: 30px;
      display: flex;
      align-items: center;
    }

    textarea {
      flex: 1;
      resize: none;
      padding: 10px;
      border: 2px solid #ffa500;
      border-radius: 5px;
      margin-right: 10px;
      box-shadow: 0 0 1px rgba(0, 0, 0, 0.5);
    }

    button {
      padding: 10px 20px;
      border: none;
      border-radius: 5px;
      background-color: #007bff;
      color: rgb(255, 255, 255);
      cursor: pointer;
      transition: background-color 0.3s ease;
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

    .item-link {
      text-decoration: none;
      color: #000;
      max-width: 100%;
    }

    /* Define fade animation */
    .fade-enter-active, .fade-leave-active {
      transition: opacity 0.5s;
    }

    .fade-enter, .fade-leave-to /* .fade-leave-active in <2.1.8 */ {
      opacity: 0;
    }
</style>