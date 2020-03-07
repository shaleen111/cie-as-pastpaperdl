import requests
from bs4 import BeautifulSoup as bs
import pickle


BASE = "https://papers.xtremepape.rs/CAIE/AS%20and%20A%20Level/"

website = requests.get(BASE)
soup = bs(website.text, "html.parser")

syllabus_codes = []
links = []

categories = [link["href"] for link in soup.select("a.autoindex_a")]
pickle.dump(categories, open("syllabus_code.p", "wb"))
