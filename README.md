# Springer_books

Script to download [ALL] the Springer Free Books at once (Covid-19 edition :P )
Supports selecting format, setting the destination folder and verifies for already downloaded books (based on name not on edition be carful there).
There are more complex versions online who let you select specific books (by name, topic, etc).
This was an experiment (a one day thing) and a little entertainment (not intended to be super, just to let me download all the books at once).
Based on the columns from the xlsx would be pretty easy to add several filters in order to download with specific chriteria,
if someone wants to play with it and collaborate, feel free.

Requirements:
- python 3
- modules: BeautifulSoup, pandas, numpy, argparse

Usage:
- '-f', '--folder' -> Folder to store the books.
- '-PDF' -> Download PDF format.
- '-EPUB' -> Download EPUB format.
