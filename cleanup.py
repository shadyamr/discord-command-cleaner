import discord
from discord.ext import commands
import asyncio

# Replace with your bot token
BOT_TOKEN = "TOKEN_HERE"

# Optional: Add specific guild IDs to clear (leave empty to only clear global)
GUILD_IDS = []  # Example: [123456789, 987654321]

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print("Starting command cleanup...")
    
    try:
        # Clear global commands
        print("\nClearing global commands...")
        global_commands = await bot.tree.fetch_commands()
        print(f"Found {len(global_commands)} global command(s)")
        
        for cmd in global_commands:
            print(f"  - Deleting global command: {cmd.name}")
            await bot.http.delete_global_command(bot.application_id, cmd.id)
        
        print("Global commands cleared!")
        
        # Clear guild-specific commands
        if GUILD_IDS:
            for guild_id in GUILD_IDS:
                print(f"\nClearing commands for guild {guild_id}...")
                try:
                    guild_commands = await bot.tree.fetch_commands(guild=discord.Object(id=guild_id))
                    print(f"Found {len(guild_commands)} command(s) in guild {guild_id}")
                    
                    for cmd in guild_commands:
                        print(f"  - Deleting guild command: {cmd.name}")
                        await bot.http.delete_guild_command(bot.application_id, guild_id, cmd.id)
                    
                    print(f"Commands cleared for guild {guild_id}!")
                except discord.Forbidden:
                    print(f"Error: Bot doesn't have access to guild {guild_id}")
                except discord.HTTPException as e:
                    print(f"Error clearing commands for guild {guild_id}: {e}")
        
        # Alternative: Clear commands for ALL guilds the bot is in
        else:
            print("\nClearing commands from all guilds the bot is in...")
            for guild in bot.guilds:
                print(f"\nChecking guild: {guild.name} (ID: {guild.id})")
                try:
                    guild_commands = await bot.tree.fetch_commands(guild=guild)
                    print(f"Found {len(guild_commands)} command(s)")
                    
                    for cmd in guild_commands:
                        print(f"  - Deleting guild command: {cmd.name}")
                        await bot.http.delete_guild_command(bot.application_id, guild.id, cmd.id)
                    
                    if guild_commands:
                        print(f"Commands cleared for {guild.name}!")
                except discord.Forbidden:
                    print(f"Error: Missing permissions in guild {guild.name}")
                except discord.HTTPException as e:
                    print(f"Error clearing commands for {guild.name}: {e}")
        
        print("\n✅ All commands have been cleared successfully!")
        print("You can now register new commands from your bot.")
        
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")
    
    finally:
        print("\nClosing bot...")
        await bot.close()

if __name__ == "__main__":
    print("Discord Command Cleaner")
    print("=" * 50)
    bot.run(BOT_TOKEN)
