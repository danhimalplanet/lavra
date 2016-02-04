import json
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
URL = "http://openlibrary.org/api/books?bibkeys=ISBN:{isbn}&format=json&jscmd=data"

r = requests.get(URL.format(isbn=isbn))
print(r.text)
