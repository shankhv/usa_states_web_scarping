import requests
from bs4 import BeautifulSoup
import csv

# URL of the Wikipedia page
url = "https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Find the table containing the states and territories data
state_details=[]
table = soup.find("table", {"class": "wikitable"})
for row in table.find_all("tr")[1:]:
    columns = row.find_all('td')
    if len(columns) > 6:
        text = row.text
        name = text.split("\n")
        name = name[1].replace("\xa0","")
        postal_abbreviations = columns[0].text.strip()
        capital = columns[1].text.strip()
        largest = columns[2].text.strip() if len(columns) == 8 else capital
        ratification_or_admission = columns[3].text.strip() if len(columns) == 8 else columns[2].text.strip()
        population = columns[4].text.strip() if len(columns) == 8 else columns[3].text.strip()
        mi = columns[5].text.strip() if len(columns) == 8 else columns[4].text.strip()
        km = columns[6].text.strip() if len(columns) == 8 else columns[5].text.strip()
        reps = columns[7].text.strip() if len(columns) == 8 else columns[6].text.strip()
        state_details.append([name,postal_abbreviations,capital,largest,ratification_or_admission,population,mi,km,reps])

csv_file = "usa_states.csv"
with open(csv_file, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['State Name','Postal Abbreviations' ,'Capital','Largest','Ratification Or Admission', 'Population','Total Area In Mi²','Total Area In Km²','Number Of Representatives'])  # Write header row
    writer.writerows(state_details)

print(f"Data has been written to {csv_file}")