from selenium.webdriver.common.by import By


class MainPageLocators:
    LINK = (By.CSS_SELECTOR, '.sbisru-Header [href="/contacts"]')


class ContactsPageLocators:
    LINK = (By.CSS_SELECTOR, '#contacts_clients [title="tensor.ru"]')
    REGION = (By.CSS_SELECTOR, '.ml-xm-0 > .sbis_ru-link')
    REGION_KAMCHATKA = (By.CSS_SELECTOR, '.sbis_ru-Region-Panel__list-l > li:nth-child(43)')
    PARTNERS_LIST = (By.CSS_SELECTOR, '.pr-xm-32')



class TensorPageLocators:
    LINK = (By.CSS_SELECTOR, '.tensor_ru-Index__block4 > .s-Grid-col--sm12 > .tensor_ru-Index__card > p:nth-child(1)')
    ABOUT_LINK = (By.CSS_SELECTOR,
                  '.tensor_ru-Index__block4 > .s-Grid-col--sm12 > .tensor_ru-Index__card [href="/about"]')


class AboutPageLocators:
    LINK = (By.CSS_SELECTOR, '.tensor_ru-About__block3 > .tensor_ru-About__block-title-block > h2')
    IMAGES_LINK = (By.CSS_SELECTOR, '.tensor_ru-About__block3 > .s-Grid-container > .s-Grid-col')
    IMAGE = (By.CSS_SELECTOR, 'img')
