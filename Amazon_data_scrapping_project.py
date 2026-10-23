from bs4 import BeautifulSoup
import pandas as pd
import requests
import datetime
import time
import smtplib
import csv

def price_check():
    url = "https://www.amazon.com/realpeoplegoods-Data-Analyst-Gift-Scientist/dp/B093DPWBY6/ref=sr_1_1?crid=RPH3QMTYBGX0&dib=eyJ2IjoiMSJ9.hRpIkVP05twHHgf3t_BDoj5NpmvYrJkOk5ZViXlqONOD1aQwqgQm_0b0VehtCGFxYX2Nki7CJdoR1W6T9m3C5t3wdeBOsmW1mOiDKA8TOsW1lXingWjH6onOiDaQesJ0l1_niVdIHlViE2rAXQt4o0fl7X1GkS5jxLY_YUVnLJMQdgs6d0dzXPQF4TQ3d-MzaK55_0sX-BfeWdvgeFQfWlg2DAeZ0vlNP_Aynt6Oz-nriaFNql-RM9tOxA40bS88c3Muh6dQ2s_N4qBWHArP83T50PkuKtWJrgQd6Bj9UwY.CpmhDGAfwtdAGmr-SQ-TI1YS0M8phFUDS-PYQM2B3Gk&dib_tag=se&keywords=data%2Banalyst%2Btshirt&qid=1792593965&sprefix=%2Caps%2C360&sr=8-1"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
    }
    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    
    soup2 = BeautifulSoup(soup1.prettify(), 'html.parser')
    title = soup2.find(id="productTitle").get_text()
    price = soup2.find(class_="a-price-whole").get_text()
    
    title = title.strip()
    price = price.strip()
    price = price.rstrip(" .\n")
    price = price.replace(",", "")
    
    today = datetime.date.today()
    # header = ["Date", "Title", "Price"]
    data = [today, title, price]
    with open("Amazon_data_Srapping.csv", "a+", newline="", encoding="UTF8") as f:
        wr = csv.writer(f)
        # wr.writerow(header)
        wr.writerow(data)

while (True):
    price_check()
    time.sleep(5)