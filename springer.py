#! /usr/bin/env python
# -*- coding: utf-8 -*-
import webbrowser
import datetime
import time
from bs4 import BeautifulSoup
import webbrowser
import urllib.request
import os
import re

string0 = "https://link.springer.com/book/10.1007%2F978-1-4939-9621-6"

def extract_books_links_and_download(url):
    pdf_not_found = True
    epub_not_found = True
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    response = opener.open(url)

    pag = response.read()
    soup = BeautifulSoup(pag, 'html.parser')
    allA = soup.find_all("a", attrs={'title': re.compile("Download this book in.")})
    for urls in allA:
        linkRel = urls.get('href')
        if ".pdf" in linkRel:
            pdf_not_found = False
            link = "https://link.springer.com" + linkRel
            print("PDF link found: "+ link)
            with open("urls_for_download.txt", "a") as urls_to_download:
                urls_to_download.write(link + "\n")
            bookName = linkRel.replace("/", "_")
            print("saving book to Books/" + bookName)
            urllib.request.urlretrieve(link, 'Books/'+ bookName)
            break
    for urls in allA:
        linkRel = urls.get('href')
        if ".epub" in linkRel:
            link = "https://link.springer.com" + linkRel
            print("ePub link found: " + link)
            with open("urls_for_download.txt", "a") as urls_to_download:
                urls_to_download.write(link + "\n")
            bookName = linkRel.replace("/", "_")
            print("Saving book to Books/" + bookName)
            urllib.request.urlretrieve(link, 'Books/' + bookName)
            break


with open("links_originales.txt", "r") as links:
    bookNumber = 1
    link = links.readline()
    while link:
        print("Book number: " + str(bookNumber))
        extract_books_links_and_download(link)
        print("Downloaded book number: " + str(bookNumber))
        bookNumber += 1
        link = links.readline()
