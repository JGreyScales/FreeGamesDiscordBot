import discord, os
from colorama import Fore
from web_scraper.discordwebscraper import webscraper

def print_message_main(str):
    print(Fore.GREEN + str + Fore.WHITE)

print_message_main('Main Imports initlized')

prefix = '$$'
client = discord.Client()

companys = {
    'steam': 'Steam',
    'itch': 'Itch.io',
    'pc': 'PC',
    'epic': 'Epic Games Store',
    'drm': 'DRM-Free', 
    'battlenet': 'Battle.net',
    'gog': 'GOG',
}

@client.event
async def on_ready():
    print_message_main("Signed into: {0.user}".format(client))

@client.event
async def on_message(message):
    message_lowered = message.content.lower()
    if message.author == client.user:
        return

    channel = client.get_channel(message.channel.id)

    if message_lowered == f'{prefix}help':
        help_embed = discord.Embed(name="Help:", color=discord.Color(7863510))
        help_embed.set_author(name="2 GreyScales#4533", url="https://github.com/JGreyScales", icon_url="https://cdn.discordapp.com/avatars/554486518543155212/6de70ebdb8796cc55cc9e8397b0985a4.png?size=4096")
        help_embed.add_field(name='Help:', value=f'{prefix}help', inline=False)
        help_embed.add_field(name='Free:', value=f'{prefix}free products\n{prefix}free games\n{prefix}free steam\n{prefix}free itch\n' +
        f'{prefix}free pc\n{prefix}free epic\n{prefix}free drm\n{prefix}free battlenet\n{prefix}free gog')

        await channel.send(embed=help_embed)

    elif message_lowered == f'{prefix}free products':
        embed = discord.Embed(title="Free Games:", color=discord.Color(3038))

        for game in webscraper.scraper():
            embed.add_field(name=game['title'], value=f"Game was: {game['worth']} now is: FREE\n Game link:{game['open_giveaway_url']}" +
            f"\n{game['description']}\n\n", inline=True)

            if len(embed) >= 5500:
                await channel.send(embed=embed)
                embed = discord.Embed(title="Free Steam Games:", colour=discord.Colour(0x3e038c))
        
        await channel.send(embed=embed)

    elif message_lowered == f'{prefix}free games':
        embed = discord.Embed(title="Free Games:", color=discord.Color(0x3e038c))

        for game in webscraper.scraper():
            if game['type'] == 'Full Game':
                embed.add_field(name=game['title'], value=f"Game was: {game['worth']} now is: FREE\n Game link:{game['open_giveaway_url']}" +
                f"\n{game['description']}\n\n", inline=False)
                
                if len(embed) >= 5500:
                    await channel.send(embed=embed)
                    embed = discord.Embed(title="Free Steam Games:", colour=discord.Colour(0x3e038c))
                
        await channel.send(embed=embed)

    elif message_lowered[7:] in companys:

        message_lowered = companys[message_lowered[7:]]
        embed = discord.Embed(title=f"Free {message_lowered} Games:", colour=discord.Colour(0x3e038c))

        for game in webscraper.scraper():

            if game['type'] == 'Full Game' and message_lowered in game['platforms']:
                embed.add_field(name=game['title'], value=f"Game was: {game['worth']} now is: FREE\n Game link:{game['open_giveaway_url']}" +
                f"\n{game['description']}\n\n", inline=False)

            if len(embed) >= 5500:
                await channel.send(embed=embed)
                embed = discord.Embed(title=f"Free {message_lowered} Games:", colour=discord.Colour(0x3e038c))
                
        await channel.send(embed=embed)

client.run(os.getenv("ToePicDiscordToken"))
