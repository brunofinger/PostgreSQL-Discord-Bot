import psycopg2
import psycopg2.extras
import discord
from dotenv import dotenv_values

# Load Discord Bot Token from .env file
token = dotenv_values(".env")["TOKEN"]

# Define database connection details
DATABASE_CONNECTION = {
	'host': '',
	'port':  1,
	'dbname': '',
	'user': '',
	'password': '',
	'connect_timeout': 10
}

# Function to create a connection to the PostgreSQL database
def pgsql_connection():
    conn = psycopg2.connect(**DATABASE_CONNECTION)
    conn.autocommit = True  # Set autocommit to True
    return conn

# Function to create a cursor with dictionary output
def pgsql_cursor(conn):
    return conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

# Function to execute a query and return the result
def execute_query(query):
    conn = pgsql_connection()
    cursor = pgsql_cursor(conn)
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

# Initialize Discord client
client = discord.Client()

# Event that runs when the bot is ready
@client.event
async def on_ready():
    print('logged in as {0.user}'.format(client))
    # Check if the "dmb" role exists in all the guilds the bot is a member of, if not create it
    for guild in client.guilds:
        for role in guild.roles:
            if role.name.lower() == "dmb":
                break
        else:
            await guild.create_role(name="dmb")

# Event that runs when the bot joins a new guild
@client.event
async def on_guild_join(guild):
    # Check if the "dmb" role exists in the guild, if not create it
    for role in guild.roles:
        if role.name.lower() == "dmb":
            break
    else:
        await guild.create_role(name="dmb")

# Embed message template
title = 'SQLite Discord Shell'
arg_missing_message = discord.Embed(title=title, description='Arguments are missing')

# Event that runs when the bot receives a message
@client.event
async def on_message(message):
    # Ignore messages from the bot itself
    if message.author == client.user:
        return

    # Check if the message starts with "sql>"
    if message.content.startswith('sql>'):
        # Check if the message is "sql>help", if so, return a help message
        if message.content == ('sql>help'):
            await message.channel.send(embed=(discord.Embed(title=title, description=""" For Initialization Help, please read project's readme.md:
             For More Commands, visit this great cheat sheet:
             https://d17h27t6h515a5.cloudfront.net/topher/2016/September/57ed880e_sql-sqlite-commands-cheat-sheet/sql-sqlite-commands-cheat-sheet.pdf
             """, color = discord.Color.blue())))
            return

        # Execute the query and return the result
        query = message.content.replace('sql>', '').strip()  # Extract the query from the message
        if not query:  # Check if
