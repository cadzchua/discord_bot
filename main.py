import discord
from discord.ext import commands
import requests
import json



intents = discord.Intents.all()
bot = commands.Bot(command_prefix= "!", intents=intents)

# Events
@bot.event
async def on_ready():
    print("The Bot is ready for use!")
    print("-------------------------")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(868170359294296107)
    await channel.send(f"Hello {member.mention}! Welcome to the server!")

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(868170359294296107)
    await channel.send(f"Bye {member.mention}!")

# Commands

@bot.command(aliases=['hi', 'hey', 'yo'])
async def hello(ctx):
    await ctx.send(f"Hello {ctx.author.mention}, I am Lieutenant-General Bot!")

@bot.command(aliases=['gm', 'good morning', 'morning'])
async def goodmorning(ctx):
    await ctx.send(f"Good morning {ctx.author.mention}!")

@bot.command()
async def ping(ctx):
    ping_embed = discord.Embed(title="Bot Information", description="Latency and Status of Bot", color= discord.Color.blue())
    ping_embed.add_field(name=f"{bot.user.name}'s Latency(ms): ", value=f"{round(bot.latency * 1000)}ms", inline=True)
    if bot.status == discord.Status.online:
        status_circle = "🟢"
    ping_embed.add_field(name=f"{bot.user.name}'s status: ", value=f"{str(bot.status).capitalize()} {status_circle}", inline=True)
    ping_embed.set_thumbnail(url=bot.user.avatar)
    ping_embed.set_image(url=ctx.guild.icon)
    ping_embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar)
    await ctx.send(embed=ping_embed)


# Running of Bot

with open("token.txt") as file:
    token = file.read()

bot.run(token)