#coding: utf-8
import time

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


    def getLinks(self, driver, file):
        while True:
            self.findPageCotent(driver, file)
            try:
                nextPage = driver.find_element_by_link_text('下一页')
            except NoSuchElementException as msg:
                print(u'到达最后一页%s'%msg)
                break
            driver.execute_script("window.scrollBy(0,document.body.scrollHeight)", "")
            nextPage.click()

    def findPageCotent(self, driver, file):
        items = driver.find_elements_by_xpath("//li[@class = 'clear LOGCLICKDATA']/a")
        for item in items:
            file.write(item.get_attribute('href')+'\n')


    def __del__(self):
        self.driver.close()
        self.f.close()



if __name__ == "__main__":
    scratchDo = scratchHousePrice()
    scratchDo.scrtchHousePrice()
