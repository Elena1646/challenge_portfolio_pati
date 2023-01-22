 from pages.base_page import BasePage


class LoginPage(BasePage):
_next > form > div > div.MuiCardContent-root > h5
 login_field_xpath = "//*[@id='login']"
password_field_xpath =
_next > form > div > div.MuiCardContent-root > a
sign_in_button_xpath =
_next > form > div > div.MuiCardActions-root > div
def type_in_email(self, email):
  self.field_send_keys(self.login_field_xpath, email)
