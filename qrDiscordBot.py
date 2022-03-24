import uuid
from os.path import exists
import discord
from secrets import DiscordBotToken
from datetime import datetime

now = datetime.now()
client = discord.Client()

@client.event
async def on_ready():
    print('\nWe are logged in as {0.user}'.format(client))

@client.event
# Listen for an incomming message
async def on_message(message):
    # If the author is the robot itself, then do nothing!
    if message.author == client.user:
        return
    # If the user writes $qr
    if message.content == "$qr":
        current_time = now.strftime("%H:%M:%S")
        print('\n')
        qrCodePath="QRCode_" + str(message.author.id) + ".png"
        # This for loop check for all the user's DiscordID in the Database
        if exists(qrCodePath) :
            print("This user received his QR Code : " + message.author.name)
            print("Discord ID : " + str(message.author.id))
            print("Current time : ", current_time)
            
            # Send the QrCode the the user who asked for
            await message.author.send(
                "------------------------------------------------\n\n\nHello " + message.author.name + "\nHere is your new QR Code to login : ")
            await message.author.send(file=discord.File(qrCodePath))
            
            return
        else:
            print("This user didn't receive a QR Code : " + message.author.name)
            print("Discord ID : " + str(message.author.id))
            print("Current time : ", current_time)
            return

#Run the client (This runs first)
client.run(DiscordBotToken)