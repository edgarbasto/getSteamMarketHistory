import os
import pandas as pd
from bs4 import BeautifulSoup


def readHtmls():
    htmls = []
    for file in os.listdir("htmls"):
        if file.endswith(".html"):
            htmls.append(file)

    item_name_list = []
    price_list = []
    data = {}

    for file in htmls:
        with open('htmls/'+file, 'r', encoding='utf8') as f:

            html = f.read()
            soup = BeautifulSoup(html, 'html.parser')
            f.close()

            steamList = soup.find(id="tabContentsMyMarketHistoryRows")
            items = steamList.find_all("div", class_="market_listing_row market_recent_listing_row")

            for item in items:
                name = item.find("span", class_="market_listing_item_name economy_item_hoverable")
                value = item.find("span", class_="market_listing_price")

                # Ignore order placement announcements
                if name == None or str(name)[148:-7:].strip() == "":
                    continue

                item_name_list.append(str(name)[148:-7:])
                price_list.append(str(value)[44:-14:])
                # print(f"{str(name)[148:-7:]} - {str(value)[44:-14:]}")

    data = {'Item Name': item_name_list, 'Price': price_list}
    if len(item_name_list) == len(price_list):
        return data
    else:
        # raise ValueError('Item and Price lists have different size. Check your output to match accordingly.')
        print('Item and Price lists have different size. Check your output to match accordingly.')
        return data


def createDf():
    data = readHtmls()
    df = pd.DataFrame(data)
    df.to_excel("output.xlsx")

createDf()



