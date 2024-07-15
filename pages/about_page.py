from .base_page import BasePage
from .locators import AboutPageLocators

class AboutPage(BasePage):

    def check_all_images(self):
        elements = self.browser.find_elements(*AboutPageLocators.IMAGES_LINK)
        all_sizes = []
        for element in elements:
            img = element.find_element(*AboutPageLocators.IMAGE)
            width, height = img.get_attribute("width"), img.get_attribute("height")
            all_sizes.append((width, height))
        assert self.is_all_elements_same(all_sizes), "Not all elements are the same"

    def should_be_work_title(self):
        assert self.is_element_present(*AboutPageLocators.LINK), "Work title is not presented"
