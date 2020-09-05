import urllib3
from bs4 import BeautifulSoup as soup
http = urllib3.PoolManager()

import sys
reload(sys)
sys.setdefaultencoding('utf8')

url = "https://www.flipkart.com/search?q=iphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
resp = http.request('GET', url)
page_soup = soup(resp.data, "html.parser")
containers = page_soup.findAll("a", {"class":"_31qSD5"})

filename = "product.csv"
f = open(filename, "w")
headers = "Product Name, Pricing, Rating\n"
f.write(headers)

for container in containers:
	naming = container.find("div", {"class":"_3wU53n"})
	name = naming.text.replace(", ", "|")
	rate = container.find("span", {"class":"_2_KrJI"})
	rating = rate.text
	pricing = container.find("div", {"class":"_1vC4OE _2rQ-NK"})
	final_price = pricing.text.strip() 

	final_rating = str(rating.split(" "))
	fi_rating = final_rating.split("'")
	frating = fi_rating[1]

	f.write(str(name) + "," + str(final_price) + "," + str(frating) + "\n")

f.close()