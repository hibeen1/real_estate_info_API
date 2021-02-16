from bs4 import BeautifulSoup
import json
import requests
import unittest


################ 버그 발생 가능성 ################
# 1. next, previous_sibling, next_sibling 등의 함수를 너무 많이 사용함 -> 네이버에서 하나만 변경 되어도 전부를 바꿔야 함
# 2. 예외 처리 남발
# 3. 검색어 처리 미흡
##############################################


def moreabangebbangyabbangya(queryName):
    html = requests.get(
        'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=' + queryName)
    soup = BeautifulSoup(html.text, 'html.parser')

    #검색어를 잘 입력한 경우
    try:
        apartment_Information = dict()
        this_Apartment = dict()
        #최근 매매 실거래 정보 parsing (없을 수도 있음)
        try:
            recent_trading_temp = soup.findAll('div', {'class': 'info_area'})[1]
            recent_trading_price = recent_trading_temp.find('span', {'class': 'item2'}).text
            recent_trading_info = recent_trading_temp.find(
                'span', {'class': 'item2'}).next_sibling.next.text
            this_Apartment["recent trade information"] = recent_trading_info + " " + \
                recent_trading_price
        except:
            this_Apartment["recent trade information"] = "None"
        acreage_num = soup.findAll('span', {'class': 'tab_inner'})
        info = soup.findAll('div', {'class': 'complex_content'})
        for i in range(0, len(acreage_num)):
            detail = dict()
            #해당 면적
            acreage = acreage_num[i].text
            detail["acreage"] = acreage
            try:
                #매물가격 1 (없을 수도 있음)
                tem = info[i].findAll('div', {'class': 'detail'})[
                    1].find('li', {'class': 'item'})
                subject_1 = tem.find(
                    'strong', {'class': 'price'}).previous_sibling
                price_of_subject_1 = tem.find('strong', {'class': 'price'}).text
                detail[subject_1] = price_of_subject_1
            except:
                detail[""] = "None"

            try:
                #매물가격 2 (없을 수도 있음)
                c1 = tem.next_sibling.next
                subject_2 = c1.find(
                    'strong', {'class': 'price'}).previous_sibling
                price_of_subject_2 = c1.find('strong', {'class': 'price'}).text
                detail[subject_2] = price_of_subject_2
            except:
                detail[""] = "None"
            
            #매물 정보(없을 수도 있음)
            try:
                tem2 = info[i].find('div', {'class': 'menu_area'}).text
                detail["Sales Info"] = tem2
            except:
                detail["Sales Info"]: "None"
            this_Apartment[acreage] = detail
        apartment_Information[queryName] = this_Apartment


        with open('../test.json', 'w', encoding='UTF-8') as make_file:
            json.dump(apartment_Information, make_file, indent="\t")

        
        # 저장한 파일 출력하기
        with open('../test.json', 'r') as f:
            json_data = json.load(f)
            #한글 인코딩 안 될 때 ensure_ascii=False
            print(json.dumps(json_data, ensure_ascii=False, indent="\t"))
    #검색어를 잘못 입력한 경우
    except:
        print("알맞은 검색어를 입력하세요")

moreabangebbangyabbangya("롯데몰송도캐슬파크")

