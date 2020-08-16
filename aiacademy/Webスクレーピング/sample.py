from bs4 import BeautifulSoup
from urllib.request import urlopen
html = urlopen("https://aiacademy.jp/assets/scraping/sample3.html")
data = html.read()
html = data.decode('utf-8')

soup = BeautifulSoup(html, 'html.parser')

h1 = soup.select_one("div#main > h1").string

li_list = soup.select("div#main > ul.items > li")
for i,li in enumerate(li_list):
    print(",".join([str(i),li.string]))
