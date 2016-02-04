#!/usr/bin/env python

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

if len(isbn) != 10 and len(isbn) != 13:
  print("ISBN values are 10 or 13 digits long")
  sys.exit()

if not isbn.isdigit():
  print("ISBN values contain only digits")
  sys.exit()

URL = "http://openlibrary.org/api/books?bibkeys=ISBN:{isbn}&format=json&jscmd=data"

r = requests.get(URL.format(isbn=isbn))
print(r.text)
