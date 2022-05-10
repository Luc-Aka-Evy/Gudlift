from selenium import webdriver


class TestAuthentification():
    def test_login(self):
        #Ouvrir le navigateur avec le webdriver
        self.browser = webdriver.Chrome("tests/functional_tests/chromedriver")
        self.browser.get("http://127.0.0.1:5000")

        email = self.browser.find_element_by_name("email")
        email.send_keys("admin@irontemple.com")

        login = self.browser.find_element_by_id("enter")
        login.click()

        assert self.browser.find_element_by_tag_name('h2').text, "Welcome, admin@irontemple.com"
        assert self.browser.find_element_by_tag_name('h3').text, "Competitions:"
        self.browser.close()


    def test_logout(self):
        self.browser = webdriver.Chrome("tests/functional_tests/chromedriver")
        self.browser.get("http://127.0.0.1:5000")

        email = self.browser.find_element_by_name("email")
        email.send_keys("admin@irontemple.com")

        login = self.browser.find_element_by_id("enter")
        login.click()

        logout =  self.browser.find_element_by_link_text('Logout')
        logout.click()

        assert self.browser.find_element_by_tag_name('h1').text, "Welcome to the GUDLFT Registration Portal!"
        self.browser.close()
