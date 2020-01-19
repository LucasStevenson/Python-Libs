from requests import get
from bs4 import BeautifulSoup
import csv
import os.path
from os import path

url = "https://www.49ers.com/team/players-roster/"

response = get(url)
nfl = BeautifulSoup(response.content, 'html.parser')

nfl_main = nfl.find(id="main-content")

nfl_roster = nfl_main.find(summary="Roster")
# print(nfl_roster)
nfl_roster_body = nfl_roster.find('tbody')
# print(nfl_roster_body)

# print(nfl_roster_body.prettify())

rows = nfl_roster_body.find_all('tr')

# i dont want duplicate information
if path.exists("fourtyNiners.csv"):
    os.remove("fourtyNiners.csv")

for row in rows:
    col = row.find_all('td')[0].text
    col2 = row.find_all('td')[7].text

    print([col.strip(), col2.strip()])

    with open("fourtyNiners.csv", 'a') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([col.strip(), col2.strip()])
