import requests
from bs4 import BeautifulSoup
import time
import datetime
import csv
import pandas as pd 

def check_price():
    url = "https://www.flipkart.com/nike-court-vision-mid-nn-high-tops-men/p/itm0623ad13c4e8e?pid=SHOG982JUBRGGAFF&lid=LSTSHOG982JUBRGGAFF2SCCFK&marketplace=FLIPKART&q=nike+court+vision&store=osp%2Fcil%2Fe1f&srno=s_1_4&otracker=AS_QueryStore_OrganicAutoSuggest_1_10_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_1_10_na_na_ps&fm=search-autosuggest&iid=369192e2-836b-4e3b-a367-e3d711d823c0.SHOG982JUBRGGAFF.SEARCH&ppt=sp&ppn=sp&ssid=8lo4n2gitc0000001677246223605&qH=bad2ad7bc930e40d"
    head = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36", 
    "X-Amzn-Trace-Id": "Root=1-63f8b679-755ac8462c2179c764b554f1"}
    page = requests.get(url, headers = head)
    first = BeautifulSoup(page.content, "html.parser")
    second = BeautifulSoup(first.prettify(), "html.parser")
    Product = second.find("span",attrs = {"class":"B_NuCI"}).getText()
    Price = second.find("div",attrs = {"class":"_30jeq3 _16Jk6d"}).getText()

    Price = Price.strip()[1:]
    Product = Product.strip()

    Today = datetime.date.today()

    heading = ['Product','Price','Date']
    scraped_data = [Product, Price, Today]
    with open("FLipkartWebScraperDataset.csv", 'w', newline="", encoding = 'UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(heading)
        writer.writerow(scraped_data)

    with open("FLipkartWebScraperDataset.csv", 'a+', newline="", encoding = 'UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(scraped_data)

    data = pd.read_csv(r'C:\Users\Sudhanshu\web scrapping\FLipkartWebScraperDataset.csv')
    print(data)


while (True):
    check_price()
    time.sleep(86400)

    

    