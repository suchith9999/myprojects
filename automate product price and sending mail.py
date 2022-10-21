from bs4 import BeautifulSoup
import requests
import time
import smtplib
url = 'https://www.amazon.in/dp/B07CVMR1TJ/ref=cm_sw_r_apa_i_NXJ3B3W6XB8AG82AAS3C_1'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}

# def check_price():
page = requests.get(url, headers=headers)

print(page)

soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find('span',class_="a-size-large product-title-word-break").get_text()

price = soup.find('span',class_="a-price-whole").get_text()
print(title)
print(price)
details = (title, price)
details
# def send_mail():
import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('suchith.nanded01@gmail.com', 'rnnslemdrckpovsg')
subject = 'check the price'
body = f"{details}'check the link https://www.amazon.in/dp/B07CVMR1TJ/ref=cm_sw_r_apa_i_NXJ3B3W6XB8AG82AAS3C_1'"
msg = f"subject: {subject}\n\n{body}"
server.sendmail('suchth.nanded01@gmail.com', 'suchith.nanded@gmail.com', msg)
print("hey email has been sent")
server.quit()


