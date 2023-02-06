import discord
from discord import app_commands
from discord.ext import commands
import TOKEN

intents = discord.Intents.default()
intents.typing = True
intents.messages = True
intents.message_content = True


bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print("Bot launch succesful")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} commands(s)")
    except Exception as e:
        print(e)
        
@bot.tree.command(name="hello")
async def hello(intercation: discord.Interaction):
    await intercation.response.send_message("Hello {interaction.user.mention}! This is a slash command")
    ephemeral=True
    
@bot.tree.command(name="say")
@app_commands.describe(thing_to_say="What I have to say?")
async def say(intercation: discord.Interaction, thing_to_say: str):
    await intercation.response.send_message(f"{intercation.user.mention} said {thing_to_say}")
    
    
@bot.tree.command(name="request_verification")
async def request_verification(interaction: discord.Interaction):
    await interaction.resposne.send_message()
    
@bot.command()
async def info(ctx, *, member: discord.Member):
    """Tells you some info about the member."""
    msg = f'{member} joined on {member.joined_at} and has {len(member.roles)} roles.'
    await ctx.send(msg)

@info.error
async def info_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send('I could not find that member...')

if __name__ == "__main__":
    bot.run(TOKEN.TOKEN())