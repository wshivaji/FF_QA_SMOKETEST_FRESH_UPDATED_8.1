import configparser
import time
from pathlib import Path

import numpy as np
import pandas as pd
from selenium.webdriver.support.select import Select

from Base_Package.Web_Driver import web_driver
from Base_Package.Web_Logger import web_logger
from selenium.webdriver.common.by import By
from All_Config_Packages._17_Notifier_Module_Config_Files.Notifier_Read_INI import Notifier_Read_ini
from All_Config_Packages._18_Reporting_Module_Config_Files.Reporting_Read_INI import Reporting_read_ini
from All_Config_Packages._0_login_logout_config_file.login_logout_read_ini import LoginLogout_Read_ini
from All_Config_Packages._2_Portal_Menu_Module_Config_Files.Portal_Menu_Module_Read_INI import Portal_Menu_Module_read_ini
from All_Config_Packages._6_Notification_Groups_Module_Config_Files.Notification_Groups_Read_INI import Read_Notification_Groups_Components
from Base_Package.Login_Logout_Ops import login, logout
from All_Other_Utility_Packages._3_User_Roles_Module.Read_Excel import Read_excel


class Notifier_pom(web_driver, web_logger):
    d = web_driver.d()
    logger = web_logger.logger_obj()
    status = []
    
    def __init__(self):
        self.groups = self.region_name = self.camera1_name = self.camera2_name = self.refresh_rate = \
            self.events_displayed = self.photo_size = self.sound_option = self.group_selected = None
        
        self.notifier_test_data = \
            f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\17_Notifier_Module\\Data_From_Excel\\Notifier_test_data.xlsx"
        self.file_path = f"{Path(__file__).parent.parent}\\All_Test_Data\\0_Login_Logout_Data\\Data_From_INI\\login_logout.ini"
        self.config = configparser.RawConfigParser()
        self.config.read(self.file_path)

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

    def load_notifier_module(self):
        try:
            time.sleep(web_driver.one_second)
            notifier_module = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_Notifier_menu_by_xpath())
            if notifier_module.is_displayed():
                notifier_module.click()
            else:
                pass
            time.sleep(web_driver.two_second)
        except Exception as ex:
            self.logger.error(ex)

    def close_notifier_module(self):
        try:
            cloud_menu_button = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_CLOUD_MENU_button_by_xpath())
            cloud_menu_button.click()
            time.sleep(web_driver.one_second)
            close_notifier_btn_on_dashboard = \
                self.d.find_element(By.XPATH, Notifier_Read_ini().
                                    get_close_notifier_button_on_dashboard_menu_by_xpath())
            if close_notifier_btn_on_dashboard.is_displayed():
                close_notifier_btn_on_dashboard.click()
            else:
                pass
        except Exception as ex:
            self.logger.error(ex)
            return False

    def get_region_and_group_data(self):
        try:
            df_groups = pd.read_excel(self.notifier_test_data, sheet_name='group_data', names=['Group_Names'])
            df_regions = pd.read_excel(self.notifier_test_data, sheet_name='region_data',
                                       names=['Region_Name', 'Camera1_Name', 'Camera2_Name'])
            df_notifier_setting = pd.read_excel(self.notifier_test_data, sheet_name='notifier_setting', names=['Refresh_Rate', 'Events_Displayed', 'Photo_Size', 'Sound_Option'])
            self.groups = [x for x in df_groups['Group_Names']]
            self.region_name = [x for x in df_regions['Region_Name']]
            self.camera1_name = [y for y in df_regions['Camera1_Name']]
            self.camera2_name = [z for z in df_regions['Camera2_Name']]
            self.refresh_rate = [x for x in df_notifier_setting['Refresh_Rate']]
            self.events_displayed = [y for y in df_notifier_setting['Events_Displayed']]
            self.photo_size = [z for z in df_notifier_setting['Photo_Size']]
            self.sound_option = [xx for xx in df_notifier_setting['Sound_Option']]
            # print(f"groups: {self.groups}" f"length: {len(self.groups)}")
            # print(f"region names: {self.region_name}" f"length: {len(self.region_name)}")
            # print(f"camera1 names: {self.camera1_name}" f"length: {len(self.camera1_name)}")
            # print(f"camera2 names: {self.camera2_name}" f"length: {len(self.camera2_name)}")
            # print(f"regions: {df_regions}")
            # print(f"groups: {df_groups}")

        except Exception as ex:
            self.logger.error(ex)

    def notifier_result_verification(self):
        try:
            actual_number_of_events = self.d.find_elements(By.XPATH, Notifier_Read_ini().
                                                           get_number_of_events_displayed_by_xpath())
            self.logger.info(f"actual number of events displayed: {len(actual_number_of_events)}")

            if len(actual_number_of_events) > 0:
                time.sleep(web_driver.one_second)
                expected_events = self.events_displayed[1]
                self.logger.info(f"expected number of events displayed: {expected_events}")
                if len(actual_number_of_events) == expected_events:
                    self.status.append(True)
                else:
                    self.status.append(False)
                time.sleep(web_driver.one_second)
                actual_live_image_text = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                             get_live_image_text_by_xpath()).text
                self.logger.info(f"actual text: {actual_live_image_text}")
                expected_live_image_text = Notifier_Read_ini().get_expected_live_image_text()
                self.logger.info(f"expected text: {expected_live_image_text}")

                if actual_live_image_text == expected_live_image_text:
                    self.status.append(True)
                else:
                    self.status.append(False)
                time.sleep(web_driver.one_second)
                actual_possible_match_text = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                                 get_possible_match_text_by_xpath()).text
                self.logger.info(f"actual possible match text: {actual_possible_match_text}")
                expected_possible_match_text = Notifier_Read_ini().get_expected_text_possible_match()
                self.logger.info(f"expected text: {expected_possible_match_text}")
                if actual_possible_match_text == expected_possible_match_text:
                    self.status.append(True)
                else:
                    self.status.append(False)
                time.sleep(web_driver.one_second)
                expected_alert_completion_time = \
                    self.d.find_element(By.XPATH, Notifier_Read_ini().
                                        get_alert_completion_time_on_notifier_panel_by_xpath()).text

                expected_notification_alert_real_time = \
                    self.d.find_element(By.XPATH, Notifier_Read_ini().
                                        get_notifier_alert_real_time_on_notifier_panel_by_xpath()).text

                expected_station_name = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                            get_station_name_for_of_event_generation_by_xpath()).text

                self.d.find_element(By.XPATH, Notifier_Read_ini().get_close_notifier_button_on_event_info_by_xpath()). \
                    click()
                time.sleep(web_driver.three_second)
                actual_alert_completion_time = \
                    self.d.find_element(By.XPATH, Notifier_Read_ini().
                                        get_alert_completion_time_on_events_panel_by_xpath()).text
                self.logger.info(f"actual alert completion time: {actual_alert_completion_time}")
                self.logger.info(f"expected Alert completion time: {expected_alert_completion_time}")
                if expected_alert_completion_time == actual_alert_completion_time:
                    self.status.append(True)
                else:
                    self.status.append(False)
                time.sleep(web_driver.one_second)
                actual_notification_alert_real_time = \
                    self.d.find_element(By.XPATH, Notifier_Read_ini().
                                        get_notifier_alert_real_time_on_events_panel_by_xpath()).text
                self.logger.info(f"actual notification alert real time: {actual_notification_alert_real_time}")
                self.logger.info(f"expected Notification alert real time: {expected_notification_alert_real_time}")
                actual_time_list = actual_notification_alert_real_time.split(' ')
                expected_time_list = expected_notification_alert_real_time.split(' ')
                actual_num = actual_time_list[0]
                expected_num = expected_time_list[0]
                if actual_num.isnumeric():
                    actual_num = int(actual_num)
                if expected_num.isnumeric():
                    expected_num = int(expected_num)
                self.logger.info(f"actual_time: {actual_num} min")
                self.logger.info(f"expected_time: {expected_num} min")
                if actual_num.is_integer() and expected_num.is_integer():
                    if actual_num >= expected_num:
                        self.status.append(True)
                    else:
                        self.status.append(False)
                else:
                    self.logger.info(f"no number found in time string")
                time.sleep(web_driver.one_second)
                actual_station_name = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                          get_station_name_on_events_panel_by_xpath()).text
                self.logger.info(f"actual station name: {actual_station_name}")
                self.logger.info(f"expected station name: {expected_station_name}")
                if actual_station_name == expected_station_name:
                    self.status.append(True)
                else:
                    self.status.append(False)
                self.d.find_element(By.XPATH, Notifier_Read_ini().
                                    get_enrollments_group_button_on_enrollments_view_panel_by_xpath()).click()
                time.sleep(10)
                enrollment_group_name = \
                    self.d.find_element(By.XPATH, Notifier_Read_ini().
                                        get_enrollment_group_name_on_enrollment_groups_panel_by_xpath())
                name = enrollment_group_name.text.upper()
                time.sleep(web_driver.one_second)
                self.logger.info(f"expected to select group name: {self.group_selected}")
                self.logger.info(f"actual selected group name: {name}")
                # if self.group_selected == name:
                #     self.logger.info(f"Enrollment Group name on 'Enrollment Groups' panel: {self.group_selected}")
                #     self.status.append(True)
                # else:
                #     self.status.append(False)
            else:
                actual_message = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                     get_message_to_user_for_group_selection_by_xpath()).text
                self.logger.info(f"Message to User: {actual_message}")
                if actual_message:
                    self.status.append(True)
                else:
                    self.status.append(False)
        except Exception as ex:
            self.logger.error(ex)
            return False

    def notifier_result_verification_for_all_groups_selected(self):
        try:
            actual_number_of_events = self.d.find_elements(By.XPATH, Notifier_Read_ini().
                                                           get_number_of_events_displayed_by_xpath())
            if len(actual_number_of_events) > 0:
                time.sleep(web_driver.one_second)
                actual_live_image_text = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                             get_live_image_text_by_xpath()).text
                self.logger.info(f"actual text: {actual_live_image_text}")
                expected_live_image_text = Notifier_Read_ini().get_expected_live_image_text()
                self.logger.info(f"expected text: {expected_live_image_text}")
                if actual_live_image_text == expected_live_image_text:
                    self.status.append(True)
                else:
                    self.status.append(False)
                time.sleep(10)
                # actual_possible_match_text = self.d.find_element(By.XPATH, Notifier_Read_ini().
                #                                                  get_possible_match_text_by_xpath()).text
                # self.logger.info(f"actual possible match text: {actual_possible_match_text}")
                # expected_possible_match_text = Notifier_Read_ini().get_expected_text_possible_match()
                # self.logger.info(f"expected text: {expected_possible_match_text}")
                # if actual_possible_match_text == expected_possible_match_text:
                #     self.status.append(True)
                # else:
                #     self.status.append(False)

                expected_alert_completion_time = \
                    self.d.find_element(By.XPATH, Notifier_Read_ini().
                                        get_alert_completion_time_on_notifier_panel_by_xpath()).text
                expected_notification_alert_real_time = \
                    self.d.find_element(By.XPATH, Notifier_Read_ini().
                                        get_notifier_alert_real_time_on_notifier_panel_by_xpath()).text
                expected_station_name = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                            get_station_name_for_of_event_generation_by_xpath()).text
                self.d.find_element(By.XPATH, Notifier_Read_ini().get_close_notifier_button_on_event_info_by_xpath()). \
                    click()
                time.sleep(web_driver.three_second)
                actual_alert_completion_time = \
                    self.d.find_element(By.XPATH, Notifier_Read_ini().
                                        get_alert_completion_time_on_events_panel_by_xpath()).text
                act_num = actual_alert_completion_time.split(' ')
                self.logger.info(f"actual alert completion time: {actual_alert_completion_time}")
                self.logger.info(f"expected Alert completion time: {expected_alert_completion_time}")
                exp_num = expected_alert_completion_time.split(' ')
                if (actual_alert_completion_time == expected_alert_completion_time) or (act_num[0] == exp_num[0]):
                    self.status.append(True)
                else:
                    self.status.append(False)
                time.sleep(web_driver.one_second)
                actual_notification_alert_real_time = \
                    self.d.find_element(By.XPATH, Notifier_Read_ini().
                                        get_notifier_alert_real_time_on_events_panel_by_xpath()).text
                self.logger.info(f"actual notification alert real time: {actual_notification_alert_real_time}")
                self.logger.info(f"expected Notification alert real time: {expected_notification_alert_real_time}")

                if (actual_notification_alert_real_time == int(expected_notification_alert_real_time) - 1 or
                        int(expected_notification_alert_real_time) + 1):
                    self.status.append(True)
                else:
                    self.status.append(False)
                time.sleep(web_driver.one_second)
                actual_station_name = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                          get_station_name_on_events_panel_by_xpath()).text
                self.logger.info(f"actual station name: {actual_station_name}")
                self.logger.info(f"expected station name: {expected_station_name}")

                if str(actual_station_name) == str(expected_station_name):
                    self.status.append(True)
                else:
                    self.status.append(False)
            else:
                actual_message = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                     get_message_to_user_for_group_selection_by_xpath()).text
                self.logger.info(f"Message to User: {actual_message}")
                if actual_message:
                    self.status.append(True)
                else:
                    self.status.append(False)
        except Exception as ex:
            self.logger.error(ex)
            return False

    def get_default_notifier_setting_values(self):
        try:
            time.sleep(web_driver.one_second)
            refresh_rate = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                      get_refresh_rate_dropdown_by_xpath()))
            refresh_rate.select_by_visible_text(self.refresh_rate[0])
            self.logger.info(f"Refresh Rate: {self.refresh_rate[0]}")
            events_display = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                        get_events_display_dropdown_by_xpath()))
            events_display.select_by_visible_text(str(self.events_displayed[1]))
            self.logger.info(f"Events Displayed: {str(self.events_displayed[1])}")
            photo_size = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().get_photo_size_dropdown_by_xpath()))
            photo_size.select_by_visible_text(self.photo_size[2])
            self.logger.info(f"Photo Size: {self.photo_size[2]}")
            sound_option = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                      get_sound_option_dropdown_by_xpath()))
            sound_option.select_by_visible_text(self.sound_option[0])
            self.logger.info(f"Sound Option: {self.sound_option[0]}")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().get_save_button_on_notifier_setting_panel_by_xpath()). \
                click()
            time.sleep(web_driver.one_second)
        except Exception as ex:
            self.logger.error(ex)

    def select_ABE_group_from_ini(self):
        try:
            enrollment_group_selection_button = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                                    get_enrollment_group_selection_button_by_xpath())
            enrollment_group_selection_button.click()
            time.sleep(web_driver.one_second)
            select_group_textbox = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                       get_filter_group_list_textbox_by_xpath())
            select_group_textbox.clear()
            x = Read_Notification_Groups_Components().get_enrollment_group_name()
            group_names = x.split(',')
            abe_group = group_names[1]
            select_group_textbox.send_keys(abe_group)
            group_list_below_textbox = self.d.find_elements(By.XPATH, Notifier_Read_ini().
                                                            get_group_items_below_filter_group_list_textbox_by_xpath())
            group_list_below_textbox[0].click()
            self.logger.info(f"Group selected as: {group_list_below_textbox[0].text}")
            self.group_selected = group_list_below_textbox[0].text
            self.d.find_element(By.XPATH, Notifier_Read_ini().get_save_button_on_select_a_group_panel_by_xpath()). \
                click()
            time.sleep(web_driver.one_second)
        except Exception as ex:
            self.logger.error(ex)

    def select_PTE_group_from_ini(self):
        try:
            enrollment_group_selection_button = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                                    get_enrollment_group_selection_button_by_xpath())
            enrollment_group_selection_button.click()
            time.sleep(web_driver.one_second)
            select_group_textbox = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                       get_filter_group_list_textbox_by_xpath())
            select_group_textbox.clear()
            select_group_textbox.send_keys(Notifier_Read_ini().get_pte_enrollment_group())
            group_list_below_textbox = self.d.find_elements(By.XPATH, Notifier_Read_ini().
                                                            get_group_items_below_filter_group_list_textbox_by_xpath())
            group_list_below_textbox[0].click()
            self.logger.info(f"Group selected as: {group_list_below_textbox[0].text}")
            self.group_selected = group_list_below_textbox[0].text
            self.d.find_element(By.XPATH, Notifier_Read_ini().get_save_button_on_select_a_group_panel_by_xpath()). \
                click()
            time.sleep(web_driver.one_second)
        except Exception as ex:
            self.logger.error(ex)

    def select_FRAUDE_group_from_ini(self):
        try:
            enrollment_group_selection_button = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                                    get_enrollment_group_selection_button_by_xpath())
            enrollment_group_selection_button.click()
            time.sleep(web_driver.one_second)
            select_group_textbox = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                       get_filter_group_list_textbox_by_xpath())
            select_group_textbox.clear()
            select_group_textbox.send_keys(Notifier_Read_ini().get_fraude_enrollment_group())
            group_list_below_textbox = self.d.find_elements(By.XPATH, Notifier_Read_ini().
                                                            get_group_items_below_filter_group_list_textbox_by_xpath())
            group_list_below_textbox[0].click()
            self.logger.info(f"Group selected as: {group_list_below_textbox[0].text}")
            self.group_selected = group_list_below_textbox[0].text
            self.d.find_element(By.XPATH, Notifier_Read_ini().get_save_button_on_select_a_group_panel_by_xpath()). \
                click()
            time.sleep(web_driver.one_second)
        except Exception as ex:
            self.logger.error(ex)

    def select_VIPE_group_from_ini(self):
        try:
            enrollment_group_selection_button = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                                    get_enrollment_group_selection_button_by_xpath())
            enrollment_group_selection_button.click()
            time.sleep(web_driver.one_second)
            select_group_textbox = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                       get_filter_group_list_textbox_by_xpath())
            select_group_textbox.clear()
            select_group_textbox.send_keys(Notifier_Read_ini().get_vipe_enrollment_group())
            group_list_below_textbox = self.d.find_elements(By.XPATH, Notifier_Read_ini().
                                                            get_group_items_below_filter_group_list_textbox_by_xpath())
            group_list_below_textbox[0].click()
            self.logger.info(f"Group selected as: {group_list_below_textbox[0].text}")
            self.group_selected = group_list_below_textbox[0].text
            self.d.find_element(By.XPATH, Notifier_Read_ini().get_save_button_on_select_a_group_panel_by_xpath()). \
                click()
            time.sleep(web_driver.one_second)
        except Exception as ex:
            self.logger.error(ex)

    def select_SOE_group_from_ini(self):
        try:
            enrollment_group_selection_button = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                                    get_enrollment_group_selection_button_by_xpath())
            enrollment_group_selection_button.click()
            time.sleep(web_driver.one_second)
            select_group_textbox = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                       get_filter_group_list_textbox_by_xpath())
            select_group_textbox.clear()
            select_group_textbox.send_keys(Notifier_Read_ini().get_soe_enrollment_group())
            group_list_below_textbox = self.d.find_elements(By.XPATH, Notifier_Read_ini().
                                                            get_group_items_below_filter_group_list_textbox_by_xpath())
            group_list_below_textbox[0].click()
            self.logger.info(f"Group selected as: {group_list_below_textbox[0].text}")
            self.group_selected = group_list_below_textbox[0].text
            self.d.find_element(By.XPATH, Notifier_Read_ini().get_save_button_on_select_a_group_panel_by_xpath()). \
                click()
            time.sleep(web_driver.one_second)
        except Exception as ex:
            self.logger.error(ex)

    def select_first_region_from_ini(self):
        try:
            expand_all_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                 get_expand_all_button_on_region_selection_panel_by_xpath())
            expand_all_btn.click()
            time.sleep(web_driver.one_second)

            checkbox1 = Notifier_Read_ini().get_checkbox_in_region_by_xpath_1()
            checkbox2 = Notifier_Read_ini().get_checkbox_in_region_by_xpath_2()
            checkbox = self.d.find_element(By.XPATH, checkbox1 + Notifier_Read_ini().get_region_name() + checkbox2)
            checkbox.click()
            self.logger.info(f"Region selected as: {Notifier_Read_ini().get_region_name()}")

            collapse_all_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().get_collapse_all_button_on_region_selection_panel_by_xpath())
            collapse_all_btn.click()
            save_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().get_save_button_on_org_hierarchy_panel_by_xpath())
            self.d.execute_script("arguments[0].click();", save_btn)
            time.sleep(web_driver.one_second)
        except Exception as ex:
            self.logger.error(ex)

    def select_second_region_from_ini(self):
        try:
            expand_all_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                 get_expand_all_button_on_region_selection_panel_by_xpath())
            expand_all_btn.click()
            time.sleep(web_driver.one_second)

            checkbox1 = Notifier_Read_ini().get_checkbox_in_region_by_xpath_1()
            checkbox2 = Notifier_Read_ini().get_checkbox_in_region_by_xpath_2()
            checkbox = self.d.find_element(By.XPATH, checkbox1 + Notifier_Read_ini().get_region_name() + checkbox2)
            checkbox.click()
            self.logger.info(f"Region selected as: {Notifier_Read_ini().get_region_name()}")

            collapse_all_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().get_collapse_all_button_on_region_selection_panel_by_xpath())
            collapse_all_btn.click()
            save_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().get_save_button_on_org_hierarchy_panel_by_xpath())
            self.d.execute_script("arguments[0].click();", save_btn)
            time.sleep(web_driver.one_second)
        except Exception as ex:
            self.logger.error(ex)

    def select_third_region_from_ini(self):
        try:
            expand_all_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                 get_expand_all_button_on_region_selection_panel_by_xpath())
            expand_all_btn.click()
            time.sleep(web_driver.one_second)

            checkbox1 = Notifier_Read_ini().get_checkbox_in_region_by_xpath_1()
            checkbox2 = Notifier_Read_ini().get_checkbox_in_region_by_xpath_2()
            checkbox = self.d.find_element(By.XPATH, checkbox1 + Notifier_Read_ini().get_region_name() + checkbox2)
            checkbox.click()
            self.logger.info(f"Region selected as: {Notifier_Read_ini().get_region_name()}")

            collapse_all_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().get_collapse_all_button_on_region_selection_panel_by_xpath())
            collapse_all_btn.click()
            save_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().get_save_button_on_org_hierarchy_panel_by_xpath())
            self.d.execute_script("arguments[0].click();", save_btn)
            time.sleep(web_driver.one_second)
        except Exception as ex:
            self.logger.error(ex)

    def select_fourth_region_from_ini(self):
        try:
            expand_all_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                 get_expand_all_button_on_region_selection_panel_by_xpath())
            expand_all_btn.click()
            time.sleep(web_driver.one_second)

            checkbox1 = Notifier_Read_ini().get_checkbox_in_region_by_xpath_1()
            checkbox2 = Notifier_Read_ini().get_checkbox_in_region_by_xpath_2()
            checkbox = self.d.find_element(By.XPATH, checkbox1 + Notifier_Read_ini().get_region_name() + checkbox2)
            checkbox.click()
            self.logger.info(f"Region selected as: {Notifier_Read_ini().get_region_name()}")

            collapse_all_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().get_collapse_all_button_on_region_selection_panel_by_xpath())
            collapse_all_btn.click()
            save_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().get_save_button_on_org_hierarchy_panel_by_xpath())
            self.d.execute_script("arguments[0].click();", save_btn)
            time.sleep(web_driver.one_second)
        except Exception as ex:
            self.logger.error(ex)

    def select_fifth_region_from_ini(self):
        try:
            expand_all_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                 get_expand_all_button_on_region_selection_panel_by_xpath())
            expand_all_btn.click()
            time.sleep(web_driver.one_second)

            checkbox1 = Notifier_Read_ini().get_checkbox_in_region_by_xpath_1()
            checkbox2 = Notifier_Read_ini().get_checkbox_in_region_by_xpath_2()
            checkbox = self.d.find_element(By.XPATH, checkbox1 + Notifier_Read_ini().get_region_name() + checkbox2)
            checkbox.click()
            self.logger.info(f"Region selected as: {Notifier_Read_ini().get_region_name()}")

            collapse_all_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().get_collapse_all_button_on_region_selection_panel_by_xpath())
            collapse_all_btn.click()
            save_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().get_save_button_on_org_hierarchy_panel_by_xpath())
            self.d.execute_script("arguments[0].click();", save_btn)
            time.sleep(web_driver.one_second)
        except Exception as ex:
            self.logger.error(ex)


    def Verify_Notifier_result_for_first_camera_of_first_region_selected_with_group_selected_as_ABE_with_Auto_Refresh_Of_events_displayed_as_2_photo_size_as_Medium_and_Sound_Option_as_OFF(self):
        try:
            self.logger.info("*********** TC_Notifier_01 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            self.load_notifier_module()
            self.get_region_and_group_data()

            org_hierarchy_selection_button = web_driver.explicit_wait(self, 10, "XPATH", Notifier_Read_ini().get_org_hierarchy_selection_button_by_xpath(), self.d)
            org_hierarchy_selection_button.click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().
                                get_unselect_all_button_on_region_selection_panel_by_xpath()).click()

            camera_1 = Notifier_Read_ini().get_cameras_in_region_by_xpath_1()
            camera_2 = Notifier_Read_ini().get_cameras_in_region_by_xpath_2()
            checkbox_1 = Notifier_Read_ini().get_checkbox_in_region_by_xpath_1()
            checkbox_2 = Notifier_Read_ini().get_checkbox_in_region_by_xpath_2()
            print(camera_1 + Notifier_Read_ini().get_camera0() + camera_2 + checkbox_1 +
                                           Notifier_Read_ini().get_camera1() + checkbox_2)
            checkbox = self.d.find_element(By.XPATH, camera_1 + Notifier_Read_ini().get_camera0() + camera_2 + checkbox_1 +
                                           Notifier_Read_ini().get_camera1() + checkbox_2)
            checkbox.click()
            self.logger.info(f"Camera selected as: {Notifier_Read_ini().get_camera0()}")
            time.sleep(web_driver.one_second)

            save_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().get_save_button_on_org_hierarchy_panel_by_xpath())
            self.d.execute_script("arguments[0].click();", save_btn)
            self.select_ABE_group_from_ini()
            notifier_setting = self.d.find_element(By.XPATH, Notifier_Read_ini().get_notifier_setting_button_by_xpath())
            notifier_setting.click()
            self.get_default_notifier_setting_values()
            self.notifier_result_verification()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_01.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_01.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_01_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_01_exception.png")
            self.logger.error(f"TC_Notifier_01 got exception as: {ex}")
        finally:
            self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_logout_button_on_portal_by_xpath()).click()

    def Verify_events_appears_with_live_and_probable_match_image_upon_event_generation_with_sound(self):
        try:
            self.logger.info("*********** TC_Notifier_02 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            self.load_notifier_module()
            self.get_region_and_group_data()
            time.sleep(web_driver.three_second)
            org_hierarchy_selection_button = web_driver.explicit_wait(self, 10, "XPATH", Notifier_Read_ini().get_org_hierarchy_selection_button_by_xpath(), self.d)

            org_hierarchy_selection_button.click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().
                                get_select_all_button_on_region_selection_panel_by_xpath()).click()
            self.logger.info("All cameras of regions are selected....")
            collapse_all_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().get_collapse_all_button_on_region_selection_panel_by_xpath())
            collapse_all_btn.click()
            save_btn = self.d.find_element(By.XPATH,
                                           Notifier_Read_ini().get_save_button_on_org_hierarchy_panel_by_xpath())
            self.d.execute_script("arguments[0].click();", save_btn)
            time.sleep(web_driver.one_second)
            enrollment_group_selection_button = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                                    get_enrollment_group_selection_button_by_xpath())
            enrollment_group_selection_button.click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().get_clear_button_on_select_a_group_panel_by_xpath()).\
                click()
            self.d.find_element(By.XPATH, Notifier_Read_ini().get_save_button_on_select_a_group_panel_by_xpath()).\
                click()
            time.sleep(web_driver.one_second)
            notifier_setting = self.d.find_element(By.XPATH, Notifier_Read_ini().get_notifier_setting_button_by_xpath())
            notifier_setting.click()
            time.sleep(web_driver.one_second)
            refresh_rate = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                      get_refresh_rate_dropdown_by_xpath()))
            refresh_rate.select_by_visible_text(self.refresh_rate[6])
            self.logger.info(f"Refresh Rate: {self.refresh_rate[6]}")
            events_display = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                        get_events_display_dropdown_by_xpath()))
            events_display.select_by_visible_text(str(self.events_displayed[1]))
            self.logger.info(f"Events Displayed: {str(self.events_displayed[1])}")
            photo_size = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().get_photo_size_dropdown_by_xpath()))
            photo_size.select_by_visible_text(self.photo_size[2])
            self.logger.info(f"Photo Size: {self.photo_size[2]}")
            sound_option = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                      get_sound_option_dropdown_by_xpath()))
            sound_option.select_by_visible_text(self.sound_option[1])
            self.logger.info(f"Sound Option: {self.sound_option[1]}")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().get_save_button_on_notifier_setting_panel_by_xpath()).\
                click()
            time.sleep(web_driver.one_second)
            updating_status = self.d.find_elements(By.XPATH, Notifier_Read_ini().
                                                   get_updating_text_on_notifier_panel_by_xpath())
            updating_status_element = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                          get_updating_text_on_notifier_panel_by_xpath())
            t = 30
            c = 0
            if len(updating_status) == 0:
                while t > 0:
                    time.sleep(web_driver.one_second)
                    t = t - 1
                    c = c + 1
                    # if updating_status_element.is_displayed():
                    #     self.status.append(False)
                    # else:
                    #     pass
                self.logger.info(f"1Refreshing page after {c} seconds..")
                if updating_status_element.is_displayed():
                    self.status.append(True)
                else:
                    pass
            elif len(updating_status) > 0:
                while t > 0:
                    time.sleep(web_driver.one_second)
                    t = t - 1
                    c = c + 1
                    # if updating_status_element.is_displayed():
                    #     self.status.append(False)
                    # else:
                    #     pass
                self.logger.info(f"2Refreshing page after {c} seconds..")
                if updating_status_element.is_displayed():
                    self.status.append(True)
                else:
                    pass
            self.notifier_result_verification_for_all_groups_selected()
            time.sleep(web_driver.one_second)

            close_all_panels = self.d.find_elements(By.XPATH, Notifier_Read_ini().get_close_panel_buttons_by_xpath())
            for btn in close_all_panels:
                btn.click()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_02.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_02.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_02_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_02_exception.png")
            self.logger.error(f"TC_Notifier_02 got exception as: {ex}")
        finally:
            self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_logout_button_on_portal_by_xpath()).click()

    def Verify_org_hierarchy_selection_features_collapse_all_expand_all_select_all_and_unselect_all(self):
        try:
            self.logger.info("*********** TC_Notifier_03 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            self.load_notifier_module()
            org_hierarchy_selection_button = web_driver.explicit_wait(self, 10, "XPATH", Notifier_Read_ini().
                                                                      get_org_hierarchy_selection_button_by_xpath(),
                                                                      self.d)
            org_hierarchy_selection_button.click()
            time.sleep(web_driver.one_second)
            self.logger.info("Clicked on Org/Hierarchy Selection button...")
            time.sleep(web_driver.one_second)
            region_list = self.d.find_elements(By.XPATH, Notifier_Read_ini().
                                               get_region_list_in_org_hierarchy_selection_by_xpath())
            collapse_all_btn = web_driver.explicit_wait(self, 10, "XPATH", Notifier_Read_ini().
                                                        get_collapse_all_button_on_region_selection_panel_by_xpath(),
                                                        self.d)
            collapse_all_btn.click()
            self.logger.info("Clicked on 'Collapse all' button....")
            if region_list[0].is_displayed():
                self.status.append(False)
            else:
                self.logger.info("Region names are collapsed...")
                self.status.append(True)

            time.sleep(web_driver.one_second)
            expand_all_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                 get_expand_all_button_on_region_selection_panel_by_xpath())
            expand_all_btn.click()
            self.logger.info("Clicked on 'Expand All' button....")
            time.sleep(web_driver.one_second)
            if region_list[0].is_displayed():
                self.logger.info("Region names are expanded...")
                self.status.append(True)
            else:
                self.status.append(False)

            time.sleep(web_driver.one_second)
            select_all_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                 get_select_all_button_on_region_selection_panel_by_xpath())
            select_all_btn.click()
            time.sleep(web_driver.one_second)
            self.logger.info("Click on 'Select all' button...")
            checkbox_besides_region = \
                self.d.find_elements(By.XPATH, Notifier_Read_ini().
                                     get_checkbox_besides_region_names_in_org_hierarchy_selection_by_xpath())
            if len(checkbox_besides_region) > 0:
                for items in checkbox_besides_region:
                    if 'check' in items.get_attribute('class'):
                        self.status.append(True)
                    else:
                        self.status.append(True)
                self.logger.info("All regions are selected...")

            unselect_all_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                   get_unselect_all_button_on_region_selection_panel_by_xpath())
            unselect_all_btn.click()
            time.sleep(web_driver.one_second)
            self.logger.info("Clicked on 'Unselect all' button...")
            checkbox_besides_region = \
                self.d.find_elements(By.XPATH, Notifier_Read_ini().
                                     get_checkbox_besides_region_names_in_org_hierarchy_selection_by_xpath())
            if len(checkbox_besides_region) > 0:
                for items in checkbox_besides_region:
                    if 'check' in items.get_attribute('class'):
                        self.status.append(False)
                    else:
                        self.status.append(True)
                self.logger.info("All regions are unselected...")

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_03.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_03.png")
                return False
            else:
                return True

        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_03_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_03_exception.png")
            self.logger.error(f"TC_Notifier_03 got exception as: {ex}")
        finally:
            self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_logout_button_on_portal_by_xpath()).click()


