from lxml import html
import requests

from bs4 import BeautifulSoup as bs
# Load the webpage content

with open('Courses_list.txt', 'r') as file:
    links = file.readlines()
links = [link.strip() for link in links]

def extract_data(url):
    response = requests.get(url)
    tree = html.fromstring(response.content)
    try:
        name = tree.xpath('/html/body/div[1]/div[2]/div/div/main/div[1]/div/div/div[3]/div/h1')[0].text.strip()
    except IndexError as e:
        name = "Null"
    try:
        category = tree.xpath('/html/body/div[1]/div[2]/div/div/main/div[1]/div/div/div[1]/div/a[2]')[0].text.strip()
    except IndexError as e:
        category = "Null"
    try:
        disc = tree.xpath('/html/body/div[1]/div[2]/div/div/main/div[1]/div/div/div[3]/div/div[1]')[0].text.strip()
    except IndexError as e:
        disc = "Null"
    try:
        rate = tree.xpath('/html/body/div[1]/div[2]/div/div/main/div[1]/div/div/div[3]/div/div[2]/div/a/span[1]/span[1]')[0].text.strip()
    except IndexError as e:
        rate = "Null"
    return [name, category, disc, rate]

def formated_message(url):
    name, catelogy, discription, rate = extract_data(url)
    message = f"""
    🎓 *{name}*

📂 *Category:* {catelogy}.
📖 *Description:* {discription}.
⭐ *Rating:* {rate} .
💲 *Price:* FREE!

    🔗 *Enroll Now:* {url}
    """

    return message

