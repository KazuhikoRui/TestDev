from .base_page import BasePage
from .locators import MainPageLocators
from .contacts_page import ContactsPage


class MainPage(BasePage):
    def go_to_contacts_page(self):
        link = self.browser.find_element(*MainPageLocators.LINK)
        link.click()
        return ContactsPage(browser=self.browser, url=self.browser.current_url)

    def should_be_contacts_link(self):
        assert self.is_element_present(*MainPageLocators.LINK), "Contacts is not presented"
