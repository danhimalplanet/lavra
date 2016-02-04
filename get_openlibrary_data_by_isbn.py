#!/usr/bin/env python

"""
get book info with ISBN via openlibrary api

Example usage:

 % ./get_openlibrary_data_by_isbn.py 1111111111
{"ISBN:1111111111": {"publishers": [{"name": "test publisher"}], "title": "test title", "url": "http://openlibrary.org/books/OL25760947M/test_title", "identifiers": {"openlibrary": ["OL25760947M"], "isbn_10": ["1111111111"]}, "publish_date": "2015", "key": "/books/OL25760947M", "authors": [{"url": "http://openlibrary.org/authors/OL650810A/abhishek_gaurav", "name": "abhishek gaurav"}]}}
"""

import requests
import sys

try:
  if len(sys.argv) == 2:
    isbn = sys.argv[1]
  else:
    print("Usage: %s ISBN" % str(sys.argv[0]))
    sys.exit()
except IndexError:
  print("Usage: %s ISBN" % str(sys.argv[0]))
  sys.exit()

isbn = sys.argv[1]

if not isbn.isdigit():
  print("ISBN values contain only digits")
  sys.exit()

if len(isbn) != 10 and len(isbn) != 13:
  print("ISBN values are 10 or 13 digits long")
  sys.exit()

URL = "https://openlibrary.org/api/books?bibkeys=ISBN:{isbn}&jscmd=data&format=json"

r = requests.get(URL.format(isbn=isbn))

if(r.status_code == 200):
  print(r.text)
else:
  print("Failed to properly contact API")
  sys.exit()
