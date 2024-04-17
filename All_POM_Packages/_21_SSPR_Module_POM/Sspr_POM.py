import pytest
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from Base_Package.Web_Driver import web_driver
from Base_Package.Web_Logger import web_logger
from Base_Package.Login_Logout_Ops import login
from All_Config_Packages._21_SSPR_Config_Fiels.Sspr_Read_INI import sspr_read_ini

class SSPR_pom(web_driver, web_logger):
    d = web_driver.d()
    logger = web_logger.logger_obj()
    status = []

    def open_portal_login_page_enter_username_password_and_click_on_login_btn_verify_password_reset_pop_up_displayed(self):
        try:
            self.logger.info("********************************** TC_SSPR_001 Started *******************************")
            self.status.clear()
            self.open_portal_url_if_not_open()
            self.enter_username_password_and_click_on_login()
            self.verify_password_change_pop_up_is_displayed()
            self.logger.info(f"status: {self.status}")

        except Exception as ex:
            self.logger.info(f"open_portal_login_page_enter_username_password_and_click_on_login_btn_verify_password_reset_pop_up_displayed ex: {ex.args}")


    # **************************** User Methods ****************************************

    def verify_password_change_pop_up_is_displayed(self):
        try:
            self.explicit_wait(5, "XPATH", sspr_read_ini().change_password_popup_by_xpath(), self.d)
            password_change_pop_up = self.d.find_elements(By.XPATH, sspr_read_ini().change_password_popup_by_xpath())
            if len(password_change_pop_up) > 0:
                if password_change_pop_up[0].is_displayed():
                    self.logger.info(f"password change pop up is visible: {password_change_pop_up[0].is_displayed()}")
                    self.status.append(True)
                else:
                    self.logger.info(f"password change pop up is not visible")
                    self.status.append(False)
            else:
                self.logger.info("password change pop up not displayed or not found")

        except Exception as ex:
            self.logger.info(f"verify_password_change_pop_up_is_displayed ex: {ex.args}")

    def enter_username_password_and_click_on_login(self):
        try:
            username = sspr_read_ini().get_username()
            password = sspr_read_ini().get_password()
            username_text_box = self.explicit_wait(5, "XPATH", sspr_read_ini().get_username_text_box_by_xpath(), self.d)
            password_text_box = self.explicit_wait(5, "XPATH", sspr_read_ini().password_textbox_by_xpath(), self.d)
            login_link = self.explicit_wait(5, "XPATH", sspr_read_ini().login_link_by_xpath(), self.d)

            if username_text_box.is_displayed():
                username_text_box.click()
                username_text_box.clear()
                username_text_box.send_keys(username)
                self.logger.info(f"username entered")
            if password_text_box.is_displayed():
                password_text_box.click()
                password_text_box.clear()
                password_text_box.send_keys(password)
                self.logger.info(f"password entered")
            if login_link.is_displayed():
                self.logger.info(f"login link is visible.")
                login_link.click()
        except Exception as ex:
            self.logger.info(f"enter_username_password_and_click_on_login ex: {ex.args}")

    def open_portal_url_if_not_open(self):
        try:
            cloud_url = sspr_read_ini().get_cloud_url()
            self.logger.info(f"cloud url: {cloud_url}")
            if self.d.current_url == cloud_url:
                username_text_box = self.d.find_elements(By.XPATH, sspr_read_ini().get_username_text_box_by_xpath())
                if len(username_text_box) > 0:
                    if username_text_box[0].is_displayed():
                        self.logger.info(f"username textbox is visible.")
                else:
                    self.logger.info("username textbox not visible")
                    logout_btn = self.d.find_elements(By.XPATH, sspr_read_ini().logout_btn_by_xpath())
                    if len(logout_btn) > 0:
                        if logout_btn[0].is_displayed():
                            logout_btn[0].click()
                    else:
                        self.logger.info("Logout btn is not visible.")

            else:
                self.d.get(cloud_url)
                self.d.maximize_window()

        except Exception as ex:
            self.logger.info(f"open_portal_url_if_not_open ex: {ex.args}")

