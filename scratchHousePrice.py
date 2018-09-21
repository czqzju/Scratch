import csv

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException




class scratchHousePrice():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.f = open("data\\link.txt", 'w')


    def scrtchHousePrice(self):
        driver = self.driver
        file = self.f
        driver.get("https://hz.lianjia.com/ershoufang/")
        driver.maximize_window()
        self.getLinks(driver, file)
        file = open("data\\link.txt", 'r')
        self.getPageContent(driver, file)


    #Get contents for all houses
    def getPageContent(self, driver, file):
        links = file.readlines()
        data_csv = open('data\\contents.csv', 'w', newline= '')
        csv_write = csv.writer(data_csv, dialect = 'excel')
        head = ('小区名字', '总价（万元）', '单价（元/平方）','建筑面积（m2）', '套内面积（m2）', '上架时间', '上次交易时间')
        csv_write.writerow(head)
        for link in links:
            print(link)
            driver.get(link)
            totalPrice = driver.find_element_by_xpath("//span[@class = 'total']").text
            unitPrice = driver.find_element_by_xpath("//span[@class = 'unitPriceValue']").text
            totalArea = driver.find_element_by_xpath("//div[@class = 'introContent']//div[@class = 'content']/ul/li[3]").text
            innerArea = driver.find_element_by_xpath("//div[@class = 'introContent']//div[@class = 'content']/ul/li[5]").text

            uploadTime = driver.find_element_by_xpath("//div[@class = 'transaction']//div[@class = 'content']/ul/li[1]").text
            lastTransaction = driver.find_element_by_xpath("//div[@class = 'transaction']//div[@class = 'content']/ul/li[3]").text

            xiaoquName = driver.find_element_by_xpath("//div[@class = 'communityName']/a[1]").text

            totalPrice = totalPrice
            unitPrice = unitPrice[:len(unitPrice)-4]
            totalArea = totalArea[4:len(totalArea)-1]
            innerArea = innerArea[4:len(innerArea)-1]
            uploadTime = uploadTime[5:]
            lastTransaction = lastTransaction[5:]
            houseData = (xiaoquName, totalPrice, unitPrice, totalArea, innerArea, uploadTime, lastTransaction)
            # print('%s %.2f %.2f %.2f %s %s'%(xiaoquName, totalPrice, totalArea, innerArea, uploadTime, lastTransaction))
            print(houseData)
            csv_write.writerow(houseData)

        data_csv.close()

    #Get all links for houses
    def getLinks(self, driver, file):
        while True:
            self.findPageLinks(driver, file)
            try:
                nextPage = driver.find_element_by_link_text('下一页')
            except NoSuchElementException as msg:
                print(u'到达最后一页%s'%msg)
                break
            driver.execute_script("window.scrollBy(0,document.body.scrollHeight)", "")
            nextPage.click()
        file.close()

    def findPageLinks(self, driver, file):
        items = driver.find_elements_by_xpath("//li[@class = 'clear LOGCLICKDATA']/a")
        for item in items:
            file.write(item.get_attribute('href')+'\n')


    def __del__(self):
        self.driver.close()



if __name__ == "__main__":
    scratchDo = scratchHousePrice()
    scratchDo.scrtchHousePrice()
