from selenium import webdriver


class TestPointsSisplayBoard():
    def test_points_display(self):
        self.browser = webdriver.Chrome("tests/functional_tests/chromedriver")
        self.browser.get("http://127.0.0.1:5000/pointsDisplay")
      
        assert self.browser.find_element_by_tag_name('h2').text, "Points Display board"
        self.browser.close()