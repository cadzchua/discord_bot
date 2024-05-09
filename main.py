import discord
from discord.ext import commands
import asyncio



intents = discord.Intents.all()
bot = commands.Bot(command_prefix= "!", intents=intents)

# Events
@bot.event
async def on_ready():
    print("The Bot is ready for use!")
    print("-------------------------")
    bot.loop.create_task(check_empty_voice_channels())

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

@bot.command()
async def join(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        await channel.connect()
    else:
        await ctx.send("You are not in a voice channel, you must be in a voice channel to run this command.")

@bot.command()
async def leave(ctx):
    if (ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send("I left the voice channel.")
    else:
        await ctx.send("I am not in a voice channel.")

async def check_empty_voice_channels():
    await bot.wait_until_ready()
    while not bot.is_closed():
        for vc in bot.voice_clients:
            if len(vc.channel.members) == 1:  # Only bot is present
                await vc.disconnect()
                ctx = await bot.get_context(vc.channel)
                await ctx.send("No one is in the voice channel. I left.")
        await asyncio.sleep(60)  # Check every minute




# Running of Bot

with open("token.txt") as file:
    token = file.read()

bot.run(token)