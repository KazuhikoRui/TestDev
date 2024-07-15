from .pages.main_page import MainPage
from .pages.contacts_page import ContactsPage
from .pages.tensor_page import TensorPage
from .pages.about_page import AboutPage
import time

def first_scenario(browser):
    link = "https://sbis.ru/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_contacts_link()
    page.go_to_contacts_page()

    contacts_page = ContactsPage(browser, browser.current_url)
    contacts_page.should_be_logo_link()
    contacts_page.go_to_logo_page()
    contacts_page.switch()

    tensor_page = TensorPage(browser, browser.current_url)
    tensor_page.should_be_power_in_people()
    tensor_page.go_to_about_page()

    about_page = AboutPage(browser, browser.current_url)
    about_page.should_be_work_title()
    about_page.check_all_images()

def test_second_scenario(browser):
    link = "https://sbis.ru/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_contacts_link()
    page.go_to_contacts_page()

    contacts_page = ContactsPage(browser, browser.current_url)
    contacts_page.should_be_my_region()
    contacts_page.change_region()
    contacts_page.should_be_partners_change()
    contacts_page.should_be_new_region()
    contacts_page.should_be_correct_url()
    contacts_page.should_be_correct_title()





