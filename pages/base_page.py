from selenium.common.exceptions import NoSuchElementException


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def switch(self):
        new_window = self.browser.window_handles[1]
        self.browser.switch_to.window(new_window)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_all_elements_same(self, elements):
        first_elem = elements[0]
        for element in elements:
            if element != first_elem:
                return False
        return True
