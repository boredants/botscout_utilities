import requests
from bs4 import BeautifulSoup as bs
import re
import sys


def botscout_latest():
    """ Scrape the IP addresses of the latest 100 bot hosts from botscout.com 
        and write the results to a text file.
    """

    url = 'https://botscout.com/last.htm'

    try:
        r = requests.get(url)
    except Exception:
        print("The URL " + url + " is not reachable.")
        sys.exit()

    soup = bs(r.content, features='lxml')

    b = []
    for link in soup.find_all('a'):
        b.append(link.string)

    with open('botscout.txt', 'w') as f:

        for c in b:
            if re.match(r'\d+', str(c)):
                print(c, file=f)


def main():
    print("\nRetrieving the BotScout Latest 100 IP Addresses\n")

    botscout_latest()


if __name__ == '__main__':
    main()
