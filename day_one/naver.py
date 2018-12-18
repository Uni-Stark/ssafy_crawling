import urllib.request
from bs4 import BeautifulSoup

def main():
    url = "http://www.naver.com"

    soup = BeautifulSoup(urllib.request.urlopen(url).read(), "html.parser")
    list = []
    cnt = 0
    for naver_text in soup.find_all("span", class_="ah_k"):
        list.append(naver_text.get_text())
        cnt +=1
        if cnt >= 20 :
            break;
    print(list)


if __name__ == "__main__":
    main()
