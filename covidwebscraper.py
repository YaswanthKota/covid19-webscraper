import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import pandas as pd
url="https://www.mohfw.gov.in/"
web=requests.get(url).content
soup=BeautifulSoup(web,"html.parser")
stats=[]
rows=soup.find_all('tr')
for row in rows:
    stat=row.find_all('td')
    if len(stats)<=29:
        stats.append(stat)
new_cols = ["Sr.No", "States/UT","Confirmed","Recovered","Deceased"]
state_data = pd.DataFrame(data = stats, columns = new_cols)
state_data.head()
print(state_data)