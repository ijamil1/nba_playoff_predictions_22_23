from bs4 import BeautifulSoup as bs4
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import csv

urls = ['https://www.nba.com/stats/teams/shooting-efficiency']
driver = webdriver.Chrome('/Users/irfanjamil/chromedriver/chromedriver')

for st in range(2013,2022):
    end = st+1-2000
    if end < 10:
        end = '0'+str(end)
    else:
        end = str(end)
    season_str = '?Season='+str(st)+'-'+end
    for url in urls:
        print(st, url, sep = ', ')
        driver.get(url+season_str)
        html = driver.page_source
        soup = bs4(html,"html.parser")
        #print(soup.prettify())
        try:
            tables = soup.find_all("table", class_="Crom_table__p1iZz")
        except:
            print(soup.prettify())
            raise Exception()
        table = tables[0]
        thead = table.thead
        cols = thead.find_all('th')
        titles = []
        header_idx = 0
        for col in cols:
            if header_idx == 0:
                header_idx += 1
                titles.append(col.string)
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
                    try:
                        span = td.span
                        values.append(span.contents[0])
                        idx+=1
                    except:
                        values.append(td.a.string)
                        idx+=1
                    continue    
                else:
                    s_val = td.string.replace(',','').replace('%','')
                    values.append(float(s_val))
            list_of_rows.append(values[:])
        with open(season_str[season_str.find('=')+1:]+'_' + url[url.rfind('/')+1:] + '.csv','w') as f:
            writer = csv.writer(f)
            writer.writerow(titles[:])
            writer.writerows(list_of_rows[:])


