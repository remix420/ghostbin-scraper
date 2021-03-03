import requests
from RandomWordGenerator import RandomWord
import bs4
import random
from colorama import Fore, Back, Style
from colorama import init
import string

init()


def make_url():
    global url, random_string
    length_of_string = random.randint(4,5)

    letters_and_digits = string.ascii_lowercase + string.digits
    random_string = ""

    for number in range(length_of_string):
        random_string += random.choice(letters_and_digits)
    url = 'https://ghostbin.co/paste/{}'.format(random_string)

while True:
    make_url()
    r = requests.get(url)
    html = bs4.BeautifulSoup(r.text)
    if r.status_code == 404:
        print('[{}BAD{}] {}'.format(Fore.RED, Style.RESET_ALL, url))
    if r.status_code == 200:
        print('[{}GOOD{}] {} '.format(Fore.GREEN, Style.RESET_ALL, url, html.title.text))

