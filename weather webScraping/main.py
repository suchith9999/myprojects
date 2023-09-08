import requests
from bs4 import BeautifulSoup as bs

query = input("please input your location:")
url = f'https://www.google.com/search?q=weather+now+in+{query}'
link = requests.get(url, headers={
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"})
soup = bs(link.content, 'html.parser')
temp = soup.find('div', class_="vk_bk TylWce SGNhVe")
unit = soup.find('div', class_="vk_bk wob-unit")
desc = soup.find('div', class_="wob_dcp").text


def run():
    ap = []
    for i in temp:
        t = i.text
        ap.append(t)
        break
    for un in unit:
        u = un.text
        ap.append(u)
        # print(ap)
        print(t, u, 'in', query, 'with', desc)
        break


run()
