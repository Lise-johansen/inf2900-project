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
                  <br>
                  <div v-if="conversation.sender.name === 'You'">
                    <div v-if="conversation.latest_message">You: {{ conversation.latest_message.message }}</div>
                  </div>
                  <div v-else>
                    <div v-if="conversation.latest_message">{{ conversation.latest_message.message }}</div>
                  </div>
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
        <div class="receiver-information">
          <div class="profilepicture-container">
          <img :src="selectedConversation.receiver.profile_picture" class="profile-picture" alt="Profile Picture" width="50" height="50"/>
          </div>
          <router-link :to="'/listing/' + selectedConversation.item.id" class="item-link">
          <h2> {{ selectedConversation.item.name }} </h2>
        </router-link>
        </div>
          <div class="mail-details" v-if="selectedConversation">
            <div class="mail-box"  ref="messageContainer">
              <div v-for="message in selectedConversation.messages" :key="message.id">
                <div class="message">
                  <!-- Check if there are messages -->
                  <div v-if="selectedConversation.messages.length !== 0">
                    <div v-if="message.sender.name === 'You'">
                      <div class="date-sender" v-if="message.created_at">{{ formatDateString(message.created_at) }}</div>
                      <div class="sender" v-if="selectedConversation.latest_message">
                          {{ message.sender.name }}
                          <div class="message-content-sender">{{ message.message }}</div>
                          <div v-if="message.image" class="image-container">
                            <Image :src="message.image" alt="Image Preview" width="250" preview />
                          </div>
                      </div>
                    </div>
                    <div v-else>
                      <div class="date-receiver" v-if="message.created_at">{{ formatDateString(message.created_at) }}</div>   
                      <div class="receiver" v-if="selectedConversation.latest_message"> 
                        {{ message.sender.name }}
                        <div class="message-content-receiver">{{ message.message }}</div>
                          <div v-if="message.image" class="image-container">
                            <Image :src="message.image" alt="Image Preview" class="message-image" preview />
                          </div>
                      </div>
                    </div>
                  </div>
                  <div v-else>
                    <h2> {{ errorMessage }}</h2>
                    <div class="message-content-sender"></div>
                  </div>
                </div>
              </div>
            </div>
            <div class="input-box">
              <Textarea v-model="newMessage" autoResize rows="2" cols="100" placeholder="Type your message..."/>
                <!-- Add image upload input button by the send message -->
                <div class="send-and-upload-buttons">
                  <!-- File input for image uploading -->
                  <input type="file" accept="image/*" style="display: none;" ref="fileInput" @change="handleImageUpload">
                  
                  <!-- Button for triggering file selection -->
                  <Button class="upload-button" icon="pi pi-link" outlined @click="$refs.fileInput.click()"/>

                  <!-- Button for sending message -->
                  <Button label="Send" raised @click="sendMessage"/>
                  
                  <!-- Image preview dialog -->
                  <Dialog v-model:visible="displayImagePreview" modal>
                    <img :src="selectedImage" alt="Image Preview" style="width: 500px; margin: 10px;"/>
                    <div class="p-d-flex p-jc-between p-mt-2">
                      <div class="close-and-send-preview">
                        <Button label="Cancel" class="p-button-text" @click="closeImagePreviewDialog" />
                        <Button label="Send" class="p-button-primary" @click="sendImage" />
                      </div>
                    </div>
                  </Dialog>
                </div>
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
  import 'primeicons/primeicons.css';
  import axios from 'axios';
  import Image from 'primevue/image';
  import Button from 'primevue/button';
  import Dialog from 'primevue/dialog';
  import Textarea from 'primevue/textarea';
  
  export default {
    components: {
      Image, Button, Dialog, Textarea
    },
    data() {
      return {
        conversations: [], // Array to store conversations with messages
        selectedConversation: null, // Object to store selected conversation
        newMessage: '', // New message input
        errorMessage: '', // Error message to display in popup
        showPopup: false, // Flag to show/hide popup
        showRightPanel: false, // Flag to show/hide right panel
        image: '', // Image data to be sent if available
        displayImagePreview: false, // Flag to show/hide image preview dialog
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

            // Convert the grouped conversations object to an array
            return Object.values(groupedConversations);
        }
    },
    methods: {
      scrollToBottom() {
        this.errorMessage = '';
        // Get the message container element using $refs
        const messageContainer = this.$refs.messageContainer;

        // Scroll the message container to the bottom
        messageContainer.scrollTop = messageContainer.scrollHeight;
      },

      fetchConversations() {
        this.errorMessage = '';
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

            // Update selectedConversation to reflect the first conversation (if available)
            if (!this.selectedConversation && this.conversations.length > 0) {
              this.selectedConversation = this.conversations[0];
            }

            // If conversation id is provided in the URL, open the conversation
            const conversationId = this.$route.params.id;
            if (conversationId) {
              const conversation = this.findConversationById(conversationId);
              if (conversation) {
                this.openConversation(conversation);
              }
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
        this.errorMessage = '';
        // Set selectedConversation to the clicked conversation to display messages
        this.selectedConversation = conversation;
        this.showRightPanel = true;
        this.fetchMessages(conversation.id);
      },

      fetchMessages(conversation_id){
        this.errorMessage = '';
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
        if (!this.newMessage && !this.image) {
          alert('Please enter a message.');
          return;
        }
  
        // Make API request to send a message
        axios.post('send-messages/', {
          sender_id: this.selectedConversation.sender.id,
          receiver_id: this.selectedConversation.receiver.id,
          message: this.newMessage,
          image: this.image,
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
          
          // Append the new message to the selected conversation
          this.selectedConversation.messages.push({
            sender: { name: "You" },
            message: this.newMessage,
            image: this.image,
            created_at: response.data.created_at
          });
          
          // Clear the new message input
          this.newMessage = '';
          this.image = '';

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

      sendImage(){
        this.image = this.selectedImage;
        this.displayImagePreview = false;
        
        // Send the message with the image
        this.sendMessage();
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

      handleImageUpload(event) {
        const file = event.target.files[0];
        if (file) {
          // Read the file as a data URL
          const reader = new FileReader();
          reader.onloadend = () => {
            const imageData = reader.result;

            // Set the selected image for preview
            this.selectedImage = imageData;

            // Open the image preview dialog
            this.displayImagePreview = true;
          };
          reader.readAsDataURL(file);
        }
      },

      closeImagePreviewDialog() {
        this.displayImagePreview = false;
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
      },

      findConversationById(conversationId) {
        console.log('Searching conversation with ID:', conversationId);
        console.log('Conversations array:', this.conversations);

        // Parse conversationId to an integer
        const id = parseInt(conversationId);

        // Find the conversation with the provided ID in the conversations array
        const conversation = this.conversations.find(conversation => {
            console.log('Type of conversation.id:', typeof conversation.id);
            return conversation.id === id;
        });

        console.log('Found conversation:', conversation);
        return conversation;
      },

      deleteConversation() {
        // Get the authentication token from cookies
        const token = this.loginCheck();
        
        console.log('Conversations:', this.conversations);
        // Get all conversations without messages
        const emptyConversations = this.conversations.filter(conversation => conversation.messages.length === 0);

        // Delete all empty conversations
        emptyConversations.forEach(conversation => {
          // Make API request to delete the conversation
          axios.delete('delete-conversation/' + conversation.id, {
            headers: {
              Authorization: `Bearer ${token}`
            }
          })
          .then(() => {
            // Handle successful response
            // Remove the conversation from the conversations array
            this.conversations = this.conversations.filter(c => c.id !== conversation.id);
          })
          .catch(error => {
            // Handle error
            console.error('Error deleting conversation:', error);
          });
        });
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
    width: 20%;
    transition: max-width 0.3s ease, margin-left 0.3s ease;
    box-shadow: 0 1px 10px rgba(0, 0, 0, 0.1);
    padding: 20px;
    border-radius: 30px;
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
    border-top: 1px solid #ffa500;
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

  .profilepicture-container {
      display: flex;
      justify-content: center;
      align-items: center;
      overflow: hidden;
      box-sizing: border-box;
      border: 3px solid #ccc;
      border-radius: 50%;
      width: 80px;
      height: 80px;
  }

  .profile-picture {
      width: 80px;
      height: 80px;
  }

  .message-content-receiver {
    color: #fff;
    text-align: left;
    margin-right: auto;
    border-top: 1px #ffa500;
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
  }

  .send-and-upload-buttons {
    display: flex;
    align-items: right;
    justify-content: space-between;
    margin-right: 10px;
    padding: 2px;
  }

  .upload-button {
    scale: 0.8;
  }

  .close-and-send-preview {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin: 10px;
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
    margin-left: auto; /* Push the item link to the right */
    margin-right: auto; /* Push the item link to the left */
  }

  .receiver-information {
    display: flex;
    align-items: center; /* Center vertically */
  }

  /* Define fade animation */
  .fade-enter-active, .fade-leave-active {
    transition: opacity 0.5s;
  }

  .fade-enter, .fade-leave-to /* .fade-leave-active in <2.1.8 */ {
    opacity: 0;
  }
</style>