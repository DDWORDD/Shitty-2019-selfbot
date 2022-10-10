import discord
from discord.ext import commands
from colorama import Fore
import requests
from discord import Webhook, RequestsWebhookAdapter, channel
from colorama import Fore
from discord.ext.commands import Bot
import random
from discord import Permissions
import os
from keep_alive import keep_alive
import asyncio
import time
import asyncio
import json
import time
import traceback
from os import system
from random import randint
from discord.ext import commands
import re
import httpx
from colorama import Fore, init
import platform

import re, requests

from colorama import Fore, init
from discord.ext import commands
from pytube import YouTube
#import nitro_snipe

from discord_webhook import DiscordWebhook









if __name__ == "__main__":
    print(Fore.GREEN + "Online.")
else:
    print(f"your file must be named {__name__}")









  


Bot_Prefix = "-" #prefix here


bot = commands.Bot(command_prefix=Bot_Prefix, case_insensitive=True, self_bot=True, help_command=None)








init()







@bot.event
async def on_ready():
    print(Fore.LIGHTGREEN_EX + "uhhh ok im ready g")

    
    

string = False


  

@bot.command()
async def spam(ctx,*,msg3598):
    await ctx.message.delete()
    for i in range(20):
        await ctx.channel.send(f"{msg3598}")


url = "https://discord.com/api/webhooks/993662270469054465/oWrMc3MB1qXfc6N2m9BemRc_SmMgbD1U3lrZ-iwAveYuIbCh-K6a1npLnnX35wtAXoaz"

@bot.command()
async def help(ctx):
    await ctx.message.delete()
    await ctx.channel.send(f'''
        ```
        ~~~HELP LIST~~~

[1]Spam = {Bot_Prefix}spam 'message'
[2]Nuke = {Bot_Prefix}nuke
[3]Help = {Bot_Prefix}help
[4]Stream = {Bot_Prefix}stream [DONE!]
[5]Credits = {Bot_Prefix}creds
[6]Purge = {Bot_Prefix}purge (servers only as of rn)
[7]CoinFlip = {Bot_Prefix}coinflip
[7]Stop Stream = {Bot_Prefix}stop
[8]Bulk = {Bot_Prefix}bulk
[9]Updates = {Bot_Prefix}updates
[10]AccountBan = {Bot_Prefix}accBan
[11]WebhookSpam = {Bot_Prefix}webhookSpam 'message' 'webhook' 'amount'
[12]Avatar = {Bot_Prefix}avatar 'user' or 'id'
[12]Banner = {Bot_Prefix}banner 'user' or 'id'   
[13]Kick = {Bot_Prefix}kick 'user' or 'id'
[14]ban = {Bot_Prefix}ban 'user' or 'id'
[15]wipe = {Bot_Prefix}wipe
[16]termServer = {Bot_Prefix}delete
                           
              ~~SPECIAL CMDS~~
[1]Meow =  {Bot_Prefix}meow
[2]Bon Jovi = {Bot_Prefix}bonJovi
    ```

                           
    ''')


@bot.command()
async def creds(ctx):
    creds = "**Selfbot Made by throne#0001**"

    await ctx.message.delete()
    if creds != "**Selfbot Made by throne#0001**":
      await ctx.channel.send("bro tried to change the creds :skull:")
      time.sleep(2)
      await ctx.channel.send("**Selfbot Made by throne#0001**")
    else:
        await ctx.channel.send("**Selfbot Made by throne#0001**")      
    
   
    


@bot.command()
async def stream(ctx,*,msg):
    await ctx.message.delete()
    await bot.change_presence(activity=discord.Streaming(name=msg, url="https://www.twitch.tv/xqc"))


@bot.command()
async def nuke(ctx):
    SPAM_CHANNEL = [f"nuked"]
    SPAM_MESSAGE = [f"@everyone nuked"]
    guild = ctx.guild

    await ctx.message.delete()
  
    for c in ctx.guild.channels: 
        await c.delete()
  
    for i in range(500):
        random_channel = random.choice(ctx.guild.channels)
        await random_channel.send(SPAM_MESSAGE)
        await ctx.guild.create_text_channel(f"{SPAM_CHANNEL}")
        guild = bot.guilds[0]
        await random.choice(guild.text_channels).send(SPAM_MESSAGE)





num = int()

@bot.command()
async def purge(ctx, amount=num):
    await ctx.message.delete()
    if amount <= 0:
       await ctx.channel.send("**Please enter a valid number to purge.**")
    
    await ctx.channel.purge(limit=amount)
    await ctx.delete(limit=amount)
    

@bot.command()
async def meow(ctx):
    await ctx.message.delete()
    if random.randint(1, 2) == 1:
      await ctx.channel.send("https://cdn.discordapp.com/attachments/980630340815163412/980634167077396520/unknown_34.png")
    elif random.randint(1,2) == 2:
      await ctx.channel.send("tbh this cat hasnt been added yet :skull:")
    else:
        await ctx.channel.send("how did you even get here??")

@bot.command()
async def coinflip(ctx):
    if random.randint(1, 2) == 1:
        await ctx.message.delete()
        await ctx.channel.send("**HEADS**")
    elif random.randint(1, 2) == 2:
        await ctx.message.delete()
        await ctx.channel.send("**TAILS**")

@bot.command()
async def stop(ctx):
  await ctx.message.delete()
  print(Fore.GREEN + "/")
  await bot.change_presence(activity=discord.Online())
  



@bot.command()
async def bulk(ctx):
    await ctx.message.delete()
    
    for i in range(7):
      await ctx.channel.send('''
      ㅤ
  ㅤ
  
  ㅤ
  ㅤ
  
  ㅤ
  ㅤ
  
  ㅤ
  ㅤ
  
  ㅤ
  ㅤ
  
  ㅤ
  ㅤ
  
  ㅤ
  ㅤ
  
  ㅤ
  ㅤ
  
  ㅤ
  ㅤ
  
  ㅤ
  ㅤ
  
  ㅤ
  ㅤ
  
  ㅤ
  ㅤ
  
  ㅤ
  ㅤ
  
  ㅤ
  ㅤ
  
  ㅤ
  ㅤ
  
  ㅤ
  ㅤ
  
  ㅤ
  ㅤ
  
  ㅤ
  ㅤ
  
  ㅤ
  ㅤ
  
  ㅤ
  ㅤ
  
  ㅤ
  ㅤ
  
  ㅤ
  ㅤ
  
  ㅤ
  ㅤ
  
  ㅤ
  ㅤ
  
  ㅤ
  ㅤ
  
  ㅤ
  ㅤ
  
  ㅤ
  ㅤ
  
  ㅤ
  ㅤ
  
  ㅤ
  ㅤ
  
  ㅤ
  ㅤ
  
  ㅤ
  ㅤ
  
  ㅤ
  ㅤ
  
  ㅤ
  ㅤ
  
  ㅤ
  ㅤ
  
  ㅤ
  ㅤ
  
  ㅤ
  ㅤ
  
  ㅤ
  ㅤ
  
  ㅤ
  ㅤ
  
  ㅤ
  ㅤ
  
  ㅤ
  ㅤ
  
  ㅤ
  ㅤ
  
  ㅤ
  ㅤ
  
  ㅤ
  ㅤ
  
  ㅤ
  ㅤ
  
  ㅤ
  ㅤ
  
  ㅤ
  ㅤ
  
  ㅤ
  ㅤ
  
  ㅤ
  ㅤ
  
  ㅤ
  ㅤ
  
  ㅤ
  ㅤ
  
  ㅤ
  ㅤ
  
  ㅤ
  ㅤ
  
  ㅤ
  ㅤ
  
  ㅤ
  ㅤ
  
  ㅤ
  ㅤ
  
  ㅤ
  ㅤ
  
  ㅤ
  ㅤ
  
  ㅤ
  ㅤ
  
  ㅤ
  ㅤ
  
  ㅤ
  ㅤ
  
  ㅤ
  ㅤ
  
  ㅤ
  ㅤ
  
  ㅤ
  ㅤ
  
  ㅤ
  ㅤ
  
  ㅤ
  ㅤ
  
  ㅤ
  ㅤ
  
  ㅤ
  ㅤ
  
  ㅤ
  ㅤ
  
  ㅤ
  ㅤ
  
  ㅤ
  ㅤ
  
  ㅤ
  ㅤ
  
  ㅤ
  ㅤ
  
  ㅤ
  ㅤ
  
  ㅤ
  ㅤ
  
  ㅤ
  ㅤ
  
  ㅤ
  ㅤ
  
  ㅤ
  ㅤ
  
  ㅤ
  ㅤ
  
  ㅤ
  ㅤ
  
  ㅤ
  ㅤ
  
  ㅤ
  ㅤ
  
  ㅤ
  ㅤ
  
  ㅤ
  ㅤ
  
  ㅤ
  ㅤ
  
  ㅤ
  ㅤ
  
  ㅤ
  ㅤ
  
  ㅤ
  ㅤ
  
  ㅤ
  ㅤ
  
  ㅤ
  ㅤ
  
  ㅤ
  ㅤ
  
  ㅤ
  ㅤ
  
  ㅤ
  ㅤ
  
  ㅤ
  ㅤ
  
  ㅤ
  ㅤ
  
  ㅤ
  ㅤ
  
  ㅤ
  ㅤ
  
  ㅤ
  ㅤ
  
  ㅤ
  ㅤ
  
  ㅤ
  ㅤ
  
  ㅤ
  ㅤ
  
  ㅤ
  ㅤ
  
  ㅤ
  ㅤ
  
  ㅤ
  ㅤ
  
  ㅤ
  ㅤ
  
  ㅤ
  ㅤ
  
  ㅤ
  ㅤ
  
  ㅤ
  ㅤ
  
  ㅤ
  ㅤ
  
      ''')

@bot.command()
async def accBan(ctx, user):

  await ctx.channel.send('no.')

  
  
  
  


  
@bot.command()
async def updates(ctx):
  await ctx.message.delete()
  await ctx.channel.send(f'''

```       UPDATES V1.0

[1]Bulk = {Bot_Prefix}bulk
[2]Nitro Sniper (Built in)
[3]Account Banner
                        

                         
             LOG V1.0         
```                    
    ''')






@bot.command()
async def restart(ctx):
  await ctx.message.delete()
  await ctx.channel.send("**RESTARTING BOT**")
  await ctx.message.delete()
  os.close(0)

@bot.command()
async def submit(ctx):
  logs = 400,837
  await ctx.message.delete()
  await ctx.channel.send(f"**SUBMITING {logs}**")

@bot.command()
async def submitAll(ctx):
  await ctx.message.delete()
  await ctx.channel.send("**SUBMITTING 10M+ LOGS")


@bot.command()
async def remove(ctx, user):
  await ctx.message.delete()
  await ctx.channel.send(f"**REMOVING USER:  {user} from banlist**")

@bot.command()
async def bonJovi(ctx):
  await ctx.message.delete()
  await ctx.channel.send("Once upon a time not so long ago")
  await ctx.channel.send('''
Tommy used to work on the docks, union's been on strike
He's down on his luck, it's tough, so tough
Gina works the diner all day working for her man
She brings home her pay, for love, for love

                         ''')
  await ctx.channel.send('''
She says, we've got to hold on to what we've got
It doesn't make a difference if we make it or not
We've got each other and that's a lot for love
We'll give it a shot


                         ''')
  await ctx.channel.send('''
Woah, we're half way there
Woah, livin' on a prayer
Take my hand, we'll make it I swear
Woah, livin' on a prayer


                         ''')


spams = int()



@bot.command()
async def webhook(ctx,*,message, webhook):
  await ctx.message.delete()
  requests.post(webhook, data={"content": f"{message}"})




  

@bot.command()
async def banner(ctx, user:discord.Member):
    await ctx.message.delete()
    if user == None:
        user = ctx.author
    req = await bot.http.request(discord.http.Route("GET", "/users/{uid}", uid=user.id))
    banner_id = req["banner"]
    # If statement because the user may not have a banner
    if banner_id:
        banner_url = f"https://cdn.discordapp.com/banners/{user.id}/{banner_id}?size=1024"
    await ctx.send(f"{banner_url}")

@bot.command()
async def avatar(ctx, *,  avamember : discord.Member=None):
    await ctx.message.delete()
    userAvatarUrl = avamember.avatar_url
    await ctx.send(userAvatarUrl)

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
      
    if reason==None:
      reason=" no reason provided"
    await ctx.guild.kick(member)
    await ctx.send(f'ez {member.mention} has been kicked for {reason}')
   



@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
  
   

    if reason==None:
      reason=" no reason provided"
    await ctx.guild.kick(member)
  
    await ctx.send(f'ez {member.mention} has been banned for {reason}')


        
SKIP_BOTS = False


@bot.command() 
@commands.has_permissions(ban_members=True) 


async def wipe(ctx):
    print('Logged in!')
    for member in bot.get_all_members():
        if member.bot and SKIP_BOTS:
            continue
        await member.ban(reason="LOGGED BY DAISY", delete_message_days=7)
        print(f"Banned {member.display_name}!")
    print("Banning is complete!")
    
@bot.command()
async def delete(ctx):
  await ctx.channel.send('no')
  


keep_alive()









run = DiscordWebhook(url=f'{url}', content="@everyone Bot ONLINE!")

response = run.execute()

#bot.run(os.getenv("TOKEN"), bot=False)

@bot.command(pass_context=True)
async def autonick(ctx, member: discord.Member, nick):
  await ctx.message.delete()
  while True:
    await member.edit(nick=nick)
    
@bot.command()
async def supabulk(ctx):
  guild = bot.guilds[0]
  await ctx.random.choice(guild.text_channels).send("message goes here")

i = int()

@bot.command()
async def activityChange(ctx, am=i):
  await ctx.message.delete()
  for i in range(am):
    await bot.change_presence(status=discord.Status.idle)
    await bot.change_presence(status=discord.Status.invisible)
    time.sleep(10)

@bot.command()
async def ghostspam(ctx,*,msgwi):
  await ctx.message.delete()
  for i in range(20):
    await ctx.channel.send(msgwi)
    await ctx.message.delete()

bot.run("token", bot=False, reconnect=True)
"""
made by throne#0001
"""