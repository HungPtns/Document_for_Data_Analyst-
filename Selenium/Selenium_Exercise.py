# du lieu ve danh sach cac tac pham cua Nguyen Nhat Anh
import csv
import time
from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
url = "https://thuvienpdf.com/sach-bo/tuyen-chon-truyen-nguyen-nhat-anh"

driver.get(url)
time.sleep(5)
element_ne = driver.find_elements(By.CSS_SELECTOR,".font-weight-bold")
element_ne2 = driver.find_elements(By.XPATH,'//*[@class="alert-link text-success btn"]')
print("danh sach tac pham Nguyen Nhat Anh")
storyTitles = [el.text for el in element_ne]
storyUrls = [el.get_attribute("href") for el in element_ne2]
with open("file_data.csv","w",encoding="utf-8",newline="") as f:
    writer = csv.writer(f)
    tup = ["ten sach","link sach"]
    writer.writerow(tup)
    for i in range(len(storyTitles)):
        print(storyTitles[i]," "*30,'{:>3}'.format(storyUrls[i]))
        tup1 = (storyTitles[i],storyUrls[i])
        writer.writerow(tup1)



