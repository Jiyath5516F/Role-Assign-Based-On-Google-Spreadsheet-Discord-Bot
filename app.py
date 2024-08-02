import gspread
from oauth2client.service_account import ServiceAccountCredentials
import discord
from discord.ext import commands, tasks

SPREADSHEET_NAME = 'YOUR_SPREADSHEET_NAME' # Name of the Google Sheet
SHEET_NAME = 'Form Responses 1' # Name of the Sheet
RANGE_NAME = 'A2:E' # Range of the Sheet
ROLE_ID_BEDROCK = 'REPLACE_YOUR_ID' # ID of the role 1
ROLE_ID_JAVA = 'REPLACE_YOUR_ID' # ID of the role 2

scope = ["https://spreadsheets.google.com/feeds",
         "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name(
    'credentials.json', scope)
client = gspread.authorize(creds)
spreadsheet = client.open(SPREADSHEET_NAME)
sheet = spreadsheet.worksheet(SHEET_NAME)

TOKEN = 'YOUR_DISCORD_BOT_TOKEN' # Discord Bot Token
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)


@tasks.loop(minutes=1)
async def assign_roles():
    records = sheet.get_all_records()

    for record in records:
        username = record['Username']
        discord_handle = record['Discord @handle']
        version = record['Which version?']
        role_id = ROLE_ID_BEDROCK if version.lower() == 'bedrock' else ROLE_ID_JAVA

        for guild in bot.guilds:
            member = discord.utils.get(guild.members, name=discord_handle)
            if member:
                role = guild.get_role(int(role_id))
                if role:
                    try:
                        await member.add_roles(role)
                        print(
                            f"Assigned {role.name} to {member.name} in {guild.name}")
                    except discord.Forbidden:
                        print(
                            f"Failed to assign {role.name} to {member.name} in {guild.name}: Missing Permissions")
                    except discord.HTTPException as e:
                        print(
                            f"Failed to assign {role.name} to {member.name} in {guild.name}: {e}")

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    assign_roles.start()

bot.run(TOKEN)