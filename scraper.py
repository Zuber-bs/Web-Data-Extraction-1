from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd

# NASA Exoplanet URL
START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

# Webdriver
browser = webdriver.Edge(r"C:\Users\prana\Desktop\Python\PRO-C127-Student-Boilerplate-Code-main/msedgedriver.exe")
browser.get(START_URL)

time.sleep(10)

planets_data = []
current_page_num = 0

# Define Exoplanet Data Scrapping Method
def scrape():

    for i in range(1, 2):
        while True:
            time.sleep(2)
            soup = BeautifulSoup(browser.page_source, "html.parser")

            if current_page_num < i:
                browser.find_element(By.XPATH, value='//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
            elif current_page_num > i:
                browser.find_element(By.XPATH, value='//*[@id="primary_column"]/footer/div/div/div/nav/span[1]/a').click()
            else:
                break

            for table_tag in soup.find_all("table", attrs={"class", "wikitable sortable jquery-tablesorter"}):
                tr_tags = table_tag.find_all("tr")
                temp_list = []

                for index, td_tag in enumerate(tr_tags):
                    if index == 0:
                        temp_list.append(td_tag.find_all("td")[0].contents[0])
                    else:
                        try:
                            temp_list.append(td_tag.contents[0])
                        except:
                            temp_list.append("")
            
            print("11111111111111111111111111111111111111111111111111111111111111111111")
            print(temp_list)
            hyperlink_li_tag=td_tag[0]
            temp_list.append("https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"+ hyperlink_li_tag.find_all("a", href=True)[0]["href"])
            planets_data.append(temp_list)

            planets_data.append(temp_list)

            browser.find_element(by=By.XPATH, value='//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()


# Calling Method    
scrape()

# Define Header
headers = ["magnitude", "name", "designation", "class", "mass", "radius", "luminosity"]

# Define pandas DataFrame   
planet_df_1 = pd.DataFrame(planets_data, columns=headers)

# Convert to CSV
planet_df_1.to_csv("scrap_data.csv", index=True, index_label="id")
    


