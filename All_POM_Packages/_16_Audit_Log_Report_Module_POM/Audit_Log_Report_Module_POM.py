import datetime
import random
import time
from pathlib import Path
import pyautogui
from selenium.common import ElementNotInteractableException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

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

    now = (datetime.datetime.now())
    DATE_IE = now.strftime('%m-%d-%Y')
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
            status = []
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
            status.append(self.verify_report_title_is_visible())
            status.append(self.click_on_download_btn())
            self.close_current_tab()
            self.logger.info(f"status: {status}")
            self.logger.info("******************************** TC_ALR_01 End ***********************************")
            if None in status:
                return False
            elif False in status:
                return False
            else:
                return True
        except Exception as ex:
            self.logger.info(f"Verify_user_is_able_to_generate_report_for_Approver_enrollments_and_download_excel_file ex: {ex.args}")

    def Verify_user_is_able_to_generate_report_for_user_enrollments_and_download_excel_file(self):
        try:
            self.logger.info("******************************** TC_ALR_02 Started ***********************************")
            status = []
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
            status.append(self.verify_report_title_is_visible())
            status.append(self.click_on_download_btn())
            self.close_current_tab()
            self.logger.info(f"status: {status}")
            self.logger.info("******************************** TC_ALR_02 End ***********************************")
            if None in status:
                return False
            elif False in status:
                return False
            else:
                return True
        except Exception as ex:
            self.logger.info(f"Verify_user_is_able_to_generate_report_for_user_enrollments_and_download_excel_file ex: {ex.args}")

    def Verify_user_is_able_to_generate_report_for_log_in_log_out_and_download_excel_file(self):
        try:
            self.logger.info("******************************** TC_ALR_03 Started ***********************************")
            status = []
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
            status.append(self.verify_report_title_is_visible())
            status.append(self.click_on_download_btn())
            self.close_current_tab()
            self.logger.info(f"status: {status}")
            self.logger.info("******************************** TC_ALR_03 End ***********************************")
            if None in status:
                return False
            elif False in status:
                return False
            else:
                return True
        except Exception as ex:
            self.logger.info(f"Verify_user_is_able_to_generate_report_for_log_in_log_out_and_download_excel_file ex: {ex.args}")

    def Verify_user_is_able_to_generate_report_for_Threshold_changes_and_download_excel_file(self):
        try:
            self.logger.info("******************************** TC_ALR_04 Started ***********************************")
            status = []
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
            status.append(self.verify_report_title_is_visible())
            status.append(self.click_on_download_btn())
            self.close_current_tab()
            self.logger.info(f"status: {status}")
            self.logger.info("******************************** TC_ALR_04 End ***********************************")
            if None in status:
                return False
            elif False in status:
                return False
            else:
                return True
        except Exception as ex:
            self.logger.info(f"Verify_user_is_able_to_generate_report_for_Threshold_changes_and_download_excel_file ex: {ex.args}")

    # ********************************** User Methods *******************************************

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
