from selenium import webdriver


class TestBookingPlaces():
    def test_booking(self):
        self.browser = webdriver.Chrome("tests/functional_tests/chromedriver")
        self.browser.get("http://127.0.0.1:5000")

        email = self.browser.find_element_by_name("email")
        email.send_keys("admin@irontemple.com")

        login = self.browser.find_element_by_id("enter")
        login.click()

        booking = self.browser.find_element_by_link_text("Book Places")
        booking.click()

        places = self.browser.find_element_by_name("places")
        places.send_keys("1")

        purchase = self.browser.find_element_by_name("purchase")
        purchase.click()

        assert self.browser.find_element_by_tag_name('h2').text, "Welcome, admin@irontemple.com"
        self.browser.close()