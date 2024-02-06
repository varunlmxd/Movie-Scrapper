import requests
from bs4 import BeautifulSoup as bs
import re

link = "https://www.boxofficemojo.com/search/?q="
search = input("Enter movie name: ")
link = link+search
url = requests.get(link)
soup = bs(url.text)
elements = soup.find_all("div",class_="a-section mojo-body aok-relative")
for element in elements:
    if element:
        a = element.find("div",class_="a-section mojo-gutter")
        if a:
            b = element.find("div",class_="a-section a-spacing-medium a-spacing-top-medium")
            if b:
                c =  element.find_all("div",class_="a-fixed-left-grid")
                
                if c:
                    d =  element.find_all("div",class_="a-fixed-left-grid-inner")
                    
                    if d:
                        e =  element.find_all("div",class_="a-fixed-left-grid-col a-col-right")
                        if e:
                            for f in e :
                                s = str(f)
                                res = [i.start() for i in re.finditer("<br/>", s)]
                                try: 
                                    genre = s[res[0]+5:res[1]]
                                except:
                                    genre = "Not-Available"
                                name = f.find("a",class_="a-size-medium a-link-normal a-text-bold")
                                year_cast = f.find_all("span",class_="a-color-secondary")
                                print("Name:",name.text.strip(),year_cast[0].text.strip())
                                print("Genre:",genre.strip())
                                print("Cast:",year_cast[1].text.strip())
                                print()
