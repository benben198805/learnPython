from urllib import request
import json
import pydash
from pydash import *
from bs4 import BeautifulSoup
import re

paths = [{
        'path':'/wordlist/7519/61237/',
        'page':10
    },
    {
        'path':'/wordlist/7519/61246/',
        'page':10
    },
    {
        'path':'/wordlist/7519/61264/',
        'page':10
    },
    {
        'path':'/wordlist/7519/61267/',
        'page':10
    },
    {
        'path':'/wordlist/7519/61276/',
        'page':10
    },
    {
        'path':'/wordlist/7519/61288/',
        'page':10
    },
    {
        'path':'/wordlist/7519/61378/',
        'page':10
    },
    {
        'path':'/wordlist/7519/61387/',
        'page':10
    },
    {
        'path':'/wordlist/7519/61393/',
        'page':10
    },
    {
        'path':'/wordlist/7519/61414/',
        'page':10
    },
    {
        'path':'/wordlist/7519/61585/',
        'page':10
    },
    {
        'path':'/wordlist/7519/61591/',
        'page':10
    },
    {
        'path':'/wordlist/7519/61597/',
        'page':10
    },
    {
        'path':'/wordlist/7519/61618/',
        'page':10
    },
    {
        'path':'/wordlist/7519/61621/',
        'page':10
    },
    {
        'path':'/wordlist/7519/61636/',
        'page':8
    }
];

allWords = []

domain = 'https://www.shanbay.com/'

for path in paths:
    pageIndex = 1
    while pageIndex <= path['page']:
        url = domain + path['path'] + '?page=' + str(pageIndex)
        req = request.Request(url)
        pageIndex = pageIndex + 1
        req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
        with request.urlopen(req) as f:
            response = f.read()
            print('--------%s:%d----'%(path['path'],pageIndex-1))
            soup = BeautifulSoup(str(response,'utf-8'), 'html.parser')
            number = soup.find_all(id="wordlist-num-vocab")[0].contents[0]

            for td in soup.find_all(class_=re.compile("span2")):
                if td.strong:
                   allWords.append(td.strong.contents[0])

wordStr = ''
for word in allWords:
    wordStr = wordStr + word +'\n';

with open('word.txt', 'w') as file:
    file.write(wordStr)

                