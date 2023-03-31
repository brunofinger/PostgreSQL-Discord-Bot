import psycopg2
import psycopg2.extras
import discord

from dotenv import dotenv_values

token  =  dotenv_values(".env")["TOKEN"]
client = discord.Client()
DATABASE_CONNECTION = {
	'host'            : '',
	'port'            :  1,
	'dbname'          : '',
	'user'            : '',
	'password'        : '',
	'connect_timeout' : 10
}


def pgsql_connection():
    conn = psycopg2.connect(**DATABASE_CONNECTION)
    conn = conn.autocommit = True
    return conn

def pgsql_cursor(conn):
    #return result as a dict
    return conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

def execute_query(query):
    conn = pgsql_connection()
    cursor = pgsql_cursor(conn)
    cursor.execute(query)
    return cursor.fetchall()


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

title = 'SQLite Discord Shell'
arg_missing_message = discord.Embed(title=title, description='Arguments are missing')

@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.content.startswith('sql>'):
        for role in message.author.roles:
            if role.name == "dmb":
                break
        else:
            await message.channel.send(embed=(discord.Embed(title=title, description="""You are not allowed to use Database Manager Bot without a role called "dmb" """, color=discord.Color.red())))
            return

    if message.content == ('sql>help'):
        await message.channel.send(embed=(discord.Embed(title=title, description=""" For Initialization Help, please read project's readme.md:
         For More Commands, visit this great cheat sheet:
         https://d17h27t6h515a5.cloudfront.net/topher/2016/September/57ed880e_sql-sqlite-commands-cheat-sheet/sql-sqlite-commands-cheat-sheet.pdf
         """, color = discord.Color.blue())))
        return

    if message.content.startswith('sql>'):
        query = ""
        for word in message.content.split():
            query += word + " "
        query = query.replace('sql>', '')
        if(query == " "):
            await message.channel.send(embed=arg_missing_message)
            return
        await message.channel.send(embed=(discord.Embed(title=title + " Query Output:", description=str(execute_query(query)), color=discord.Color.light_gray())))

client.run(token)
