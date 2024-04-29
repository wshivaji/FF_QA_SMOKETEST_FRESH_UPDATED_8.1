import time
from selenium import webdriver
import pyautogui
from selenium.webdriver.common.by import By
from All_Config_Packages._1_Portal_Login_Module_Config_Files.Portal_Login_Page_Read_INI import Portal_login_page_read_ini
from Base_Package.Login_Logout_Ops import login
from Base_Package.Web_Driver import web_driver
from Base_Package.Web_Logger import web_logger


class Portal_Login_Page_Pom(web_driver, web_logger):
    d = web_driver.d()
    logger = web_logger.logger_obj()
    status = []

    def wait_for_element_to_appear(self, element_list, xpath):
        count = 0
        if len(element_list) == 0:
            while len(element_list) == 0 or count == 10:
                element_list = self.d.find_elements(By.XPATH, xpath)
                time.sleep(web_driver.one_second)
                if len(element_list) > 0:
                    self.logger.info("element is visible...")
                    return element_list[0]
                else:
                    self.logger.info("waiting for element...")
                count += 1
                self.logger.info(f"wait count: {count}")
        else:
            self.logger.info(f"element length: {len(element_list)}")
            return element_list[0]

    def open_portal_url_and_verify_expected_url_is_visible_verify_expected_page_title_is_visible_and_verify_face_first_logo_is_visible(self):
        try:
            self.logger.info("********** TC_Portal_Login_01 started ********")
            self.logger.info("open_portal_url_and_verify_expected_url_is_visible_verify_expected_page_title_is_visible_and_verify_face_first_logo_is_visible")
            self.load_portal_login_page_if_not_loaded()
            time.sleep(web_driver.one_second)
            actual_url = self.d.current_url
            self.logger.info(f"actual url: {actual_url}")
            expected_url = Portal_login_page_read_ini().get_portal_url()
            self.logger.info(f"expected Portal url: {expected_url}")

            if actual_url == expected_url:
                self.status.append(True)
            else:
                self.status.append(False)
            actual_title = self.d.title
            self.logger.info(f"actual title: {actual_title}")
            expected_title = Portal_login_page_read_ini().get_portal_title()
            self.logger.info(f"expected title: {expected_title}")
            if actual_title == expected_title:
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)

            if self.explicit_wait(10, "XPATH", Portal_login_page_read_ini().get_face_first_company_logo_by_xpath(), self.d). \
                    is_displayed():
                self.logger.info(f"logo image is visible: ")
                self.status.append(True)
            else:
                self.logger.error(f"logo image is not visible: ")
                self.status.append(False)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Portal_Login_01.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Portal_Login_01.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Portal_Login_01_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Portal_Login_01_exception.png")
            self.logger.error(f"TC_Portal_Login_01 got exception as: {ex}")

    def verify_user_login_with_valid_credentials_and_click_on_cloud_login_and_verify_it_is_navigating_to_cloud_menu_panel(
            self):
        try:
            self.logger.info("********** TC_Portal_Login_02 started ********")
            self.logger.info("verify_user_login_with_valid_credentials_and_click_on_cloud_login_and_verify_it_is_navigating_to_cloud_menu_panel")

            self.load_portal_login_page_if_not_loaded()
            time.sleep(web_driver.one_second)
            self.status.clear()
            time.sleep(web_driver.one_second)
            username_textbox = self.explicit_wait(10, "XPATH", Portal_login_page_read_ini()
                                                  .get_portal_login_username_textbox_by_xpath(), self.d)
            username_textbox.clear()
            time.sleep(web_driver.one_second)
            username_textbox.send_keys(Portal_login_page_read_ini().get_valid_login_username())
            self.logger.info(f"username entered: {Portal_login_page_read_ini().get_valid_login_username()}")
            time.sleep(web_driver.one_second)
            password_textbox = self.d.find_element(By.XPATH, Portal_login_page_read_ini().
                                                   get_portal_login_password_textbox_by_xpath())
            password_textbox.send_keys(Portal_login_page_read_ini().get_portal_login_password())
            self.logger.info(f"password entered: {Portal_login_page_read_ini().get_portal_login_password()}")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Portal_login_page_read_ini().get_cloud_login_button_on_portal_by_xpath()). \
                click()
            self.logger.info("Clicked on CLOUD LOGIN button....")
            time.sleep(web_driver.two_second)
            time.sleep(web_driver.one_second)
            if self.explicit_wait(10, "XPATH", Portal_login_page_read_ini()
                    .get_cloud_menu_on_dashboard_by_xpath(), self.d).is_displayed():
                self.logger.info("Login successful...")
                self.status.append(True)
            else:
                self.logger.error("user is not able to Login....")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Portal_login_page_read_ini().get_logout_button_on_portal_by_xpath()).click()
            time.sleep(web_driver.one_second)

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Portal_Login_02.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Portal_Login_02.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Portal_Login_02_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Portal_Login_02_exception.png")
            self.logger.error(f"TC_Portal_Login_02 got an exception as: {ex}")

    def verify_face_first_copy_rights_is_visible_and_clickable_click_on_copyrights_and_verify_versions_of_webapi_and_server_both_are_visible_verify_latest_version_of_webapi_and_server_is_appeared(
            self):
        try:
            self.logger.info("********** TC_Portal_Login_03 started ********")
            self.logger.info("verify_face_first_copy_rights_is_visible_and_clickable_click_on_copyrights_and_verify_versions_of_webapi_and_server_both_are_visible_verify_latest_version_of_webapi_and_server_is_appeared")

            self.load_portal_login_page_if_not_loaded()
            time.sleep(web_driver.one_second)
            self.status.clear()
            face_first_copyright = web_driver.explicit_wait(self, 5, "XPATH", Portal_login_page_read_ini().get_face_first_copyright_text_by_xpath(), self.d)
            if face_first_copyright.is_displayed():
                self.logger.info("FaceFirst Copyright is visible..")
                self.status.append(True)
            else:
                self.status.append(False)
            if face_first_copyright.is_enabled():
                self.logger.info("FaceFirst Copyright is clickable..")
                self.status.append(True)
            else:
                self.status.append(False)
            actual_copyright_text = face_first_copyright.text
            self.logger.info(f"actual copyright text: {actual_copyright_text}")
            print(f"actual copyright text: {actual_copyright_text}")
            expected_copyright_text = Portal_login_page_read_ini().get_expected_copyright_text()
            self.logger.info(f"expected copyright text: {expected_copyright_text}")

            if expected_copyright_text != actual_copyright_text:
                self.status.append(False)
            else:
                self.status.append(True)
            self.d.find_element(By.XPATH, Portal_login_page_read_ini().get_face_first_copyright_text_by_xpath()).click()
            time.sleep(web_driver.one_second)
            copyright_on_display_version_info = self.d.find_elements(By.XPATH, Portal_login_page_read_ini().get_copyright_on_display_version_page())
            copyright_on_display_version_info = self.wait_for_element_to_appear(copyright_on_display_version_info, Portal_login_page_read_ini().get_copyright_on_display_version_page())

            if actual_copyright_text in copyright_on_display_version_info.text:
                self.status.append(True)
            else:
                self.status.append(False)
            actual_webapi_text_on_version_info = self.d.find_elements(By.XPATH, Portal_login_page_read_ini().get_WebAPI_text_on_version_info_by_xpath())
            actual_webapi_text_on_version_info = self.wait_for_element_to_appear(actual_webapi_text_on_version_info, Portal_login_page_read_ini().get_WebAPI_text_on_version_info_by_xpath())
            expected_webapi_text_on_version_info = Portal_login_page_read_ini().get_expected_webapi_text_on_version_info()

            if actual_webapi_text_on_version_info.text == expected_webapi_text_on_version_info:
                self.status.append(True)
            else:
                self.status.append(False)
            actual_webapi_version_number = self.d.find_element(By.XPATH, Portal_login_page_read_ini().
                                                               get_webapi_version_info_by_xpath()).text
            self.logger.info(f"actual webapi version: {actual_webapi_text_on_version_info.text} v{actual_webapi_version_number}")
            expected_webapi_version_number = Portal_login_page_read_ini().get_expected_webapi_version_number()
            self.logger.info(
                f"expected webapi version: {expected_webapi_text_on_version_info} v{expected_webapi_version_number}")
            if actual_webapi_version_number == expected_webapi_version_number:
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            actual_server_text_on_version_info = self.d.find_element(By.XPATH, Portal_login_page_read_ini().
                                                                     get_Server_text_on_version_info_by_xpath()).text
            expected_server_text_on_version_info = Portal_login_page_read_ini(). \
                get_expected_server_text_on_version_info()
            if actual_server_text_on_version_info == expected_server_text_on_version_info:
                self.status.append(True)
            else:
                self.status.append(False)
            actual_portal_version_number = self.d.find_element(By.XPATH, Portal_login_page_read_ini().
                                                               get_portal_version_number_by_xpath()).text
            self.logger.info(
                f"actual portal version: {actual_server_text_on_version_info} v{actual_portal_version_number}")
            expected_portal_version_number = Portal_login_page_read_ini().get_expected_portal_version_number()
            self.logger.info(
                f"expected portal number: {expected_server_text_on_version_info} v{expected_portal_version_number}")
            if actual_portal_version_number == expected_portal_version_number:
                self.status.append(True)
            else:
                self.status.append(False)
            self.d.find_element(By.XPATH, Portal_login_page_read_ini().
                                get_close_button_on_version_info_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Portal_Login_03.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Portal_Login_03.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Portal_Login_03_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Portal_Login_03_exception.png")
            self.logger.error(f"TC_Portal_Login_03 got an exception as: {ex}")

    def Verify_user_login_to_webportal_should_fail_with_invalid_credentials(self):
        try:
            self.logger.info("********** TC_Portal_Login_04 started ********")
            self.logger.info("Verify_user_login_to_webportal_should_fail_with_invalid_credentials")

            self.load_portal_login_page_if_not_loaded()
            time.sleep(web_driver.one_second)
            self.status.clear()
            username_textbox = self.d.find_elements(By.XPATH, Portal_login_page_read_ini().get_portal_login_username_textbox_by_xpath())
            username_textbox = self.wait_for_element_to_appear(username_textbox, Portal_login_page_read_ini().get_portal_login_username_textbox_by_xpath())
            self.logger.info("Scenario1: verifying with valid username and invalid password")
            username_textbox.clear()
            username_textbox.send_keys(Portal_login_page_read_ini().get_valid_login_username())
            time.sleep(web_driver.one_second)

            self.logger.info(f"Entered username as: {Portal_login_page_read_ini().get_valid_login_username()}")
            password_textbox = self.d.find_elements(By.XPATH, Portal_login_page_read_ini().get_portal_login_password_textbox_by_xpath())
            password_textbox = self.wait_for_element_to_appear(password_textbox, Portal_login_page_read_ini().get_portal_login_password_textbox_by_xpath())
            password_textbox.clear()
            password_textbox.send_keys(Portal_login_page_read_ini().get_portal_login_invalid_password())
            self.logger.info(f"Entered password as: {Portal_login_page_read_ini().get_portal_login_invalid_password()}")

            login_btn = self.d.find_elements(By.XPATH, Portal_login_page_read_ini().get_cloud_login_button_on_portal_by_xpath())
            login_btn = self.wait_for_element_to_appear(login_btn, Portal_login_page_read_ini().get_cloud_login_button_on_portal_by_xpath())
            login_btn.click()
            time.sleep(web_driver.one_second)

            actual_error_invalid_password = self.d.find_elements(By.XPATH, Portal_login_page_read_ini().get_invalid_password_text_on_alert_by_xpath())
            actual_error_invalid_password = self.wait_for_element_to_appear(actual_error_invalid_password, Portal_login_page_read_ini().get_invalid_password_text_on_alert_by_xpath())

            self.logger.info(f"actual invalid password error: {actual_error_invalid_password.text}")
            expected_error_invalid_password = Portal_login_page_read_ini().get_expected_invalid_password_error_text()
            expected_password_not_matching = Portal_login_page_read_ini().get_expected_password_not_match()
            self.logger.info(f"expected error: {expected_error_invalid_password}")
            if expected_error_invalid_password in actual_error_invalid_password.text or expected_password_not_matching in actual_error_invalid_password.text:
                self.status.append(True)
            else:
                logout_btn = self.d.find_elements(By.XPATH, Portal_login_page_read_ini().get_logout_button_on_portal_by_xpath())
                logout_btn = self.wait_for_element_to_appear(logout_btn, Portal_login_page_read_ini().get_logout_button_on_portal_by_xpath())
                logout_btn.click()
                time.sleep(web_driver.one_second)
                self.status.append(False)
            invalid_login_btn = self.d.find_elements(By.XPATH, Portal_login_page_read_ini().get_close_invalid_password_alert_by_xpath())
            invalid_login_btn = self.wait_for_element_to_appear(invalid_login_btn, Portal_login_page_read_ini().get_close_invalid_password_alert_by_xpath())
            if invalid_login_btn.is_displayed():
                invalid_login_btn.click()

            # *************************************************************************************************
            self.logger.info("Scenario2: verifying with invalid username and valid password")
            username_textbox.clear()
            username_textbox.send_keys(Portal_login_page_read_ini().get_portal_login_invalid_username())

            self.logger.info(f"Entered username as: {Portal_login_page_read_ini().get_portal_login_invalid_username()}")
            password_textbox = self.d.find_elements(By.XPATH,
                                                    Portal_login_page_read_ini().get_portal_login_password_textbox_by_xpath())
            password_textbox = self.wait_for_element_to_appear(password_textbox,
                                                               Portal_login_page_read_ini().get_portal_login_password_textbox_by_xpath())
            password_textbox.clear()
            password_textbox.send_keys(Portal_login_page_read_ini().get_portal_login_password())

            self.logger.info(f"Entered password as: {Portal_login_page_read_ini().get_portal_login_password()}")
            login_btn = self.d.find_elements(By.XPATH,
                                             Portal_login_page_read_ini().get_cloud_login_button_on_portal_by_xpath())
            login_btn = self.wait_for_element_to_appear(login_btn,
                                                        Portal_login_page_read_ini().get_cloud_login_button_on_portal_by_xpath())
            login_btn.click()
            time.sleep(web_driver.one_second)

            actual_invalid_username_error_msg = self.d.find_elements(By.XPATH,
                                                                     Portal_login_page_read_ini().get_invalid_username_text_on_alert_by_xpath())
            actual_invalid_username_error_msg = self.wait_for_element_to_appear(actual_invalid_username_error_msg,
                                                                                Portal_login_page_read_ini().get_invalid_username_text_on_alert_by_xpath())

            self.logger.info(f"actual invalid username error: {actual_invalid_username_error_msg.text}")
            username = Portal_login_page_read_ini().get_portal_login_invalid_username()
            error_msg = Portal_login_page_read_ini().get_expected_invalid_username_error_text()
            expected_error_invalid_username = error_msg + " '" + username + "'"
            self.logger.info(f"expected error: {expected_error_invalid_username}")
            if expected_error_invalid_username in actual_invalid_username_error_msg.text:
                self.status.append(True)
            else:
                login_btn = self.d.find_elements(By.XPATH,
                                                 Portal_login_page_read_ini().get_logout_button_on_portal_by_xpath())
                login_btn = self.wait_for_element_to_appear(login_btn,
                                                            Portal_login_page_read_ini().get_logout_button_on_portal_by_xpath())
                login_btn.click()
                time.sleep(web_driver.one_second)
                self.status.append(False)
            invalid_username = self.d.find_elements(By.XPATH,
                                                    Portal_login_page_read_ini().get_close_invalid_username_alert_by_xpath())
            invalid_username = self.wait_for_element_to_appear(invalid_username,
                                                               Portal_login_page_read_ini().get_close_invalid_username_alert_by_xpath())
            invalid_username.click()
            # *************************************************************************************************
            self.logger.info("Scenario3: verifying with invalid username and invalid password")
            username_textbox.clear()
            username_textbox.send_keys(Portal_login_page_read_ini().get_portal_login_invalid_username())
            time.sleep(web_driver.one_second)
            self.logger.info(f"Entered username as: {Portal_login_page_read_ini().get_portal_login_invalid_username()}")

            password_textbox = self.d.find_elements(By.XPATH,
                                                    Portal_login_page_read_ini().get_portal_login_password_textbox_by_xpath())
            password_textbox = self.wait_for_element_to_appear(password_textbox,
                                                               Portal_login_page_read_ini().get_portal_login_password_textbox_by_xpath())
            password_textbox.clear()
            password_textbox.send_keys(Portal_login_page_read_ini().get_portal_login_invalid_password())

            self.logger.info(f"Entered password as: {Portal_login_page_read_ini().get_portal_login_invalid_password()}")
            login_btn = self.d.find_elements(By.XPATH,
                                             Portal_login_page_read_ini().get_cloud_login_button_on_portal_by_xpath())
            login_btn = self.wait_for_element_to_appear(login_btn,
                                                        Portal_login_page_read_ini().get_cloud_login_button_on_portal_by_xpath())
            login_btn.click()
            time.sleep(web_driver.one_second)
            actual_invalid_username_error_msg = self.d.find_elements(By.XPATH,
                                                                     Portal_login_page_read_ini().get_invalid_username_text_on_alert_by_xpath())
            actual_invalid_username_error_msg = self.wait_for_element_to_appear(actual_invalid_username_error_msg,
                                                                                Portal_login_page_read_ini().get_invalid_username_text_on_alert_by_xpath())
            self.logger.info(f"actual invalid username error: {actual_invalid_username_error_msg.text}")
            username = Portal_login_page_read_ini().get_portal_login_invalid_username()
            error_msg = Portal_login_page_read_ini().get_expected_invalid_username_error_text()
            expected_error_invalid_username = error_msg + " '" + username + "'"
            self.logger.info(f"expected error: {expected_error_invalid_username}")
            if expected_error_invalid_username in actual_invalid_username_error_msg.text:
                self.status.append(True)
            else:
                logout_btn = self.d.find_elements(By.XPATH,
                                                  Portal_login_page_read_ini().get_logout_button_on_portal_by_xpath())
                logout_btn = self.wait_for_element_to_appear(logout_btn,
                                                             Portal_login_page_read_ini().get_logout_button_on_portal_by_xpath())
                logout_btn.click()
                time.sleep(web_driver.one_second)
                self.status.append(False)
            invalid_username = self.d.find_elements(By.XPATH,
                                                    Portal_login_page_read_ini().get_close_invalid_username_alert_by_xpath())
            invalid_username = self.wait_for_element_to_appear(invalid_username,
                                                               Portal_login_page_read_ini().get_close_invalid_username_alert_by_xpath())
            invalid_username.click()

            self.logger.info(f"status: {self.status}")
            # logout().logout_from_core()
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Portal_Login_04.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Portal_Login_04.png")
                time.sleep(web_driver.one_second)
                # logout().logout_from_core()
                self.d.find_element(By.XPATH, Portal_login_page_read_ini().get_logout_button_on_portal_by_xpath()).click()
                time.sleep(web_driver.one_second)
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Portal_Login_04_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Portal_Login_04_exception.png")
            self.logger.error(f"TC_Portal_Login_04 got an exception as: {ex}")

    def verify_user_account_blocked_for_30_min_if_user_enter_wrong_password_for_6_times_verify_message_warning(self):
        try:
            self.logger.info("********** TC_Portal_Login_05 started ********")
            self.logger.info("verify_user_account_blocked_for_30_min_if_user_enter_wrong_password_for_6_times_verify_message_warning")
            self.load_portal_login_page_if_not_loaded()
            print("portal logged in")
            logout_btn = self.d.find_elements(By.XPATH, Portal_login_page_read_ini().get_logout_button_on_portal_by_xpath())
            time.sleep(web_driver.one_second)
            if len(logout_btn) > 0:
                self.logger.info("Someone already logged in..")
                logout_btn[0].click()
            else:
                self.logger.info("Unable to click logout")
            time.sleep(web_driver.two_second)
            self.status.clear()
            for x in range(7):
                self.d.find_element(By.XPATH,
                                    Portal_login_page_read_ini().get_portal_login_username_textbox_by_xpath()).clear()
                self.d.find_element(By.XPATH,
                                    Portal_login_page_read_ini().get_portal_login_username_textbox_by_xpath()). \
                    send_keys(Portal_login_page_read_ini().get_portal_login_username())
                self.d.find_element(By.XPATH,
                                    Portal_login_page_read_ini().get_portal_login_password_textbox_by_xpath()). \
                    send_keys(Portal_login_page_read_ini().get_portal_login_invalid_password())
                self.d.find_element(By.XPATH,
                                    Portal_login_page_read_ini().get_cloud_login_button_on_portal_by_xpath()).click()
                time.sleep(web_driver.one_second)
                self.logger.info(f"Wrong password entered count: {x}")
            actual_account_blocked_msg = self.d.find_element(By.XPATH, Portal_login_page_read_ini().
                                                             get_invalid_password_text_on_alert_by_xpath()).text
            self.logger.info(f"actual account blocked message: {actual_account_blocked_msg}")
            expected_account_blocked_msg = Portal_login_page_read_ini(). \
                get_account_blocked_message_after_entering_invalid_password_six_times()
            self.logger.info(f"expected message: {expected_account_blocked_msg}")
            if expected_account_blocked_msg in actual_account_blocked_msg:
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Portal_login_page_read_ini().
                                get_close_invalid_password_alert_by_xpath()).click()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Portal_Login_05.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Portal_Login_05.png")
                self.d.find_element(By.XPATH, Portal_login_page_read_ini().get_logout_button_on_portal_by_xpath()).click()
                time.sleep(web_driver.one_second)
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Portal_Login_05_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Portal_Login_05_exception.png")
            self.logger.error(f"TC_Portal_Login_05 got an exception as: {ex}")

    def load_portal_login_page_if_not_loaded(self):
        try:
            if self.d.title == Portal_login_page_read_ini().get_portal_title():
                pass
            else:
                self.d.get(Portal_login_page_read_ini().get_portal_url())
                self.d.maximize_window()
                time.sleep(web_driver.one_second)
                for i in range(4):
                    pyautogui.hotkey('ctrl', '-')
                    time.sleep(0.5)

        except Exception as ex:
            self.logger.error(ex)

