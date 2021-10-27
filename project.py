from bs4 import BeautifulSoup
import requests
import pandas as pd
import time
import selenium
names = []
distance =[]
mass = []
radius =[]
star_url = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'
page = requests.get(star_url)
time.sleep(10)
soup = BeautifulSoup(page.text,'html.parser')
star_table = soup.find_all('table')
temp_list = []
table = star_table[7].find_all('tr')
for tr in table:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)
for i in range(1,len(temp_list)):
    names.append(temp_list[i][0])
    distance.append(temp_list[i][5])
    mass.append(temp_list[i][7])
    radius.append(temp_list[i][8])
df = pd.DataFrame(list(zip(names,distance,mass,radius,)),columns=['Name','Distance','Mass','Radius'])
df.to_csv('stars3.csv')
