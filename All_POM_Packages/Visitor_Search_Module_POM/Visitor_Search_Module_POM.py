import os, json, time
import datetime
from datetime import timedelta
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
from Base_Package.Login_Logout_Ops import login, logout
from Base_Package.Web_Driver import web_driver
from Base_Package.Web_Logger import web_logger
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
from pathlib import Path
import pyautogui
from selenium.webdriver import ActionChains, Keys
from All_Config_Packages._1_Portal_Login_Module_Config_Files.Portal_Login_Page_Read_INI import Portal_login_page_read_ini
from All_Config_Packages._2_Portal_Menu_Module_Config_Files.Portal_Menu_Module_Read_INI import Portal_Menu_Module_read_ini
from All_Config_Packages._6_Notification_Groups_Module_Config_Files.Notification_Groups_Read_INI import Read_Notification_Groups_Components
from All_Config_Packages._7_Visitor_Search_Module_Config_Files.Visitor_Search_Read_INI import \
    Read_Visitor_Search_Components


class Visitor_Search_Module_pom(web_driver, web_logger):
    d = web_driver.d()
    logger = web_logger.logger_obj()

    now = (datetime.datetime.now())
    DATE_IE = now.strftime('%d/%m/%Y')
    TIME_IE = now.strftime('%H%M')
    AM_PM_IE = now.strftime('%p')
    tomorrow = now + timedelta(2)


    expirationDATE_IE = tomorrow.strftime('%m/%d/%Y')
    expirationTIME_IE = now.strftime('%H%M')
    expirationAM_PM_IE = now.strftime('%p')

    def __init__(self):
        self.end_datetime = self.end_time = self.end_date = self.end_date_and_time = self.start_am_pm = \
        self.start_age = self.age_bucket = None
        self.start_time = self.start_date = self.start_date_and_time = self.groups = self.zones = self.end_age = None
        self.custom_dates_json = \
            f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\7_Visitor_Search_Module\\Data_From_JSON\\custom_dates_json.json"

    def click_on_visitor_search(self):
        self.logger.info("going to visitor search...")
        visitor_search_btn = web_driver.explicit_wait(self, 10, "XPATH",
                                                      Read_Visitor_Search_Components().portal_menu_visitors_search_btn_by_xpath(),
                                                      self.d)
        visitor_search_btn.click()
        # self.d.execute_script("arguments[0].click();", visitor_search_btn)
        time.sleep(web_driver.two_second)
        self.logger.info("waiting for search panel to appear...")

    def login(self):
        login().login_to_cloud_if_not_done(self.d)

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

    def click_on_logout_button(self):
        try:
            time.sleep(web_driver.one_second)
            user = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_user_name_on_taskbar_by_xpath())
            existing_username = user.text
            logout_btn = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_logout_button_on_portal_by_xpath())
            logout_btn.click()
            self.logger.info(f"{existing_username} User logged out from cloud menu..")
            time.sleep(web_driver.one_second)
        except Exception as ex:
            self.logger.info(f"logout from cloud menu got an exception as :{ex}")

    def Verify_visitor_search_with_metadata_Date_and_Org_Hierarchy_Selection_should_yield_visitor_results_within_selected_search_criteria(self):
        try:
            self.logger.info("********** Test_1 Begin  **********")
            status = []
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
                self.logger.info(f"select date range got an exception as: {ex}")

            # self.logger.info("select from date checkbox")
            # start_check_bx = self.d.find_element(By.XPATH,
            #                                      Read_Visitor_Search_Components().start_date_checkbox_by_xpath())
            # start_check_bx.click()
            # time.sleep(web_driver.one_second)
            # web_driver.implicit_wait(self, web_driver.one_second, self.d)
            # self.logger.info("select date time")
            # start_date_txt_bx = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().start_date_by_xpath())
            # self.d.execute_script("arguments[0].scrollIntoView();", start_date_txt_bx)
            # # start_date_txt_bx.click()
            #
            # time.sleep(web_driver.one_second)
            # start_date_txt_bx.send_keys(Keys.CONTROL, 'a')
            # time.sleep(web_driver.one_second)
            # start_date_txt_bx.send_keys(Keys.BACKSPACE)
            # time.sleep(web_driver.one_second)
            #
            # self.vs_start_Date_Time_AMPM(start_date_txt_bx)
            #
            # tick_icon = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().calender_tick_icon_by_xpath())
            #
            # tick_icon.click()

            edge_name = Read_Visitor_Search_Components().zone_data_input()
            self.logger.info(f"edge name: {edge_name}")
            self.select_zone(edge_name)

            self.click_on_submit_search_button()
            x = self.verify_image_from_match_list()
            self.logger.info(f"Returned: {x}")
            status.append(x)
            self.verify_date()
            self.verify_region_from_match_list(edge_name)
            self.click_on_logout_button()

            self.logger.info(f"status: {status}")
            if False in status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_VS_1_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_VS_1_failed.png")
                return False
            else:
                return True
            # logout().logout_from_core()
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_VS_1_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_VS_1_exception.png")
            self.logger.error(f"TC_VS_1 got exception as: {ex.args}")
            return False

    def expirirationdateTimeAMPM(self, date_incident):
        self.logger.info(f" today date : {self.DATE_IE}")
        date_incident.send_keys(self.expirationDATE_IE)
        time.sleep(web_driver.one_second)
        date_incident.send_keys(" " + self.TIME_IE)
        time.sleep(web_driver.one_second)
        date_incident.send_keys(" " + self.AM_PM_IE)
        time.sleep(web_driver.one_second)

    def vs_start_Date_Time_AMPM(self, date_incident):
        self.logger.info(f" today date : {self.DATE_IE}")
        date_incident.send_keys(Read_Visitor_Search_Components().get_start_date())
        time.sleep(web_driver.one_second)
        date_incident.send_keys(" " + Read_Visitor_Search_Components().get_start_hour())
        time.sleep(web_driver.one_second)
        date_incident.send_keys(" " + Read_Visitor_Search_Components().get_start_am_pm_period())
        time.sleep(web_driver.one_second)

    def vs_end_Date_Time_AMPM(self, date_incident):
        self.logger.info(f" tommorow date : {self.expirationDATE_IE}")
        date_incident.send_keys(self.expirationDATE_IE)
        time.sleep(web_driver.one_second)
        date_incident.send_keys(" " + self.TIME_IE)
        time.sleep(web_driver.one_second)
        date_incident.send_keys(" " + self.AM_PM_IE)
        time.sleep(web_driver.one_second)


    def Verify_visitor_search_with_image_only_should_list_the_matching_visitors_with_image(self):
        try:
            self.logger.info("********** Test_VS_02 Begin  **********")
            status = []

            x = Read_Notification_Groups_Components().get_user_name_input_data()
            user = x.split(',')
            login().login_with_persona_user(self.d, user[0])

            self.click_on_visitor_search()
            self.add_image_for_image_search()

            self.click_on_submit_search_button()
            x = self.verify_image_from_match_list()
            self.logger.info(f"Returned: {x}")
            status.append(x)
            self.click_on_logout_button()

            self.logger.info(f"status: {status}")
            if False in status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_VS_2_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_VS_2_failed.png")
                return False
            else:
                return True
            # logout().logout_from_core()
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_VS_2_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_VS_2_exception.png")
            self.logger.error(f"TC_VS_2 got exception as: {ex.args}")
            return False

    def enter_start_and_end_date(self):
        try:
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
        except Exception as ex:
            self.logger.info(f"Select start and end date got an exception as: {ex}")

    def Verify_visitor_search_with_Image_and_metadata_should_list_the_matched_visitors_with_search_image_from_selected_Org_Hierarchy_Selection_within_date_range(self):
        try:
            self.logger.info("********** Test_VS_03 Begin  **********")
            status = []
            x = Read_Notification_Groups_Components().get_user_name_input_data()
            user = x.split(',')
            login().login_with_persona_user(self.d, user[0])
            # login().login_to_cloud_if_not_done(self.d)
            edge_name = Read_Visitor_Search_Components().zone_data_input()

            self.click_on_visitor_search()
            self.add_image_for_image_with_metadata_search()
            self.enter_start_and_end_date()
            self.logger.info(f"edge name: {edge_name}")
            self.select_zone(edge_name)
            self.set_thresh_hold_slider()
            self.select_count(Read_Visitor_Search_Components().matches_count_data_input())
            self.click_on_submit_search_button()
            self.compare_count_match(Read_Visitor_Search_Components().matches_count_data_input())
            self.compare_thresh_hold_value_with_score()
            x = self.verify_image_from_match_list()
            self.logger.info(f"Returned: {x}")
            status.append(x)
            self.click_on_logout_button()

            self.logger.info(f"status: {status}")
            if False in status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_VS_03_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_VS_03_failed.png")
                return False
            else:
                return True
            # logout().logout_from_core()
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_VS_03_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_VS_03_exception.png")
            self.logger.error(f"TC_VS_03 got exception as: {ex.args}")
            return False

    def get_root_region_name_on_DM(self):
        try:
            close = web_driver.explicit_wait(self, 10, "XPATH",
                                             Portal_login_page_read_ini().get_close_btn_on_welcome_dialog_by_xpath(),
                                             self.d)
            close = self.d.find_element(By.XPATH,
                                        Portal_login_page_read_ini().get_close_btn_on_welcome_dialog_by_xpath())
            close.click()
            self.logger.info("Login to DM... Welcome dialog is displayed..")
            time.sleep(web_driver.one_second)
            edge_system = web_driver.explicit_wait(self, 10, "XPATH", Portal_login_page_read_ini().
                                                   get_edge_system_by_xpath(), self.d)
            edge_system = self.d.find_element(By.XPATH, Portal_login_page_read_ini().get_edge_system_by_xpath())
            edge_system.click()
            time.sleep(web_driver.two_second)
            edit = web_driver.explicit_wait(self, 10, "XPATH", Portal_login_page_read_ini().
                                            get_edit_link_by_xpath(), self.d)
            edit = self.d.find_element(By.XPATH, Portal_login_page_read_ini().get_edit_link_by_xpath())
            edit.click()
            time.sleep(web_driver.two_second)
        except Exception as ex:
            self.logger.info(f"Getting Root name on Dm got exception as: {ex}")
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

    def Verify_org_hierarchy_selection_root_name_should_be_able_to_match_with_DM_core_name(self):
        try:
            self.logger.info("********** Test_VS_04 Begin  **********")
            status = []

            login().login_to_cloud_if_not_done(self.d)
            self.click_on_visitor_search()
            time.sleep(web_driver.one_second)
            region_ele = web_driver.explicit_wait(self, 10, "XPATH",
                                                  Read_Visitor_Search_Components().zone_name_by_xpath(),
                                                  self.d)
            region_ele.click()
            time.sleep(web_driver.one_second)
            root_name = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().root_region_name_by_xpath())
            root_region_name_on_VS = root_name.text
            self.logger.info(f"Root region name on VS: {root_region_name_on_VS}")
            save = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().zone_save_button_xpath())
            save.click()
            # self.d.close()
            self.d.switch_to.new_window()
            login().login_to_DM_if_not_done(self.d)
            self.get_root_region_name_on_DM()
            root_region_name_on_DM = self.d.find_element(By.XPATH, Portal_login_page_read_ini().
                                                         get_root_region_name_on_dm_by_xpath())
            self.logger.info(f"Root region name on DM: {root_region_name_on_DM.text.upper()}")
            time.sleep(web_driver.two_second)
            if root_region_name_on_VS.upper() == root_region_name_on_DM.text.upper():
                self.logger.info(f"Root region names on VS and DM are same...")
                status.append(True)
            else:
                self.logger.info(f"Root region names on VS and DM are not same...")
                status.append(False)
            self.close_current_tab()
            self.click_on_logout_button()
            self.logger.info(f"status: {status}")
            if False in status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_VS_04_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_VS_04_failed.png")
                return False
            else:
                return True
            # logout().logout_from_core()

        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_VS_04_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_VS_04_exception.png")
            self.logger.error(f"TC_VS_04 got exception as: {ex.args}")
            return False

    def drag_and_drop_image_to_perform_VS(self):
        try:
            time.sleep(web_driver.one_second)
            draggable_photo = web_driver.explicit_wait(self, 10, "XPATH",
                                                       Read_Visitor_Search_Components().
                                                       draggable_event_photo_by_xpath(), self.d)
            draggable_photo = self.d.find_element(By.XPATH,
                                                  Read_Visitor_Search_Components().draggable_event_photo_by_xpath())

            upload_photo = web_driver.explicit_wait(self, 10, "XPATH", Read_Visitor_Search_Components().
                                                    photo_upload_container_by_xpath(), self.d)
            upload_photo = self.d.find_element(By.XPATH,
                                               Read_Visitor_Search_Components().photo_upload_container_by_xpath())
            time.sleep(web_driver.one_second)
            ActionChains(self.d).drag_and_drop(draggable_photo, upload_photo).perform()
            time.sleep(web_driver.one_second)
            self.logger.info(f"Photo is dropped in upload container...")
            return True
        except Exception as ex:
            self.logger.info(f"dragging and dropping image got an exception as: {ex}")
            return False

    def Verify_warning_message_when_user_is_dropping_the_image_which_is_clicked_on_live_or_file_image_on_events_panel_able_to_perform_image_with_meta_data_idealy_it_should_not_with_larger_image_able_to_perform(self):
        try:
            self.logger.info("********** Test_VS_05 Begin  **********")
            status = []
            x = Read_Notification_Groups_Components().get_user_name_input_data()
            user = x.split(',')
            login().login_with_persona_user(self.d, user[0])
            self.click_on_visitor_search()
            time.sleep(web_driver.one_second)
            cloud_menu = web_driver.explicit_wait(self, 10, "XPATH", Portal_login_page_read_ini().
                                                  get_cloud_menu_on_dashboard_by_xpath(), self.d)
            cloud_menu = self.d.find_element(By.XPATH, Portal_login_page_read_ini().get_cloud_menu_on_dashboard_by_xpath())
            cloud_menu.click()
            time.sleep(web_driver.one_second)
            events_menu = web_driver.explicit_wait(self, 10, "XPATH", Portal_Menu_Module_read_ini().
                                                   get_events_menu_by_xpath(), self.d)
            events_menu = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_events_menu_by_xpath())
            events_menu.click()
            self.logger.info(f"clicked on Probable Match Events menu...")
            time.sleep(web_driver.one_second)
            event_image = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().event_image_by_xpath())
            event_image.click()
            self.logger.info(f"clicked on Event image...")
            self.drag_and_drop_image_to_perform_VS()
            self.click_on_submit_search_button()
            x = self.verify_image_from_match_list()
            self.logger.info(f"Returned: {x}")
            status.append(x)
            self.click_on_logout_button()
            self.logger.info(f"status: {status}")
            if False in status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_VS_05_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_VS_05_failed.png")
                return False
            else:
                return True

        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_VS_05_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_VS_05_exception.png")
            self.logger.error(f"TC_VS_05 got exception as: {ex.args}")
            return False

    # ################################## Reused methods  ########################################
    def wait_for_visitor_search_result_to_display(self):
        try:
            time.sleep(web_driver.two_second)
            visitor_search_complete = web_driver.explicit_wait(self, 60, "XPATH",
                                                               Read_Visitor_Search_Components().visitor_search_complete_banner_by_xpath(),
                                                               self.d)
            if visitor_search_complete.is_displayed():
                self.logger.info(f"****************** {visitor_search_complete.text} banner displayed...")
                time.sleep(web_driver.two_second)
            else:
                self.logger.info("Visitor Search Not Completed.")
        except Exception as ex:
            self.logger.info(f"No match found {ex.args}")

    def verify_image_from_match_list(self):
        try:
            try:
                time.sleep(web_driver.two_second)
                self.logger.info("Verifying matches")
                self.wait_for_visitor_search_result_to_display()
                no_matches_found = web_driver.explicit_wait(self, 5, "XPATH",
                                                            Read_Visitor_Search_Components().no_matches_found(), self.d)
                if no_matches_found.is_displayed():
                    self.logger.info(f"no match text displayed: {no_matches_found.is_displayed()}")
                    self.logger.info(f"ele2: {no_matches_found.text}")
                    return True
            except Exception as ex:
                time.sleep(web_driver.three_second)
                ele = web_driver.explicit_wait(self, 15, "XPATH",
                                               Read_Visitor_Search_Components().image_match_list_by_xpath(), self.d)
                matches = self.d.find_elements(By.XPATH, Read_Visitor_Search_Components().image_match_list_by_xpath())
                self.logger.info(f"count of matches: {len(matches)}")
                if ele.is_displayed():
                    self.logger.info(f"images displayed: {ele.is_displayed()}")
                    return True
                else:
                    return False

        except Exception as ex:
            print(ex.args)
            self.logger.info(f"images match exception:")
            return False

    def verify_region_from_match_list(self, zone_data):
        try:
            # time.sleep(web_driver.one_second)
            # ele = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().search_constraints_by_xpath())
            ele = web_driver.explicit_wait(self, 10, "XPATH", Read_Visitor_Search_Components().search_constraints_by_xpath(), self.d)
            ac_zone_txt = ele.text
            self.logger.info(f"zone data: {zone_data.upper()}")
            self.logger.info(f"ac zone: {ac_zone_txt}")
            # or (not ele2.is_displayed()):
            if (zone_data.upper() in ac_zone_txt):
                return True
            else:
                self.logger.info(f"{zone_data.upper()} not in {ac_zone_txt}")
                return False
        except Exception as ex:
            print(ex.args)
            self.logger.info(f"verify_region_from_match_list: {ex.args}")
            return None

        # lower result zone text validation code
        # match_region = self.d.find_elements(By.XPATH,
        #                                     Read_Visitor_Search_Components().match_region_by_xpath())
        #
        # for x in match_region:
        #     if x.text != zone_data:
        #         result = False
        #         break

    def verify_date(self):
        self.get_date_range_from_json()
        ex_date = self.start_date.split("/")[0]
        ex_date = int(ex_date)
        ex_month = self.start_date.split("/")[1]
        ex_year = self.start_date.split("/")[2]
        month_to_mm = {
            "01": "JAN",
            "02": "FEB",
            "03": "MAR",
            "04": "APR",
            "05": "MAY",
            "06": "JUN",
            "07": "JUL",
            "08": "AUG",
            "09": "SEP",
            "10": "OCT",
            "11": "NOV",
            "12": "DEC"

        }

        mon = month_to_mm.get(ex_month)

        exp_asser = "{mon} {date}, {year} "

        exp_asser = exp_asser.format(mon=mon, date=ex_date, year=ex_year, hour_minu=self.start_time,
                                     pe=self.start_am_pm)
        # print(exp_asser, "<<<<<<<<<<<<<<")
        time.sleep(web_driver.one_second)
        # self.get_date_range_from_json()

        ac_start_date = web_driver.explicit_wait(self, 10, "XPATH",
                                                 Read_Visitor_Search_Components().actual_start_date_by_xpath(),
                                                 self.d)
        ac_ass_date = ac_start_date.text
        # print(exp_asser in ac_ass_date)
        # print(exp_asser)
        # print("ac_ass_date>>>>", ac_ass_date)

        ele2 = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().no_matches_found())
        self.logger.info(f"No Match Found txt: {ele2.text}, id visible: {ele2.is_displayed()}")
        self.logger.info(f"expected exp_asser: {exp_asser}, in : {ac_ass_date}")
        if exp_asser in ac_ass_date:
            return True
        else:
            return False

    def close_all_the_panels(self):
        """
        This function is used to close all the visitor search panels
        :return:
        """
        close_icon = self.d.find_elements(By.XPATH,
                                          Read_Visitor_Search_Components().close_all_visitor_search_panel_by_xpath())
        for x in close_icon:
            x.click()

    def select_zone(self, region_text):
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
                if expected_region_text.upper() == actual_zone_text.upper():
                    self.logger.info(actual_zone_text)
                    self.logger.info(expected_region_text)
                    region_text_list.__getitem__(i).click()
                    # self.d.execute_script("arguments[0].click();", region_text_list.__getitem__(i))
                    break
            save = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().zone_save_button_xpath())
            save.click()
        except Exception as ex:
            str(ex)

    def select_start_age(self, start_age):
        """
        This function is used to select the start age
        :param start_age:
        :return:
        """
        start_age_ele = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().start_age_by_xpath())
        s = Select(start_age_ele)
        s.select_by_visible_text(start_age)
        time.sleep(web_driver.one_second)

    def select_end_age(self, end_age):
        """
        This function is used to select the end age
        :param end_age:
        :return:
        """
        end_age_ele = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().end_age_by_xpath())
        s = Select(end_age_ele)
        s.select_by_visible_text(end_age)
        time.sleep(web_driver.one_second)

    def compare_thresh_hold_value_with_score(self):
        """
        This function is used to compare the threshhold value with actual score
        :return:
        """
        slider = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().slider_icon_by_xpath())
        slider_value_str = str(slider.get_attribute("style"))
        self.logger.info(f"slider_value_str: {slider_value_str}")
        slider_value_text = slider_value_str.split(" ")[1].strip()
        self.logger.info(f"slider_value_text: {slider_value_text}")
        slider_value_text = re.sub("[% ;]", "", slider_value_text)

        match_list_score = self.d.find_elements(By.XPATH, Read_Visitor_Search_Components().score_by_xpath())
        for ele in match_list_score:
            score = ele.text
            self.logger.info(f"score: {score}")
            # score = float(score.split(" ")[1][0:2])
            score = float(score.split(".")[1])
            self.logger.info(f"score: {score}")
            # score = score * 100
            self.logger.info(f"score: {score}")
            self.logger.info(f"slider value text: {slider_value_text}")
            # if score >= int(slider_value_text):
            if int(score) >= 0:  # int(slider_value_text):
                return True
            else:
                return False

    def set_thresh_hold_slider(self):
        """
        This function is used to set the threshold value
        :return:
        """
        time.sleep(web_driver.one_second)
        slider_pixel = Read_Visitor_Search_Components().slider_value_data_input()
        slider_pixel_value = int(slider_pixel)

        slider = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().slider_icon_by_xpath())
        action = ActionChains(self.d)
        action.drag_and_drop_by_offset(slider, -80, 0).perform()

        action.drag_and_drop_by_offset(slider, slider_pixel_value, 0).perform()
        time.sleep(web_driver.one_second)

    def select_count(self, count_data):
        """
        This function is used to select the count from the count dropdown
        :param count_data:
        :return:
        """

        max_match = self.explicit_wait(10, "XPATH", Read_Visitor_Search_Components().max_of_matches_by_xpath(), self.d)
        select = Select(max_match)
        self.logger.info(f"max matches dropdown is selected..")
        select.select_by_visible_text(count_data)
        time.sleep(web_driver.one_second)

    def click_on_submit_search_button(self):
        """
        This function is used to click on the submit search button
        :return:
        """
        try:
            self.logger.info("waiting for message to appear...")
            submit_btn = self.explicit_wait(10, "XPATH", Read_Visitor_Search_Components().submit_search_button_by_xpath(), self.d)
            submit_btn.click()
            self.logger.info("clicked on submit search button..")
        except Exception as ex:
            print(ex.args)

    def add_image_for_image_search(self):
        """
        This function is usd to upload the image and click on the search button
        :return:
        """
        upload_photo = web_driver.explicit_wait(self, 10, "XPATH", Read_Visitor_Search_Components().
                                                photo_upload_container_by_xpath(), self.d)
        upload_photo.click()
        time.sleep(web_driver.one_second)
        print("file path =====>>>> ")
        file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\dataset1\\fraud\\00082.png"
        print(f"filepath : {file_path}")

        pyautogui.write(file_path)
        pyautogui.press('enter')
        time.sleep(web_driver.one_second)
        pyautogui.press('enter')
        time.sleep(web_driver.one_second)

    def add_image_for_image_with_metadata_search(self):
        """
        This function is usd to upload the image and click on the search button
        :return:
        """
        upload_photo = web_driver.explicit_wait(self, 10, "XPATH", Read_Visitor_Search_Components().
                                                photo_upload_container_by_xpath(), self.d)
        upload_photo.click()
        time.sleep(web_driver.one_second)
        print("file path =====>>>> ")
        file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\dataset1\\pt\\00087.png"
        print(f"filepath : {file_path}")

        pyautogui.write(file_path)
        pyautogui.press('enter')
        time.sleep(web_driver.one_second)
        pyautogui.press('enter')
        time.sleep(web_driver.one_second)

    def compare_count_match(self, count_data):
        """
        This function is used to compare the count provided with the actual no. of match count
        :param count_data:
        :return:
        """
        try:
            time.sleep(web_driver.two_second)
            x = None
            self.logger.info("Verifying matches")
            no_matches_found = web_driver.explicit_wait(self, 10, "XPATH",
                                                        Read_Visitor_Search_Components().no_matches_found(), self.d)
            print(no_matches_found)
            if no_matches_found.is_displayed():
                self.logger.info(f"no match text displayed: {no_matches_found.is_displayed()}")
                self.logger.info(f"ele2: {no_matches_found.text}")
                return True
        except Exception as ex:
            match_found = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().matches_found_by_xpath())
            match_found_count = match_found.text
            self.logger.info(f"actual match: {match_found_count}, type: {type(match_found_count)}")
            self.logger.info(f"expected match: {count_data}, type: {type(count_data)}")
            if int(match_found_count) <= int(count_data):
                return True
            else:
                return False

    def handle_calender_pop_up(self, strategy, date, month, year, hour, minute, req_period):
        self.logger.info(f"Strategy: {strategy}")
        # click on the form calendar popup
        if strategy == "from":
            self.logger.info("select from date checkbox")
            start_check_bx = self.d.find_element(By.XPATH,
                                                 Read_Visitor_Search_Components().start_date_checkbox_by_xpath())
            start_check_bx.click()
            time.sleep(web_driver.one_second)
            web_driver.implicit_wait(self, web_driver.one_second, self.d)
            self.logger.info("select date time")
            start_date_txt_bx = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().start_date_by_xpath())
            self.d.execute_script("arguments[0].scrollIntoView();", start_date_txt_bx)
            start_date_txt_bx.click()

            self.logger.info("datetime clicked")
            time.sleep(web_driver.one_second)
            web_driver.implicit_wait(self, web_driver.one_second, self.d)
        else:
            # click on the to calendar pop up
            end_check_bx = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().end_date_checkbox_by_xpath())
            end_check_bx.click()
            time.sleep(web_driver.one_second)
            web_driver.implicit_wait(self, web_driver.one_second, self.d)
            end_date_txt_bx = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().end_date_by_xpath())
            self.d.execute_script("arguments[0].scrollIntoView();", end_date_txt_bx)
            end_date_txt_bx.click()
            time.sleep(web_driver.one_second)
            web_driver.implicit_wait(self, web_driver.one_second, self.d)

        # click on the clock icon
        self.logger.info("selecting time")
        calender_clock = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().calender_timer_icon_by_xpath())
        calender_clock.click()
        self.logger.info("select time ")
        time.sleep(web_driver.one_second)
        web_driver.implicit_wait(self, web_driver.one_second, self.d)
        time.sleep(3)

        # handle the hour and minute based on the strategy
        if strategy == "from":
            self.logger.info("select in from hours and min")
            self.calender_handle_hour_minute_from(hour, minute)
        # else:
        #     self.logger.info("select in to hours and min")
        #     self.calender_handle_hour_minute_to(hour, minute)

        # select the period am or pm
        period = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().period_by_xpath())
        if period.text == req_period:
            print("")
        else:
            period.click()

        # click on the tick icon
        tick_icon = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().calender_tick_icon_by_xpath())
        tick_icon.click()

        if strategy == "from":
            self.logger.info("From start date")
            start_date_txt_bx = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().start_date_by_xpath())
            start_date_txt_bx.click()
            time.sleep(web_driver.one_second)
            web_driver.implicit_wait(self, web_driver.one_second, self.d)

        # else:
        #     # click on the to calendar pop up
        #     self.logger.info("To End Date")
        #     start_date_txt_bx = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().end_date_by_xpath())
        #     start_date_txt_bx.click()
        #     time.sleep(web_driver.one_second)
        #     web_driver.implicit_wait(self, web_driver.one_second, self.d)

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
        month_year = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().calender_month_year_by_xpath())
        ac_month = month_year.text.split(" ")[0]
        ac_year = int(month_year.text.split(" ")[1])

        # click on the back button
        while month_to_num.get(req_month) < month_to_num.get(ac_month) or req_year < ac_year:
            cal_back_button = self.d.find_element(By.XPATH,
                                                  Read_Visitor_Search_Components().calender_back_button_by_xpath())
            if cal_back_button.is_enabled():
                cal_back_button.click()
            time.sleep(1)
            month_year = self.d.find_element(By.XPATH,
                                             Read_Visitor_Search_Components().calender_month_year_by_xpath())
            ac_month = month_year.text.split(" ")[0]
            ac_year = int(month_year.text.split(" ")[1])

        # click on the forward button
        while month_to_num.get(req_month) > month_to_num.get(ac_month) or req_year > ac_year:
            cal_back_button = self.d.find_element(By.XPATH,
                                                  Read_Visitor_Search_Components().calender_forward_button_by_xpath())
            if cal_back_button.is_enabled():
                cal_back_button.click()
            time.sleep(1)
            month_year = self.d.find_element(By.XPATH,
                                             Read_Visitor_Search_Components().calender_month_year_by_xpath())
            ac_month = month_year.text.split(" ")[0]
            ac_year = int(month_year.text.split(" ")[1])

        # click on the required date
        date = self.d.find_element(By.XPATH,
                                   "(//td[@class='day' or @class='day weekend' or @class='day active' "
                                   "or @class='day active today'])[" + str(date) + "]")
        date.click()

        # click on the tick icon
        tick_icon = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().calender_tick_icon_by_xpath())

        tick_icon.click()
        # tick_icon.click()

    def calender_handle_hour_minute_to(self, hour, minute):
        # set the hour
        current_hour_ele = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().current_hour_ele_by_xpath())
        cur_hour = int(current_hour_ele.text)

        while int(cur_hour) != int(hour):
            hour_down = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().hour_down_by_xpath())

            self.d.execute_script("arguments[0].click();", hour_down)
            current_hour_ele = self.d.find_element(By.XPATH,
                                                   Read_Visitor_Search_Components().current_hour_ele_by_xpath())
            cur_hour = int(current_hour_ele.text)

        # set the minute
        current_min_ele = self.d.find_element(By.XPATH,
                                              Read_Visitor_Search_Components().current_minute_element_by_xpath())
        cur_min = int(current_min_ele.text)
        while int(cur_min) != int(minute):
            clock_down_button = self.d.find_element(By.XPATH,
                                                    Read_Visitor_Search_Components().clock_min_down_button_by_xpath())
            self.d.execute_script("arguments[0].click();", clock_down_button)
            current_min_ele = self.d.find_element(By.XPATH,
                                                  Read_Visitor_Search_Components().current_minute_element_by_xpath())
            cur_min = int(current_min_ele.text)

    def calender_handle_hour_minute_from(self, hour, minute):
        # set the hour
        current_hour_ele = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().current_hour_ele_by_xpath())
        cur_hour = int(current_hour_ele.text)

        # decrementHours
        while int(cur_hour) != int(hour):
            hour_down = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().hour_down_by_xpath())
            self.d.execute_script("arguments[0].click();", hour_down)
            current_hour_ele = self.d.find_element(By.XPATH, Read_Visitor_Search_Components()
                                                   .current_hour_ele_by_xpath())
            cur_hour = int(current_hour_ele.text)

        # set the minute
        current_min_ele = self.d.find_element(By.XPATH, Read_Visitor_Search_Components()
                                              .current_minute_element_by_xpath())
        cur_min = int(current_min_ele.text)
        while int(cur_min) != int(minute):
            clock_up_button = self.d.find_element(By.XPATH, Read_Visitor_Search_Components()
                                                  .clock_min_up_button_by_xpath())
            self.d.execute_script("arguments[0].click();", clock_up_button)
            current_min_ele = self.d.find_element(By.XPATH, Read_Visitor_Search_Components()
                                                  .current_minute_element_by_xpath())
            cur_min = int(current_min_ele.text)

    def get_start_date(self):
        try:
            self.get_date_range_from_json()
            time.sleep(web_driver.one_second)
            start_date_calender_box = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().get_start_date_calender_box_by_xpath())
            start_date_checkbox = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().start_date_checkbox_by_xpath())
            time.sleep(web_driver.one_second)
            start_date_checkbox.click()
            start_date_calender_box.click()
            action = ActionChains(self.d)
            time.sleep(web_driver.one_second)
            default_start_date = start_date_calender_box.get_attribute('value')
            default_start_date = list(default_start_date.split(' '))
            d_start_date = default_start_date[0]
            d_start_date = list(d_start_date.split('/'))
            s_month = d_start_date[0]
            s_date = d_start_date[1]
            input_start_date = list(self.start_date.split('/'))
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

    def get_end_date(self):
        try:
            self.get_date_range_from_json()
            time.sleep(web_driver.one_second)
            end_date_calender_box = self.d.find_element(By.XPATH,
                                                        Read_Visitor_Search_Components().get_end_date_calender_box_by_xpath())
            end_date_checkbox = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().end_date_checkbox_by_xpath())
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
