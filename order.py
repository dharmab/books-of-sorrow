#!/usr/bin/env python3

import os
import sys
from bs4 import BeautifulSoup

cards_directory = 'www.ishtar-collective.net/cards/'
cards_html = []

for filename in os.listdir(cards_directory):
    path = os.path.join(cards_directory, filename)
    with open(os.path.join(path)) as f:
        try:
            html = f.read()
            cards_html.append(html)
            sys.stderr.write("Read " + path + "\n")
        except UnicodeDecodeError:
            # Poor man's text file detection
            sys.stderr.write(path + "is not a text file. Skipping!\n")
            pass

for html in cards_html:
    soup = BeautifulSoup(html, 'html.parser')
    # import pdb; pdb.set_trace()
    title = soup.title.text.split('\u2014')[0]  # split on em-dash
    text = soup.find(attrs={"name": "twitter:description"})['content']

    print(title)
    print()
    print(text)
    print()
    print()