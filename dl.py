import pickle
import re
from bs4 import BeautifulSoup as bs
import requests
import os

BASE = "https://papers.xtremepape.rs/CAIE/AS%20and%20A%20Level/"
CODE = "9702"


def main():
    codes = pickle.load(open("syllabus_code.p", "rb"))
    for i in codes:
        if re.search(f".*\({CODE}\)\/", i):
            SUB = i
    URL = f"{BASE}{SUB}".replace(" ", "%20")
    site = bs(requests.get(URL).text, "html.parser")
    urls = {}
    print(URL)
    for link in site.select("a.autoindex_a"):
        href = link.get("href")
        if(href.endswith("pdf")):
            urls[href] = URL + href

    for key, value in urls.items():
        res = requests.get(value)

        if(not os.path.isdir("pdfs")):
            os.mkdir("pdfs")

        if(not os.path.isdir(f"pdfs/{CODE}")):
            os.mkdir(f"pdfs/{CODE}")

        with open(f"pdfs/{CODE}/{key}", 'wb') as pdf:
            print(f"Downloading {key}")
            pdf.write(res.content)
            print(f"Done with {key}")


if __name__ == "__main__":
    main()
