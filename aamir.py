import os
import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.indiaglitz.com/aamir-khan-photos-hindi-actor-2628990-7950")
soup = BeautifulSoup(r.text,"html.parser")
links = []
x = soup.select('img[src^="https://1847884116.rsc.cdn77.org/hindi/gallery/actor/aamirkhan/"]')
for img in x:
    links.append(img['src'])
for l in links:
    print(l)
os.mkdir("aamir_khan")
for index,img_link in enumerate(links):
    img_data=requests.get(img_link).content
    open("aamir_khan/"+str(index+1)+".jpg","wb").write(img_data)
