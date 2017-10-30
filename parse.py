#!/usr/bin/env python3

import os
import sys
from bs4 import BeautifulSoup

cards_directory = 'www.ishtar-collective.net/cards/'
chapters = []

for filename in os.listdir(cards_directory):
    path = os.path.join(cards_directory, filename)
    with open(os.path.join(path)) as f:
        try:
            html = f.read()
            sys.stderr.write("Read " + path + "\n")
        except UnicodeDecodeError:
            # Poor man's text file detection
            sys.stderr.write(path + " is not a text file. Skipping!\n")
            pass

    soup = BeautifulSoup(html, 'html.parser')
    full_title = soup.find('h2', attrs={'class': 'card-title'}).text
    title, subtitle = full_title.split(':', 1)
    twitter_description = soup.find('meta', attrs={'name': 'twitter:description'})['content']
    verse_text = " ".join(twitter_description.split(" ")[0:2])
    verse_number = float(twitter_description.split(" ")[1].replace(':', '.'))
    text = soup.find('div', attrs={'class': 'description'}).text

    chapter = {
        'title': title,
        'subtitle': subtitle,
        'verse': verse_text,
        'text': text,
        'sort': verse_number
    }
    chapters.append(chapter)

chapters.sort(key=lambda c: c['sort'])

for chapter in chapters:
    print(chapter['title'].strip())
    print(chapter['subtitle'].strip())
    print(chapter['verse'].strip())
    print(chapter['text'].strip())
