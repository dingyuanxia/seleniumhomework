import time

from selenium.webdriver.common.by import By

from selenium_wework_add.page.base_page import BasePage


class AddMember(BasePage):

    def add_member(self):
        self.find(By.ID, 'username').send_keys("test99")
        self.find(By.ID, 'memberAdd_acctid').send_keys('test99')
        self.find(By.ID, 'memberAdd_phone').send_keys('12345678909')
        self.find(By.XPATH, '//*[@class="qui_btn ww_btn js_btn_save"]').click()

    def update_page(self):
        content: str = self.find(By.XPATH, '//*[@class="ww_pageNav_info_text"]').text
        #对1/10进行切割
        return [int(x) for x in content.split("/", 1)]

    def get_member(self, value):
        time.sleep(2)
        cur_page, total_page = self.update_page()
        while True:
            elements = self.finds(By.XPATH, '//*[@class="member_colRight_memberTable_td"]')
            for ele in elements:
                if value == ele.get_attribute('title'):
                    print("title---", ele.get_attribute("title"))
                    return True

            cur_page = self.update_page()[0]
            if cur_page == total_page:
                return False
            self.find(By.CSS_SELECTOR, '.js_next_page').click()
            time.sleep(2)
