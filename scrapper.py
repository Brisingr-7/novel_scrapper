from bs4 import BeautifulSoup
import requests

f = open("Renegade_Immortal_1.txt", "w",encoding='utf-8', errors='ignore')

next_url = "/renegade-immortal/chapter-2083-qualification-to-enter.html"
domain = "https://novelfull.com"


for pages in range(1,10):
    req = requests.get(domain + next_url)
    soup = BeautifulSoup(req.text, "html.parser")
    #print(soup)

    chapter = ""
    chap_title = soup.select("h2")[0]
    #chapter += chap_title + "\n\n"
    print (chap_title.text)
    f.write(chap_title.text + "\n\n\n\n\n")

    next_url = soup.find(id="next_chap")
    next_url = next_url['href']
    #print(next_url['href'])

    all_para = soup.find_all('p')
    para_count = (len(all_para))


    for i in range(2,para_count-1):
        chapter += all_para[i].text + "\n\n"
    #print(chapter)

    f.write(chapter)
    f.write("\n\n\n\n\n\n\n\n\n\n")

f.close()
