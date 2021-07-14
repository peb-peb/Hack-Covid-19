import csv
import requests
from datetime import datetime

from bs4 import BeautifulSoup

# site from which data is being parsed
url = "https://www.worldometers.info/coronavirus/"
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")

# finding all countries data in today's table 
content = soup.find(id="main_table_countries_today").find_all("td")


def parse_site(content):
    data = {"date": 0, "countries": 0, "total_cases": 0, "new_cases": 0, "total_deaths": 0, "new_deaths": 0, "total_recovered": 0, "new_recovered": 0, "active_cases": 0, "total_tests": 0}
    data["date"] = datetime.today().strftime('%Y-%m-%d')

    for i in range(len(content)):
        result_text = content[i].text.strip()
        if result_text == "India":
            data["countries"] = "India"
            data["total_cases"] = content[i+1].text.strip()
            data["new_cases"] = content[i+2].text.strip()
            data["total_deaths"] = content[i+3].text.strip()
            data["new_deaths"] = content[i+4].text.strip()
            data["total_recovered"] = content[i+5].text.strip()
            data["new_recovered"] = content[i+6].text.strip()
            data["active_cases"] = content[i+7].text.strip()
            data["total_tests"] = content[i+11].text.strip()
    return data

def read_csv(data, fieldnames):
    with open("data.csv", 'r') as file:
        csv_file = csv.reader(file)
        for row in csv_file:
            if row[0] == datetime.today().strftime('%Y-%m-%d'): 
                return row
        write_csv(data, fieldnames)
    return ["", "", "", "", "", "", "", "", "", ""]

def write_csv(data, fieldnames):
    with open("data.csv", mode='a') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(data)

def get_today_data():
    fieldnames = ["date", "countries", "total_cases", "new_cases", "total_deaths", "new_deaths", "total_recovered", "new_recovered", "active_cases", "total_tests"]
    data = parse_site(content)

    try:
        info = read_csv(data, fieldnames)
    except:
        write_csv(data, fieldnames)
        info = read_csv(data, fieldnames)

    dict_data = [dict(zip(fieldnames, info))]
    return dict_data

if __name__ == "__main__":
    print(get_today_data()) 
