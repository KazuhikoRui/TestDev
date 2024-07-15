from .base_page import BasePage
from .locators import TensorPageLocators
from .about_page import AboutPage

class TensorPage(BasePage):

    def go_to_about_page(self):
        link = self.browser.find_element(*TensorPageLocators.ABOUT_LINK)
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", link)
        link.click()
        return AboutPage(browser=self.browser, url=self.browser.current_url)

    def should_be_power_in_people(self):
        assert self.is_element_present(*TensorPageLocators.LINK), "Power in people is not presented"