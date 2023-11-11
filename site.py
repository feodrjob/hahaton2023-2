from requests import Session
from bs4 import BeautifulSoup

for i in range(1,5):
    headers = {"User-Agent":
                "Mozilla/5.0 (<system-information>) <platform> (<platform-details>) <extensions>"}

    work = Session()

    work.get("https://quotes.toscrape.com/",headers=headers)

    response = work.get ("https://quotes.toscrape.com/login", headers=headers)
    soup = BeautifulSoup(response.text,"lxml")
    token = soup.find("form").find("input").get("value")
    data = {"csrf_token": token, "username": "123", "password": "123"}
    result = work.post("https://quotes.toscrape.com/login",headers=headers,data=data,allow_redirects=True)

#print (result.text)
    print (token)