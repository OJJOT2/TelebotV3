import requests, csv
from bs4 import BeautifulSoup
from urllib3.filepost import writer

head = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36 Edg/89.0.774.77",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",}
# URL of the webpage you want to scrape

# Send a GET request to the webpage
def external_page_scrap(max_pages, url2):
    courses=[]
    courses2=[]
    for page in range(max_pages):
        # url = "https://www.discudemy.com/all/" + str(page+1)
        url = url2 + str(page+1)
        r = requests.get(url, headers=head)
        print(url)
        soup = BeautifulSoup(r.content, "html.parser")
        courses_got = soup.find_all("section", "card")
        print(f"Page {page+1} Done with {len(courses_got)} courses got")
        for cc in courses_got:
            courses.append(cc)

    for link in range(len(courses)):
        try:
            c_link = courses[link].find('a', class_="card-header").get("href")
            c_link = c_link.replace(str('/' + c_link.split("/")[3] + '/'), "/go/")
            print(c_link)
            courses2.append(c_link)
        except AttributeError as x:
            print(f"error;{x}")
    print(f"all courses = {len(courses2)}")
    return courses2

def internal_page_scrap(link):
    main1 = requests.get(link, headers=head)
    main2 = BeautifulSoup(main1.content, "html.parser")
    Course_link = main2.find("div", class_="ui segment").a["href"]
    return Course_link


def udemy_links(url2):
    udemy_links = []
    courses_list = external_page_scrap(5, url2)
    print(courses_list)
    print("One step left")
    vv = 0
    with open('Courses_list.txt', 'w') as file:
        file.write('')
    for x in courses_list:
        udemy_links.append(internal_page_scrap(x))
        with open("Courses_list.txt", "a") as file:
            file.writelines(udemy_links[-1])
            file.write("\n")
            file.close()
        vv +=1
        print(f"Process: {vv}/{len(courses_list)}.")
    print(udemy_links)
    print(f"Done with {len(udemy_links)} coueses")
#Remaining: make a code to