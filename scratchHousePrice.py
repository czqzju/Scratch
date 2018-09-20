from selenium import webdriver




class scratchHousePrice():
    def __init__(self):
        self.driver = webdriver.Chrome()


    def scrtchHousePrice(self):
        driver = self.driver
        driver.get("https://hz.lianjia.com/ershoufang/")
        content = self.findPageCotent(driver)

    def findPageCotent(self, driver):
        items = driver.find_elements_by_xpath("//li[@class = 'clear LOGCLICKDATA']/a")
        print(len(items))
        print("Hello")

    def __del__(self):
        self.driver.close()



if __name__ == "__main__":
    scratchDo = scratchHousePrice()
    scratchDo.scrtchHousePrice()
