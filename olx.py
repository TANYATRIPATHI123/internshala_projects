import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.olx.in/items/q-car-cover"

headers = {
    "User-Agent": "Mozilla/5.0"
}

def get_data(page_url):
    print("Getting data from:", page_url)
    try:
        r = requests.get(page_url, headers=headers)
        return r.text
    except:
        print("Something went wrong while requesting the page.")
        return ""

def parse_html(html):
    soup = BeautifulSoup(html, "html.parser")
    all_items = []

    items = soup.find_all("li", class_="EIR5N")
    
    for i in items:
        try:
            title = i.find("span", class_="_2tW1I").text.strip()
        except:
            title = "No title"
        
        try:
            price = i.find("span", class_="_89yzn").text.strip()
        except:
            price = "No price"
        
        try:
            location = i.select_one("span._2tW1I + span").text.strip()
        except:
            location = "No location"
        
        d = {
            "Title": title,
            "Price": price,
            "Location": location
        }

        all_items.append(d)

    return all_items

def save_to_file(data):
    filename = "olx_results.csv"
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["Title", "Price", "Location"])
        writer.writeheader()
        for d in data:
            writer.writerow(d)
    print("Saved results to", filename)

def main():
    html_content = get_data(url)
    if html_content:
        listings = parse_html(html_content)
        save_to_file(listings)
    else:
        print("Failed to get listings.")

main()
