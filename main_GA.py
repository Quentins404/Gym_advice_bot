import random
import colorsys
import discord
import defer
from discord import app_commands
from discord import embeds
from discord import colour
from discord.ext import commands
from discord import *
from discord.ext import commands, tasks
import os
from TOKEN import TOKEN
import pyrandmeme
from pyrandmeme import *
import time
from BlockedWords import blockedWords
from adviceList import randomAdvicelist
from Backexerciselist import random_Back_exercicelist
from Chestexerciceslist import random_Chest_exercielist

intents = discord.Intents.all()
intents.message_content = True

client = commands.Bot(command_prefix="/", intents=discord.Intents.all())




@client.event
async def on_ready():
    # this runs when the account is logged into
    print("We have logged in as {0.user}".format(client))
    try:
        synced = await client.tree.sync()
        print(f"Synced {len(synced)} commands(s)")
    except Exception as e:
        print(e)




# You can now use the 'random_Chest_exercielist' in your program for further processing or displaying the exercises.
@client.tree.command(name="chest_exercise" , description="Gives you a list of chest exercises")
async def chest_exercise(interaction: discord.Interaction):
                   numJoke = random.randint(0,len(random_Chest_exercielist))
                   await interaction.response.send_message(random_Chest_exercielist[numJoke])


@client.tree.command(name="back_exercise" , description="Gives you a list of back exercises")
async def back_exercise(interaction: discord.Interaction):
                   numJoke = random.randint(0,len(random_Back_exercicelist))
                   await interaction.response.send_message(random_Back_exercicelist[numJoke])
# You can now use the 'backexercicelist' in your program for further processing or displaying the exercises.



@client.tree.command(name="advice", description="Gives you bodybuilding adivces ")
async def advice(interaction: discord.Interaction):
                   numJoke = random.randint(0,len(randomAdvicelist))
                   await interaction.response.send_message(randomAdvicelist[numJoke])


@client.event
async def on_message(ctx):
    print(f"{ctx.channel}: {ctx.author}: {ctx.author.name}: {ctx.content}")
    if any(x in message for x in blockedWords):
        await message.delete()


@client.tree.command(name="help" , description="Gives you all the commands")
async def help(interaction: discord.Interaction):
    embed=discord.Embed(title="**My commands are**",description="\n /advice \n /help \n /back_exercise \n /chest_exercise \n /greetings \n /link \n /ping \n /meme(beta))" ,color=discord.Colour.green())
    await interaction.response.send_message(embed=embed)
    await defer(ephemeral=False, thinking=False)

@client.tree.command(name="link", description="Gives you a permanent link to the server")
async def link(interaction: discord.Interaction):
    await interaction.response.send_message("Here is a permanent link to the server: https://discord.gg/eGCX8GCf53 ")

@client.tree.command(name="socials" , description="Gives you all the links to ethano's social medias")
async def socials(interaction: discord.Interaction):
    embed=discord.Embed(title="**Ethano's social media links**",description="Instagram :  \n Discord: https://discord.gg/eGCX8GCf53" ,color=discord.Colour.green())
    await interaction.response.send_message(embed=embed)
    await defer(ephemeral=False, thinking=False)

@client.tree.command(name="meme" , description="Send a random meme")
async def meme(interaction:discord.Interaction):
    await interaction.response.send_message(embed=await pyrandmeme())
    



@client.tree.command(name="ping" , description="Replies with a Pong!")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(f"Pong! {round(client.latency * 1000)}ms")

client.run(TOKEN)