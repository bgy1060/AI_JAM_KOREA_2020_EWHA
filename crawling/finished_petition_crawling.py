import requests
from bs4 import BeautifulSoup
import openpyxl

wb = openpyxl.load_workbook("finish_petition.xlsx")
sheet = wb.active


raw=requests.get("https://www1.president.go.kr/petitions/answer?page=8",
                 headers={"User-Agent":"Mozilla/5.0"})
html=BeautifulSoup(raw.text,"html.parser")

petition=html.select("div.ans_name_title h2.TDepTitle a")


for p in petition:
    url = "https://www1.president.go.kr" + p.attrs["href"]

    raw_each=requests.get(url,headers={"User-Agent":"Mozilla/5.0"})
    html_each=BeautifulSoup(raw_each.text,"html.parser")


    #컨테이너 div.petitionsView_left_pg
    #제목 h3.petitionsView_title
    #청원수 h2.petitionsView_count span
    #카테고리 ul.petitionsView_info_list li:nth-of-type(1)
    #시작일 ul.petitionsView_info_list li:nth-of-type(2)
    #마감일 ul.petitionsView_info_list li:nth-of-type(3)
    #본문 div.View_write:nth-of-type

    # 제목
    try:
        title = html_each.select_one("h3.petitionsView_title").text
    except:
        continue
    # 청원수
    people = html_each.select_one("h2.petitionsView_count span").text
    # 카테고리
    category = html_each.select_one("ul.petitionsView_info_list li:nth-of-type(1)").text.replace("카테고리", "")
    # 시작일
    start = html_each.select_one("ul.petitionsView_info_list li:nth-of-type(2)").text.replace("청원시작", "")
    # 마감일
    end = html_each.select_one("ul.petitionsView_info_list li:nth-of-type(3)").text.replace("청원마감", "")
    # 본문
    content = html_each.select("div.View_write")

    print(title)
    print(people)
    print(category)
    print(start)
    print(end)
    for c in content:
        content=c.get_text(strip=True, separator=" ")
        print(c.get_text(strip=True, separator=" "))
    print("=" * 50)

    sheet.append([title, people, category, start, end, content])

    url = "https://www1.president.go.kr/petitions/answer?page=8"

    raw_each = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    html_each = BeautifulSoup(raw_each.text, "html.parser")

wb.save("finish_petition.xlsx")




















