from bs4 import BeautifulSoup
import ast
import requests
import csv

# a.html 파일 읽기
with open("a.html", "r", encoding="utf-8") as f:
    html = f.read()

# BeautifulSoup 파싱
soup = BeautifulSoup(html, "html.parser")
lst = []
faq = []
for i in soup.select("li"):
    append_lst = []
    idx = i.select_one('a').get("data-enlog-dt-param")  # 문자열
    if idx:
        data = ast.literal_eval(idx)["idbid"]   # 문자열 dict → 실제 dict
        append_lst.append(data)
        
    car_nm = i.select_one('a > strong.tit_car').text
    append_lst.append(car_nm)
    lst.append(append_lst)
        
s = requests.Session()

for car_dt in lst:
    url = f"https://www.encar.com/mocha/ajaxcommonContent.do?method=getMochaDetail&type=faq&idbid={car_dt[0]}&WT.hit=Mochadetail_tab_faq"
    res = s.post(url)
    res.raise_for_status()
    result = res.json()
    faq_data = result[0]["result"]["contentsFaq"]
    
    for dt in faq_data:
        faq.append({
            "faqCarNbr": car_dt[0]
            ,"faqCarNm": car_dt[1]
            ,"question": dt["question"]
            ,"answer" : dt["answer"]
        })
        print(car_dt[1]+" append 완료")
        
with open("faq.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["faqCarNbr", "faqCarNm", "question", "answer"])
    writer.writeheader()
    writer.writerows(faq)
    print("csv파일 생성완료")
    
    f.close()
    
