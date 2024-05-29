from All_Config_Packages._6_Notification_Groups_Module_Config_Files.Notification_Groups_Read_INI import \
    Read_Notification_Groups_Components
from All_Config_Packages._7_Visitor_Search_Module_Config_Files.Visitor_Search_Read_INI import \
    Read_Visitor_Search_Components
from All_Config_Packages._8_Visitor_Search_Jobs_Module_Config_Files.Visitor_Search_Jobs_Read_INI import Read_Visitor_Search_jobs_Components
from All_POM_Packages.Visitor_Search_Module_POM.Visitor_Search_Module_POM import Visitor_Search_Module_pom
from Base_Package.Web_Driver import web_driver
from Base_Package.Web_Logger import web_logger
from Base_Package.Login_Logout_Ops import login
from selenium.webdriver.common.by import By
import time
import re
import pandas as pd
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains, Keys
from pathlib import Path
import pyautogui


class Visitor_Search_Jobs_Module_pom(web_driver, web_logger):
    d = web_driver.d()
    logger = web_logger.logger_obj()

    def __init__(self):
        self.end_datetime = self.end_time = self.end_date = self.end_date_and_time = self.start_datetime = \
            self.start_age = None
        self.start_time = self.start_date = self.start_date_and_time  = None

        self.custom_dates_json = \
            (f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\18_Reporting_Module\\Data_From_JSON"
             f"\\custom_dates_json.json")

    def wait_for_visitor_search_result_to_display(self):
        try:
            time.sleep(web_driver.two_second)
            visitor_search_complete = web_driver.explicit_wait(self, 60, "XPATH",
                                                               Read_Visitor_Search_jobs_Components().visitor_search_completed_banner(),
                                                               self.d)
            if visitor_search_complete.is_displayed():
                self.logger.info("Visitor Search Completed.")
            else:
                self.logger.info("Visitor Search Not Completed.")
        except Exception as ex:
            self.logger.info(f"No match found {ex.args}")

    def wait_for_element_to_appear(self, element_list, xpath):
        count = 0
        if len(element_list) == 0:
            while len(element_list) == 0 or count > 150:
                element_list = self.d.find_elements(By.XPATH, xpath)
                time.sleep(web_driver.two_second)
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

    def click_on_visitor_search_jobs_btn(self):
        time.sleep(web_driver.three_second)
        visitor_search_jobs_btn = web_driver.explicit_wait(self, 10, "XPATH",
                                 Read_Visitor_Search_jobs_Components().visitors_search_job_btn_by_xpath(),
                                 self.d)
        self.d.execute_script("arguments[0].click();", visitor_search_jobs_btn)
        time.sleep(web_driver.two_second)
        visitor_search_jobs_panel_list = self.d.find_elements(By.XPATH, Read_Visitor_Search_jobs_Components().visitor_search_jobs_panel_heading_by_xpath())
        count = 0
        while len(visitor_search_jobs_panel_list) == 0 or count > 150:
            visitor_search_jobs_panel_list = self.d.find_elements(By.XPATH, Read_Visitor_Search_jobs_Components().visitor_search_jobs_panel_heading_by_xpath())
            self.logger.info("waiting for vsj panel")
            time.sleep(web_driver.two_second)
            count += 1
            self.logger.info(f"visitor search job panel search function count: {count}")

    def login(self):
        login().login_to_cloud_if_not_done(self.d)

    #############################################################################################################

    def verify_the_visitor_search_job_contains_user_performs_visitor_search_with_date_and_org_selection(self):
        result = []
        try:
            x = Read_Notification_Groups_Components().get_user_name_input_data()
            user = x.split(',')
            login().login_with_persona_user(self.d, user[0])
            self.click_on_visitor_search()
            date = int(Read_Visitor_Search_Components().get_start_date())
            month = str(Read_Visitor_Search_Components().get_start_month())
            year = int(Read_Visitor_Search_Components().get_start_year())
            hour = str(Read_Visitor_Search_Components().get_start_hour())
            minute = Read_Visitor_Search_Components().get_start_minuet()
            period = str(Read_Visitor_Search_Components().get_start_am_pm_period())

            e_month = str(Read_Visitor_Search_Components().get_end_month())
            e_date = int(Read_Visitor_Search_Components().get_end_date())
            e_year = int(Read_Visitor_Search_Components().get_end_year())
            e_hour = str(Read_Visitor_Search_Components().get_end_hour())
            e_minute = Read_Visitor_Search_Components().get_end_minuet()
            e_period = str(Read_Visitor_Search_Components().get_end_am_pm_period())

            try:
                Visitor_Search_Module_pom().handle_calender_pop_up("from", date, month, year, hour, minute, period)
                time.sleep(web_driver.one_second)
                Visitor_Search_Module_pom().handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute,
                                                                   e_period)
                time.sleep(web_driver.three_second)
            except Exception as ex:
                print(ex)

            zone_data = Read_Visitor_Search_jobs_Components().zone_data_input()
            self.select_zone_vsj(zone_data)
            self.click_on_submit_search_button()

            matches_found = self.d.find_element(By.XPATH,
                                                Read_Visitor_Search_jobs_Components()
                                                .visitor_search_result_panel_matches_found())
            max_count = matches_found.text
            max_number = max_count.split(" ")[0]

            self.click_on_cloud_menu()
            time.sleep(web_driver.two_second)
            self.click_on_visitor_search_jobs_btn()
            time.sleep(web_driver.two_second)
            view_result = web_driver.explicit_wait(self, 10, "XPATH",
                                                   Read_Visitor_Search_jobs_Components().
                                                   visitor_search_jobs_panel_view_results(), self.d)
            # view_result = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().
            #                                   visitor_search_jobs_panel_view_results())
            view_result.click()
            self.logger.info("Clicked on view results button..")
            max_matches = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
                                              .visitors_search_jobs_panel_max_matches_by_xpath())
            max_matches_text = max_matches.text
            max_number_counted = max_matches_text.split(" ")[0]
            if max_number_counted == max_number:
                self.logger.info(f"Matches counts are equal...")
                result.append(True)
            else:
                result.append(False)
            # self.compare_thresh_hold_value_with_score()
            result.append(self.verify_region_from_match_list(zone_data))
            result.append(self.verify_date_1(date, month, year, hour, minute, period))

            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_006_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_006_exception.png")
            self.logger.info(f"test_VSJ_006_exception:  {ex}")
            return False
        finally:
            self.click_on_logout_button()

    def Verify_visitor_search_status_banner_is_visible_visitor_search_jobs_on_VSJ_panel(self):
        result = []
        try:
            self.login()
            time.sleep(web_driver.two_second)
            self.click_on_visitor_search_jobs_btn()
            search_dropdown = web_driver.explicit_wait(self, 10, "XPATH",
                                                       Read_Visitor_Search_jobs_Components().
                                                       visitor_search_jobs_panel_search_button(), self.d)
            search_dropdown.click()
            include_jobs_from_all_users = web_driver.explicit_wait(self, 10, "XPATH",
                                                                   Read_Visitor_Search_jobs_Components().
                                                                   yes_btn_for_include_jobs_for_all_users_by_xpath(),
                                                                   self.d)
            include_jobs_from_all_users.click()
            self.logger.info("Clicked on Include Jobs For All Users option...")
            time.sleep(web_driver.one_second)
            search_button = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().
                                                search_button_on_search_dialog_by_xpath())
            search_button.click()
            time.sleep(web_driver.one_second)
            status_banner = web_driver.explicit_wait(self, 10, "XPATH",
                                                     Read_Visitor_Search_jobs_Components().
                                                     visitor_search_jobs_status_banner_by_xpath(), self.d)
            status_banners = self.d.find_elements(By.XPATH, Read_Visitor_Search_jobs_Components().
                                                  visitor_search_jobs_status_banner_by_xpath())

            for i in range(len(status_banners)):
                if status_banners[i].is_displayed():
                    result.append(True)
                else:
                    result.append(False)

            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_02_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_02_exception.png")
            self.logger.info(f"test_VSJ_02_exception:  {ex}")
            return False
        finally:
            self.click_on_logout_button()

    def verify_when_user_click_on_View_Results_button_of_VSJ_should_display_visitor_search_results_panel(self):
        result = []
        try:
            self.login()
            time.sleep(web_driver.two_second)
            self.click_on_visitor_search_jobs_btn()
            search_dropdown = web_driver.explicit_wait(self, 10, "XPATH",
                                                       Read_Visitor_Search_jobs_Components().
                                                       visitor_search_jobs_panel_search_button(), self.d)
            search_dropdown.click()
            include_jobs_from_all_users = web_driver.explicit_wait(self, 10, "XPATH",
                                                                   Read_Visitor_Search_jobs_Components().
                                                                   yes_btn_for_include_jobs_for_all_users_by_xpath(),
                                                                   self.d)
            include_jobs_from_all_users.click()
            self.logger.info("Clicked on Include Jobs For All Users option...")
            time.sleep(web_driver.one_second)
            search_button = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().
                                                search_button_on_search_dialog_by_xpath())
            search_button.click()
            time.sleep(web_driver.one_second)
            view_result = web_driver.explicit_wait(self, 10, "XPATH", Read_Visitor_Search_jobs_Components().
                                                   visitor_search_jobs_panel_view_results(), self.d)
            view_result = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().visitor_search_jobs_panel_view_results())
            possible_results_found = self.d.find_elements(By.XPATH, Read_Visitor_Search_jobs_Components().possible_results_found_by_xpath())

            for i in range(len(possible_results_found)):
                if view_result.is_displayed():
                    possible_matches = possible_results_found[i].text
                    possible_matches = possible_matches.split(' ')
                    act_no_of_matches = possible_matches[0]
                    self.logger.info(f"Expected possible matches: {act_no_of_matches}")
                    time.sleep(web_driver.one_second)
                    view_result.click()
                    self.logger.info("Clicked on View Results button..")
                    ele = web_driver.explicit_wait(self, 15, "XPATH",
                                                   Read_Visitor_Search_Components().image_match_list_by_xpath(), self.d)
                    matches = self.d.find_elements(By.XPATH,
                                                   Read_Visitor_Search_Components().image_match_list_by_xpath())
                    self.logger.info(f"Actual count of matches: {len(matches)}")
                    Visitor_Search_Module_pom().verify_image_from_match_list()
                    if len(matches) == int(act_no_of_matches):
                        result.append(True)
                    else:
                        result.append(False)
                    break

            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_03_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_03_exception.png")
            self.logger.info(f"test_VSJ_03_exception:  {ex}")
            return False
        finally:
            self.click_on_logout_button()

    def Verify_the_visitor_search_job_contains_the_selected_threshold_visitors_in_date_range_and_belongs_to_search_Org_Hierarchy_Selection_when_user_performs_a_visitor_search_with_Date_Org(self):
        result = []
        try:
            x = Read_Notification_Groups_Components().get_user_name_input_data()
            user = x.split(',')
            login().login_with_persona_user(self.d, user[0])
            self.click_on_visitor_search()
            self.add_image_search()

            date = int(Read_Visitor_Search_Components().get_start_date())
            month = str(Read_Visitor_Search_Components().get_start_month())
            year = int(Read_Visitor_Search_Components().get_start_year())
            hour = str(Read_Visitor_Search_Components().get_start_hour())
            minute = Read_Visitor_Search_Components().get_start_minuet()
            period = str(Read_Visitor_Search_Components().get_start_am_pm_period())

            e_month = str(Read_Visitor_Search_Components().get_end_month())
            e_date = int(Read_Visitor_Search_Components().get_end_date())
            e_year = int(Read_Visitor_Search_Components().get_end_year())
            e_hour = str(Read_Visitor_Search_Components().get_end_hour())
            e_minute = Read_Visitor_Search_Components().get_end_minuet()
            e_period = str(Read_Visitor_Search_Components().get_end_am_pm_period())

            try:
                Visitor_Search_Module_pom().handle_calender_pop_up("from", date, month, year, hour, minute, period)
                time.sleep(web_driver.one_second)
                Visitor_Search_Module_pom().handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute,
                                                                   e_period)
                time.sleep(web_driver.three_second)
            except Exception as ex:
                print(ex)

            # org_hierarchy_btn_by_xpath = web_driver.explicit_wait(self, 10, "XPATH",
            #                                                       Read_Visitor_Search_jobs_Components().zone_by_xpath(),
            #                                                       self.d)
            # org_hierarchy_btn_by_xpath.click()
            zone_data = Read_Visitor_Search_jobs_Components().zone_data_input()
            self.select_zone_vsj(zone_data)

            threshold_data = self.set_thresh_hold_slider()

            count_data = Read_Visitor_Search_jobs_Components().matches_count_data_input()
            self.select_count(count_data)

            self.click_on_submit_search_button()
            # Visitor_Search_Module_pom().wait_for_visitor_search_result_to_display()

            matches_found = self.d.find_element(By.XPATH,
                                                Read_Visitor_Search_jobs_Components()
                                                .visitor_search_result_panel_matches_found())
            max_count = matches_found.text
            max_number = max_count.split(" ")[0]

            result.append(int(max_number) <= int(threshold_data))
            self.logger.info(f" {int(max_number) <= int(threshold_data)}")
            result.append(int(max_number) <= int(count_data))

            self.click_on_cloud_menu()
            time.sleep(web_driver.two_second)

            self.click_on_visitor_search_jobs_btn()
            time.sleep(web_driver.two_second)
            view_result = web_driver.explicit_wait(self, 10, "XPATH",
                                                   Read_Visitor_Search_jobs_Components().
                                                   visitor_search_jobs_panel_view_results(), self.d)
            # view_result = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().
            #                                   visitor_search_jobs_panel_view_results())
            view_result.click()
            self.logger.info("Clicked on view results button..")
            max_matches = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
                                              .visitors_search_jobs_panel_max_matches_by_xpath())
            max_matches_text = max_matches.text
            max_number_counted = max_matches_text.split(" ")[0]
            if max_number_counted == max_number:
                self.logger.info(f"Matches counts are equal...")
                result.append(True)
            else:
                result.append(False)
            self.compare_thresh_hold_value_with_score()
            result.append(self.verify_region_from_match_list(zone_data))

            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_04_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            print(ex)
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_04_exception.png")
            self.logger.info(f"test_VSJ_04_exception:  {ex}")
            return False
        finally:
            self.click_on_logout_button()

    def select_jobs_for_all_users(self):
        try:
            search_dropdown = web_driver.explicit_wait(self, 10, "XPATH",
                                                       Read_Visitor_Search_jobs_Components().
                                                       visitor_search_jobs_panel_search_button(), self.d)
            search_dropdown.click()
            time.sleep(web_driver.one_second)
            include_jobs_from_all_users = web_driver.explicit_wait(self, 10, "XPATH",
                                                                   Read_Visitor_Search_jobs_Components().
                                                                   yes_btn_for_include_jobs_for_all_users_by_xpath(),
                                                                   self.d)
            include_jobs_from_all_users.click()
            self.logger.info("Clicked on Include Jobs For All Users option...")
            time.sleep(web_driver.one_second)
            search_button = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().
                                                search_button_on_search_dialog_by_xpath())
            search_button.click()
            time.sleep(web_driver.one_second)
        except Exception as ex:
            self.logger.info(f"Select jobs for all users got an exception as: {ex}")

    def select_date_range(self):
        try:
            search_dropdown = web_driver.explicit_wait(self, 10, "XPATH",
                                                       Read_Visitor_Search_jobs_Components().
                                                       visitor_search_jobs_panel_search_button(), self.d)
            search_dropdown.click()
            time.sleep(web_driver.one_second)
            date = int(Read_Visitor_Search_Components().get_start_date())
            month = str(Read_Visitor_Search_Components().get_start_month())
            year = int(Read_Visitor_Search_Components().get_start_year())
            hour = str(Read_Visitor_Search_jobs_Components().meta_data_start_hour())
            minute = Read_Visitor_Search_jobs_Components().meta_data_start_minuet()
            period = str(Read_Visitor_Search_jobs_Components().meta_data_start_am_pm_period())

            e_month = str(Read_Visitor_Search_Components().get_end_month())
            e_date = int(Read_Visitor_Search_Components().get_end_date())
            e_year = int(Read_Visitor_Search_Components().get_end_year())
            e_hour = str(Read_Visitor_Search_jobs_Components().meta_data_end_hour())
            e_minute = Read_Visitor_Search_jobs_Components().meta_data_end_minuet()
            e_period = str(Read_Visitor_Search_jobs_Components().meta_data_end_am_pm_period())

            try:
                Visitor_Search_Module_pom().handle_calender_pop_up("from", date, month, year, hour, minute, period)

                time.sleep(web_driver.one_second)
                Visitor_Search_Module_pom().handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute,
                                                                   e_period)
                time.sleep(web_driver.three_second)
            except Exception as ex:
                print(ex)

            include_jobs_from_all_users = web_driver.explicit_wait(self, 10, "XPATH",
                                                                   Read_Visitor_Search_jobs_Components().
                                                                   yes_btn_for_include_jobs_for_all_users_by_xpath(),
                                                                   self.d)
            include_jobs_from_all_users.click()
            self.logger.info("Clicked on Include Jobs For All Users option...")
            time.sleep(web_driver.one_second)
            search_button = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().
                                                search_button_on_search_dialog_by_xpath())
            search_button.click()
            time.sleep(web_driver.one_second)
        except Exception as ex:
            self.logger.info(f"Select date range got an exception as: {ex}")

    def select_delete_jobs_option(self):
        try:
            action_dropdown = web_driver.explicit_wait(self, 10, "XPATH",
                                                       Read_Visitor_Search_jobs_Components().
                                                       visitor_search_jobs_panel_action_button(), self.d)
            action_dropdown.click()
            delete_option = web_driver.explicit_wait(self, 10, "XPATH",
                                                     Read_Visitor_Search_jobs_Components().
                                                     visitor_search_jobs_panel_delete_jobs(), self.d)
            delete_text = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
                                              .visitor_search_jobs_panel_delete_jobs())
            self.logger.info("Delete Jobs option is visible..")
            delete_text.click()
            time.sleep(web_driver.one_second)
        except Exception as ex:
            self.logger.info(f"Select delete jobs option got an exception as: {ex}")

    def verify_user_able_to_delete_VS_jobs(self):
        result = []
        try:
            x = Read_Notification_Groups_Components().get_user_name_input_data()
            user = x.split(',')
            login().login_with_persona_user(self.d, user[4])
            time.sleep(web_driver.two_second)
            self.click_on_visitor_search_jobs_btn()
            self.select_jobs_for_all_users()

            job_checkbox = web_driver.explicit_wait(self, 10, "XPATH",
                                                    Read_Visitor_Search_jobs_Components().VSJ_checkbox_by_xpath(), self.d)
            job_checkbox = self.d.find_elements(By.XPATH, Read_Visitor_Search_jobs_Components().VSJ_checkbox_by_xpath())
            total_no_of_jobs = len(job_checkbox)
            job_checkbox[1].click()
            self.select_delete_jobs_option()
            yes_delete = web_driver.explicit_wait(self, 10, "XPATH",
                                                  Read_Visitor_Search_jobs_Components().
                                                  yes_delete_selected_search_job_by_xpath(), self.d)
            yes_delete.click()
            time.sleep(web_driver.two_second)
            job_checkbox = self.d.find_elements(By.XPATH, Read_Visitor_Search_jobs_Components().VSJ_checkbox_by_xpath())
            jobs_after_deleting_one = len(job_checkbox)

            if total_no_of_jobs == jobs_after_deleting_one + 1:
                self.logger.info(f"Total Jobs before deletion: {total_no_of_jobs},  Total Jobs after deletion: {jobs_after_deleting_one}")
                result.append(True)
            else:
                result.append(False)

            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_05_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            print(ex)
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_05_exception.png")
            self.logger.info(f"test_VSJ_05_exception:  {ex}")
            return False
        finally:
            self.click_on_logout_button()

    def Verify_VSJ_filtering_with_date_range_selection_should_list_VSJ_in_the_selected_date_range_only(self):
        result = []
        try:
            x = Read_Notification_Groups_Components().get_user_name_input_data()
            user = x.split(',')
            login().login_with_persona_user(self.d, user[4])
            time.sleep(web_driver.two_second)
            self.click_on_visitor_search_jobs_btn()
            search_dropdown = web_driver.explicit_wait(self, 10, "XPATH",
                                                       Read_Visitor_Search_jobs_Components().
                                                       visitor_search_jobs_panel_search_button(), self.d)
            search_dropdown.click()
            include_jobs_from_all_users = web_driver.explicit_wait(self, 10, "XPATH",
                                                                   Read_Visitor_Search_jobs_Components().
                                                                   yes_btn_for_include_jobs_for_all_users_by_xpath(),
                                                                   self.d)
            include_jobs_from_all_users.click()
            self.logger.info("Clicked on Include Jobs For All Users option...")
            time.sleep(web_driver.one_second)
            search_button = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().
                                                search_button_on_search_dialog_by_xpath())
            search_button.click()
            time.sleep(web_driver.one_second)
            job_checkbox = web_driver.explicit_wait(self, 10, "XPATH",
                                                    Read_Visitor_Search_jobs_Components().VSJ_checkbox_by_xpath(),
                                                    self.d)
            job_checkbox = self.d.find_elements(By.XPATH, Read_Visitor_Search_jobs_Components().VSJ_checkbox_by_xpath())
            no_of_jobs_before = len(job_checkbox)
            self.logger.info(f"before: {no_of_jobs_before}")
            self.select_date_range()
            time.sleep(web_driver.one_second)
            job_checkbox = web_driver.explicit_wait(self, 10, "XPATH",
                                                    Read_Visitor_Search_jobs_Components().VSJ_checkbox_by_xpath(),
                                                    self.d)
            job_checkbox = self.d.find_elements(By.XPATH, Read_Visitor_Search_jobs_Components().VSJ_checkbox_by_xpath())
            no_of_jobs_after = len(job_checkbox)
            self.logger.info(f"after: {no_of_jobs_after}")
            time.sleep(web_driver.two_second)
            if len(job_checkbox) == 1:
                no_results_message = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().there_are_no_results_message_by_xpath())
                if no_results_message.is_displayed():
                    self.logger.info(f"{no_results_message.text}")
                    result.append(True)
            elif no_of_jobs_before >= no_of_jobs_after:
                result.append(True)
            else:
                result.append(False)
            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_06_failed.png")
                return False
            else:
                return True

        except Exception as ex:
            print(ex)
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_06_exception.png")
            self.logger.info(f"test_VSJ_06_exception:  {ex}")
            return False
        finally:
            self.click_on_logout_button()

    ################################# generic methods ##############################################

    def close_all_panel_one_by_one(self):
        try:
            time.sleep(web_driver.two_second)
            close_panel_list = self.d.find_elements(By.XPATH,
                                                    Read_Visitor_Search_jobs_Components().close_panel_one_by_one_list())
            for i in close_panel_list:
                i.click()
        except Exception as ex:
            print(ex)

    def verify_image_from_match_list(self):
        time.sleep(web_driver.two_second)
        ele = self.d.find_elements(By.XPATH, Read_Visitor_Search_jobs_Components().image_match_list_by_xpath())
        for e in ele:
            if not e.is_displayed():
                return False
            else:
                return True

    def verify_region_from_match_list(self, zone_data):
        time.sleep(web_driver.two_second)
        ele = web_driver.explicit_wait(self, 10, "XPATH", Read_Visitor_Search_jobs_Components().visitor_search_jobs_panel_search_constraints(), self.d)
        ac_zone_txt = ele.text
        self.logger.info(f"zone test : {ac_zone_txt}")
        ac_zone_txt = ac_zone_txt[-11:]
        self.logger.info(f"actual zone: {ac_zone_txt}")
        self.logger.info(f"expected zone: {zone_data}")
        if zone_data != ac_zone_txt:
            self.logger.info("zone returning False")
            return False
        else:
            self.logger.info("zone returning True")
            return True

    def verify_date(self):
        self.get_date_range_from_json()
        ex_date = self.start_date.split("/")[0]
        ex_date = int(ex_date)
        ex_month = self.start_date.split("/")[1]
        ex_year = self.start_date.split("/")[2]
        ed_date = self.end_date.split("/")[0]
        ed_date = int(ed_date)
        ed_month = self.end_date.split("/")[1]
        ed_year = self.end_date.split("/")[2]
        print(ed_date)
        print(ed_month)
        print(ed_year)
        month_to_mm = {
            "01": "Jan",
            "02": "Feb",
            "03": "Mar",
            "04": "Apr",
            "05": "May",
            "06": "Jun",
            "07": "Jul",
            "08": "Aug",
            "09": "Sep",
            "10": "Oct",
            "11": "Nov",
            "12": "Dec"

        }

        mon = month_to_mm.get(ex_month)
        exp_asser = "{mon} {date}, {year} "
        mon_ed = month_to_mm.get(ed_month)
        exp_asser_2 = "{mon_ed} {date}, {year} "
        exp_asser = exp_asser.format(mon=mon, date=ex_date, year=ex_year)
        exp_asser_2 = exp_asser_2.format(mon_ed=mon_ed, date=ed_date, year=ed_year)
        time.sleep(web_driver.one_second)

        ac_start_date = web_driver.explicit_wait(self, 10, "XPATH", Read_Visitor_Search_jobs_Components().
                                                 visitor_search_jobs_panel_search_constraints(), self.d)
        ac_ass_date = ac_start_date.text
        self.logger.info(f"expected exp_asser: {exp_asser}, in : {ac_ass_date}")
        self.logger.info(f"expected exp_asser2: {exp_asser_2}, in : {ac_ass_date}")
        if exp_asser in ac_ass_date and exp_asser_2 in ac_ass_date:
            return True
        else:
            return False

    def verify_date_1(self, date, month, year, hour, minute, period):
        time.sleep(web_driver.two_second)
        month_to_mm = {
            "January": "JAN",
            "February": "FEB",
            "March": "MAR",
            "April": "APR",
            "May": "MAY",
            "June": "JUN",
            "July": "JUL",
            "August": "AUG",
            "September": "SEP",
            "October": "OCT",
            "November": "NOV",
            "December": "DEC"
        }
        mon = month_to_mm.get(month)

        # exp_asser = "{mon} {date}, {year} {hour}:{minu} {pe}"
        exp_asser = "{mon} {date}, {year}"
        self.logger.info(f"before format: {exp_asser}")
        exp_asser = exp_asser.format(mon=mon, date=date, year=year, hour=int(hour), minu=minute, pe=period)
        self.logger.info(f"expected formatted: {exp_asser}")
        
        ac_start_date = web_driver.explicit_wait(self, 10, "XPATH",
                                 Read_Visitor_Search_jobs_Components().visitor_search_jobs_panel_search_constraints(),
                                 self.d)
        ac_ass_date = ac_start_date.text.upper()
        ac_ass_date = ac_ass_date[20:]
        self.logger.info(f"expected date: {exp_asser}")
        self.logger.info(f"actual date: {ac_ass_date}")
        if exp_asser in ac_ass_date:
            self.logger.info("date returning true")
            return True
        else:
            self.logger.info("date returning false")
            return False

    def close_all_the_panels(self):
        """
        This function is used to close all the visitor search panels
        :return:
        """
        close_icon = self.d.find_elements(By.XPATH, Read_Visitor_Search_jobs_Components().close_all_visitor_search_panel_by_xpath())
        for x in close_icon:
            x.click()
            time.sleep(web_driver.two_second)

    def matches_found(self):

        matches_found = self.d.find_elements(By.XPATH, Read_Visitor_Search_jobs_Components().visitor_search_result_panel_matches_found())
        # self.wait_for_element_to_appear(self, matches_found, Read_Visitor_Search_jobs_Components().visitor_search_result_panel_matches_found())
        count = 0
        while len(matches_found) == 0 or count > 150:
            matches_found = self.d.find_elements(By.XPATH, Read_Visitor_Search_jobs_Components().visitor_search_result_panel_matches_found())
            time.sleep(web_driver.two_second)
            count += 1
            self.logger.info(f"matches found function count: {count}")
        if len(matches_found) > 0:
            x = matches_found[0]
            if x.text == Read_Visitor_Search_jobs_Components().matches_found_text():
                self.logger.info("no matches found... ")
                return x.text
            else:
                matches_found = self.d.find_elements(By.XPATH, Read_Visitor_Search_jobs_Components().visitor_search_result_panel_matches_found())
                y = matches_found[0]
                time.sleep(web_driver.two_second)
                count_data = Read_Visitor_Search_jobs_Components().matches_count_data_input()
                max_count = y.text
                max_number = max_count.split(" ")[0]
                return int(max_number) <= int(count_data)

    def max_matches(self):
        max_matches = self.d.find_elements(By.XPATH, Read_Visitor_Search_jobs_Components().visitors_search_jobs_panel_max_matches_by_xpath())
        count = 0
        while len(max_matches) == 0 or count > 150:
            max_matches = self.d.find_elements(By.XPATH, Read_Visitor_Search_jobs_Components().visitors_search_jobs_panel_max_matches_by_xpath())
            time.sleep(web_driver.two_second)
            count += 1
            self.logger.info(f"max matches function count: {count}")
        max_number_counted = 0
        if len(max_matches) > 0:
            max_matches_text = max_matches[0].text
            max_number_counted = max_matches_text.split(" ")[0]
            return max_number_counted
        else:
            self.logger.info("no max match found")
            return max_number_counted

    def select_zone(self, zone):
        """
        This function is used to handle the zone drop-down and select the required options
        :return:
        """
        time.sleep(web_driver.three_second)
        self.explicit_wait(10, "XPATH", Read_Visitor_Search_jobs_Components().zone_name_by_xpath(), self.d)
        zone_ele = self.d.find_elements(By.XPATH, Read_Visitor_Search_jobs_Components().zone_name_by_xpath())

        for actual_zone in zone_ele:
            if actual_zone.text == zone:
                self.logger.info(f"actual zone: {actual_zone.text}")
                actual_zone.click()
                break

        # zone_ele.click()
        time.sleep(web_driver.two_second)
        zone_text_list = self.d.find_elements(By.XPATH, Read_Visitor_Search_jobs_Components().zone_text_list_xpath())
        expected_zone_text = zone.upper()
        self.logger.info(f"expected zone: {expected_zone_text}")
        self.logger.info(f"zone list length: {len(zone_text_list)}")
        try:
            for i in range(len(zone_text_list)):
                actual_zone_text = zone_text_list.__getitem__(i).text
                if expected_zone_text.upper() in actual_zone_text.upper():
                    zone_text_list.__getitem__(i).click()
                    break
            save = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().zone_save_button_xpath())
            self.d.execute_script("arguments[0].click();", save)
            time.sleep(web_driver.two_second)
        except Exception as ex:
            str(ex)

    def select_zone_vsj(self, region_text):
        """
            This function is used to handle the region drop-down and select the required options
                    :param region_text:
                    :return:
                    """
        time.sleep(web_driver.one_second)
        region_ele = web_driver.explicit_wait(self, 10, "XPATH", Read_Visitor_Search_Components().zone_name_by_xpath(),
                                              self.d)
        region_ele.click()
        time.sleep(web_driver.one_second)
        region_text_list = self.d.find_elements(By.XPATH, Read_Visitor_Search_Components().zone_text_list_xpath())
        expected_region_text = region_text
        try:
            for i in range(len(region_text_list) + 1):
                # self.logger.info(f"for loop: {i}")
                actual_zone_text = region_text_list.__getitem__(i).text
                if expected_region_text.upper() == actual_zone_text.upper() :
                    self.logger.info(actual_zone_text)
                    self.logger.info(expected_region_text)
                    region_text_list.__getitem__(i).click()
                    # self.d.execute_script("arguments[0].click();", region_text_list.__getitem__(i))
                    break
            save = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().zone_save_button_xpath())
            save.click()
        except Exception as ex:
            str(ex)

    def compare_thresh_hold_value_with_score(self):
        """
        This function is used to compare the threshhold value with actual score
        :return:
        """
        slider = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().slider_icon_by_xpath())
        slider_value_str = str(slider.get_attribute("style"))
        slider_value_text = slider_value_str.split(" ")[1].strip()
        slider_value_text = re.sub("[% ;]", "", slider_value_text)

        match_list_score = self.d.find_elements(By.XPATH, Read_Visitor_Search_jobs_Components().score_by_xpath())
        for ele in match_list_score:
            score = ele.text
            score = int(score.split(".")[1][0:2])
            if not score >= int(slider_value_text):
                return False
            else:
                self.logger.info(f"Threshold values are greater than set threshold...")
                return True
        pass

    def set_thresh_hold_slider(self):
        """
        This function is used to set the threshold value
        :return:
        """
        slider_pixel = Read_Visitor_Search_jobs_Components().slider_value_data_input()
        slider_pixel_value = int(slider_pixel)

        slider = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().slider_icon_by_xpath())
        action = ActionChains(self.d)
        action.drag_and_drop_by_offset(slider, -80, 0).perform()

        action.drag_and_drop_by_offset(slider, slider_pixel_value, 0).perform()
        return slider_pixel

    def select_count(self, count_data):
        """
        This function is used to select the count from the count dropdown
        :param count_data:
        :return:
        """
        max_match = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().max_of_matches_by_xpath())

        select = Select(max_match)

        select.select_by_visible_text(count_data)
        time.sleep(web_driver.two_second)

    def click_on_submit_search_button(self):
        """
        This function is used to click on the submit search button
        :return:
        """

        submit_btn = web_driver.explicit_wait(self, 10, "XPATH", Read_Visitor_Search_jobs_Components().submit_search_button_by_xpath(), self.d)
        submit_btn.click()
        time.sleep(web_driver.two_second)
        try:
            result_wait = web_driver.explicit_wait(self, 10, "XPATH", "//div[@class='job-progress-container posrel fl disblk cb']", self.d)
            while result_wait.is_displayed():
                time.sleep(web_driver.two_second)
        except Exception as ex:
            pass

    def add_image_search(self):
        """
        This function is usd to upload the image and click on the search button
        :return:
        """
        self.login()
        self.click_on_visitor_search()

        upload_photo = web_driver.explicit_wait(self, 20, "XPATH", Read_Visitor_Search_jobs_Components().photo_upload_container_by_xpath(), self.d)
        upload_photo.click()
        time.sleep(web_driver.two_second)
        file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\dataset3\\ab\\1824_20220526-124520.png"

        time.sleep(web_driver.two_second)
        pyautogui.write(file_path)
        # pyautogui.write(file_path)
        pyautogui.press('enter')
        time.sleep(web_driver.two_second)
        pyautogui.press('enter')
        time.sleep(web_driver.two_second)

    def compare_count_match(self, count_data):
        """
        This function is used to compare the count provided with the actual no. of match count
        :param count_data:
        :return:
        """
        # match_found = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().matches_found_by_xpath())
        # match_found_count = int(match_found.text)

        #
        pass

    def handle_calender_pop_up(self, strategy, date, month, year, hour, minute, req_period):

        # click on the form calendar popup
        if strategy == "from":
            start_check_bx = web_driver.explicit_wait(self, 10, "XPATH", Read_Visitor_Search_jobs_Components().start_date_checkbox_by_xpath(), self.d)
            start_check_bx.click()
            time.sleep(web_driver.two_second)
            self.logger.info("checkbox selected...")
            start_date_txt_bx = web_driver.explicit_wait(self, 10, "XPATH", Read_Visitor_Search_jobs_Components().start_date_by_xpath(), self.d)
            self.d.execute_script("arguments[0].scrollIntoView();", start_date_txt_bx)
            start_date_txt_bx.click()
            self.logger.info("start date selected")
        else:
            # click on the to calendar pop up
            end_check_bx = web_driver.explicit_wait(self, 10, "XPATH", Read_Visitor_Search_jobs_Components().end_date_checkbox_by_xpath(), self.d)
            end_check_bx.click()
            time.sleep(web_driver.two_second)
            self.logger.info(f"end_ check box selected: {end_check_bx.is_displayed()}")
            end_date_txt_bx = web_driver.explicit_wait(self, 10, "XPATH", Read_Visitor_Search_jobs_Components().end_date_by_xpath(), self.d)
            self.d.execute_script("arguments[0].scrollIntoView();", end_date_txt_bx)
            end_date_txt_bx.click()
            self.logger.info(f"end date selected: {end_check_bx.is_displayed()}")

        # click on the clock icon
        calender_clock = web_driver.explicit_wait(self, 10, "XPATH", Read_Visitor_Search_jobs_Components().calender_timer_icon_by_xpath(), self.d)
        calender_clock.click()

        time.sleep(3)

        # handle the hour and minute based on the strategy
        if strategy == "from":
            self.calender_handle_hour_minute_from(hour, minute)
        else:
            self.calender_handle_hour_minute_to(hour, minute)

        # select the period am or pm
        period = web_driver.explicit_wait(self, 10, "XPATH", Read_Visitor_Search_jobs_Components().period_by_xpath(), self.d)
        if period.text == req_period:
            print("")
        else:
            period.click()

        # click on the tick icon

        tick_icon = web_driver.explicit_wait(self, 10, "XPATH", Read_Visitor_Search_jobs_Components().calender_tick_icon_by_xpath(), self.d)
        tick_icon.click()

        if strategy == "from":

            start_date_txt_bx = web_driver.explicit_wait(self, 10, "XPATH", Read_Visitor_Search_jobs_Components().start_date_by_xpath(), self.d)
            start_date_txt_bx.click()
        else:
            # click on the to calendar pop up
            start_date_txt_bx = web_driver.explicit_wait(self, 10, "XPATH", Read_Visitor_Search_jobs_Components().end_date_by_xpath(), self.d)
            start_date_txt_bx.click()

        req_month = month
        req_year = year
        month_to_num = {
            "January": 1,
            "February": 2,
            "March": 3,
            "April": 4,
            "May": 5,
            "June": 6,
            "July": 7,
            "August": 8,
            "September": 9,
            "October": 10,
            "November": 11,
            "December": 12
        }

        month_year = web_driver.explicit_wait(self, 10, "XPATH", Read_Visitor_Search_jobs_Components().calender_month_year_by_xpath(), self.d)
        ac_month = month_year.text.split(" ")[0]
        ac_year = int(month_year.text.split(" ")[1])

        # click on the back button
        count = 0
        while month_to_num.get(req_month) < month_to_num.get(ac_month) or req_year < ac_year:

            cal_back_button = web_driver.explicit_wait(self, 10, "XPATH", Read_Visitor_Search_jobs_Components().calender_back_button_by_xpath(), self.d)
            if cal_back_button.is_enabled():
                cal_back_button.click()
            time.sleep(1)

            month_year = web_driver.explicit_wait(self, 10, "XPATH", Read_Visitor_Search_jobs_Components().calender_month_year_by_xpath(), self.d)
            ac_month = month_year.text.split(" ")[0]
            ac_year = int(month_year.text.split(" ")[1])
            count += 1
            self.logger.info(f"month and year function count: {count}")

        # click on the forward button
        count = 0
        while month_to_num.get(req_month) > month_to_num.get(ac_month) or req_year > ac_year:
            # action = ActionChains(self.d)
            # action.key_down(Keys.ARROW_RIGHT).key_up(Keys.ARROW_RIGHT).perform()
            try:
                cal_back_button = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().calender_forward_button_by_xpath())
                if cal_back_button.is_enabled():
                    cal_back_button.click()
            except Exception as ex:
                title_name = self.d.find_element(By.XPATH, "//a[@title='Close the picker'']")
                title_name.click()
                pass
            time.sleep(1)
            month_year = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().calender_month_year_by_xpath())
            ac_month = month_year.text.split(" ")[0]
            ac_year = int(month_year.text.split(" ")[1])
            count += 1

            self.logger.info(f"month and year function count: {count}")

        time.sleep(web_driver.three_second)
        # click on the required date
        web_driver.explicit_wait(self, 10, "XPATH", "(//td[@class='day' or @class='day weekend' or @class='day active' or @class='day active today' or @class='day today'])[" + str(date) + "]", self.d)
        date = self.d.find_element(By.XPATH, "(//td[@class='day' or @class='day weekend' or @class='day active' or @class='day active today' or @class='day today'])[" + str(date) + "]")
        date.click()
        time.sleep(web_driver.two_second)
        # click on the tick icon
        tick_icon = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().calender_tick_icon_by_xpath())
        time.sleep(web_driver.two_second)
        tick_icon.click()
        time.sleep(web_driver.two_second)
        
    def calender_handle_hour_minute_to(self, hour, minute):

        # set the minute
        current_min_ele = web_driver.explicit_wait(self, 10, "XPATH", Read_Visitor_Search_jobs_Components().current_minute_element_by_xpath(), self.d)
        cur_min = int(current_min_ele.text)
        self.logger.info(f"current minute: {cur_min}")
        while int(cur_min) != int(minute):
            self.logger.info(f"current min: {cur_min} and expected min: {minute}")
            clock_down_button = web_driver.explicit_wait(self, 10, "XPATH", Read_Visitor_Search_jobs_Components().clock_min_down_button_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", clock_down_button)
            current_min_ele = web_driver.explicit_wait(self, 10, "XPATH", Read_Visitor_Search_jobs_Components().current_minute_element_by_xpath(), self.d)
            cur_min = int(current_min_ele.text)

        # set the hour
        current_hour_ele = web_driver.explicit_wait(self, 10, "XPATH", Read_Visitor_Search_jobs_Components().current_hour_ele_by_xpath(), self.d)
        cur_hour = int(current_hour_ele.text)
        self.logger.info(f"current hour: {cur_hour}")
        self.logger.info(f"calender handler hour to : {hour}")
        self.logger.info(f"calender handler minute to : {minute}")
        while int(cur_hour) != int(hour):
            hour_down = web_driver.explicit_wait(self, 10, "XPATH", Read_Visitor_Search_jobs_Components().hour_down_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", hour_down)
            current_hour_ele = web_driver.explicit_wait(self, 10, "XPATH", Read_Visitor_Search_jobs_Components().current_hour_ele_by_xpath(), self.d)
            cur_hour = int(current_hour_ele.text)

    def calender_handle_hour_minute_from(self, hour, minute):
        current_hour_ele = web_driver.explicit_wait(self, 10, "XPATH", Read_Visitor_Search_jobs_Components().current_hour_ele_by_xpath(), self.d)
        cur_hour = int(current_hour_ele.text)
        self.logger.info(f"calender handler hour from : {hour}")
        self.logger.info(f"calender handler minute from : {minute}")
        # decrementHours
        while int(cur_hour) != int(hour):
            hour_down = web_driver.explicit_wait(self, 10, "XPATH", Read_Visitor_Search_jobs_Components().hour_down_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", hour_down)
            current_hour_ele = web_driver.explicit_wait(self, 10, "XPATH", Read_Visitor_Search_jobs_Components().current_hour_ele_by_xpath(), self.d)
            cur_hour = int(current_hour_ele.text)

        # set the minute
        current_min_ele = web_driver.explicit_wait(self, 10, "XPATH", Read_Visitor_Search_jobs_Components().current_minute_element_by_xpath(), self.d)
        cur_min = int(current_min_ele.text)
        print(cur_min)
        while int(cur_min) != int(minute):
            clock_up_button = web_driver.explicit_wait(self, 10, "XPATH", Read_Visitor_Search_jobs_Components().clock_min_up_button_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", clock_up_button)
            current_min_ele = web_driver.explicit_wait(self, 10, "XPATH", Read_Visitor_Search_jobs_Components().current_minute_element_by_xpath(), self.d)
            cur_min = int(current_min_ele.text)

    def verify_date_range(self, start_year, end_year):
        month_to_num = {
            "JAN": 1,
            "FEB": 2,
            "MAR": 3,
            "APR": 4,
            "MAY": 5,
            "JUN": 6,
            "JUL": 7,
            "AUG": 8,
            "SEP": 9,
            "OCT": 10,
            "NOV": 11,
            "DEC": 12
        }
        date_list = self.d.find_elements(By.XPATH, Read_Visitor_Search_jobs_Components().match_date_list_by_xpath())
        ac_date = int()
        ac_month = int()
        ac_year = int()
        for x in date_list:
            dt = x.text
            b = dt.split(" ")
            ac_year = int(b[2])
        ele2 = web_driver.explicit_wait(self, 10, "XPATH", Read_Visitor_Search_jobs_Components().no_matches_found(), self.d)
        if (start_year <= ac_year <= end_year) or (ele2.is_displayed()):
            return True
        else:
            return False

    def click_on_logout_button(self):
        try:
            time.sleep(web_driver.two_second)
            logout_button = web_driver.explicit_wait(self, 10, "XPATH", Read_Visitor_Search_jobs_Components().logout_btn_by_xpath(), self.d)
            logout_button.click()
            time.sleep(web_driver.two_second)
        except Exception as ex:
            print(ex)

    def check_if_match_is_found(self):
        ele = web_driver.explicit_wait(self, 10, "XPATH", Read_Visitor_Search_jobs_Components().no_match_found_by_xpath(), self.d)
        if ele.is_displayed():
            return False
        else:
            return True

    def click_on_visitor_search(self):
        time.sleep(web_driver.two_second)
        visitor_search_btn = web_driver.explicit_wait(self, 10, "XPATH", Read_Visitor_Search_jobs_Components().portal_menu_visitors_search_btn_by_xpath(), self.d)
        visitor_search_btn.click()
        time.sleep(web_driver.two_second)

    def click_on_cloud_menu(self):
        # visitor_search_btn = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().cloud_menu_by_xpath())
        click_on_cloud_menu = web_driver.explicit_wait(self, 10, "XPATH", Read_Visitor_Search_jobs_Components().cloud_menu_by_xpath(), self.d)
        # click_on_cloud_menu.click()
        time.sleep(web_driver.two_second)
        self.d.execute_script("arguments[0].click();", click_on_cloud_menu)
        time.sleep(web_driver.two_second)

    def get_date_range_from_json(self):
        try:
            df_custom_dates = pd.read_json(self.custom_dates_json)
            self.start_date_and_time = list({df_custom_dates['date_range'][0]['start_date']})
            for items in self.start_date_and_time:
                items = items.split(' ')
                self.start_date = items[0]
                self.start_time = items[1]
                self.start_datetime = items[2]
            self.logger.info(f"start date: {self.start_date}{self.start_time}{self.start_datetime}")
            self.end_date_and_time = list({df_custom_dates['date_range'][0]['end_date']})
            for items in self.end_date_and_time:
                items = items.split(' ')
                self.end_date = items[0]
                self.end_time = items[1]
                self.end_datetime = items[2]
            self.logger.info(f"end date: {self.end_date}{self.end_time}{self.end_datetime}")
        except Exception as ex:
            self.logger.error(ex)

    def get_start_date(self):
        try:
            # self.get_date_range_from_json()
            time.sleep(web_driver.one_second)

            start_date_calender_box = web_driver.explicit_wait(self, 10, "XPATH", Read_Visitor_Search_jobs_Components().start_date_calender_box_by_xpath(), self.d)
            start_date_checkbox = web_driver.explicit_wait(self, 10, "XPATH", Read_Visitor_Search_jobs_Components().start_date_checkbox_by_xpath(), self.d)
            time.sleep(web_driver.one_second)
            # start_date_checkbox.click()
            start_date_calender_box.click()
            action = ActionChains(self.d)
            time.sleep(web_driver.one_second)
            default_start_date = start_date_calender_box.get_attribute('value')
            default_start_date = list(default_start_date.split(' '))
            d_start_date = default_start_date[0]
            d_start_date = list(d_start_date.split('/'))
            s_month = d_start_date[0]
            s_date = d_start_date[1]
            start_date = Read_Visitor_Search_jobs_Components().vsj_start_date()
            self.logger.info(f"expected date: {start_date}")
            input_start_date = list(start_date.split('/'))
            input_s_date = input_start_date[0]
            input_s_month = input_start_date[1]
            input_s_year = input_start_date[2]
            status = True
            if s_month < input_s_month:
                while status:
                    action.key_down(Keys.ARROW_RIGHT).key_up(Keys.ARROW_RIGHT).perform()
                    current_date_and_time = start_date_calender_box.get_attribute('value')
                    current_date_and_time = list(current_date_and_time.split(' '))
                    current_date = current_date_and_time[0]
                    current_date = list(current_date.split('/'))
                    c_date = current_date[1]
                    c_month = current_date[0]
                    # c_year = current_date[2]
                    if c_month == input_s_month and c_date == input_s_date:
                        action.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
                        self.logger.info(F"Start date selected as:- {input_s_date}/{input_s_month}/{input_s_year}")
                        status = False
            elif s_month > input_s_month:
                while status:
                    action.key_down(Keys.ARROW_LEFT).key_up(Keys.ARROW_LEFT).perform()
                    current_date_and_time = start_date_calender_box.get_attribute('value')
                    current_date_and_time = list(current_date_and_time.split(' '))
                    current_date = current_date_and_time[0]
                    current_date = list(current_date.split('/'))
                    c_date = current_date[1]
                    c_month = current_date[0]
                    if c_month == input_s_month and c_date == input_s_date:
                        action.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
                        self.logger.info(F"Start date selected as:- {input_s_date}/{input_s_month}/{input_s_year}")
                        status = False
            else:
                if s_date > input_s_date:
                    while status:
                        action.key_down(Keys.ARROW_LEFT).key_up(Keys.ARROW_LEFT).perform()
                        current_date_and_time = start_date_calender_box.get_attribute('value')
                        current_date_and_time = list(current_date_and_time.split(' '))
                        current_date = current_date_and_time[0]
                        current_date = list(current_date.split('/'))
                        c_date = current_date[1]
                        c_month = current_date[0]
                        if c_month == input_s_month and c_date == input_s_date:
                            action.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
                            self.logger.info(F"Start date selected as:- {input_s_date}/{input_s_month}/{input_s_year}")
                            status = False
                elif s_date < input_s_date:
                    while status:
                        action.key_down(Keys.ARROW_RIGHT).key_up(Keys.ARROW_RIGHT).perform()
                        current_date_and_time = start_date_calender_box.get_attribute('value')
                        current_date_and_time = list(current_date_and_time.split(' '))
                        current_date = current_date_and_time[0]
                        current_date = list(current_date.split('/'))
                        c_date = current_date[1]
                        c_month = current_date[0]
                        if c_month == input_s_month and c_date == input_s_date:
                            action.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
                            self.logger.info(F"Start date selected as:- {input_s_date}/{input_s_month}/{input_s_year}")
                            status = False
                else:
                    action.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
        except Exception as ex:
            self.logger.error("start date method exception")
            self.logger.error(ex)

    def select_time(self, strategy, hour, minute, req_period):
        try:
            # click on the form calendar popup
            if strategy == "from":
                start_check_bx = web_driver.explicit_wait(self, 10, "XPATH",
                                                          Read_Visitor_Search_jobs_Components().start_date_checkbox_by_xpath(),
                                                          self.d)
                start_check_bx.click()
                time.sleep(web_driver.two_second)
                self.logger.info("checkbox selected...")
                start_date_txt_bx = web_driver.explicit_wait(self, 10, "XPATH",
                                                             Read_Visitor_Search_jobs_Components().start_date_by_xpath(),
                                                             self.d)
                self.d.execute_script("arguments[0].scrollIntoView();", start_date_txt_bx)
                start_date_txt_bx.click()
                self.logger.info("start date selected")
            else:
                # click on the to calendar pop up
                end_check_bx = web_driver.explicit_wait(self, 10, "XPATH",
                                                        Read_Visitor_Search_jobs_Components().end_date_checkbox_by_xpath(),
                                                        self.d)
                end_check_bx.click()
                time.sleep(web_driver.two_second)
                self.logger.info(f"end_ check box selected: {end_check_bx.is_displayed()}")
                end_date_txt_bx = web_driver.explicit_wait(self, 10, "XPATH",
                                                           Read_Visitor_Search_jobs_Components().end_date_by_xpath(),
                                                           self.d)
                self.d.execute_script("arguments[0].scrollIntoView();", end_date_txt_bx)
                end_date_txt_bx.click()
                self.logger.info(f"end date selected: {end_check_bx.is_displayed()}")

            # click on the clock icon
            calender_clock = web_driver.explicit_wait(self, 10, "XPATH",
                                                      Read_Visitor_Search_jobs_Components().calender_timer_icon_by_xpath(),
                                                      self.d)
            calender_clock.click()

            time.sleep(3)

            # handle the hour and minute based on the strategy
            if strategy == "from":
                self.calender_handle_hour_minute_from(hour, minute)
            else:
                self.calender_handle_hour_minute_to(hour, minute)

            # select the period am or pm
            period = web_driver.explicit_wait(self, 10, "XPATH",
                                              Read_Visitor_Search_jobs_Components().period_by_xpath(), self.d)
            if period.text == req_period:
                print("")
            else:
                period.click()

            # click on the tick icon

            tick_icon = web_driver.explicit_wait(self, 10, "XPATH",
                                                 Read_Visitor_Search_jobs_Components().calender_tick_icon_by_xpath(),
                                                 self.d)
            tick_icon.click()
        except Exception as ex:
            self.logger.info(f"Select time got an exception as: {ex}")

    def get_end_date(self):
        try:
            self.get_date_range_from_json()
            time.sleep(web_driver.one_second)
            end_date_calender_box = self.d.find_element(By.XPATH,
                                                        Read_Visitor_Search_jobs_Components().end_date_calender_box_by_xpath())
            end_date_checkbox = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().end_date_checkbox_by_xpath())
            time.sleep(web_driver.one_second)
            end_date_checkbox.click()
            end_date_calender_box.click()
            action = ActionChains(self.d)
            default_end_date = end_date_calender_box.get_attribute('value')
            default_end_date = list(default_end_date.split(' '))
            d_end_date = default_end_date[0]
            d_end_date = list(d_end_date.split('/'))
            e_month = d_end_date[0]
            e_date = d_end_date[1]
            input_end_date = list(self.end_date.split('/'))
            input_e_date = input_end_date[0]
            input_e_month = input_end_date[1]
            input_e_year = input_end_date[2]
            status = True
            if e_month < input_e_month:
                while status:
                    action.key_down(Keys.ARROW_RIGHT).key_up(Keys.ARROW_RIGHT).perform()
                    current_date_and_time = end_date_calender_box.get_attribute('value')
                    current_date_and_time = list(current_date_and_time.split(' '))
                    current_date = current_date_and_time[0]
                    current_date = list(current_date.split('/'))
                    c_date = current_date[1]
                    c_month = current_date[0]
                    if c_month == input_e_month and c_date == input_e_date:
                        action.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
                        self.logger.info(F"End date selected as:- {input_e_date}/{input_e_month}/{input_e_year}")
                        status = False
            elif e_month > input_e_month:
                while status:
                    action.key_down(Keys.ARROW_LEFT).key_up(Keys.ARROW_LEFT).perform()
                    current_date_and_time = end_date_calender_box.get_attribute('value')
                    current_date_and_time = list(current_date_and_time.split(' '))
                    current_date = current_date_and_time[0]
                    current_date = list(current_date.split('/'))
                    c_date = current_date[1]
                    c_month = current_date[0]
                    if c_month == input_e_month and c_date == input_e_date:
                        action.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
                        self.logger.info(F"End date selected as:- {input_e_date}/{input_e_month}/{input_e_year}")
                        status = False
            elif e_month == input_e_month:
                if e_date > input_e_date:
                    while status:
                        action.key_down(Keys.ARROW_LEFT).key_up(Keys.ARROW_LEFT).perform()
                        current_date_and_time = end_date_calender_box.get_attribute('value')
                        current_date_and_time = list(current_date_and_time.split(' '))
                        current_date = current_date_and_time[0]
                        current_date = list(current_date.split('/'))
                        c_date = current_date[1]
                        c_month = current_date[0]
                        if c_month == input_e_month and c_date == input_e_date:
                            action.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
                            self.logger.info(F"End date selected as:- {input_e_date}/{input_e_month}/{input_e_year}")
                            status = False
                elif e_date < input_e_date:
                    while status:
                        action.key_down(Keys.ARROW_RIGHT).key_up(Keys.ARROW_RIGHT).perform()
                        current_date_and_time = end_date_calender_box.get_attribute('value')
                        current_date_and_time = list(current_date_and_time.split(' '))
                        current_date = current_date_and_time[0]
                        current_date = list(current_date.split('/'))
                        c_date = current_date[1]
                        c_month = current_date[0]
                        if c_month == input_e_month and c_date == input_e_date:
                            action.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
                            self.logger.info(F"End date selected as:- {input_e_date}/{input_e_month}/{input_e_year}")
                            status = False
                else:
                    action.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
        except Exception as ex:
            self.logger.error("end date method exception")
            self.logger.error(ex)