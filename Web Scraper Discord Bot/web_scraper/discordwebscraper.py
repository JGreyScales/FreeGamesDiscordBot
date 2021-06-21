from bs4 import BeautifulSoup as bs
from colorama import Fore

import urllib.request, json

class webscraper():
    def __init__(self):
        print(f'{Fore.BLUE}\tSub Imports Initlized {Fore.WHITE}')

    def scraper():

        htmlParse = str(bs(urllib.request.urlopen('https://www.gamerpower.com/api/giveaways?platform=pc'), 'html.parser')).replace('</a>', '')
        return json.loads(htmlParse)