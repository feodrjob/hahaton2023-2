import requests
from bs4 import BeautifulSoup
def array():
    headers = {"User-Agent":
                  "Mozilla/5.0 (<system-information>) <platform> (<platform-details>) <extensions>"}

    url = "https://hakaton.helllab.ru/"


    response = requests.get(url) #Доступ к сайту GET значение АТРИБУТА

    soup = BeautifulSoup(response.text, "lxml") #парсим весь сайт

    data = soup.find_all("div",class_="quote")# конкертный элемент findполучает содержимое всего тега
    for i in data:
        mail = i.find("span",class_="text").text
        namee = i.find ("small",class_="author").text

        yield mail,namee
#def array():
    #for i in data:


        #name = i.find("h4").text #findполучает содержимое всего ТЕГА
        #price = i.find ("h5").text
        #url_img ="https://scrapingclub.com" + i.find ("img", class_="card-img-top img-fluid").get("src")

        #yield name, price,url_img

        #print (name)
        #print (price)
        #print (url_img)