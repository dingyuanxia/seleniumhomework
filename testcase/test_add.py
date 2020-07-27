from selenium_wework_add.page.homepage import HomePage


class TestAdd():
    def setup(self):
        self.homepage = HomePage()
    def test_add(self):
        newmember = self.homepage.goto_addmember()
        newmember.add_member()
        assert newmember.get_member("136")
