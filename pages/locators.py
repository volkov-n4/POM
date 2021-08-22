from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    REGISTRATION_FORM = (By.ID, 'register_form')
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    URL_IN_LINK = (By.PARTIAL_LINK_TEXT, 'login')