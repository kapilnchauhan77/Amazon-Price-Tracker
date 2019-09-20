import requests
from bs4 import BeautifulSoup
import smtplib
import time

def get_price(URL, headers):

	page = requests.get(URL, headers = headers)

	soup = BeautifulSoup(page.content, 'html.parser')

	title = soup.find(id = 'title_feature_div').get_text().strip()

	price = soup.find(id = 'priceblock_ourprice').get_text()
	price = float(price[2:len(price)].replace(',',''))

	print(title)
	print(price)

	if price < 9000:
		send_mail()
	else:
		pass


def send_mail():

	server = smtplib.SMTP('smtp.gmail.com', 587)

	server.ehlo()
	server.starttls()
	server.ehlo()

	server.login('einstein435@gmail.com', 'vkienybodpexzpew')

	subject = 'Price fell down!!!'
	body = ('Go to this link - https://www.amazon.in/Samsung-2-5-inch-Internal-SATA-MZ-76Q1T0BW/dp/B07KSHCG3R/ref=sr_1_2?keywords=ssd+1tb&qid=1567943398&s=luggage&sr=8-2')
	msg = f"Subject: {subject}\n\n{body}"
	msg = str(msg)
	print(msg)

	server.sendmail('einstein435@gmail.com', 'kapilnchauhan77@gmail.com', msg)

	print('Email sent!!!')

	server.quit()

URL = 'https://www.amazon.in/Samsung-2-5-inch-Internal-SATA-MZ-76Q1T0BW/dp/B07KSHCG3R/ref=sr_1_2?keywords=ssd+1tb&qid=1567943398&s=luggage&sr=8-2'
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}

while 1:
	get_price(URL, headers)
	time.sleep(60)