from urllib import request
import xmltodict
#pip3 install xmltodict if not already installed


def botscout_check_username(name):
    """Query BotScout.com for usernames banned from forums"""

    api_key = "<YOUR_BOTSCOUT_API_KEY>"

    url = "https://botscout.com/test/?name=" + name + "&key=" + api_key + "&format=xml"

    file = request.urlopen(url)

    data = file.read()

    xmldict = xmltodict.parse(data)

    if xmldict['response']['matched'] == 'Y':
        print("{} is on the list with {} occurence(s)".format(name, xmldict['response']['count']))
    else:
        print("{} is not on the list".format(name))


def main():
    print("Check to see if a username is banned by BotScout.com\n")

    user_name = input("Enter a user name to check: ")

    botscout_check_username(user_name)


if __name__ == '__main__':
    main()
