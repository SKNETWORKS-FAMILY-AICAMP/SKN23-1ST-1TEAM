import streamlit as st
import re
import requests
import json
from bs4 import BeautifulSoup
import csv

def app():
     # CSV 저장을 위한 리스트
    car_data = []               # car_data
    grade_data = []             # grade_data
    distance_rows = []          # getChartData
    gender_rows = []            # getTradeStatistics
    age_rows = []               # getTradeStatistics
    region_rows = []            # getTradeStatistics
    grade_price_rows = []       # getGradePriceInfo
    
    for carClassNbr in range(3715, 7559):
        try : 
            ###### Car, Grade Data START ######
            
            html = requests.get(f"https://www.carisyou.com/price/{carClassNbr}").text
            soup = BeautifulSoup(html, 'html.parser')
            scripts = soup.find_all("script")
            raw = ""
            for s in scripts:
                if "topCarGradeList" in s.text:
                    raw = s.text
                    break
            pattern1 = r"topCarGradeList\s*:\s*(\[[^\]]*\])"
            top_list = re.search(pattern1, raw, re.DOTALL).group(1)
            clean_top = re.sub(r",\s*]", "]", top_list)
            top_data = json.loads(clean_top)

            if top_data[0]["gradeUsedCarPrice"] == 0 :
                continue
            #print("car_data : ", car_data)
            #print("grade_data : ", grade_data) #list 안에 딕셔너리  > 포문 돌려서 
            ###### Car, Grade Data END ######
            
            
            
            ###### Distance Data START ######    
                    
            s = requests.Session()

            # 필수 1) 쿠키 설정
            s.cookies.set("usedCarList", str(carClassNbr))
            
            s.get(f"https://www.carisyou.com/price/{carClassNbr}")
            
            # 
            url = "https://www.carisyou.com/usedcar/axios/getChartData.do"
            headers = {
                "User-Agent": "Mozilla/5.0",
                "Accept": "application/json, text/plain, */*",
                "Origin": "https://www.carisyou.com",
                "Referer": f"https://www.carisyou.com/price/{carClassNbr}",
                "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
            }
            data = {
                "carClassNbr": carClassNbr,
                "agent": "ETC",
                "dealTypeSelected": "매입,매도",
                "fromDate": "",
                "toDate": ""
            }
            res = s.post(url, headers=headers, data=data)
            distance_data = res.json()["trvlChart"]
            ###### Distance Data END ######
            
            
            
            ###### Gender, Age, Region Data START ######    
            
            url = "https://www.carisyou.com/usedcar/axios/getTradeStatistics.do"
            data = {
                "carClassNbr": carClassNbr,
                "spcfModelYear": '',
                "carMakerKor": '',
                "carModelDt": '',
                "carModelKor": '',
                "impSeNm": '',
                "fromDate": "",
                "toDate": "",
                "agent": "ETC",
                "dealTypeSelected": "매입,매도",
            }
            res = s.post(url, headers=headers, data=data)
            res.raise_for_status()
            gender_data = res.json()["assigneeSexRankList"]
            age_data = res.json()["assigneeAgeRankList"]
            region_data = res.json()["assigneeAddressRankList"]

            ###### Gender, Age, Region Data END ######    



            ###### Price Data START ######    

            url = "https://www.carisyou.com/usedcar/axios/getGradePriceInfo.do"
            data = {
                "carClassNbr": carClassNbr,
                "importYn": "N",
                "yearType": '',
                "trvlDstnc": 10000,
                "userTrvlDstncYn": "Y",
            }
            
            res = s.post(url, headers=headers, data=data)
            res.raise_for_status()
            price_data1 = res.json()
            if price_data1["gradeList"][0]["gradeUsedCarPrice"] == 0:
                continue
            
            url = "https://www.carisyou.com/usedcar/axios/getGradePriceInfo.do"
            data = {
                "carClassNbr": carClassNbr,
                "importYn": "N",
                "yearType": '',
                "trvlDstnc": 50000,
                "userTrvlDstncYn": "Y",
            }
            
            res = s.post(url, headers=headers, data=data)
            res.raise_for_status()
            price_data2 = res.json()
                  
            url = "https://www.carisyou.com/usedcar/axios/getGradePriceInfo.do"
            data = {
                "carClassNbr": carClassNbr,
                "importYn": "N",
                "yearType": '',
                "trvlDstnc": 100000,
                "userTrvlDstncYn": "Y",
            }
            
            res = s.post(url, headers=headers, data=data)
            res.raise_for_status()
            price_data3 = res.json()
            
            url = "https://www.carisyou.com/usedcar/axios/getGradePriceInfo.do"
            data = {
                "carClassNbr": carClassNbr,
                "importYn": "N",
                "yearType": '',
                "trvlDstnc": 150000,
                "userTrvlDstncYn": "Y",
            }
            
            res = s.post(url, headers=headers, data=data)
            res.raise_for_status()
            price_data4 = res.json()
            
            ###### Price Data END ######    

            
            
            ###### 데이터 파싱 및 list에 추가 ######
            car_data.append({
               "brandNbr":top_data[0]["brandNbr"]
               ,"brandNm":top_data[0]["brandNm"]
               ,"repCarClassNbr":top_data[0]["repCarClassNbr"]
               ,"repCarClassNm":top_data[0]["repCarClassNm"]
               ,"carClassNbr":top_data[0]["carClassNbr"]
               ,"carClassNm":top_data[0]["carClassNm"]
               ,"yearType":top_data[0]["yearType"]
               ,"brandImage":top_data[0]["brandImage"]
            })
            
            for data in top_data:
                grade_data.append({
                    "carGradeNbr":data["carGradeNbr"]
                    ,"carGradeNm":data["carGradeNm"]
                    ,"carClassNbr":data["carClassNbr"]
                    ,"rn":data["rn"]
                    ,"fuel":data["fuel"]
                    ,"fuelNm":data["fuelNm"]
                    ,"gradeFuelRate":data["gradeFuelRate"]
                    ,"fuelRateGrade":data["fuelRateGrade"]
                    ,"extShape":data["extShape"]
                    ,"extShapeNm":data["extShapeNm"]
                    ,"carSize":data["carSize"]
                    ,"carClassRepImage":data["carClassRepImage"]  
                })
                
            for data in distance_data:
                distance_rows.append({
                    "carClassNbr": carClassNbr
                    ,"trvlDstnc":data["trvlDstnc"]
                    ,"avgPrice":data["avgPrice"]
                    ,"cnt" : data["cnt"]
                    ,"percent":data["percent"]
                })
            for data in gender_data:
                gender_rows.append({
                    "carClassNbr": carClassNbr
                    ,"rn":data["rn"]
                    ,"gender":data["sex"]
                    ,"cnt" : data["cnt"]
                    ,"percent":data["percent"]
                })
            for data in age_data:
                age_rows.append({
                    "carClassNbr": carClassNbr
                    ,"rn":data["rn"]
                    ,"age":data["age"]
                    ,"cnt" : data["cnt"]
                    ,"percent":data["percent"]
                })

            for data in region_data:
                region_rows.append({
                    "carClassNbr": carClassNbr
                    ,"rn":data["rn"]
                    ,"address":data["address"]
                    ,"cnt" : data["cnt"]
                    ,"percent":data["percent"]
                })
                
            for data in price_data1["gradeList"]:
                grade_price_rows.append({
                    "carClassNbr": carClassNbr
                    ,"carGradeNbr":data["carGradeNbr"]
                    ,"gradeSalePrice":data["gradeSalePrice"]
                    ,"gradeUsedCarPrice" : data["gradeUsedCarPrice"]
                    ,"grade1yearLaterPrice":data["grade1yearLaterPrice"]
                    ,"grade2yearLaterPrice":data["grade2yearLaterPrice"]
                    ,"grade3yearLaterPrice":data["grade3yearLaterPrice"]
                    ,"trvlDstnc":"10000"
                })
            for data in price_data2["gradeList"]:
                grade_price_rows.append({
                    "carClassNbr": carClassNbr
                    ,"carGradeNbr":data["carGradeNbr"]
                    ,"gradeSalePrice":data["gradeSalePrice"]
                    ,"gradeUsedCarPrice" : data["gradeUsedCarPrice"]
                    ,"grade1yearLaterPrice":data["grade1yearLaterPrice"]
                    ,"grade2yearLaterPrice":data["grade2yearLaterPrice"]
                    ,"grade3yearLaterPrice":data["grade3yearLaterPrice"]
                    ,"trvlDstnc":"50000"
                })
            for data in price_data3["gradeList"]:
                grade_price_rows.append({
                    "carClassNbr": carClassNbr
                    ,"carGradeNbr":data["carGradeNbr"]
                    ,"gradeSalePrice":data["gradeSalePrice"]
                    ,"gradeUsedCarPrice" : data["gradeUsedCarPrice"]
                    ,"grade1yearLaterPrice":data["grade1yearLaterPrice"]
                    ,"grade2yearLaterPrice":data["grade2yearLaterPrice"]
                    ,"grade3yearLaterPrice":data["grade3yearLaterPrice"]
                    ,"trvlDstnc":"100000"
                })
            for data in price_data4["gradeList"]:
                grade_price_rows.append({
                    "carClassNbr": carClassNbr
                    ,"carGradeNbr":data["carGradeNbr"]
                    ,"gradeSalePrice":data["gradeSalePrice"]
                    ,"gradeUsedCarPrice" : data["gradeUsedCarPrice"]
                    ,"grade1yearLaterPrice":data["grade1yearLaterPrice"]
                    ,"grade2yearLaterPrice":data["grade2yearLaterPrice"]
                    ,"grade3yearLaterPrice":data["grade3yearLaterPrice"]
                    ,"trvlDstnc":"150000"
                })
            print(str(carClassNbr)+" 종료")
        except:
            continue
    # ① car_data.csv
    with open("car.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["brandNbr", "brandNm", "repCarClassNbr", "repCarClassNm", "carClassNbr", "carClassNm", "yearType", "brandImage"])
        writer.writeheader()
        writer.writerows(car_data)
        
        
    # ① grade_data.csv
    with open("grade.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["carGradeNbr","carGradeNm","carClassNbr","rn","fuel","fuelNm","gradeFuelRate","fuelRateGrade","extShape","extShapeNm","carSize","carClassRepImage"])
        writer.writeheader()
        writer.writerows(grade_data)

    # ① dstnc_rank.csv
    with open("dstnc_rank.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["carClassNbr", "trvlDstnc", "avgPrice", "cnt", "percent"])
        writer.writeheader()
        writer.writerows(distance_rows)
        
    # ② gender_statistics.csv
    with open("gender_rank.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["carClassNbr", "rn", "gender", "cnt", "percent"])
        writer.writeheader()
        writer.writerows(gender_rows)
    # ② age_statistics.csv
        with open("age_rank.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["carClassNbr", "rn", "age", "cnt", "percent"])
            writer.writeheader()
            writer.writerows(age_rows)
    # ② region_statistics.csv
    with open("region_rank.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["carClassNbr", "rn", "address", "cnt", "percent"])
        writer.writeheader()
        writer.writerows(region_rows)

    # ③ price_info.csv
    with open("price.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["carClassNbr", "carGradeNbr", "gradeSalePrice", "gradeUsedCarPrice", "grade1yearLaterPrice", "grade2yearLaterPrice", "grade3yearLaterPrice", "trvlDstnc"])
        writer.writeheader()
        writer.writerows(grade_price_rows)

app()