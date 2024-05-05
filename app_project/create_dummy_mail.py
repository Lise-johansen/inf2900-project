import os
import django
import random
import sys

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app_project.settings_test')
django.setup()

from airfinn.models import Message, User, Item, Conversation

def create_dummy_message(sender_username=None, receiver_username=None):
    # Assuming you have some users and listings in your database
    users = User.objects.all()  # Get all users
    
    # If sender and receiver usernames are provided, find the corresponding users
    if sender_username:
        sender = User.objects.get(username=sender_username)
    else:
        sender = random.choice(users)  # Choose a random sender if not provided
    
    if receiver_username:
        receiver = User.objects.get(username=receiver_username)
        listings = Item.objects.filter(owner=receiver)  # Get listings owned by the receiver
    else:
        receiver = random.choice(users)  # Choose a random receiver if not provided
        listings = Item.objects.filter(owner=receiver)  # Get listings owned by the random receiver
    
    if not listings.exists():
        print(f"No listings found for user '{receiver.username}'.")
        return
    
    # Choose a random listing from the filtered listings
    listing = random.choice(listings)
    
    # Check if there is an existing conversation between sender and receiver for this listing
    conversation = Conversation.objects.filter(user1=sender, user2=receiver, item=listing).first()
    
    if not conversation:
        # If no existing conversation found, create a new one
        conversation = Conversation.objects.create(user1=sender, user2=receiver, item=listing)
    
    # Create a dummy message for the conversation
    dummy_message = Message.objects.create(
        conversation=conversation,
        sender=sender,
        receiver=receiver,
        message="This is a test message.",
    )
    
    # Print the created message details
    print("Dummy message created:")
    print("Sender:", dummy_message.sender.username)
    print("Receiver:", dummy_message.receiver.username)
    print("Listing:", dummy_message.conversation.item.name)
    print("Message:", dummy_message.message)
    print("Created At:", dummy_message.created_at)
    
    return dummy_message  # Return the created message object if needed

def main():
    args = sys.argv[1:]

    if args:
        if args[0] == '-message':
            # enter the sender and receiver usernames
            sender_username = input("Enter sender username: ")
            receiver_username = input("Enter receiver username: ")
            create_dummy_message(sender_username, receiver_username)
            print('Dummy message created')
    else:
        print('No arguments given. Use -message <sender_username> <receiver_username> to create a dummy message, or leave the usernames empty to create a random message.')

if __name__ == '__main__':
    main()
