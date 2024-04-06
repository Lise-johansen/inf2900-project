import os
import django
import random

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app_project.settings_test')
django.setup()

from airfinn.models import Message, User, Item, Conversation

def create_dummy_message():
    # Assuming you have some users and listings in your database
    users = User.objects.all()  # Get all users
    listings = Item.objects.all()  # Get all listings
    
    # Choose a random listing
    listing = random.choice(listings)
    
    # Choose the owner of the listing as the receiver
    receiver = listing.owner
    
    # Randomly select a sender who is not the owner of the listing
    sender = random.choice(users.exclude(id=receiver.id))
    
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

# Call the function to create the dummy message
create_dummy_message()
