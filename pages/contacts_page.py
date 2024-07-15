from .base_page import BasePage
from .locators import ContactsPageLocators
from .tensor_page import TensorPage


def get_list_from_elements(browser, locator):
    elements = browser.find_elements(*locator)
    elements_text = []
    for element in elements:
        elements_text.append(element.text)
    return elements_text


class ContactsPage(BasePage):
    old_partners_list = []
    new_partners_list = []

    def go_to_logo_page(self):
        link = self.browser.find_element(*ContactsPageLocators.LINK)
        link.click()
        return TensorPage(browser=self.browser, url=self.browser.current_url)

    def change_region(self):
        self.old_partners_list = get_list_from_elements(self.browser, ContactsPageLocators.PARTNERS_LIST)
        region = self.browser.find_element(*ContactsPageLocators.REGION)
        region.click()
        new_region = self.browser.find_element(*ContactsPageLocators.REGION_KAMCHATKA)
        new_region.click()
        self.new_partners_list = get_list_from_elements(self.browser, ContactsPageLocators.PARTNERS_LIST)

    def should_be_partners_change(self):
        assert set(self.old_partners_list) == set(self.new_partners_list), "The list of partners has not changed"

    def should_be_partners(self):
        assert self.is_element_present(*ContactsPageLocators.PARTNERS_LIST), "Partners list is not presented"

    def should_be_logo_link(self):
        assert self.is_element_present(*ContactsPageLocators.LINK), "Logo is not presented"

    def should_be_my_region(self):
        assert self.browser.find_element(*ContactsPageLocators.REGION).text == "Новосибирская обл.", ("Region does not "
                                                                                                      "match")

    def should_be_new_region(self):
        assert self.browser.find_element(*ContactsPageLocators.REGION).text == "Камчатский край", ("Region does not "
                                                                                                   "match")

    def should_be_correct_url(self):
        assert "kamchatskij-kraj" in self.browser.current_url, "URL hasn't changed"

    def should_be_correct_title(self):
        assert "Камчатский край" in self.browser.title, "Title hasn't changed"
