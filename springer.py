#! /usr/bin/env python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import webbrowser
import urllib.request
import re
import pandas as pd
import os
import numpy
import argparse
import requests

formatos = []

def extract_books_links_and_download(url, name, folder, formatos):
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    response = opener.open(url)

    pag = response.read()
    soup = BeautifulSoup(pag, 'html.parser')
    
    print("Trying to download: " + name)
    for formato in formatos:
        try:
            attrs = attrs_for_format(formato)
            links = soup.find_all("a", attrs=attrs)
            linkRel = links[0].get('href')
            link = "https://link.springer.com" + linkRel
            print("Link for " + formato + " found: "+ link)
            saveLinkToFile("urls_for_download1.txt", link)
            bookName = createName(name, formato)
            path = os.path.join(folder, bookName)
            print("saving book to: " + path)
            urllib.request.urlretrieve(link, path)
        except:
            print("Not able to download " + formato + " version")


def attrs_for_format(format):
    if format == 'pdf':
        attrs = {'title': 'Download this book in PDF format'}  
    if format == 'epub':
        attrs = {'title': 'Download this book in EPUB format'}
    return attrs


def createName(name, formato):
    new_name = name.replace(":", "").replace("\\", "") + "." + formato
    return new_name


def saveLinkToFile(urls_file, link):
    with open(urls_file, "a") as urls_to_download:
        urls_to_download.write(link + "\n")


books_list = "Free+English+textbooks.xlsx"
print("Reading books list from "+ books_list)
print("Saving links extracted to urls_for_download1.txt")
df_books = pd.read_excel(books_list, index_col=0, headers=0)

books = df_books[['OpenURL','Book Title']]
parser = argparse.ArgumentParser()
parser.add_argument('-f', '--folder', help='folder to store the books')
parser.add_argument('-PDF', help='Download PDF format', action='store_true')
parser.add_argument('-EPUB', help='Download EPUB format', action='store_true')
args = parser.parse_args()

if not(args.PDF) and not(args.EPUB):
    formatos = ['pdf', 'epub']
if args.PDF:
    formatos.append('pdf')
if args.EPUB:
    formatos.append('epub')

if args.folder != None:
    carpeta = args.folder
else:
    carpeta = "Books"

print("Will download every book on format: "+ str(formatos))
print("Will save those at " + carpeta)

for urls, nombres in books.values:
    extract_books_links_and_download(urls, nombres, carpeta, formatos)
