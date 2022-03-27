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
    discordname = message.author.name + "#" + message.author.discriminator
    discordid=str(message.author.id)
    # If the user writes $qr
    if message.content == "$qr":
        current_time = now.strftime("%H:%M:%S")
        print('QR Requested')
        qrCodePath="NONE"
        qrCodePath_name="qrcodes/QRCode_" + discordname + ".png"
        qrCodePath_id="qrcodes/QRCode_" + discordid + ".png"
        # This for loop check for all the user's DiscordID in the Database        
        if exists(qrCodePath_id) :
            print('Found QR by discord ID')
            qrCodePath = qrCodePath_id
        elif exists(qrCodePath_name) :
            print('Found QR by discord name#discr')
            qrCodePath = qrCodePath_name
        else:
            print(current_time, "A user didn't receive a non existing QR Code : " + qrCodePath_name + " or " + qrCodePath_id)               
            print("Discord ID : " + discordid)
            print("Discord Name # Discr : " + discordname )
            print("Current time : ", current_time)     
            await message.author.send(
                "------------------------------------------------\n\n\nHello " + message.author.name + "\nSorry, there is no QR Code for you \n" +
                "If you want to become a Plei Scholar, please register on this website: https://plei.games/contacto/")                
            return

        print(current_time, "This user received his QR Code : " + qrCodePath)
        print("Discord ID : " + discordid)
        print("Discord Name#Discriminator : " + discordname )
        # Send the QrCode the the user who asked for
        await message.author.send(
            "------------------------------------------------\n\n\nHello " + message.author.name + "\nHere is your new QR Code: ")
        await message.author.send(file=discord.File(qrCodePath))
        
        return
                        
            
        
        
            
    

#Run the client (This runs first)
client.run(DiscordBotToken)
