import datetime
import random
import time
from pathlib import Path
import pyautogui
from selenium.common import ElementNotInteractableException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from All_Config_Packages._12_Identify_and_Enroll_Config_Files.Identify_and_Enroll_Readd_INI import \
    Read_Identify_and_Enroll_Components
from All_Config_Packages._4_Users_Module_Config_Files.Users_Read_INI import Read_Users_Components
# from All_Test_Cases_Package.conftest import web_driver
from Base_Package.Web_Driver import web_driver
from Base_Package.Web_Logger import web_logger
from Base_Package.Login_Logout_Ops import login
# from Config_Package.INI_Config_Files.Audit_Log_Report_Read_INI import Audit_Log_Report_Components
# from Config_Package.INI_Config_Files.Portal_Menu_Read_INI import Read_Portal_Menu_Components
from All_Config_Packages._16_Audit_Log_Report_Module_Config_Files.Audit_Log_Report_Read_INI import \
    Audit_Log_Report_Components


def generate_random_number():
    return random.randint(1, 10000)


def date_difference_from_today(target_date_str, date_format="%m/%d/%Y"):
    try:
        # Convert the target date string to a datetime object
        target_date = datetime.datetime.strptime(target_date_str, date_format)
        # Get the current date
        current_date = datetime.datetime.now()
        # Calculate the difference between the target date and the current date
        difference = abs(target_date - current_date)
        return difference.days  # Returns the difference in days
    except ValueError:
        raise ValueError("Invalid date format. Please provide dates in the format 'm/d/Y'.")


def are_dates_ascending(date_strings):
    # Check if each date is greater than or equal to the previous date

    date_parts_list = [date_str.split(', ') for date_str in date_strings]

    for i in range(1, len(date_parts_list)):
        current_date_parts = date_parts_list[i]
        previous_date_parts = date_parts_list[i - 1]

        current_date = datetime.datetime.strptime(current_date_parts[0], '%m/%d/%Y')
        previous_date = datetime.datetime.strptime(current_date_parts[0], '%m/%d/%Y')
        if current_date < previous_date:
            return True
    return True


def is_datetime_accurate(datetime_str, tolerance_seconds=60):
    # Convert the input datetime string to a datetime object
    input_datetime = datetime.datetime.strptime(datetime_str, '%m/%d/%Y, %I:%M:%S %p')

    # Get the current datetime
    current_datetime = datetime.datetime.now()

    # Calculate the difference in seconds between the current time and the input datetime
    time_difference = (current_datetime - input_datetime).total_seconds()
    # Check if the absolute time difference is within the tolerance range
    if abs(time_difference) >= tolerance_seconds:
        return True
    else:
        return False


def is_valid_date_format(date_str, date_format='%m/%d/%Y'):
    try:
        datetime.datetime.strptime(date_str, date_format)
        return True
    except ValueError:
        return False


def is_valid_time_format(time_str, time_format='%I:%M:%S %p'):
    try:
        datetime.datetime.strptime(time_str, time_format)
        return True
    except ValueError:
        return False


def filter_login_logout(target_text):
    temp = str(target_text).replace("-", "")
    temp = temp.replace("/", "")
    temp = temp.replace(" ", "")
    return temp


def is_ascending(lst):
    return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))


class Audit_log_report_pom(web_driver, web_logger):
    d = web_driver.d()
    logger = web_logger().logger_obj()
    status = []
    now = (datetime.datetime.now())
    DATE_IE = now.strftime('%d-%m-%Y')
    TIME_IE = now.strftime('%H:%M')
    AM_PM_IE = now.strftime('%p')

    def dateTimeAMPM(self, date_incident):
        date_incident.send_keys(self.DATE_IE)
        time.sleep(web_driver.two_second)
        date_incident.send_keys(self.TIME_IE)
        time.sleep(web_driver.two_second)
        date_incident.send_keys(self.AM_PM_IE)
        time.sleep(web_driver.two_second)

    # def close_current_tab(self):
    #     tab_list = self.d.window_handles
    #     tab_count = len(tab_list)
    #     self.logger.info(f"tab count: {tab_count}")
    #     while tab_count > 1:
    #         win = self.d.window_handles[tab_count - 1]
    #         self.d.switch_to.window(win)
    #         tab_count -= 1
    #         self.d.close()

    def login_before(self):
        # login().login_to_cloud_if_not_done(self.d)
        try:
            login_object = login()
            self.logger.info(f"url: {login_object.cloud_url}")
            self.d.get(login_object.cloud_url)
            # login_object.username_textbox.send_keys(login_object.config().get("user_info", "username"))
            # time.sleep(web_driver.two_second)
            # login_object.password_textbox.send_keys(login_object.config().get("user_info", "password"))
            # time.sleep(web_driver.two_second)
            # login_object.login_btn.click()
            web_driver.implicit_wait(self, web_driver.two_second, self.d)
            time.sleep(web_driver.two_second)
            username = self.d.find_element(By.XPATH,
                                           login_object.config.get("login_page_locators", "username_textbox_by_xpath"))
            web_driver.explicit_wait(self, 10, username, self.d)
            username.send_keys(login_object.config.get("user_info", "username"))
            web_driver.implicit_wait(self, web_driver.two_second, self.d)
            time.sleep(web_driver.two_second)
            password = self.d.find_element(By.XPATH,
                                           login_object.config.get("login_page_locators", "password_textbox_by_xpath"))
            password.send_keys(login_object.config.get("user_info", "password"))
            web_driver.explicit_wait(self, 10, password, self.d)
            web_driver.implicit_wait(self, web_driver.two_second, self.d)
            login_btn = self.d.find_element(By.XPATH,
                                            login_object.config.get("login_page_locators", "login_link_by_xpath"))
            self.d.execute_script("arguments[0].click();", login_btn)
            web_driver.implicit_wait(self, 10, self.d)
            self.d.maximize_window()
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\login_before.png")
            self.logger.info(f"login_before:  {ex}")
            return False
        # pass

    def login(self):
        if self.d.title == "" or self.d.find_element(By.ID,
                                                     Audit_Log_Report_Components().get_loginButton()).is_displayed():
            self.login_before()
            time.sleep(web_driver.two_second)

    def Verify_user_is_able_to_generate_report_for_Approver_enrollments_and_download_excel_file(self):
        try:
            self.logger.info("******************************** TC_ALR_01 Started ***********************************")
            self.status.clear()
            login().login_to_facecirst_portal_if_not_done(self.d)
            self.click_on_alr_and_option_alr_panel()
            self.switch_control_to_alr_panel()
            self.click_on_report_type_dropdown_on_alr_panel()
            report_type = "Approver Enrollments"
            self.select_type_of_report_you_want_to_generate(report_type)
            self.click_on_custom_date_range()
            date_range = "Last 7 days"
            self.select_custom_date_range(date_range)
            self.click_on_users_select_dropdown()
            user = "All Users"
            self.select_user_from_users_dropdown_list(user)
            self.click_on_outside_panel()
            self.click_on_submit_report()
            self.status.append(self.verify_report_title_is_visible())
            self.status.append(self.click_on_download_btn())

            self.logger.info(f"self.status: {self.status}")
            self.logger.info("******************************** TC_ALR_01 End ***********************************")
            if None in self.status:
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_ALR_01_failed.png")
                self.close_current_tab()
                return False
            elif False in self.status:
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_ALR_01_failed.png")
                self.close_current_tab()
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_ALR_01_exception.png")
            self.logger.info(f"Verify_user_is_able_to_generate_report_for_Approver_enrollments_and_download_excel_file ex: {ex.args}")
            return False

    def Verify_user_is_able_to_generate_report_for_user_enrollments_and_download_excel_file(self):
        try:
            self.logger.info("******************************** TC_ALR_02 Started ***********************************")
            self.status.clear()
            login().login_to_facecirst_portal_if_not_done(self.d)
            self.click_on_alr_and_option_alr_panel()
            self.switch_control_to_alr_panel()
            self.click_on_report_type_dropdown_on_alr_panel()
            report_type = "User Enrollments"
            self.select_type_of_report_you_want_to_generate(report_type)
            self.click_on_custom_date_range()
            date_range = "Last 7 days"
            self.select_custom_date_range(date_range)
            self.click_on_users_select_dropdown()
            user = "All Users"
            self.select_user_from_users_dropdown_list(user)
            self.click_on_outside_panel()
            self.click_on_submit_report()
            self.status.append(self.verify_report_title_is_visible())
            self.status.append(self.click_on_download_btn())

            self.logger.info(f"status: {self.status}")
            self.logger.info("******************************** TC_ALR_02 End ***********************************")
            if None in self.status:
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_ALR_02_failed.png")
                self.close_current_tab()
                return False
            elif False in self.status:
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_ALR_02_failed.png")
                self.close_current_tab()
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_ALR_02_exception.png")
            self.logger.info(f"Verify_user_is_able_to_generate_report_for_user_enrollments_and_download_excel_file ex: {ex.args}")
            return False

    def Verify_user_is_able_to_generate_report_for_log_in_log_out_and_download_excel_file(self):
        try:
            self.logger.info("******************************** TC_ALR_03 Started ***********************************")
            self.status.clear()
            login().login_to_facecirst_portal_if_not_done(self.d)
            self.click_on_alr_and_option_alr_panel()
            self.switch_control_to_alr_panel()
            self.click_on_report_type_dropdown_on_alr_panel()
            report_type = "Log-in / Log-out"
            self.select_type_of_report_you_want_to_generate(report_type)
            self.click_on_custom_date_range()
            date_range = "Last 7 days"
            self.select_custom_date_range(date_range)
            self.click_on_users_select_dropdown()
            user = "All Users"
            self.select_user_from_users_dropdown_list(user)
            self.click_on_outside_panel()
            self.click_on_submit_report()
            self.status.append(self.verify_report_title_is_visible())
            self.status.append(self.click_on_download_btn())
            self.close_current_tab()
            self.logger.info(f"status: {self.status}")
            self.logger.info("******************************** TC_ALR_03 End ***********************************")
            if None in self.status:
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_ALR_03_failed.png")
                self.close_current_tab()
                return False
            elif False in self.status:
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_ALR_03_failed.png")
                self.close_current_tab()
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_ALR_03_exception.png")
            self.logger.info(f"Verify_user_is_able_to_generate_report_for_log_in_log_out_and_download_excel_file ex: {ex.args}")
            return False

    def Verify_user_is_able_to_generate_report_for_Threshold_changes_and_download_excel_file(self):
        try:
            self.logger.info("******************************** TC_ALR_04 Started ***********************************")
            self.status.clear()
            login().login_to_facecirst_portal_if_not_done(self.d)
            self.click_on_alr_and_option_alr_panel()
            self.switch_control_to_alr_panel()
            self.click_on_report_type_dropdown_on_alr_panel()
            report_type = "Threshold Changes"
            self.select_type_of_report_you_want_to_generate(report_type)
            self.click_on_custom_date_range()
            date_range = "Last 7 days"
            self.select_custom_date_range(date_range)
            self.click_on_users_select_dropdown()
            user = "All Users"
            self.select_user_from_users_dropdown_list(user)
            self.click_on_outside_panel()
            self.click_on_submit_report()
            self.status.append(self.verify_report_title_is_visible())
            self.status.append(self.click_on_download_btn())

            self.logger.info(f"status: {self.status}")
            self.logger.info("******************************** TC_ALR_04 End ***********************************")
            if None in self.status:
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_ALR_04_failed.png")
                self.close_current_tab()
                return False
            elif False in self.status:
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_ALR_04_failed.png")
                self.close_current_tab()
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_ALR_04_failed.png")
            self.logger.info(f"Verify_user_is_able_to_generate_report_for_Threshold_changes_and_download_excel_file ex: {ex.args}")
            return False

    def Verify_user_with_all_permissions_enrolled_mask_subject_should_be_in_Disable_status_for_user_enrollments(self):
        try:
            self.logger.info("******************************** TC_ALR_05 Started ***********************************")
            self.status.clear()
            login().login_to_facecirst_portal_if_not_done(self.d)
            self.enroll_masked_subject_with_user_having_all_permissions()
            self.close_all_panel_one_by_one()
            self.open_user_enrollments_report_for_all_users()
            self.verify_disabled_status_of_last_enrollment()

            self.logger.info(f"status: {self.status}")
            self.logger.info("******************************** TC_ALR_05 End ***********************************")
            if None in self.status:
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_ALR_05_failed.png")
                self.close_current_tab()
                return False
            elif False in self.status:
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_ALR_05_failed.png")
                self.close_current_tab()
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_ALR_05_exception.png")
            self.logger.info(f"Verify_user_with_all_permissions_enrolled_mask_subject_should_be_in_Disable_status_for_user_enrollments ex: {ex.args}")
            return False

    def Verify_core_should_be_able_to_enable_above_mask_subject_and_verify_Enabled_status_and_action_by_core_for_user_enrollments(self):
        try:
            self.logger.info("******************************** TC_ALR_06 Started ***********************************")
            self.status.clear()
            login().login_to_facecirst_portal_if_not_done(self.d)
            # self.enroll_normal_subject_with_user_having_all_permissions()
            self.enable_masked_enrolled_subject_with_core_credentials()
            self.select_checkbox_on_enrollment_panel()
            self.click_on_action_dropdown_on_enrollments_panel()
            self.click_on_enable_selected_enrollment_option()
            self.close_all_panel_one_by_one()
            self.open_user_enrollments_report_for_all_users()
            self.verify_enabled_status_of_last_enrollment()
            self.logger.info(f"status: {self.status}")
            self.logger.info("******************************** TC_ALR_06 End ***********************************")
            if None in self.status:
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_ALR_06_failed.png")
                self.close_current_tab()
                return False
            elif False in self.status:
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_ALR_06_failed.png")
                self.close_current_tab()
                return False
            else:
                self.close_current_tab()
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_ALR_06_exception.png")
            self.logger.info(f"Verify_core_should_be_able_to_enable_above_mask_subject_and_verify_Enabled_status_and_action_by_core_for_user_enrollments ex: {ex.args}")
            return False

    def Verify_for_above_enable_mask_subject_status_is_Enabled_in_Approver_Enrollments_too(self):
        try:
            self.logger.info("******************************** TC_ALR_07 Started ***********************************")
            self.status.clear()
            login().login_to_facecirst_portal_if_not_done(self.d)
            # self.enroll_normal_subject_with_user_having_all_permissions()
            self.enable_masked_enrolled_subject_with_core_credentials()
            self.select_checkbox_on_enrollment_panel()
            self.click_on_action_dropdown_on_enrollments_panel()
            self.click_on_enable_selected_enrollment_option()
            self.close_all_panel_one_by_one()
            self.open_approver_enrollments_report_for_all_users()
            self.verify_enabled_status_of_last_enrollment_on_approver_enrollments_report()
            self.logger.info(f"status: {self.status}")
            self.logger.info("******************************** TC_ALR_07 End ***********************************")
            if None in self.status:
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_ALR_07_failed.png")
                self.close_current_tab()
                return False
            elif False in self.status:
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_ALR_07_failed.png")
                self.close_current_tab()
                return False
            else:
                self.close_current_tab()
                return True
        except Exception as ex:
            self.logger.info(f"Verify_for_above_enable_mask_subject_status_is_Enabled_in_Approver_Enrollments_too ex: {ex.args}")

    def Verify_user_with_2FA_enrolled_subject_should_be_able_to_see_Pending_status_for_user_enrollments(self):
        try:
            self.logger.info("******************************** TC_ALR_08 Started ***********************************")
            self.status.clear()
            login().login_to_facecirst_portal_if_not_done(self.d)
        except Exception as ex:
            self.logger.info(f"Verify_user_with_2FA_enrolled_subject_should_be_able_to_see_Pending_status_for_user_enrollments ex: {ex.args}")

    # ********************************** User Methods *******************************************

    def upload_image_not_enrolled(self, img_path):

        """
        This function is usd to upload the image and click on the search button
        :return:
        """
        file_path = img_path
        time.sleep(2)
        self.logger.info(f"image uploaded: {file_path}")
        # upload_image = self.explicit_wait(10, "NAME", "image", self.d)
        upload_image = self.d.find_element(By.NAME, "image")
        upload_image.send_keys(file_path)

    def click_on_alr_and_option_alr_panel(self):
        try:
            alr_menu = self.explicit_wait(5, "XPATH", Audit_Log_Report_Components().audit_log_report_menu_btn(), self.d)
            if alr_menu.is_displayed():
                self.logger.info(f"alr menu item is visible.")
                alr_menu.click()
            else:
                self.logger.info(f"alr menu item is not visible on cloud menu.")
        except Exception as ex:
            self.logger.info(f"click_on_alr_and_option_alr_panel ex: {ex.args}")

    def click_on_report_type_dropdown_on_alr_panel(self):
        try:
            time.sleep(web_driver.one_second)
            self.logger.info(f"clicking on report type dropdown.")
            report_type = self.explicit_wait(5, "XPATH", Audit_Log_Report_Components().report_type_select(), self.d)
            if report_type.is_displayed():
                self.logger.info(f"report type dropdown is visible.")
                report_type.click()
            else:
                self.logger.info(f"report type dropdown is not visible.")

        except Exception as ex:
            self.logger.info(f"click_on_report_type_dropdown_on_alr_panel ex: {ex.args}")

    def select_type_of_report_you_want_to_generate(self, report_type):
        try:
            self.explicit_wait(5, "XPATH", Audit_Log_Report_Components().report_list_xpath(), self.d)
            report_option_list = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().report_list_xpath())
            for option in report_option_list:
                self.logger.info(f"option : {option.text}")
                if option.text == report_type:
                    option.click()
                    self.logger.info(f"{option.text} report type selected.")

        except Exception as ex:
            self.logger.info(f"select_type_of_report_you_want_to_generate ex: {ex.args}")

    def switch_control_to_alr_panel(self):
        try:
            self.d.switch_to.window(self.d.window_handles[1])
        except Exception as ex:
            self.logger.info(f"switch_control_to_alr_panel: {ex.args}")

    def click_on_custom_date_range(self):
        try:
            custom_date_range = self.explicit_wait(5, "XPATH", Audit_Log_Report_Components().filter_by_select(), self.d)
            if custom_date_range.is_displayed():
                self.logger.info(f"custom date range dropdown is visible: {custom_date_range.is_displayed()}")
                custom_date_range.click()
            else:
                self.logger.info(f"custom date range dropdown is visible: {custom_date_range.is_displayed()}")
        except Exception as ex:
            self.logger.info(f"click_on_custome_date_range ex:{ex.args}")

    def select_custom_date_range(self, date_range):
        try:
            self.explicit_wait(5, "XPATH", Audit_Log_Report_Components().report_list_xpath(), self.d)
            date_range_options = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().report_list_xpath())
            for option in date_range_options:
                self.logger.info(f"option in date range option visible: {option.text}")
                if option.text == date_range:
                    self.logger.info(f"selected date range: {option.text}")
                    option.click()

        except Exception as ex:
            self.logger.info(f"select_custom_date_range ex: {ex.args}")

    def click_on_users_select_dropdown(self):
        try:
            users_select = self.explicit_wait(5, "XPATH", Audit_Log_Report_Components().users_select(), self.d)
            if users_select.is_displayed():
                self.logger.info(f"users select dropdown is visible: {users_select.is_displayed()}")
                users_select.click()
            else:
                self.logger.info(f"users select dropdown is visible: {users_select.is_displayed()}")
        except Exception as ex:
            self.logger.info(f"click_on_users_select_dropdown ex:{ex.args}")

    def select_user_from_users_dropdown_list(self, user):
        try:
            self.explicit_wait(5, "XPATH", Audit_Log_Report_Components().user_select_options_by_xpath(), self.d)
            options_list = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().user_select_options_by_xpath())
            for option in options_list:
                self.logger.info(f"users enlisted: {option.text}")
                if option.text == user:
                    self.logger.info(f"selected user: {option.text}")
                    option.click()

        except Exception as ex:
            self.logger.info(f"select_user_from_users_dropdown_list ex: {ex.args}")

    def click_on_outside_panel(self):
        try:
            main_panel = self.explicit_wait(5, "XPATH", Audit_Log_Report_Components().main_panel_by_xpath(), self.d)
            main_panel.click()
        except Exception as ex:
            self.logger.info(f"click_on_outside_panel ex: {ex.args}")

    def click_on_submit_report(self):
        try:
            submit_report_btn = self.explicit_wait(5, "XPATH", Audit_Log_Report_Components().submit_report_button(), self.d)
            if submit_report_btn.is_displayed():
                self.logger.info(f"submit report btn is visible: {submit_report_btn.is_displayed()}")
                submit_report_btn.click()
            else:
                self.logger.info(f"submit report btn is visible: {submit_report_btn.is_displayed()}")

        except Exception as ex:
            self.logger.info(f"click_on_submit_report ex: {ex.args}")

    def verify_report_title_is_visible(self):
        try:
            report_title = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().report_type_heading_by_xpath(), self.d)
            if report_title.is_displayed():
                self.logger.info(f"report type heading is visible : {report_title.is_displayed()}")
                return True
            else:
                self.logger.info(f"report type heading is visible : {report_title.is_displayed()}")
                return False
        except Exception as ex:
            self.logger.info(f"verify_report_title_is_visible ex: {ex.args}")

    def click_on_download_btn(self):
        try:
            download_btn = self.explicit_wait(5, "XPATH", Audit_Log_Report_Components().csv_button(), self.d)

            if download_btn.is_displayed():
                self.logger.info(f" download btn : {download_btn.is_displayed()} ")
                download_btn.click()
                self.logger.info(f"download btn is clicked.")
                return True
            else:
                self.logger.info(f"download btn : {download_btn.is_displayed()}")
                return False
        except Exception as ex:
            self.logger.info(f"click_on_download_btn ex: {ex.args}")

    def close_current_tab(self):
        try:
            open_tabs = self.d.window_handles
            parent = self.d.window_handles[0]
            child = self.d.window_handles[1]
            # i = 1
            # for i in range(open_tabs):
            #     child = self.d.window_handles[i]
            self.d.switch_to.window(child)
            self.d.close()
            self.d.switch_to.window(parent)
        except Exception as ex:
            self.logger.info(f"close current tab: {ex.args}")

    def enroll_masked_subject_with_user_having_all_permissions(self):
        try:
            self.open_identify_and_enroll_panel()
            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\dataset2\\disabled.png"
            self.upload_image_not_enrolled(file_path)
            self.click_on_identify_enroll_btn_on_IE_panel()
            self.add_details_for_enrollment()
            self.verify_enrollment_success_message_after_enrollments()
        except Exception as ex:
            self.logger.info(f"enroll_masked_subject_with_user_having_all_permissions ex: {ex.args}")

    def open_identify_and_enroll_panel(self):
        try:
            identify_enroll_menu_item = self.explicit_wait(5, "XPATH", Audit_Log_Report_Components().identify_and_enroll_link_by_xpath(), self.d)
            if identify_enroll_menu_item.is_displayed():
                self.logger.info(f"identify enroll menu btn visible: {identify_enroll_menu_item.is_displayed()}")
                identify_enroll_menu_item.click()
            else:
                self.logger.info(f"identify enroll menu btn visible: {identify_enroll_menu_item.is_displayed()}")
        except Exception as ex:
            self.logger.info(f"open_identify_and_enroll_panel ex: {ex.args}")

    def click_on_identify_enroll_btn_on_IE_panel(self):
        try:
            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)
            if identify_enroll_btn.is_displayed():
                self.logger.info("Identify & Enroll button is visible...")
                self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            else:
                self.logger.info("Identify & Enroll button is not visible...")
        except Exception as ex:
            self.logger.info(f"click_on_identify_enroll_btn_on_IE_panel ex: {ex.args}")

    def add_details_for_enrollment(self):
        """
        This function is used to add details for the enrollment
        :return:
        """

        wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                        .identifying_photo_wait_by_xpath())
        count = 0
        while wait_icon.is_displayed() or count == 120:
            time.sleep(web_driver.two_second)
            count += 1
            self.logger.info(f"waiting for wait icon, count: {count}")

        time.sleep(web_driver.two_second)
        enrollment_basis = self.d.find_element(By.XPATH,
                                               Read_Identify_and_Enroll_Components().enrollment_basis_by_xpath())
        select = Select(enrollment_basis)
        select.select_by_index(1)

        time.sleep(web_driver.two_second)
        enrollment_group = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .enrollment_group_by_xpath())
        select = Select(enrollment_group)
        select.select_by_index(2)
        time.sleep(web_driver.one_second)
        region_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().region_btn_by_xpath())
        time.sleep(web_driver.one_second)
        region_btn.click()
        time.sleep(web_driver.one_second)
        region_names = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().edge_name_list())
        edge_name = Read_Identify_and_Enroll_Components().edge_name()
        for i in range(len(region_names)):
            if edge_name in region_names[i].text:
                region_names[i].click()
                break
        save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().save_btn_by_xpath())
        save_btn.click()
        time.sleep(web_driver.two_second)

        enrollment_group = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .enrollment_group_by_xpath())
        select = Select(enrollment_group)
        select.select_by_index(1)

        location_store = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                             .location_store_inpt_bx_by_xpath())
        location_store.send_keys(Read_Identify_and_Enroll_Components().location_store_data())

        case_subject = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                           .case_subject_inpt_bx_by_xpath())
        case_subject.send_keys(Read_Identify_and_Enroll_Components().case_subject_data())

        reported_loss = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .reported_loss_inpt_bx_by_xpath())
        reported_loss.send_keys(Read_Identify_and_Enroll_Components().reported_loss_data())

        date_incident = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .date_incident_inpt_bx_by_xpath())
        time.sleep(web_driver.two_second)
        self.dateTimeAMPM(date_incident)
        time.sleep(web_driver.two_second)
        action_input = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                           .action_inpt_bx_by_xpath())
        action_input.send_keys(Read_Identify_and_Enroll_Components().action_input_data())

        save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .add_details_save_btn_by_xpath())
        save_btn.click()
        self.logger.info("Enrollment details filled and save btn is clicked")
        wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                        .enrollment_success_loader())
        count = 0
        while wait_icon.is_displayed() or count == 120:
            time.sleep(web_driver.two_second)
            count += 1
            self.logger.info(f"waiting for wait icon, count: {count}")

    def close_all_panel_one_by_one(self):
        try:
            # close_panel_list = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().close_all_panel_one_by_one())
            time.sleep(web_driver.one_second)
            cloud_menu = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().cloud_menu_by_xpath())
            cloud_menu.click()
            web_driver.implicit_wait(self, web_driver.one_second, self.d)
            close_all_panels_menu = self.d.find_elements(By.XPATH,
                                                         Read_Identify_and_Enroll_Components().close_all_panels_btn_by_xpath())
            time.sleep(web_driver.one_second)
            if len(close_all_panels_menu) > 0:
                close_all_panels_menu[0].click()
                time.sleep(web_driver.one_second)
                try:
                    self.d.switch_to.alert.accept()
                except Exception as ex:
                    self.logger.info(f"exception: {ex.args}")
                    self.logger.info("Alert handled")
            else:
                pass
            time.sleep(web_driver.one_second)

        except Exception as ex:
            self.logger.error(f"Exception crated: {ex.args}")
            self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\test_TC_IE_20_exception.png")
            return False

    def verify_enrollment_success_message_after_enrollments(self):
        try:
            self.logger.info(f"verifying success message")
            success_msg = self.explicit_wait(10, "XPATH",
                                             Read_Identify_and_Enroll_Components().enrollment_success_msg_xpath(),
                                             self.d)
            if success_msg.text.lower() == Read_Identify_and_Enroll_Components().enrollment_success_msg_validation(). \
                    lower():
                self.logger.info(f"Success msg is visible : {True}")
                self.status.append(True)
            else:
                self.logger.info(f"Success msg is visible : {False}")
                self.status.append(False)
        except Exception as ex:
            self.logger.info(f"verify_enrollment_success_message_after_enrollments ex: {ex.args}")

    def open_user_enrollments_report_for_all_users(self):
        try:
            self.logger.info(f"opening user enrollments report with all users")
            self.click_on_alr_and_option_alr_panel()
            self.switch_control_to_alr_panel()
            self.click_on_report_type_dropdown_on_alr_panel()
            report_type = "User Enrollments"
            self.select_type_of_report_you_want_to_generate(report_type)
            self.click_on_custom_date_range()
            date_range = "Last 7 days"
            self.select_custom_date_range(date_range)
            self.click_on_users_select_dropdown()
            user = "All Users"
            self.select_user_from_users_dropdown_list(user)
            self.click_on_outside_panel()
            self.click_on_submit_report()
            self.status.append(self.verify_report_title_is_visible())
            self.logger.info("user enrollments report opened.")
        except Exception as ex:
            self.logger.info(f"open_user_enrollments_report_for_all_users ex: {ex.args}")

    def verify_disabled_status_of_last_enrollment(self):
        try:
            last_page_btn = self.explicit_wait(5, "XPATH", Audit_Log_Report_Components().last_page_btn_by_xpath(), self.d)
            self.logger.info(f"last page btn is visible: {last_page_btn.is_displayed()}")
            if last_page_btn.is_enabled():
                last_page_btn.click()
            if last_page_btn.is_enabled():
                last_page_btn.click()
            else:
                enrollment_Status = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().user_enrollment_status_list())
                for status in enrollment_Status:
                    self.logger.info(f"status: {status.text}")
                if enrollment_Status[-1].text == "Disabled":
                    self.status.append(True)
                else:
                    self.status.append(False)

        except Exception as ex:
            self.logger.info(f"verify_disabled_status_of_last_enrollment ex: {ex.args}")

    def enroll_normal_subject_with_user_having_all_permissions(self):
        try:
            self.open_identify_and_enroll_panel()
            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\dataset2\\img1.png"
            self.upload_image_not_enrolled(file_path)
            self.click_on_identify_enroll_btn_on_IE_panel()
            self.add_details_for_enrollment()
            self.verify_enrollment_success_message_after_enrollments()
        except Exception as ex:
            self.logger.info(f"enroll_masked_subject_with_user_having_all_permissions ex: {ex.args}")

    def verify_enabled_status_of_last_enrollment(self):
        try:
            last_page_btn = self.explicit_wait(5, "XPATH", Audit_Log_Report_Components().last_page_btn_by_xpath(), self.d)
            self.logger.info(f"last page btn is visible: {last_page_btn.is_displayed()}")
            if last_page_btn.is_enabled():
                last_page_btn.click()
            if last_page_btn.is_enabled():
                last_page_btn.click()
            else:
                enrollment_Status = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().user_enrollment_status_list())
                for status in enrollment_Status:
                    self.logger.info(f"status: {status.text}")
                if enrollment_Status[-1].text == "Enabled":
                    self.status.append(True)
                else:
                    self.status.append(False)

        except Exception as ex:
            self.logger.info(f"verify_disabled_status_of_last_enrollment ex: {ex.args}")

    def enable_masked_enrolled_subject_with_core_credentials(self):
        try:
            self.open_enrollments_panel()
            self.select_disabled_option_inside_filter_dropdown()
        except Exception as ex:
            self.logger.info(f"enable_masked_enrolled_subject_with_core_credentials ex: {ex.args}")

    def open_enrollments_panel(self):
        try:
            enrollments_panel_menu_item = self.explicit_wait(5, "XPATH", Audit_Log_Report_Components().enrollments_portal_menu(), self.d)
            self.logger.info(f"enrollments menu item is visible: {enrollments_panel_menu_item.is_displayed()}")
            if enrollments_panel_menu_item.is_displayed():
                enrollments_panel_menu_item.click()

            else:
                self.logger.info("enrollments menu btn is not visible")

        except Exception as ex:
            self.logger.info(f"open_enrollments_panel ex: {ex.args}")

    def select_disabled_option_inside_filter_dropdown(self):
        try:
            filter_dropdown = self.explicit_wait(5, "XPATH", Audit_Log_Report_Components().filter_dropdown_on_enrollments_panel_by_xpath(), self.d)
            self.logger.info(f"filter dropdown visible: {filter_dropdown.is_displayed()}")
            if filter_dropdown.is_displayed():
                filter_dropdown.click()
            else:
                self.logger.info(f"filter dropdown is not visible.")

            disable_option = self.explicit_wait(5, "XPATH", Audit_Log_Report_Components().disable_option_under_filter_dropdown_by_xpath(), self.d)
            self.logger.info(f"disable option visible: {disable_option.is_displayed()}")
            if disable_option.is_displayed():
                disable_option.click()
            else:
                self.logger.info("disable option is not visible.")

        except Exception as ex:
            self.logger.info(f"select_disabled_option_inside_filter_dropdown ex: {ex.args}")

    def select_checkbox_on_enrollment_panel(self):
        try:
            select_checkbox = self.explicit_wait(5, "XPATH", Audit_Log_Report_Components().select_checkbox_on_enrollments_panel_by_xpath(), self.d)
            self.logger.info(f"select checkbox visible: {select_checkbox.is_displayed()}")
            if select_checkbox.is_displayed():
                select_checkbox.click()
            else:
                self.logger.info("select checkbox is not visible.")
        except Exception as ex:
            self.logger.info(f"select_checkbox_on_enrollment_panel ex: {ex.args}")

    def click_on_action_dropdown_on_enrollments_panel(self):
        try:
            action_dropdown = self.explicit_wait(5, "XPATH", Audit_Log_Report_Components().enrollment_groups_action_drop_down(), self.d)
            self.logger.info(f"action dropdown visible: {action_dropdown.is_displayed()}")
            if action_dropdown.is_displayed():
                action_dropdown.click()
            else:
                self.logger.info("action dropdown is not visible")
        except Exception as ex:
            self.logger.info(f"click_on_action_dropdown_on_enrollments_panel ex: {ex.args}")

    def click_on_enable_selected_enrollment_option(self):
        try:
            enable_selected_enrollment_option = self.explicit_wait(5, "XPATH", Audit_Log_Report_Components().enable_selected_enrollment_option_on_enrollments_panel_by_xpath(), self.d)
            self.logger.info(f"enable selected enrollment option visible: {enable_selected_enrollment_option.is_displayed()}")
            if enable_selected_enrollment_option.is_displayed():
                enable_selected_enrollment_option.click()
            else:
                self.logger.info("enable selected enrollments panel is visible.")

        except Exception as ex:
            self.logger.info(f"click_on_enable_selected_enrollment_option ex: {ex.args}")

    def open_approver_enrollments_report_for_all_users(self):
        try:
            self.logger.info(f"opening user enrollments report with all users")
            self.click_on_alr_and_option_alr_panel()
            self.switch_control_to_alr_panel()
            self.click_on_report_type_dropdown_on_alr_panel()
            report_type = "Approver Enrollments"
            self.select_type_of_report_you_want_to_generate(report_type)
            self.click_on_custom_date_range()
            date_range = "Last 7 days"
            self.select_custom_date_range(date_range)
            self.click_on_users_select_dropdown()
            user = "All Users"
            self.select_user_from_users_dropdown_list(user)
            self.click_on_outside_panel()
            self.click_on_submit_report()
            self.status.append(self.verify_report_title_is_visible())
            self.logger.info("user enrollments report opened.")
        except Exception as ex:
            self.logger.info(f"open_approver_enrollments_report_for_all_users ex: {ex.args}")

    def verify_enabled_status_of_last_enrollment_on_approver_enrollments_report(self):
        try:
            last_page_btn = self.explicit_wait(5, "XPATH", Audit_Log_Report_Components().last_page_btn_by_xpath(),
                                               self.d)
            self.logger.info(f"last page btn is visible: {last_page_btn.is_displayed()}")
            if last_page_btn.is_enabled():
                last_page_btn.click()
            if last_page_btn.is_enabled():
                last_page_btn.click()
            else:
                enrollment_Status = self.d.find_elements(By.XPATH,
                                                         Audit_Log_Report_Components().enrollment_status_list_in_report())
                for status in enrollment_Status:
                    self.logger.info(f"status: {status.text}")
                if enrollment_Status[-1].text == "Enabled":
                    self.status.append(True)
                else:
                    self.status.append(False)
        except Exception as ex:
            self.logger.info(f"verify_enabled_status_of_last_enrollment_on_approver_enrollments_report ex: {ex.args}")
