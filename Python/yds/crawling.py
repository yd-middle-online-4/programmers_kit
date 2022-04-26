import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
# HTML을 파싱해서 구조를 가져오는 라이브러리
# 파싱(pausing) : 문서구조, 단어 기준 구별 하는것을 말한다.

page = open("03. test_first.html")
soup = BeautifulSoup(page, "html.parser") # page라는 html을 html.parser을 이용하여 파싱해라
print(type(soup))                         # type : bs4.BeautifulSoup

#print(list(soup.children))              # 3가지의 정보를 가지고있다 [Html, 공백, 전체의 Html 내용]
#print(list(soup.children)[0])           # html

html = list(soup.children)[2]             # 변수 html에 html의 전체내용을 넣는다.

# html.children : 공백 헤더 공백 바디 순으로 들어가있다. 즉 html.children[3] = body에 해당하는 부분

head = list(html.children)[1]
body = list(html.children)[3]
# children을 통하여 파싱하는 것은 잘 이용하지 않음 (특정한 것을 뽑을 때는 find, find all을 사용)
# 어떠한 태그들로 구성되어 있는지 분석할 때 자주 사용

first_p_tag = soup.find("p")   # p태그의 첫번째에 해당하는 부분

# p_tags = soup.find_all("p")             # p태그의 전부
p_tags = soup.find_all("p", class_ = "inner-text second-item")  # p태그 중 class가 outer에 해당하는 부분 전부
print(p_tags)

# p_tag1 = soup.find_all(class_ = "inner-text second-item")     # p_tag == p_tag1

print("#################################")
# print(body.p)               # find("p") 와 같다.
# print(body.p.next_sibling.next_sibling)

p_tags = soup.find_all("p")
# print(type(p_tags))
# bs4.element.ResultSet = ResultSet : find_all 로 여러가지가 나오면 타입이 정의된다.
# bs4.element.Tag = Tag : find로 한가지가 출력되면 타입이 정의된다.

for tag_string in p_tags :
    print(tag_string.get_text()) # 각 p 태그의 text를 출력

print("####################################")
# 속성값과 하이퍼링크 가져오기
links = soup.find_all("a")
print(links)

for each in links :
    href = each["href"]     # 태그에서 href 속성의 값을 의미
    web_name = each.get_text()
    print("{} -> {}".format(web_name, href))
    
    
import pandas as pd
from urllib.request import urlopen
import urllib
from bs4 import BeautifulSoup

baseurl = "https://movie.naver.com"
suburl = "/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20201123"

url = baseurl + suburl
page = urlopen(url)

soup = BeautifulSoup(page, "html.parser")
movieT = soup.find_all("div", class_ = "tit5")

# 첫번 째 영화 제목
firstMT = movieT[0].get_text()
print(firstMT)
# firstMT = movieT[0].find("a").get_text()  위에 코드와 동일

# 첫번 째 영화 포인트
moviePT = soup.find_all("td", class_ = "point")
firstPT = moviePT[0].get_text()
# print(firstPT)

# 날짜를 생성 후 해당 날짜의 영화 정보를 추출
date = pd.date_range("2020-10-01", periods= 30, freq="d")

MT = []
PT = []
DT = []

for today in date:
    url = "https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date={date}"
    page = urlopen(url.format(date=urllib.parse.quote(today.strftime("%Y%m%d"))))
    # print(url.format(date=urllib.parse.quote(today.strftime("%Y%m%d"))))
    # today.strftime("%Y%m%d") = 20201010 형태로 바꿔줌
    # url에 {date} 부분을 20101010 형식으로 바꿔줌
    soup = BeautifulSoup(page, "html.parser")

    # 특정 날짜별 한페이지에 영화 개수 (평점으로 구하기)
    end = len(soup.find_all("td", class_="point"))
    # print(end)

    # 50개의 영화를 추출하여 동일한 날짜에 추가
    # append, extend의 차이
    # append([1,2]) => [1,2] 리스트 하나가 추가 -> 추가되는 리스트 1개
    # extend([1,2]) => 1과 2가 따로 추가가 된다 -> 추가되는 리스트 2개

    DT.extend(today for n in range(0, end))
    MT.extend([soup.find_all("div", "tit5")[n].a.string for n in range(0, end)] )           # a.string = a태그
    PT.extend([float(soup.find_all("td", "point")[n].string) for n in range(0, end)])

print(DT)
print((MT))
print(len(PT))

movie_info = pd.DataFrame({"date" : DT, "title" : MT, "point" : PT})
movie_info.to_excel("네이버 영화.xlsx")


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

naver_movie = pd.read_excel("네이버 영화.xlsx", sheet_name= "Sheet1")
# print(naver_movie)

movie_unique = pd.pivot_table(naver_movie, index= "title",values= "point", aggfunc=np.sum)
# pivot_table
print(movie_unique)

# 특정 영화 검색
tmp = naver_movie.query("title == ['먼 훗날 우리']")
print(tmp)

# plt.figure(figsize=(12, 8))
# plt.plot(tmp["date"], tmp["point"])
# plt.legend(loc = "best")
# plt.grid()
# plt.show()

# 영화별 날짜 변화에 따른 평점 변화 확인
movie_pivot = pd.pivot_table(naver_movie, index = ["date"], columns=["title"], values=["point"])
print(movie_pivot)
print("#### {}".format(movie_pivot.columns))
movie_pivot.columns = movie_pivot.columns.droplevel()       # 컬럼이 title, point로 잡히기 때문에 단계를 하나 낮추는 의미 ?
print(movie_pivot.columns)

font_name = font_manager.FontProperties(fname= "C:\Windows\Fonts\H2HDRM.ttf").get_name()
rc("font", family=font_name)
movie_pivot.plot(y = ["먼 훗날 우리", "원더"], figsize=(12, 6))
plt.legend(loc = "best")
plt.grid()
plt.show()
