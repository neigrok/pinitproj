import requests
import re
import random

re_title = re.compile(r'<title>\n?(.*)\n?<.title>', flags=re.I | re.MULTILINE | re.DOTALL)
re_p = re.compile(r'<p>(.*)<.p>', flags=re.I | re.MULTILINE | re.DOTALL)
re_cleaner = re.compile('<.*?>')

def collectinfo(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1)\
                    AppleWebKit/537.36 (KHTML, like Gecko)\
                     Chrome/39.0.2171.95 Safari/537.36'}
    try:
        page = requests.get(url, headers=headers).text
    except Exception as e:
        #need solution
        print(e)
        return url, 'Error'

    #extract title
    title_group = re.search(re_title, page)
    try:
        title = title_group.group()[7: -8]
    except AttributeError:
        title = url[7:]

    #extract first paragraph
    paragraph_group = re.search(re_p, page)
    if paragraph_group:
        paragraph = paragraph_group.group()[3: -4]
    else:
        #blank then
        paragraph = ""
    return title, cleantags(paragraph)[:150].replace('\n', '')


#clean all html tags from a string
def cleantags(text):
    return re.sub(re_cleaner, '', text)


#get random char sequence
def random_chars(length=8):
    chars = 'abcdefghijklmnopqrstuvwxyz1234567890'
    line = ''
    for _ in range(length):
        line += random.choice(chars)
    return line