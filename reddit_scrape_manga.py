from collections import defaultdict
from email import message
import requests
import bs4
import json
from discord import Webhook, RequestsWebhookAdapter
import datetime as dt
import time

# TODO: MAKE STRING PROCESSING FUNCTION SUPPORT MULTIPLE NUMBERS AND RANGES(EG.35-37) AND FLOATS


def extract_chap_num(txt):
    ls = [int(s) for s in txt.split() if s.isdigit()]
    if len(ls) == 1:
        return ls[0]
    else:
        return -1


def chap_from_text(s):
    return s.split('\n')[0]


def link_from_text(s):
    for w in s:
        try:
            return w['href']
        except:
            return "no link"


def make_message_string(md, s):
    message_string = f'New Chap of:{s}\nChap No.{str(md[s][1])}\nlink: {md[s][2]}'
    return message_string


def send_message_to_discord(s):
    webhook = Webhook.from_url(
        "https://discord.com/api/webhooks/989101925028999239/CYyD-5lLxIUxvxTetAOi5XeKSprFO3vX_hNAGuSGzHt4iJWMkSCwiBLdE5UHQ8By68Zi", adapter=RequestsWebhookAdapter())
    webhook.send(s)


i = 0

i += 1
headers = {'User-Agent': 'Mozilla/5.0'}
url = "https://www.reddit.com/r/manga/search?q=title%3A%5BDISC%5D&restrict_sr=on&sort=new&t=all&utm_source=reddit&utm_medium=usertext&utm_name=manga&utm_content=t5_2ql0i"
link_class = "_13svhQIUZqD9PVzFcLwOKT.styled-outbound-link.a6Bzb7gqvN3mqBOAEyFIv"
manga_class = "_eYtD2XCVieq6emjKBH3m"

def update_json(di):
    with open("manga_list.json", "w") as outfile:
        json.dump(di, outfile)
def update():
    message_list = []
    with open('manga_list.json') as json_file:
        my_manga_dict = json.load(json_file)
    my_manga_list = my_manga_dict.keys()

    res = requests.get(url, headers=headers)
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    new_manga = soup.select('._19FzInkloQSdrf0rh3Omen')
    for new in new_manga:
        for manga in my_manga_list:
            if manga in new.text and int(extract_chap_num(
                    chap_from_text(new.text))) > my_manga_dict[manga][1]:
                      
                      my_manga_dict[manga] = [str(dt.datetime.now()), int(extract_chap_num(
                    chap_from_text(new.text))),           
                link_from_text(new.select('._13svhQIUZqD9PVzFcLwOKT'))]
                      message_list.append(make_message_string(my_manga_dict, manga))
                      print(message_list)
                      print(manga)
                      update_json(my_manga_dict)
    if len(message_list) == 0:
        message_list = ["Sorry No New Updates"]
    return message_list




# time.sleep(300)
#update()
