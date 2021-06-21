from bs4 import BeautifulSoup as bs
from colorama import Fore
import urllib.request, json

print(f'{Fore.RED}\tSub Imports Initlized {Fore.WHITE}')
class webscraper():
    def __init__(self):
        pass

    def scraper():
        print(f'{Fore.RED}\tRequesting url\n\tConverting Json to Python{Fore.WHITE}')
        return json.loads(str(bs(urllib.request.urlopen('https://www.gamerpower.com/api/giveaways?platform=pc'), 'html.parser')).replace('</a>', ''))
        
