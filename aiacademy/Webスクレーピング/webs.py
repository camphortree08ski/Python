import urllib.request

imgname = "logo_courses_ai.png"
url = "https://aiacademy.jp/assets/images/" + imgname

urllib.request.urlretrieve(url, imgname)
print("done.")

from urllib.request import urlopen
html = urlopen("https://aiacademy.jp")
data = html.read()
decoded_data = data.decode('utf-8')
print(decoded_data)

import requests

res = requests.get("https://aiacademy.jp")
print(res)
print(res.text)
