# Discord Command Cleaner

A simple Python script to clear all registered Discord bot commands (global and guild-specific).

## Prerequisites

- Python 3.8+
- discord.py library

```bash
pip install discord.py
```

## Setup

1. Open the script and replace `YOUR_BOT_TOKEN_HERE` with your bot token
2. (Optional) Configure `GUILD_IDS` list:
   - Leave empty `[]` to clear commands from **all guilds** the bot is in
   - Add specific guild IDs `[123456789, 987654321]` to target only those guilds

## Usage

Run the script:

```bash
python clear_commands.py
```

The bot will:
1. Log in
2. Clear all global commands
3. Clear guild commands (from all guilds or specified guilds)
4. Display what was deleted
5. Automatically shut down

## Example Output

```
Found 10 global command(s)
  - Deleting global command: ping
  - Deleting global command: help
  ...
Global commands cleared!

✅ All commands have been cleared successfully!
```

## When to Use

- Cleaning up old commands before registering new ones
- Switching between development and production bots
- Removing commands that are stuck or won't update

---

**Note:** After clearing, you can freely register new commands from your main bot without conflicts.
