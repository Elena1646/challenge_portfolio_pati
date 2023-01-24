class LoginPage(BasePage):
Login_field_xpath = "//*[@id='login']"
password_field_xpath = "//input[@data-type='password']"
sign_in_button_xpath ="//button[@name = ‘websubmit’] "

def type_in_email(self, email):
  self.field_send_keys(self.login_field_xpath, email)

