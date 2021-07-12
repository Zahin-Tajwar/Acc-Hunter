import requests
import time
import colorama
from colorama import Fore
colorama.init()

print(Fore.YELLOW + r'''

|\  \|\  \|\  \|\  \|\   ___  \|\___   ___\\  ___ \ |\   __  \     
\ \  \\\  \ \  \\\  \ \  \\ \  \|___ \  \_\ \   __/|\ \  \|\  \    
 \ \   __  \ \  \\\  \ \  \\ \  \   \ \  \ \ \  \_|/_\ \   _  _\   
  \ \  \ \  \ \  \\\  \ \  \\ \  \   \ \  \ \ \  \_|\ \ \  \\  \|  
   \ \__\ \__\ \_______\ \__\\ \__\   \ \__\ \ \_______\ \__\\ _\  
    \|__|\|__|\|_______|\|__| \|__|    \|__|  \|_______|\|__|\|__|
    

''')

# INPUT USERNMAE
print(Fore.GREEN + '')
username = input('Enter username to search: ')

# INSTAGRAM
instagram = f'https://www.instagram.com/{username}'

# FACEBOOK
facebook = f'https://www.facebook.com/{username}'

#TWITTER
twitter = f'https://www.twitter.com/{username}'

# YOUTUBE
youtube = f'https://www.youtube.com/{username}'

# BLOGGER
blogger = f'https://{username}.blogspot.com'

# REDDIT
reddit = f'https://www.reddit.com/user/{username}'

# WORDPRESS
wordpress = f'https://{username}.wordpress.com'

# PINTEREST
pinterest = f'https://www.pinterest.com/{username}'

# GITHUB
github = f'https://www.github.com/{username}'

# TUMBLR
tumblr = f'https://{username}.tumblr.com'

# FLICKR
flickr = f'https://www.flickr.com/people/{username}'

# STEAM
steam = f'https://steamcommunity.com/id/{username}'

# VIMEO
vimeo = f'https://vimeo.com/{username}'

# SOUNDCLOUD
soundcloud = f'https://soundcloud.com/{username}'

# MEDIUM
medium = f'https://medium.com/@{username}'

# DEVIANTART
deviantart = f'https://{username}.deviantart.com'

# ABOUT.ME
aboutme = f'https://about.me/{username}'

# FLIPBOARD
flipboard = f'https://flipboard.com/@{username}'

# SPOTIFY
spotify = f'https://open.spotify.com/user/{username}'

# BADOO
badoo = f'https://www.badoo.com/en/{username}'

# PATREON
patreon = f'https://www.patreon.com/{username}'

# BITBUCKET
bitbucket = f'https://bitbucket.org/{username}'

# DAILYMOTION
dailymotion = f'https://www.dailymotion.com/{username}'

# ETSY
etsy = f'https://www.etsy.com/shop/{username}'

# BEHANCE
behance = f'https://www.behance.net/{username}'

# GOODREADS
goodreads = f'https://www.goodreads.com/{username}'

# INSTRUCTABLES
instructables = f'https://www.instructables.com/member/{username}'

# KONGREGATE
kongregate = f'https://kongregate.com/accounts/{username}'

# LIVEJOURNAL
livejournal = f'https://{username}.livejournal.com'

# ANGELLIST
angellist = f'https://angel.co/{username}'

# DRIBBBLE
dribbble = f'https://dribbble.com/{username}'

# CODECADEMY
codecademy = f'https://www.codecademy.com/{username}'

# PASTEBIN
pastebin = f'https://pastebin.com/u/{username}'

# ROBLOX
roblox = f'https://www.roblox.com/user.aspx?username={username}'

# NEWSGROUND
newsground = f'https://{username}.newgrounds.com'

# WATTPAD
wattpad = f'https://www.wattpad.com/user/{username}'

# CANVA
canva = f'https://www.canva.com/{username}'

# CREATIVEMARKET
creative_market = f'https://creativemarket.com/{username}'

# TRAKT
trakt = f'https://www.trakt.tv/users/{username}'

# 500PX
five_hundred_px = f'https://500px.com/{username}'

# BUZZFEED
buzzfeed = f'https://buzzfeed.com/{username}'

# TRIPADVISOR
tripadvisor = f'https://tripadvisor.com/members/{username}'

# HOUZZ
houzz = f'https://houzz.com/user/{username}'

#BLIP.FM
blipfm = f'https://blip.fm/{username}'

# WIKIPEDIA
wikipedia = f'https://www.wikipedia.org/wiki/User:{username}'

# HACKERNEWS
hackernews = f'https://news.ycombinator.com/user?id={username}'

# CODEMENTOR
codementor = f'https://www.codementor.io/{username}'

# REVERBNATION
reverb_nation = f'https://www.reverbnation.com/{username}'

# DESIGNSPIRATION
designspiration = f'https://www.designspiration.net/{username}'

#PayPal
paypal = f'https://www.paypal.com/paypalme/{username}'

# EBAY
ebay = f'https://www.ebay.com/usr/{username}'


# WEBSITE LIST - USED FOR SEARCHING OF USERNAME
WEBSITES = [
instagram, facebook, twitter, youtube, blogger, reddit, behance,
wordpress, pinterest, github, tumblr, flickr, steam, vimeo,
medium, deviantart, aboutme, flipboard, spotify, soundcloud,
badoo, patreon, bitbucket, dailymotion, etsy, canva, paypal,
goodreads, instructables, kongregate, livejournal, angellist,
dribbble, codecademy, pastebin, roblox, newsground, wattpad, ebay,
creative_market, trakt, five_hundred_px, buzzfeed, tripadvisor,
houzz, blipfm, wikipedia, hackernews, reverb_nation, designspiration
]


def write_urls_to_file(urls, output_file):
    with open(output_file, 'a') as fp:
        fp.write(urls + '\n')
        fp.close()

def search():
    print(Fore.GREEN + f'Searching for username:{username}.')
    time.sleep(0.5)
    print(Fore.GREEN + '.......')
    time.sleep(0.5)
    print(Fore.YELLOW + '.......\n')
    time.sleep(0.5)

    print(Fore.GREEN + f'Hunter v 1.00 is working.\n')
    time.sleep(0.5)
    print(Fore.YELLOW + '.......')
    time.sleep(0.5)
    print(Fore.GREEN + '.......\n')
    time.sleep(1.5)

    count = 0
    match = True
    for url in WEBSITES:
        try:
            r = requests.get(url)
        except requests.exceptions.ConnectionError:
            r.status_code = "Connection refused"

        if r.status_code == 200:
            if match == True:
                print(Fore.GREEN + 'FOUND MATCHES')
                match = False
            print(Fore.YELLOW + f'\n{url} - {r.status_code} - OK')
            if username in r.text:
                print(Fore.GREEN + f'POSITIVE MATCH: Username:{username} - text has been detected in url.')
                write_urls_to_file(url, "Positives.txt")
            else:
                print(Fore.RED + f'POSITIVE MATCH: Username:{username} - text has NOT been detected in url, could be a FALSE POSITIVE.')
                write_urls_to_file(url, "False_Positives.txt")
        count += 1

    print("\n")
    print(Fore.GREEN + f'FINISHED!!')



if __name__=='__main__':
    search()

input("")
