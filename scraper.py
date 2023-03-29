from bs4 import BeautifulSoup as bs4
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import csv

urls = ['https://www.nba.com/stats/teams/traditional','https://www.nba.com/stats/teams/advanced','https://www.nba.com/stats/teams/opponent','https://www.nba.com/stats/teams/defense']
driver = webdriver.Chrome('/Users/irfanjamil/chromedriver/chromedriver')
for url in urls:
    driver.get(url)
    html = driver.page_source
    soup = bs4(html,"html.parser")
    tables = soup.find_all("table", class_="Crom_table__p1iZz")
    for table in tables:
        thead = table.thead
        cols = thead.find_all('th')
        titles = []
        header_idx = 0
        for col in cols:
            if header_idx == 0:
                header_idx += 1
                continue
            if col.has_attr('hidden'):
                break
            title = col.contents[0]
            titles.append(title)
        list_of_rows = []
        body = table.tbody
        rows = body.find_all('tr')
        for row in rows:
            idx = 0
            tds = row.find_all('td')
            values = []
            for td in tds:
                if idx == 0:
                    idx+=1
                    continue
                elif idx == 1:
                    print(td.prettify())
                    span = td.span
                    values.append(span.contents[0])
                    idx+=1
                    continue
                    
                else:
                    values.append(float(td.string))
            list_of_rows.append(values[:])
        with open('test.csv','w') as f:
            writer = csv.writer(f)
            writer.writerow(titles)
            writer.writerows(list_of_rows)
    break


