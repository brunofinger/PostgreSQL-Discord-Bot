
# PostgreSQL Discord Bot

The PostgreSQL Discord Bot is a Python-based bot designed to provide easy access to a PostgreSQL server directly from a Discord server. With this bot, users can execute SQL queries, manage database schema, and even perform backups of their PostgreSQL databases, all from the comfort of their Discord server. The bot is built using the Discord.py module and uses the psycopg2 library to connect to the PostgreSQL server. It also features a command system that allows users to interact with the bot and perform various actions, such as creating tables, inserting data, and more. Overall, the PostgreSQL Discord Bot is a useful tool for those who want to manage their PostgreSQL databases from the convenience of their Discord server.

![](https://cdn.iconscout.com/icon/free/png-512/postgresql-11-1175122.png)

## About

PostgreSQL Discord Bot is a Python-based bot created by [Bruno Finger](https://github.com/brunofinger) that allows you to manage PostgreSQL databases in your Discord server. With just a few simple commands, you can create and manage tables, insert data, update data, and more.

## Features

-   No premium or subscription required
-   Full access to your PostgreSQL database
-   Simple and easy to use commands
-   Lightweight and fast

## Installation

PostgreSQL Discord Bot requires Python 3 and the psycopg2 library to run. Here's how to install everything you need:

## Basic SQL Commands

`$ git clone https://github.com/brunofinger/PostgreSQL-Discord-Bot.git
$ cd PostgreSQL-Discord-Bot
$ pip3 install -r requirements.txt` 

| Command          | Syntax                                      |
| ---------------- | ------------------------------------------- |
| Create Table     | `CREATE TABLE IF NOT EXISTS name (parameters);` |
| Select a Value   | `SELECT column-name FROM table-name WHERE type='identifier';` |
| Insert a Value   | `INSERT INTO table-name (parameters) VALUES (values of parameters);` |
| Delete a Value   | `DELETE FROM table-name WHERE type='identifier';` |
| Update a Value   | `UPDATE table-name SET column-name = 'new value' WHERE type='identifier';` |


## Usage

To use PostgreSQL Discord Bot, you will need to set up a bot and add it to your Discord server. Here's how:

1.  Go to the [Discord Developer Portal](https://discord.com/developers/applications) and create a new application.
2.  Click on "Bot" in the left-hand menu and then click "Add Bot".
3.  Give your bot a name and a profile picture, and then copy the bot token.
4.  Rename the `example.env` file to `.env` and paste your bot token after `DISCORD_TOKEN=`.
5.  Create a PostgreSQL database and copy its connection string.
6.  Paste the connection string after `DATABASE_URL=` in the `.env` file.
7.  Save the `.env` file and start the bot by running `python3 discord_bot.py`.
