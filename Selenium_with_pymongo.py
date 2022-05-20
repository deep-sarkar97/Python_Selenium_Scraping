import pymongo
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


PATH="C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.stfrancismedicalcenter.com/find-a-provider/")
names=[]
specl=[]
phnum=[]
stradd=[]
city=[]
state=[]
Zip=[]
fulladd=[]
Url=[]

try:
    for i in range(3):
        Names = driver.find_elements(By.XPATH,'//span[@class="title-style-5"]')
        for i in Names:
            names.append(i.text)
        List2 = driver.find_elements(By.XPATH,'//span[@data-item="i"]')
        for i in List2:
            specl.append(i.text)
        List3 = driver.find_elements(By.XPATH,'//li[@class="inline-svg phone"]')
        for i in List3:
            phnum.append(i.text)
        for i in range(2, 14):
            stradd.append(driver.find_element(By.XPATH, '//*[@id="PhysicianSearch"]/div[2]/ul/li[' + str(
        i) + ']/div/div[1]/div/meta[1]').get_attribute('content'))
            city.append(driver.find_element(By.XPATH, '//*[@id="PhysicianSearch"]/div[2]/ul/li['+str(i)+']/div/div[1]/div/meta[2]').get_attribute('content'))
            state.append(driver.find_element(By.XPATH, '//*[@id="PhysicianSearch"]/div[2]/ul/li[' + str(
        i) + ']/div/div[1]/div/meta[3]').get_attribute('content'))
            Zip.append(driver.find_element(By.XPATH, '//*[@id="PhysicianSearch"]/div[2]/ul/li[' + str(
        i) + ']/div/div[1]/div/meta[4]').get_attribute('content'))
            Url.append(driver.find_element(By.XPATH, '//*[@id="PhysicianSearch"]/div[2]/ul/li['+str(i)+']/a').get_attribute('href'))
        for i in range(0, 12):
            fulladd.append(stradd[i] + city[i] + state[i] + Zip[i])
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//a[@class="next"]'))).click()
        time.sleep(5)
except Exception as e:
    print(e)


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

for j in range(35):
    mydict = { "Name": names[j], "Speciality": specl[j], "PhoneNumber": phnum[j], "Full_Address": fulladd[j], "Street" : stradd[j], "City": city[j], "State": state[j], "Zip":Zip[j], "Url": Url[j]}
    x = mycol.insert_one(mydict)




driver.quit()


