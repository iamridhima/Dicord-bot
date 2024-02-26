import discord
import random

# Predefined responses for the trigger word
trigger_responses = {
    "jheu lagyo": ["Padhna jauu", "Malai pani", "Hya hami 3rd year ma khatra huni ho"],
    "janu":["koder nibida", "nibida proo"],
    "bhattu":["bhattu ek number ko alchhi","Bhattu sutira hola pakkai","bhattu padhna jauu"],
    "gujju":["topper gujju", "yo sem ni 80 hanchhu","dheraiii burnt out nabhau"],
}

# Define the intents
intents = discord.Intents.default()

# Create a client instance with intents
client = discord.Client(intents=intents)

# Event handler for when the bot is ready
@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

# Event handler for when a message is sent
@client.event
async def on_message(message):
    # Check if the message was sent by the bot itself to avoid infinite loops
    if message.author == client.user:
        return

    # Check if the message content matches any trigger word
    for trigger, responses in trigger_responses.items():
        if trigger.lower() in message.content.lower():
            # Choose a random predefined response associated with the trigger word
            chosen_response = random.choice(responses)
            # Send the chosen response
            await message.channel.send(chosen_response)
            break  # Break out of the loop after sending a response

# Run the bot with its token
client.run('MTIxMTY2MDgwOTYwNDk1NjE5MQ.GuOVfQ.2frz38kWxI24BATfc6UDtPrTO8Eh1mFl0YX1eQ')
