from urllib import request
import xmltodict
#pip3 install xmltodict if not already installed


def botscout_check_ip(address):
    """Query BotScout.com for IP addresses banned from forums"""

    api_key = "<YOUR_BOTSCOUT_API_KEY>"

    url = "https://botscout.com/test/?ip=" + address + "&key=" + api_key + "&format=xml"

    file = request.urlopen(url)

    data = file.read()

    xmldict = xmltodict.parse(data)

    if xmldict['response']['matched'] == 'Y':
        print("{} is on the list with {} occurence(s)".format(address, xmldict['response']['count']))
    else:
        print("{} is not on the list".format(address))


def main():
    print("Check to see if an IP address is banned by BotScout.com\n")

    ip_address = input("Enter an IP Address to check: ")

    botscout_check_ip(ip_address)


if __name__ == '__main__':
    main()
