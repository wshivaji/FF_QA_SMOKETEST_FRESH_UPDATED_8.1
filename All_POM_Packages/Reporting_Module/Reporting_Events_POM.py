import configparser
import os
from pathlib import Path
import time
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from All_Config_Packages._7_Visitor_Search_Module_Config_Files.Visitor_Search_Read_INI import \
    Read_Visitor_Search_Components
from Base_Package.Web_Driver import web_driver
from Base_Package.Web_Logger import web_logger
from Base_Package.Login_Logout_Ops import login
from All_Config_Packages._6_Notification_Groups_Module_Config_Files.Notification_Groups_Read_INI import Read_Notification_Groups_Components
from All_Config_Packages._18_Reporting_Module_Config_Files.Reporting_Read_INI import Reporting_read_ini
from All_Config_Packages._2_Portal_Menu_Module_Config_Files.Portal_Menu_Module_Read_INI import Portal_Menu_Module_read_ini


class Reporting_Events_pom(web_driver, web_logger):
    d = web_driver.d()
    logger = web_logger.logger_obj()
    status = []
    current_file_path = os.path.abspath(__file__)

    def __init__(self):
        self.end_datetime = self.end_time = self.end_date = self.end_date_and_time = self.start_datetime = \
            self.start_age = self.age_bucket = None
        self.start_time = self.start_date = self.start_date_and_time = self.groups = self.zones = self.end_age = None
        self.age_range_zones_groups_xlsx = \
            f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\18_Reporting_Module\\Data_From_Excel\\age_range_zones_groups_xlsx.xlsx"
        self.custom_dates_json = \
            f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\18_Reporting_Module\\Data_From_JSON\\custom_dates_json.json"

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

    def load_reporting_module(self):
        try:
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            reporting_module = self.d.find_element(By.XPATH, Reporting_read_ini().get_reporting_module_by_xpath())
            if reporting_module.is_displayed():
                reporting_module.click()
                time.sleep(web_driver.one_second)
                panel_heading = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                    get_reporting_panel_heading_by_xpath())
            else:
                pass
            time.sleep(web_driver.one_second)
        except Exception as ex:
            self.logger.error(ex)
    
    def load_reporting_module_for_admin(self):
        try:
            x = Read_Notification_Groups_Components().get_user_name_input_data()
            username = x.split(',')
            login().login_with_persona_user(self.d, username[3])
            time.sleep(web_driver.one_second)
            reporting_module = self.explicit_wait(10, "XPATH", Reporting_read_ini().get_reporting_module_by_xpath(), self.d)
            if reporting_module.is_displayed():
                reporting_module.click()
                time.sleep(web_driver.one_second)
                panel_heading = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                    get_reporting_panel_heading_by_xpath())
            else:
                pass
            time.sleep(web_driver.one_second)
        except Exception as ex:
            self.logger.error(ex)

    def logout_from_portal(self):
        try:
            logout = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_logout_button_on_portal_by_xpath())
            logout.click()
            time.sleep(web_driver.one_second)

        except Exception as ex:
            print(ex)

    def get_age_range(self):
        try:
            df_age_range = pd.read_excel(self.age_range_zones_groups_xlsx, sheet_name='age_range',
                                         names=['Start Age', 'End Age', 'Age Bucket'])
            df_zones = pd.read_excel(self.age_range_zones_groups_xlsx, sheet_name='zones', names=['Zones'])
            df_groups = pd.read_excel(self.age_range_zones_groups_xlsx, sheet_name='groups', names=['Groups'])
            self.start_age = [x for x in df_age_range['Start Age']]
            self.end_age = [y for y in df_age_range['End Age']]
            self.age_bucket = [z for z in df_age_range['Age Bucket']]
            self.zones = [x for x in df_zones['Zones']]
            self.groups = [x for x in df_groups['Groups']]
            # print(f"start age: {self.start_age}" f"length: {len(self.start_age)}")
            # print(f"df age range: {df_age_range}")
            # print(f"df zones: {df_zones}")
            # print(f"df groups: {df_groups}")
        except Exception as ex:
            self.logger.error(ex)

    def select_number_of_events_by_enrollment(self):
        try:
            time.sleep(web_driver.three_second)
            field1 = self.explicit_wait(10, "XPATH", Reporting_read_ini().get_report_field1_dropdown_by_xpath(), self.d)
            field2 = self.d.find_element(By.XPATH, Reporting_read_ini().get_report_field2_dropdown_for_events_by_xpath())
            if field2.is_displayed():
                pass
            else:
                print("enter else >>>>>>>>.")
                field1_dropdown = Select(field1)
                time.sleep(web_driver.one_second)
                field1_dropdown.select_by_visible_text('number of probable match events')
                field2_dropdown = Select(field2)
                time.sleep(web_driver.one_second)
                field2_dropdown.select_by_visible_text('enrollment')
                time.sleep(web_driver.one_second)
        except Exception as ex:
            self.logger.error(ex)

    def select_number_of_events_by_zone(self):
        try:
            time.sleep(web_driver.three_second)
            field1 = self.explicit_wait(10, "XPATH", Reporting_read_ini().get_report_field1_dropdown_by_xpath(), self.d)
            field2 = self.d.find_element(By.XPATH, Reporting_read_ini().get_report_field2_dropdown_for_events_by_xpath())
            if field2.is_displayed():
                pass
            else:
                print("enter else >>>>>>>>.")
                field1_dropdown = Select(field1)
                time.sleep(web_driver.one_second)
                field1_dropdown.select_by_visible_text('number of probable match events')
                field2_dropdown = Select(field2)
                time.sleep(web_driver.one_second)
                field2_dropdown.select_by_visible_text('zone')
                time.sleep(web_driver.one_second)
        except Exception as ex:
            self.logger.error(ex)

    def get_events_by_zone_data(self):
        try:
            common_test_data_ini_file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_Data\\common_test_data.ini"
            file = Path(common_test_data_ini_file_path)
            config = configparser.ConfigParser()
            config.read(file)
            events_by_zone_counts = self.d.find_element(By.XPATH, "//*[local-name()='svg']")
            # all_devices = all_devices.text.replace(" ", ",")
            cleaned_string = events_by_zone_counts.text.replace('\n', ',').replace('\t', '')
            print(cleaned_string)
            config.set("Reporting_Data", "events_by_zone_counts", cleaned_string)
            config.write(file.open('w'))

        except Exception as ex:
            self.logger.info(f"get_events_by_zone_counts_data ex: {ex.args}")

    def get_events_count_by_edge(self, edge):
        try:
            region_name = edge
            search_dropdown = self.explicit_wait(10, "XPATH", Reporting_read_ini().
                                                 get_search_dropdown_on_events_panel_by_xpath(), self.d)
            search_dropdown.click()
            self.logger.info(f"clicked on search dropdown")
            time.sleep(web_driver.one_second)
            org_hierarchy_btn = self.explicit_wait(10, "XPATH", Reporting_read_ini().
                                                   get_org_hierarchy_selection_btn_on_event_search_by_xpath(), self.d)
            org_hierarchy_btn.click()
            self.logger.info(f"clicked on org hierarchy btn")
            time.sleep(web_driver.one_second)
            region_text_list = self.d.find_elements(By.XPATH, Reporting_read_ini().get_regions_text_list_by_xpath())
            self.logger.info(f"length of regions: {len(region_text_list)}")
            expected_region_text = region_name
            self.logger.info(f"expected_region: {expected_region_text}")
            region_checkboxes = self.d.find_elements(By.XPATH, Reporting_read_ini().get_region_checkboxes_by_xpath())
            try:
                time.sleep(web_driver.one_second)
                for i in range(len(region_text_list) + 1):
                    # self.logger.info(f"for loop: {i}")
                    actual_zone_text = region_text_list.__getitem__(i).text
                    if expected_region_text.upper() == actual_zone_text.upper():
                        self.logger.info(actual_zone_text)
                        self.logger.info(expected_region_text)
                        region_checkboxes.__getitem__(i).click()
                        # self.d.execute_script("arguments[0].click();", region_text_list.__getitem__(i))
                        break
                save = self.d.find_element(By.XPATH, Reporting_read_ini().get_save_button_on_org_hierarchy_by_xpath())
                save.click()
                self.logger.info("clicked on save button..")
                search_btn = self.explicit_wait(10, "XPATH", Reporting_read_ini().
                                                get_search_btn_on_search_dropdown_on_events_panel_by_xpath(), self.d)
                search_btn.click()
            except Exception as ex:
                str(ex)
            time.sleep(web_driver.one_second)
            expected_edge_events_count = self.explicit_wait(10, "XPATH", Reporting_read_ini().
                                                           get_total_events_count_on_events_panel_by_xpath(), self.d)
            expected_edge_events_count = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                            get_total_events_count_on_events_panel_by_xpath()).text
            self.logger.info(f"expected_edge_events_count: {expected_edge_events_count}")
            return expected_edge_events_count
        except Exception as ex:
            self.logger.info(f"events count by edge got an exception as: {ex}")

    def get_events_by_enrollment_count(self):
        try:
            common_test_data_ini_file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_Data\\common_test_data.ini"
            file = Path(common_test_data_ini_file_path)
            config = configparser.ConfigParser()
            config.read(file)
            events_by_enrollment_count = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                   get_events_by_enrollments_count_on_reporting_by_xpath())
            # all_devices = all_devices.text.replace(" ", ",")
            config.set("Reporting_Data", "events_by_enrollment_count", events_by_enrollment_count.text)
            config.write(file.open('w'))
            self.logger.info(f"enrollments_count: {events_by_enrollment_count.text}")

        except Exception as ex:
            self.logger.info(f"verify events by enrollments count got an exception as: {ex}")

    def select_number_of_enrollments_by_zone(self):
        try:
            time.sleep(web_driver.one_second)
            field1 = self.d.find_element(By.XPATH, Reporting_read_ini().get_report_field1_dropdown_by_xpath())
            field2 = self.d.find_element(By.XPATH, Reporting_read_ini().get_field2_dropdown_for_enrollments_by_xpath())
            if field2.is_displayed():
                pass
            else:
                field1_dropdown = Select(field1)
                field1_dropdown.select_by_visible_text('number of enrollments')
                time.sleep(web_driver.one_second)
                field2_dropdown = Select(field2)
                field2_dropdown.select_by_visible_text('zone')
                time.sleep(web_driver.one_second)
        except Exception as ex:
            self.logger.error(ex)

    def get_enrollment_by_zone_count(self):
        try:
            common_test_data_ini_file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_Data\\common_test_data.ini"
            file = Path(common_test_data_ini_file_path)
            config = configparser.ConfigParser()
            config.read(file)
            enrollments_by_zone_count = self.d.find_element(By.XPATH, "//*[local-name()='svg']")
            cleaned_string = enrollments_by_zone_count.text.replace('\n', ',').replace('\t', '')
            print(cleaned_string)
            config.set("Reporting_Data", "enrollments_by_zone_count", cleaned_string)
            config.write(file.open('w'))
            self.logger.info(f"enrollments_by_zone_count: {cleaned_string}")

        except Exception as ex:
            self.logger.info(f"verify enrollments by zone count got an exception as: {ex}")

    def get_enrollments_count_by_edge(self, edge):
        try:
            region_name = edge
            search_dropdown = self.explicit_wait(10, "XPATH", Reporting_read_ini().
                                                 get_search_dropdown_on_enrollments_panel_by_xpath(), self.d)
            search_dropdown.click()
            self.logger.info(f"clicked on search dropdown")
            time.sleep(web_driver.one_second)
            org_hierarchy_btn = self.explicit_wait(10, "XPATH", Reporting_read_ini().
                                                   get_org_hierarchy_selection_btn_on_event_search_by_xpath(), self.d)
            org_hierarchy_btn.click()
            self.logger.info(f"clicked on org hierarchy btn")
            time.sleep(web_driver.one_second)
            region_text_list = self.d.find_elements(By.XPATH, Read_Visitor_Search_Components().zone_text_list_xpath())
            self.logger.info(f"length of regions: {len(region_text_list)}")
            expected_region_text = region_name
            self.logger.info(f"expected_region: {expected_region_text}")
            # region_checkboxes = self.d.find_elements(By.XPATH, Reporting_read_ini().get_region_checkboxes_by_xpath())

            time.sleep(web_driver.one_second)
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
            self.logger.info("clicked on save button..")
            search_btn = self.explicit_wait(10, "XPATH", Reporting_read_ini().
                                            get_search_btn_on_search_dropdown_on_enrollments_panel_by_xpath(), self.d)
            search_btn.click()

            time.sleep(web_driver.one_second)
            expected_edge_enrollments_count = (
                self.explicit_wait(10, "XPATH", Reporting_read_ini().
                                   get_total_enrollments_count_on_enrollments_panel_by_xpath(), self.d))
            expected_edge_enrollments_count = (
                self.d.find_element(By.XPATH, Reporting_read_ini().
                                    get_total_enrollments_count_on_enrollments_panel_by_xpath()).text)
            self.logger.info(f"expected_edge_enrollments_count: {expected_edge_enrollments_count}")
            return expected_edge_enrollments_count
        except Exception as ex:
            self.logger.info(f"enrollments count by edge got an exception as: {ex}")

    def select_number_of_zones_by_enrollment(self):
        try:
            time.sleep(web_driver.one_second)
            field1 = self.d.find_element(By.XPATH, Reporting_read_ini().get_report_field1_dropdown_by_xpath())
            field2 = self.d.find_element(By.XPATH, Reporting_read_ini().get_field2_dropdown_for_zones_by_xpath())
            if field2.is_displayed():
                pass
            else:
                field1_dropdown = Select(field1)
                field1_dropdown.select_by_visible_text('number of zones')
                time.sleep(web_driver.one_second)
                field2_dropdown = Select(field2)
                field2_dropdown.select_by_visible_text('enrollment')
                time.sleep(web_driver.one_second)
        except Exception as ex:
            self.logger.error(ex)

    def get_zones_by_enrollment_count(self):
        try:
            common_test_data_ini_file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_Data\\common_test_data.ini"
            file = Path(common_test_data_ini_file_path)
            config = configparser.ConfigParser()
            config.read(file)
            zones_by_enrollment_count = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                   get_events_by_enrollments_count_on_reporting_by_xpath())
            # all_devices = all_devices.text.replace(" ", ",")
            config.set("Reporting_Data", "zones_by_enrollment_count", zones_by_enrollment_count.text)
            config.write(file.open('w'))
            self.logger.info(f"enrollments_count: {zones_by_enrollment_count.text}")

        except Exception as ex:
            self.logger.info(f"verify zones by enrollments count got an exception as: {ex}")

    def Verify_report_for_number_of_probable_match_events_by_zone_with_default_dates_and_optional_filters(self):
        try:
            self.logger.info("********* TC_Reporting_01 started ************")
            self.status.clear()
            self.load_reporting_module_for_admin()
            self.select_number_of_events_by_zone()
            time.sleep(web_driver.one_second)
            generate_report = self.explicit_wait(10, "XPATH",
                                                Reporting_read_ini().get_generate_report_button_by_xpath(), self.d)
            generate_report.click()
            time.sleep(web_driver.two_second)
            self.logger.info("Clicked on generate report button...")
            new_reporting_panel = self.explicit_wait(10, "XPATH",
                                                     Reporting_read_ini().get_new_reporting_panel_heading(), self.d)
            if new_reporting_panel.is_displayed():
                self.logger.info(f"Reporting panel heading: {new_reporting_panel.text}")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)

            self.get_events_by_zone_data()
            region_names_and_events_count = Reporting_read_ini().get_events_by_zone_counts()
            region_names_and_events_count = region_names_and_events_count.split(',')
            all_devices_events_count = region_names_and_events_count[1]
            self.logger.info(f"expected_all_events_count: {all_devices_events_count}")

            cloud_menu_button = self.explicit_wait(10, "XPATH", Portal_Menu_Module_read_ini().
                                                  get_CLOUD_MENU_button_by_xpath(), self.d)
            cloud_menu_button.click()
            time.sleep(web_driver.one_second)

            events_panel = self.explicit_wait(10, "XPATH",
                                              Portal_Menu_Module_read_ini().get_events_menu_by_xpath(), self.d)
            events_panel.click()
            time.sleep(web_driver.one_second)
            actual_all_events_count = self.explicit_wait(10, "XPATH", Reporting_read_ini().
                                              get_total_events_count_on_events_panel_by_xpath(), self.d)
            self.logger.info(f"actual_all_devices_events_count: {actual_all_events_count.text}")

            if all_devices_events_count == actual_all_events_count.text:
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.logger.info(f"expected edge event count: {region_names_and_events_count[3]}")
            get_edge_event_count = self.get_events_count_by_edge(region_names_and_events_count[2])
            self.logger.info(f"actual edge event count: {get_edge_event_count}")
            time.sleep(web_driver.one_second)
            if get_edge_event_count == region_names_and_events_count[3]:
                self.status.append(True)
            else:
                self.status.append(False)

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_01.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_01.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_01_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_01_exception.png")
            self.logger.error(f"TC_Reporting_01 got exception as: {ex}")
        finally:
            self.logout_from_portal()

    def Verify_report_for_number_of_probable_match_events_by_enrollment_with_default_dates_and_optional_filters(self):
        try:
            self.logger.info("********* TC_Reporting_02 started ************")
            self.status.clear()
            self.load_reporting_module_for_admin()
            self.select_number_of_events_by_enrollment()
            time.sleep(web_driver.one_second)

            generate_report = self.explicit_wait(10, "XPATH",
                                                 Reporting_read_ini().get_generate_report_button_by_xpath(), self.d)
            generate_report.click()
            time.sleep(web_driver.two_second)
            self.logger.info("Clicked on generate report button...")

            new_reporting_panel = self.explicit_wait(10, "XPATH", Reporting_read_ini().
                                                      get_new_reporting_panel_heading(), self.d)
            if new_reporting_panel.is_displayed():
                self.logger.info(f"title on the report panel:- {new_reporting_panel.text}")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.get_events_by_enrollment_count()
            time.sleep(web_driver.one_second)
            x = Reporting_read_ini().events_by_enrollment_count()
            x = x.strip("viewing 1 thru ")
            x = x.split(' ')
            events_by_enrollment_count = x[2]
            self.logger.info(f"actual events_by_enrollment_count: {events_by_enrollment_count}")
            cloud_menu_button = self.explicit_wait(10, "XPATH", Portal_Menu_Module_read_ini().
                                                   get_CLOUD_MENU_button_by_xpath(), self.d)
            cloud_menu_button.click()
            time.sleep(web_driver.one_second)

            enrollment_panel = self.explicit_wait(10, "XPATH",
                                              Portal_Menu_Module_read_ini().get_Enrollments_menu_by_xpath(), self.d)
            enrollment_panel.click()
            time.sleep(web_driver.one_second)
            total_enrollments_count = self.explicit_wait(10, "XPATH", Reporting_read_ini().
                                                          get_total_enrollments_count_on_enrollments_panel_by_xpath(),
                                                          self.d)
            self.logger.info(f"expected events_by_enrollment_count: {total_enrollments_count.text}")
            time.sleep(web_driver.one_second)
            if events_by_enrollment_count <= total_enrollments_count.text:
                self.status.append(True)
            else:
                self.status.append(False)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_02.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_02.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_02_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_02_exception.png")
            self.logger.error(f"TC_Reporting_02 got exception as: {ex}")
        finally:
            self.logout_from_portal()

    def Verify_report_for_number_of_enrollment_by_zones_with_default_dates_and_optional_filters(self):
        try:
            self.logger.info("*********** TC_Reporting_03 started **********")
            self.status.clear()
            self.load_reporting_module_for_admin()
            self.select_number_of_enrollments_by_zone()
            time.sleep(web_driver.one_second)
            generate_report = self.explicit_wait(10, "XPATH", Reporting_read_ini().
                                                 get_generate_report_button_by_xpath(), self.d)
            generate_report.click()
            self.logger.info("Clicked on Generate report button")
            time.sleep(web_driver.two_second)
            new_reporting_panel = self.explicit_wait(10, "XPATH", Reporting_read_ini().
                                                      get_new_reporting_panel_heading(), self.d)
            time.sleep(web_driver.one_second)
            if new_reporting_panel.is_displayed():
                self.logger.info(f"title on the report panel:- {new_reporting_panel.text}")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.get_enrollment_by_zone_count()
            y = Reporting_read_ini().get_enrollments_by_zone_count()
            enrollments_by_zone_on_reporting = y.split(',')
            expected_all_devices_enrollments_count = enrollments_by_zone_on_reporting[-1]
            self.logger.info(f"zone name: {enrollments_by_zone_on_reporting[-2]}")
            self.logger.info(f"expected All Devices enrollments count: {expected_all_devices_enrollments_count}")
            cloud_menu_button = self.explicit_wait(10, "XPATH", Portal_Menu_Module_read_ini().
                                                   get_CLOUD_MENU_button_by_xpath(), self.d)
            cloud_menu_button.click()
            time.sleep(web_driver.one_second)

            enrollment_panel = self.explicit_wait(10, "XPATH",
                                                  Portal_Menu_Module_read_ini().get_Enrollments_menu_by_xpath(), self.d)
            enrollment_panel.click()
            time.sleep(web_driver.one_second)
            actual_all_devices_enrollments_count = self.explicit_wait(10, "XPATH", Reporting_read_ini().
                                                         get_total_enrollments_count_on_enrollments_panel_by_xpath(),
                                                         self.d)
            self.logger.info(f"actual all devices enrollments count: {actual_all_devices_enrollments_count.text}")
            if actual_all_devices_enrollments_count.text >= expected_all_devices_enrollments_count:
                self.status.append(True)
            else:
                self.status.append(False)

            time.sleep(web_driver.one_second)
            edge_name = enrollments_by_zone_on_reporting[0]
            expected_enrollments_by_edge = self.get_enrollments_count_by_edge(edge_name)
            self.logger.info(f"actual enrollments by edge count for: {edge_name} is {enrollments_by_zone_on_reporting[1]}")
            if expected_enrollments_by_edge >= enrollments_by_zone_on_reporting[1]:
                self.status.append(True)
            else:
                self.status.append(False)

            self.logger.info(f"expected_enrollments_by_edge: {expected_enrollments_by_edge}")
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_03.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_03.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_03_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_03_exception.png")
            self.logger.error(f"TC_Reporting_03 got exception as: {ex}")
        finally:
            self.logout_from_portal()

    def Verify_report_for_number_of_zones_by_enrollment_with_default_dates_and_optional_filters(self):
        try:
            self.logger.info("*********** TC_Reporting_04 started **********")
            self.status.clear()
            self.load_reporting_module_for_admin()
            self.select_number_of_zones_by_enrollment()

            time.sleep(web_driver.one_second)

            generate_report = self.explicit_wait(10, "XPATH", Reporting_read_ini().
                                                 get_generate_report_button_by_xpath(), self.d)
            generate_report.click()
            self.logger.info("Clicked on Generate report button")
            time.sleep(web_driver.two_second)
            new_reporting_panel = self.explicit_wait(10, "XPATH",  Reporting_read_ini().
                                                      get_new_reporting_panel_heading(), self.d)
            if new_reporting_panel.is_displayed():
                self.logger.info(f"Reporting panel heading: {new_reporting_panel.text}")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.get_zones_by_enrollment_count()

            x = Reporting_read_ini().get_zones_by_enrollment_count()
            x = x.strip("viewing 1 thru 10 of")
            zones_by_enrollment_count = x
            self.logger.info(f"expected zones_by_enrollment_count: {zones_by_enrollment_count}")
            cloud_menu_button = self.explicit_wait(10, "XPATH", Portal_Menu_Module_read_ini().
                                                   get_CLOUD_MENU_button_by_xpath(), self.d)
            cloud_menu_button.click()
            time.sleep(web_driver.one_second)

            enrollment_panel = self.explicit_wait(10, "XPATH",
                                                  Portal_Menu_Module_read_ini().get_Enrollments_menu_by_xpath(), self.d)
            enrollment_panel.click()
            time.sleep(web_driver.one_second)
            total_enrollments_count = self.explicit_wait(10, "XPATH", Reporting_read_ini().
                                                         get_total_enrollments_count_on_enrollments_panel_by_xpath(),
                                                         self.d)
            self.logger.info(f"actual events_by_enrollment_count: {total_enrollments_count.text}")
            if zones_by_enrollment_count <= total_enrollments_count.text:
                self.status.append(True)
            else:
                self.status.append(False)

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_04.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_04.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_04_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_04_exception.png")
            self.logger.error(f"TC_Reporting_04 got exception as: {ex}")
        finally:
            self.logout_from_portal()

