import psycopg2
from psycopg2 import OperationalError
import discord

from dotenv import dotenv_values

token = dotenv_values(".env")["TOKEN"]
client = discord.Client()

# ? Database

database = dotenv_values(".env")["DB_NAME"]
user = dotenv_values(".env")["DB_USER"]
password = dotenv_values(".env")["DB_PASSWORD"]
host = dotenv_values(".env")["DB_HOST"]
port = dotenv_values(".env")["DB_PORT"]

def create_connection():
    conn = None
    try:
        conn = psycopg2.connect(
            database=database,
            user=user,
            password=password,
            host=host,
            port=port
        )
        print("Connection successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return conn


conn = create_connection()

def execute_query(query):
    if conn is not None:
        try:
            output = ""
            cur = conn.cursor()
            try:
                cur.execute(query)
            except Exception as e:
                return e
            info = cur.fetchall()
            conn.commit()
            for value in info:
                output += str(value) + "\n"
            if output=="":
                return "No Output / Empty"
            return output
        except Exception as e:
            return e
    return "Error! the database connection was not created."


# ? Discord Bot

@client.event
async def on_ready():
    print('logged in as {0.user}'.format(client))
    guilds = client.guilds
    for guild in guilds:
        for role in guild.roles:
            if role.name.lower() == "dmb".lower():
                break
        else:
            await guild.create_role(name="dmb")

@client.event
async def on_guild_join(guild):
    for role in guild.roles:
        if role.name.lower() == "dmb".lower():
            break
    else:
           await guild.create_role(name="dmb")

title = 'PostgreSQL Discord Shell'
arg_missing_message = discord.Embed(title=title, description='Arguments are missing')
blue_color = discord.Color.blue()
gray_color = discord.Color.light_gray()
red_color = discord.Color.red()

@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.content.startswith('sql>'):
        for role in message.author.roles:
            if role.name == "dmb":
                break
        else:
            await message.channel.send(embed=(discord.Embed(title=title, description="""You are not allowed to use Database Manager Bot without a role called "dmb" """, color=red_color)))
            return

    if message.content == ('sql>help'):
        await message.channel.send(embed=(discord.Embed(title=title, description=""" For Initialization Help, please read project's readme.md:
         For More Help, visit PostgreSQL's website:
         https://www.postgresql.org/docs/
         To check my project's cool Website, visit alTab Developers:
         http://www.altab.dev/
         For More Commands, visit this great cheat sheet:
         https://www.postgresqltutorial.com/postgresql-cheat-sheet/
         """, color=blue_color)))
        return

    if message.content.startswith('sql>'):
        query = ""
        for word in message.content.split():
            query += word + " "
        query = query.replace('sql>', '')
        if(query == " "):
            await message.channel.send(embed=arg_missing_message)
            return
        await message.channel.send(embed=(discord.Embed(title=title + " Query Output:",
