from typing import MutableSequence
from colorama import Fore
from utils.discordwebscraper import webscraper
from utils.Admin import admin
print(f'{Fore.RED}\tSub Imports Initlized {Fore.WHITE}')

import discord, os, asyncio, random

def print_message_main(str):
    print(Fore.GREEN + str + Fore.WHITE)


print_message_main('Main Imports Initlized')
client = discord.Client()

prefix = '$$'

admins = 554486518543155212
## scuffed coroutine work around, please no judge
def prefix_shit(message):
    global prefix
    old_prefix, prefix = prefix, admin.prefix_change(prefix, message)
    return old_prefix
    
companys = {
    'steam': 'Steam',
    'itch': 'Itch.io',
    'pc': 'PC',
    'epic': 'Epic Games Store',
    'drm': 'DRM-Free', 
    'battlenet': 'Battle.net',
    'gog': 'GOG',
}
statuses = [f'Type "{prefix}help" for help', 'Doing dumb shit', 'Listening to some busting tunes', 'LUST MONTH LUST MONTH LUST MONTH', 'Vibing', 
'Single/Depressed/Bullied/Half Demon/Trans/Has A Huge Secret ;)/Quirky/Mysterious/Gay/straight', 'Visual Studio Code', 'Adding a backend...',
'Stealing server info', 'Pampcakes', 'hehe, A-10 chan go BRRRRRRRRRRRRRRRRTTTTTTT', 'BRRRRRRRRRRRRRRRTTTTTT', 'with your mom']

for item in list(companys.values()):
    statuses.append('Looking for free games on ' + item)

@client.event
async def status_changer():
    await client.change_presence(activity=discord.Game(name=random.choice(statuses)))
    print_message_main(f'\t\tstatus changed')
    await asyncio.sleep(60)
    await status_changer()


@client.event
async def on_ready():
    print_message_main("Signed into: {0.user}".format(client))
    await status_changer()

@client.event
async def on_message(message):
    message_lowered = message.content.lower()
    if message.author == client.user:
        return

    channel = client.get_channel(message.channel.id)

    if message_lowered == f'{prefix}help':
        help_embed = discord.Embed(name="Help:", color=discord.Color(7863510))
        help_embed.set_author(name="2 GreyScales#4533", url="https://github.com/JGreyScales", icon_url="https://i.imgur.com/KzRorR8.gif")
        help_embed.add_field(name='Prefix is currently:', value=prefix, inline=False)
        help_embed.add_field(name='Help:', value=f'{prefix}help', inline=False)
        help_embed.add_field(name='Free:', value=f'{prefix}free products\n{prefix}free games', inline=False)
        for company in companys:
            help_embed.add_field(name=f'Free {company} games:', value=f'{prefix}free {company}\nWill return all free GAMES for {companys[company]}', inline=True)
        help_embed.set_footer(text='if there are any problems contact 2 GreyScales#4533. I might fix it I might not. All games gathered from GamerPower')

        await channel.send(embed=help_embed)

    elif message_lowered == f'{prefix}free products':
        embed = discord.Embed(title="Free Products:", color=discord.Color(3038))

        for game in webscraper.scraper():
            embed.add_field(name=game['title'], value=f"Game was: {game['worth']} now is: FREE\nends on: {game['end_date']}\n Game link:{game['open_giveaway_url']}" +
                f"\n{game['description']}\n\n", inline=False)

            if len(embed) >= 5500:
                await channel.send(embed=embed)
                embed = discord.Embed(title="Free Products:", colour=discord.Colour(0x3e038c))
        
        await channel.send(embed=embed)

    elif message_lowered == f'{prefix}free games':
        embed = discord.Embed(title="Free Games:", color=discord.Color(0x3e038c))

        for game in webscraper.scraper():
            if game['type'] == 'Full Game':
                embed.add_field(name=game['title'], value=f"Game was: {game['worth']} now is: FREE\nends on: {game['end_date']}\n Game link:{game['open_giveaway_url']}" +
                f"\n{game['description']}\n\n", inline=False)
                
                if len(embed) >= 5500:
                    await channel.send(embed=embed)
                    embed = discord.Embed(title="Free Games:", colour=discord.Colour(0x3e038c))
                
        await channel.send(embed=embed)

    elif message_lowered[7:] in companys:

        message_lowered = companys[message_lowered[7:]]
        embed = discord.Embed(title=f"Free {message_lowered} Games:", colour=discord.Colour(0x3e038c))

        for game in webscraper.scraper():

            if game['type'] == 'Full Game' and message_lowered in game['platforms']:
                embed.add_field(name=game['title'], value=f"Game was: {game['worth']} now is: FREE\nends on: {game['end_date']}\n Game link:{game['open_giveaway_url']}" +
                f"\n{game['description']}\n\n", inline=False)

            if len(embed) >= 5500:
                await channel.send(embed=embed)
                embed = discord.Embed(title=f"Free {message_lowered} Games:", colour=discord.Colour(0x3e038c))
                
        await channel.send(embed=embed)



    ## admin stuff

    elif message_lowered.startswith(f'{prefix}prefix') and message.author.id == admins:
        await channel.send(f'Old prefix: {prefix_shit(message_lowered)}\nNew prefix: {prefix}')

    elif message_lowered == f'{prefix}off' and message.author.id == admins:
        await channel.send('Fuck you ig')
        print_message_main('Closing')
        quit()


client.run(os.getenv("ToePicDiscordToken"))