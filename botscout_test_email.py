from urllib import request
import xmltodict
#pip3 install xmltodict if not already installed


def botscout_check_email(email):
    """Query BotScout.com for email addresses banned from forums"""

    api_key = "<YOUR_BOTSCOUT_API_KEY>"

    url = "https://botscout.com/test/?mail=" + email + "&key=" + api_key + "&format=xml"

    file = request.urlopen(url)

    data = file.read()

    xmldict = xmltodict.parse(data)

    if xmldict['response']['matched'] == 'Y':
        print("{} is on the list with {} occurence(s)".format(email, xmldict['response']['count']))
    else:
        print("{} is not on the list".format(email))


def main():
    print("Check to see if a email address is banned by BotScout.com\n")

    email_address = input("Enter an email address to check: ")

    botscout_check_email(email_address)


if __name__ == '__main__':
    main()
