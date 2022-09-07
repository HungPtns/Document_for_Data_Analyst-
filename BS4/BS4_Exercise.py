# du lieu ve thoi tiet cua 63 tinh thanh
import csv
from bs4 import BeautifulSoup as bs
import requests as rp
import lxml
url = rp.get("https://www.24h.com.vn/du-bao-thoi-tiet-c568.html")
soup = bs(url.text,"lxml")

# training
day = soup.find("thead",class_="tabBttHead")
days = day.find_all("b", class_="tit")
print("{:>20}".format(" "),end=" ")
for m_day in days:
     if m_day.text != "Hiện tại":
         print("{:<60}".format(m_day.text),end=" ")
print()
tam=0
city = soup.find_all("td",class_="add")
temp = soup.find_all("span",class_="ndSmallBtt")
future = soup.find_all("span",class_="hTuongBttSmall")

# xu ly du lieu
def nhap(i):
    print("{:>20}".format(temp[i].text.rjust(10)), "{:>10}".format(future[i].text.rjust(10)), end=" ")
    print("{:>30}".format(temp[i + 1].text.rjust(10)), "{:>10}".format(future[i + 1].text.rjust(10)), end=" ")
    print("{:>30}".format(temp[i + 2].text.rjust(10)), "{:>10}".format(future[i + 2].text.rjust(10)))
tup2 = [" "]

# ghi du lieu vao file data.csv
with open("data.csv","w",encoding="utf-8",newline="") as f:
    writer = csv.writer(f)
    for m_day in days:
        if m_day.text != "Hiện tại":
            tup2.append(m_day.text)
    writer.writerow(tup2)
    tam += 3
    for m_city in city:
        print(m_city.text,end=" ")
        nhap(tam)
        tup = (m_city.text,temp[tam].text,temp[tam+1].text,temp[tam+2].text)
        tup3 =(" ",future[tam].text,future[tam+1].text,future[tam+2].text)
        # writer.writerow(m_city.text)
        writer.writerow(tup)
        writer.writerow(tup3)
        writer.writerow(" ")
        tam += 3 if tam <= len(temp)-4 else 0
        print()






