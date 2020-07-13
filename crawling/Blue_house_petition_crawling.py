from selenium import webdriver
import time

driver=webdriver.Chrome("C:/chromedriver")

page=590661

for i in range(page,589674,-1):
    driver.get("https://www1.president.go.kr/petitions/" + str(i))
    time.sleep(1)

    detail_petition = driver.find_element_by_css_selector("div.petitionsView_left_pg")
    # 제목
    title = detail_petition.find_element_by_css_selector("h3.petitionsView_title").text
    # 청원수
    people = detail_petition.find_element_by_css_selector("h2.petitionsView_count span").text
    # 카테고리
    category = detail_petition.find_element_by_css_selector("ul.petitionsView_info_list li:nth-of-type(1)").text.replace("카테고리\n","")
    # 시작일
    start = detail_petition.find_element_by_css_selector("ul.petitionsView_info_list li:nth-of-type(2)").text.replace("청원시작\n","")
    # 마감일
    end = detail_petition.find_element_by_css_selector("ul.petitionsView_info_list li:nth-of-type(3)").text.replace("청원마감\n","")
    # 본문
    content = detail_petition.find_element_by_css_selector("div.petitionsView_left_pg div.View_write").text

    time.sleep(1)
    print(title)
    print(people)
    print(category)
    print(start)
    print(end)
    print(content)
    print("="*50)
