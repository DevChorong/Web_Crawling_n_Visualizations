import requests
from bs4 import BeautifulSoup

def get_sentence(data):
    text = str(data)

    start = text.find("</span>") + len("</span>")
    end = text.find("</p>")

    sentence = text[start:end]
    return sentence

# 결과물
data_array = []

for page in range(1, 10):
    # request 부분
    URL = 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code=163608&type=after&onlyActualPointYn=Y&page='+str(page)

    connect = requests.get(URL)

    html = connect.text

    # Beautiful Soup 부분
    soup = BeautifulSoup(html,'html.parser')

    sentence_array = soup.select('body > div > div > div > ul > li > div > p')

    # 하나의 결과물 배열로 모으기
    for i in range(len(sentence_array)):
        data_array.append(get_sentence(sentence_array[i]))


# 하나의 문장으로 모으기
text = ""

for i in range (len(data_array)):
    text = text + " " + data_array[i]

print(text)












