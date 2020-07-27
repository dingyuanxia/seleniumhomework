from selenium.webdriver.common.by import By

from selenium_wework_add.page.add_member import AddMember
from selenium_wework_add.page.base_page import BasePage

class HomePage(BasePage):
    base_url = "https://work.weixin.qq.com/wework_admin/frame#index"

    def goto_addmember(self):
        self.find(By.XPATH, '//*[@class="index_service_cnt js_service_list"]//a[1]').click()
        return AddMember(self.driver)
