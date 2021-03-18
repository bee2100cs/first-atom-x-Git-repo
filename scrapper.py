from bs4 import BeautifulSoup
import requests
import pandas as pd

#use requests to make an HTTP GET request
r = requests.get('https://api.scrapingdog.com/linkedin/?api_key=604102c4f6cbfe5fda060333&type=company&linkId=google/about/').text
#use beautiful soup to parse the html
soup = BeautifulSoup(r, 'html.parser')
l = {}
u = list()

#extract title of company from the div class
try:
    l["Company"] = soup.find("hi", {"class": "org-top-card-summary__title t-24 t-black t-bold truncate"}).text.replace("\n", "")
except:
    l["Company"] = None
#use variable soup to extract all the properties since they are stored in same class
allProp = soup.find_all("dd", {"class": "org-page-details__definition-text t-14 t-black--light t-normal"})

#extract the properties from allProp list

try:
    l["website"] = allProp[0].text.replace("\n", "")
except:
    l["website"] = None
try:
    l["Industry"] = allProp[1].text.replace("\n", "")
except:
    l["Industry"] = None
try:
    l["Address"] = allProp[2].text.replace("\n", "")
except:
    l["Address"] = None
try:
    l["Type"] = allProp[3].text.replace("\n", "")
except:
    l["Type"] = None
try:
    l["Specialties"] = allProp[4].text.replace("\n", "")
except:
    l["Specialties"] = None

#next we'll scrap Company size
try:
    l["Company Size"] = soup.find("dd", {"class": "org-about-company-module__company-size-definition-text t-14 t-black--light mb1 fl"}).text.replace("\n", " ")
except:
    l["Company Size"] = None
#push dictionary l to list u and then create a dataframe of list u using pandas
u.append(l)
df = pd.json_normalize(u)
#save the data to a CSV file
df.to_csv('linkedin.csv', index=False, encoding='utf-8')
print(df)
