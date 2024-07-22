import configparser
import time
from pathlib import Path

from selenium.webdriver.common.by import By

from All_Config_Packages._20_Insight_Dashboard_Config_File.Insight_Dashboard_Read_INI import insight_dashboard_read_ini
from Base_Package.Web_Driver import web_driver
from Base_Package.Web_Logger import web_logger
from Base_Package.Login_Logout_Ops import login, logout
from All_Config_Packages._2_Portal_Menu_Module_Config_Files.Portal_Menu_Module_Read_INI import Portal_Menu_Module_read_ini
from All_Config_Packages._10_Account_config_Files.Accounts_Read_INI import account_Read_Ini


class account_pom(web_driver, web_logger):

    d = web_driver.d()
    logger = web_logger.logger_obj()
    status = []

    def click_on_logout(self):
        try:
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_logout_button_on_portal_by_xpath()).click()
        except Exception as ex:
            self.logger.info(f"click on logout got an exception as: {ex}")

    def validate_enrollments_count(self, strategy):
        try:
            time.sleep(web_driver.two_second)
            cloud_menu = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_CLOUD_MENU_button_by_xpath())
            cloud_menu.click()
            time.sleep(web_driver.one_second)
            enrollments_menu = web_driver.explicit_wait(self, 10, "XPATH",
                                                        Portal_Menu_Module_read_ini().get_Enrollments_menu_by_xpath(),
                                                        self.d)
            enrollments_menu.click()
            time.sleep(web_driver.two_second)

            enrollments_count_text = self.explicit_wait(5, "XPATH",
                                                        insight_dashboard_read_ini().total_enrollments_text_on_enrollments_panel_by_xpath(),
                                                        self.d)
            self.logger.info(f"text: {enrollments_count_text.text}")
            text_list = enrollments_count_text.text.split(" ")
            self.logger.info(text_list)
            if strategy == "before":
                e = account_Read_Ini().start_enrollments_count().split('/')
            else:
                e = account_Read_Ini().end_enrollments_count().split('/')
            actual_enrollments_count = e[0]
            self.logger.info(f"actual_enrollments_count: {actual_enrollments_count}")
            self.logger.info(f"expected_enrollments_count: {text_list[3]}")
            if int(text_list[3]) == int(actual_enrollments_count):
                return True
            else:
                return False

        except Exception as ex:
            self.logger.info(f"validate details before execution got an exception as: {ex}")

    def validate_users_count(self, strategy):
        try:
            time.sleep(web_driver.two_second)
            cloud_menu = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_CLOUD_MENU_button_by_xpath())
            cloud_menu.click()
            time.sleep(web_driver.one_second)
            users_menu = web_driver.explicit_wait(self, 10, "XPATH",
                                                        Portal_Menu_Module_read_ini().get_Users_menu_by_xpath(),
                                                        self.d)
            users_menu.click()
            time.sleep(web_driver.two_second)
            count_of_users = self.d.find_elements(By.XPATH,account_Read_Ini().count_of_users_by_xpath())
            if strategy == "before":
                users = len(count_of_users) + int(account_Read_Ini().user_accounts_number())
                self.logger.info(f"length of users: {users}")
                e = account_Read_Ini().start_users_count().split('/')
                actual_users_count = e[0]
                self.logger.info(f"actual_users_count: {actual_users_count}")
                if users >= int(actual_users_count):
                    return True
                else:
                    return False
            else:
                users = len(count_of_users) + int(account_Read_Ini().user_accounts_number())
                self.logger.info(f"length of users: {users}")
                e = account_Read_Ini().end_users_count().split('/')
                actual_users_count = e[0]
                self.logger.info(f"actual_users_count: {actual_users_count}")
                if users >= int(actual_users_count):
                    return True
                else:
                    return False
        except Exception as ex:
            self.logger.info(f"validate details before execution got an exception as: {ex}")

    def validate_enrollment_groups_count(self, strategy):
        try:
            time.sleep(web_driver.two_second)
            cloud_menu = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_CLOUD_MENU_button_by_xpath())
            cloud_menu.click()
            time.sleep(web_driver.one_second)
            eg_menu = web_driver.explicit_wait(self, 10, "XPATH",
                                                        Portal_Menu_Module_read_ini().get_Enrollment_Groups_menu_by_xpath(),
                                                        self.d)
            eg_menu.click()
            time.sleep(web_driver.two_second)
            count_of_egs = self.d.find_elements(By.XPATH, account_Read_Ini().count_of_enrollment_groups_by_xpath())
            self.logger.info(f"length of enrollment groups: {len(count_of_egs)}")
            if strategy == "before":
                e = account_Read_Ini().start_enrollment_groups_count().split('/')
            else:
                e = account_Read_Ini().end_enrollment_groups_count().split('/')
            actual_egs_count = e[0]
            self.logger.info(f"actual_egs_count: {actual_egs_count}")
            if len(count_of_egs) == int(actual_egs_count):
                return True
            else:
                return False
        except Exception as ex:
            self.logger.info(f"validate details before execution got an exception as: {ex}")

    def validate_notification_groups_count(self, strategy):
        try:
            time.sleep(web_driver.two_second)
            cloud_menu = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_CLOUD_MENU_button_by_xpath())
            cloud_menu.click()
            time.sleep(web_driver.one_second)
            ng_menu = web_driver.explicit_wait(self, 10, "XPATH",
                                                        Portal_Menu_Module_read_ini().get_Notification_Groups_menu_by_xpath(),
                                                        self.d)
            ng_menu.click()
            time.sleep(web_driver.two_second)
            count_of_ngs = self.d.find_elements(By.XPATH, account_Read_Ini().count_of_notification_groups_by_xpath())
            self.logger.info(f"length of notification groups: {len(count_of_ngs)}")

            if strategy == "before":
                e = account_Read_Ini().start_notification_groups_count().split('/')
            else:
                e = account_Read_Ini().end_notification_groups_count().split('/')
            actual_ngs_count = e[0]
            self.logger.info(f"actual_ngs_count: {actual_ngs_count}")
            if len(count_of_ngs) == int(actual_ngs_count):
                return True
            else:
                return False
        except Exception as ex:
            self.logger.info(f"validate details before execution got an exception as: {ex}")

    def validate_stations_count(self):
        try:
            time.sleep(web_driver.two_second)

            image_sources = web_driver.explicit_wait(self, 10, "XPATH", account_Read_Ini().view_Image_source_button(), self.d)
            image_sources.click()
            time.sleep(web_driver.two_second)
            count_of_stations = self.d.find_elements(By.XPATH, account_Read_Ini().count_of_stations_by_xpath())
            self.logger.info(f"length of stations: {len(count_of_stations)}")
            actual_stations_count = account_Read_Ini().end_stations_count()
            self.logger.info(f"actual_stations_count: {actual_stations_count}")
            if len(count_of_stations) == int(actual_stations_count):
                return True
            else:
                return False

        except Exception as ex:
            self.logger.info(f"validate details before execution got an exception as: {ex}")

    def validate_stations_count_before(self):
        try:
            time.sleep(web_driver.two_second)

            image_sources = web_driver.explicit_wait(self, 10, "XPATH", account_Read_Ini().view_Image_source_button(), self.d)
            image_sources.click()
            time.sleep(web_driver.two_second)
            count_of_stations = self.d.find_elements(By.XPATH, account_Read_Ini().count_of_stations_by_xpath())
            self.logger.info(f"length of stations: {len(count_of_stations)}")
            actual_stations_count = account_Read_Ini().start_stations_count()
            self.logger.info(f"actual_stations_count: {actual_stations_count}")
            if len(count_of_stations) == int(actual_stations_count):
                return True
            else:
                return False

        except Exception as ex:
            self.logger.info(f"validate details before execution got an exception as: {ex}")

    def Verify_account_panel_details_after_execution(self):
        try:
            self.logger.info("********TC_002******* started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.open_accounts_panel()

            time.sleep(web_driver.one_second)
            account_panel_heading = self.explicit_wait(5, "XPATH", account_Read_Ini().Account_panel_heading(), self.d)
            # account_panel_heading = self.d.find_element(By.XPATH, account_Read_Ini().Account_panel_heading())
            self.logger.info(f"account_panel_heading_displayed: {account_panel_heading.is_displayed()}")
            if account_panel_heading.is_displayed():
                self.logger.info("Account panel heading is displayed")
                self.status.append(True)
            else:
                self.logger.info("Account panel heading is not visible")
                self.status.append(False)

            self.verify_enabled_status_and_its_value_after_execution()
            self.status.append(self.validate_enrollments_count(strategy="after"))
            self.status.append(self.validate_users_count(strategy="after"))
            self.status.append(self.validate_enrollment_groups_count(strategy="after"))
            self.status.append(self.validate_notification_groups_count(strategy="after"))
            self.status.append(self.validate_stations_count())

            self.logger.info(f"status: {self.status}")
            time.sleep(web_driver.one_second)

            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_account_002_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_account_002_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.info(f"save_account_panel_details_after_execution ex: {ex.args}")
        finally:
            self.click_on_logout()

    def Verify_account_panel_details_before_execution(self):
        try:
            self.logger.info("********TC_001******* started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.open_accounts_panel()
            time.sleep(web_driver.one_second)
            account_panel_heading = self.explicit_wait(5, "XPATH", account_Read_Ini().Account_panel_heading(), self.d)
            self.logger.info(f"account_panel_heading_displayed: {account_panel_heading.is_displayed()}")
            if account_panel_heading.is_displayed():
                self.logger.info("Account panel heading is displayed")
                self.status.append(True)
            else:
                self.logger.info("Account panel heading is not visible")
                self.status.append(False)

            self.verify_enabled_status_and_its_value()
            self.status.append(self.validate_enrollments_count(strategy="before"))
            self.status.append(self.validate_users_count(strategy="before"))
            self.status.append(self.validate_enrollment_groups_count(strategy="before"))
            self.status.append(self.validate_notification_groups_count(strategy="before"))
            self.status.append(self.validate_stations_count_before())
            self.logger.info(f"status: {self.status}")
            time.sleep(web_driver.one_second)

            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_account_001_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_account_001_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.info(f"save_account_panel_details_before_execution ex: {ex.args}")
        finally:
            self.click_on_logout()

    def click_on_image_sources_and_check_theplanel_heading_of_Account_Image_sources_is_displayed(self):
        try:
            self.logger.info("**********TC_034******** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            account = self.d.find_element(By.XPATH, account_Read_Ini().account_in_dashboarditems())
            account.click()
            self.logger.info("click on account dashboard items")
            time.sleep(web_driver.two_second)
            image_source = self.d.find_element(By.XPATH, account_Read_Ini().view_Image_source_button())
            time.sleep(web_driver.two_second)
            image_source.click()
            self.logger.info("click on image_source")
            time.sleep(web_driver.two_second)
            image_source_panel_heading = self.d.find_element(By.XPATH, account_Read_Ini().account_image_sources_panel_heading())
            self.logger.info(f"image_source_panel_heading displayed: {image_source_panel_heading.is_displayed()}")
            if image_source_panel_heading.is_displayed():
                self.logger.info("image source panel heading is visible")
                self.status.append(True)
            else:
                self.logger.info("image source panel heading is not visible")
                self.status.append(False)
            self.logger.info(f"status :{self.status}")
            time.sleep(web_driver.one_second)
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_account_34_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_account_34_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_account_34_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_account_034_Exception.png")
            self.logger.error(f"TC_account_034 got exception as: {ex} ")

    def click_on_location_on_View_dropdown_map_is_visible(self):
        try:
            self.logger.info("*******TC_036****** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            account = self.d.find_element(By.XPATH, account_Read_Ini().account_in_dashboarditems())
            account.click()
            self.logger.info("click on account dashboard items")
            time.sleep(web_driver.two_second)
            image_source = self.d.find_element(By.XPATH, account_Read_Ini().view_Image_source_button())
            time.sleep(web_driver.two_second)
            image_source.click()
            self.logger.info("click on image_source")
            time.sleep(web_driver.two_second)
            view_dropdown = self.d.find_element(By.XPATH, account_Read_Ini().view_dropdown())
            view_dropdown.click()
            self.logger.info("click on view_dropdown")
            time.sleep(web_driver.two_second)
            location = self.d.find_element(By.XPATH, account_Read_Ini().location_in_viewdropdown())
            location.click()
            self.logger.info("click on location")
            time.sleep(web_driver.two_second)
            a = self.d.switch_to.alert
            a.accept()
            time.sleep(web_driver.one_second)
            checkbox = self.d.find_element(By.XPATH, account_Read_Ini().select_checkbox())
            checkbox.click()
            self.logger.info("click on checkbox")
            time.sleep(web_driver.one_second)
            view_dropdown = self.d.find_element(By.XPATH, account_Read_Ini().view_dropdown())
            view_dropdown.click()
            self.logger.info("click on view_dropdown")
            time.sleep(web_driver.two_second)
            location = self.d.find_element(By.XPATH, account_Read_Ini().location_in_viewdropdown())
            location.click()
            self.logger.info("click on location")
            time.sleep(web_driver.two_second)
            map_1 = self.d.find_element(By.XPATH, account_Read_Ini().get_map())
            if map_1.is_displayed():
                self.logger.info("map is display")
                self.status.append(True)
            else:
                self.logger.info("map is not visible")
                self.status.append(False)
            self.logger.info(f"status :{self.status}")
            time.sleep(web_driver.one_second)
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_account_36_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_account_36_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_account_36_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_account_036_exception.png")
            self.logger.error(f"TC_account_036 got exception as: {ex} ")

    def click_on_regions_button_verify_panel_heading(self):
        try:
            self.logger.info("******TC_038****** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            account = self.d.find_element(By.XPATH, account_Read_Ini().account_in_dashboarditems())
            account.click()
            self.logger.info("click on account dashboard items")
            time.sleep(web_driver.two_second)
            image_source = self.d.find_element(By.XPATH, account_Read_Ini().view_Image_source_button())
            time.sleep(web_driver.one_second)
            image_source.click()
            self.logger.info("click on image_source")
            time.sleep(web_driver.three_second)
            regions = self.d.find_element(By.XPATH, account_Read_Ini().regions_button())
            regions.click()
            self.logger.info("click on regions")
            time.sleep(web_driver.two_second)
            zones_panel_heading = self.d.find_element(By.XPATH, account_Read_Ini().zones_panel_heading())
            if zones_panel_heading.is_displayed():
                self.logger.info("zones panel heading is visible")
                self.status.append(True)
            else:
                self.logger.info("zones panel heading is not visible")
                self.status.append(False)
            self.logger.info(f"status :{self.status}")
            time.sleep(web_driver.one_second)
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_account_38_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_account_38_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_account_38_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_account_038_exception.png")
            self.logger.error(f"TC_account_038 got exception as: {ex} ")

    def verify_details_button_is_visible(self):
        try:
            self.logger.info("********TC_039******* started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            account = self.d.find_element(By.XPATH, account_Read_Ini().account_in_dashboarditems())
            account.click()
            self.logger.info("click on account dashboard items")
            time.sleep(web_driver.two_second)
            image_source = self.d.find_element(By.XPATH, account_Read_Ini().view_Image_source_button())
            time.sleep(web_driver.two_second)
            image_source.click()
            self.logger.info("click on image_source")
            time.sleep(web_driver.two_second)
            details_button = self.d.find_element(By.XPATH, account_Read_Ini().details_button())
            if details_button.is_displayed():
                self.logger.info("details button is visible")
                self.status.append(True)
            else:
                self.logger.info("details button is not visible")
                self.status.append(False)
            self.logger.info(f"status :{self.status}")
            time.sleep(web_driver.one_second)
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_account_39_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_account_39_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_account_39_Exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_account_039_Exception.png")
            self.logger.error(f"TC_account_039 got exception as: {ex} ")

    def click_on_detailsbutton_verify_imagesource_panel_heading_is_visible(self):
        try:
            self.logger.info("*******TC_040******* started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            account = self.d.find_element(By.XPATH, account_Read_Ini().account_in_dashboarditems())
            account.click()
            self.logger.info("click on account dashboard items")
            time.sleep(web_driver.two_second)
            image_source = self.d.find_element(By.XPATH, account_Read_Ini().view_Image_source_button())
            time.sleep(web_driver.two_second)
            image_source.click()
            self.logger.info("click on image_source")
            time.sleep(web_driver.two_second)
            details_button = self.d.find_element(By.XPATH, account_Read_Ini().details_button())
            details_button.click()
            self.logger.info("click on details_button")
            time.sleep(web_driver.two_second)
            image_source_panel_heading = self.d.find_element(By.XPATH, account_Read_Ini().image_source_panel_heading())
            if image_source_panel_heading.is_displayed():
                self.logger.info("image source panel heading is visible")
                self.status.append(True)
            else:
                self.logger.info("image source panel heading is not visible")
                self.status.append(False)
            self.logger.info(f"status :{self.status}")
            time.sleep(web_driver.one_second)
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_account_40_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_account_40_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_account_40_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_account_040_exception.png")
            self.logger.error(f"TC_account_040 got exception as: {ex} ")

    def click_on_viewlocation_button_on_imagesource_verify_location(self):
        try:
            self.logger.info("********TC_042****** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            account = self.d.find_element(By.XPATH, account_Read_Ini().account_in_dashboarditems())
            account.click()
            self.logger.info("click on account dashboard items")
            time.sleep(web_driver.two_second)
            image_source = self.d.find_element(By.XPATH, account_Read_Ini().view_Image_source_button())
            time.sleep(web_driver.two_second)
            image_source.click()
            self.logger.info("click on image_source")
            time.sleep(web_driver.two_second)
            details_button = self.d.find_element(By.XPATH, account_Read_Ini().details_button())
            details_button.click()
            self.logger.info("click on details_button")
            time.sleep(web_driver.two_second)
            view_location = self.d.find_element(By.XPATH, account_Read_Ini().view_location_button())
            view_location.click()
            self.logger.info("click on view_location")
            time.sleep(web_driver.two_second)
            events_location = self.d.find_element(By.XPATH, account_Read_Ini().events_location_panel_heading())
            facefirst_logo = self.d.find_element(By.XPATH, account_Read_Ini().get_facefirst_logo_in_map())
            if events_location.is_displayed():
                self.logger.info("events location panel heading is visible")
                self.status.append(True)
            else:
                self.logger.info("events location panel heading is not visible")
                self.status.append(False)
            if facefirst_logo.is_displayed():
                self.logger.info("facefirst logo is visible")
                self.status.append(True)
            else:
                self.logger.info("facefirst logo is not visible")
                self.status.append(False)
            self.logger.info(f"status :{self.status}")
            time.sleep(web_driver.one_second)
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_account_42_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_account_42-failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_account_42_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_account_042_exception.png")
            self.logger.error(f"TC_account_042 got exception as: {ex} ")

    # ************************************* User Methods ********************************************

    def open_accounts_panel(self):
        try:
            self.explicit_wait(5, "XPATH", account_Read_Ini().account_in_dashboarditems(), self.d)
            account = self.d.find_element(By.XPATH, account_Read_Ini().account_in_dashboarditems())
            self.logger.info(f"account menu item visible: {account.is_displayed()}")
            account.click()
            self.logger.info("click on account dashboard items")
        except Exception as ex:
            self.logger.info(f"open_accounts_panel ex: {ex.args}")

    def verify_enabled_status_and_its_value(self):
        try:
            self.explicit_wait(5, "XPATH", account_Read_Ini().account_details_table_data_list_by_xpath(), self.d)
            account = self.d.find_elements(By.XPATH, account_Read_Ini().account_details_table_data_list_by_xpath())
            self.logger.info(f"account length: {len(account)}")
            i = 0
            for x in range(len(account)-1):
                self.logger.info(f"{account[x].text}")
                if i < (len(account)-1):
                    self.store_data_to_common_ini_file(account[x].text, account[x+1].text)
                    self.status.append(True)
                else:
                    self.status.append(False)

        except Exception as ex:
            self.logger.info(f"verify_enabled_status_and_its_value ex: {ex.args}")

    def store_data_to_common_ini_file(self, x, y):
        try:
            common_test_data_ini_file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_Data\\common_test_data.ini"
            file = Path(common_test_data_ini_file_path)
            config = configparser.ConfigParser()
            config.read(file)

            if x == account_Read_Ini().enabled_status_text():
                config.set("Account_Module_Data", "start_enabled_status", y)
                config.write(file.open('w'))
            elif x == account_Read_Ini().enrollments_text():
                config.set("Account_Module_Data", "start_enrollments_count", y)
                config.write(file.open('w'))
            elif x == account_Read_Ini().users_text():
                config.set("Account_Module_Data", "start_users_count", y)
                config.write(file.open('w'))
            elif x == account_Read_Ini().max_investigation_length_text():
                config.set("Account_Module_Data", "start_max_investigation_length_count", y)
                config.write(file.open('w'))
            elif x == account_Read_Ini().enrollment_groups_text():
                config.set("Account_Module_Data", "start_enrollment_groups_count", y)
                config.write(file.open('w'))
            elif x == account_Read_Ini().notification_groups_text():
                config.set("Account_Module_Data", "start_notification_groups_count", y)
                config.write(file.open('w'))
            elif x == account_Read_Ini().stations_text():
                config.set("Account_Module_Data", "start_stations_count", y)
                config.write(file.open('w'))
            elif x == account_Read_Ini().first_name_text():
                config.set("Account_Module_Data", "start_first_name", y)
                config.write(file.open('w'))
            elif x == account_Read_Ini().middle_name_text():
                config.set("Account_Module_Data", "start_middle_name", y)
                config.write(file.open('w'))
            elif x == account_Read_Ini().last_name_text():
                config.set("Account_Module_Data", "start_last_name", y)
                config.write(file.open('w'))
            elif x == account_Read_Ini().company_text():
                config.set("Account_Module_Data", "start_company", y)
                config.write(file.open('w'))
            elif x == account_Read_Ini().department_text():
                config.set("Account_Module_Data", "start_department", y)
                config.write(file.open('w'))
            elif x == account_Read_Ini().title_text():
                config.set("Account_Module_Data", "start_title", y)
                config.write(file.open('w'))
            elif x == account_Read_Ini().email_text():
                config.set("Account_Module_Data", "start_email", y)
                config.write(file.open('w'))
            elif x == account_Read_Ini().home_phone_text():
                config.set("Account_Module_Data", "start_home_phone", y)
                config.write(file.open('w'))
            elif x == account_Read_Ini().work_phone_text():
                config.set("Account_Module_Data", "start_work_phone", y)
                config.write(file.open('w'))
            elif x == account_Read_Ini().fax_number_text():
                config.set("Account_Module_Data", "start_fax_number", y)
                config.write(file.open('w'))
            elif x == account_Read_Ini().address_text():
                config.set("Account_Module_Data", "start_address", y)
                config.write(file.open('w'))
            elif x == account_Read_Ini().address_2_text():
                config.set("Account_Module_Data", "start_address_2", y)
                config.write(file.open('w'))
            elif x == account_Read_Ini().city_text():
                config.set("Account_Module_Data", "start_city", y)
                config.write(file.open('w'))
            elif x == account_Read_Ini().state_text():
                config.set("Account_Module_Data", "start_state", y)
                config.write(file.open('w'))
            elif x == account_Read_Ini().zip_code_text():
                config.set("Account_Module_Data", "start_zip_code", y)
                config.write(file.open('w'))
            elif x == account_Read_Ini().timezone_text():
                config.set("Account_Module_Data", "start_timezone", y)
                config.write(file.open('w'))
            elif x == account_Read_Ini().case_TTL_text():
                config.set("Account_Module_Data", "start_case_TTL", y)
                config.write(file.open('w'))
            else:
                self.logger.info(f"some error appeared while storing to ini")
        except Exception as ex:
            self.logger.info(f"store_data_to_common_ini_file ex: {ex.args}")

    def verify_enabled_status_and_its_value_after_execution(self):
        try:
            self.explicit_wait(5, "XPATH", account_Read_Ini().account_details_table_data_list_by_xpath(), self.d)
            account = self.d.find_elements(By.XPATH, account_Read_Ini().account_details_table_data_list_by_xpath())
            self.logger.info(f"account length: {len(account)}")
            i = 0
            for x in range(len(account) - 1):
                self.logger.info(f"{account[x].text}, {account[x + 1].text}")
                if i < (len(account) - 1):
                    self.store_data_to_common_ini_file_after_execution(account[x].text, account[x + 1].text)
                    self.status.append(True)
                else:
                    self.status.append(False)
        except Exception as ex:
            self.logger.info(f"verify_enabled_status_and_its_value_after_execution ex: {ex.args}")

    def store_data_to_common_ini_file_after_execution(self, x, y):
        try:
            common_test_data_ini_file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_Data\\common_test_data.ini"
            file = Path(common_test_data_ini_file_path)
            config = configparser.ConfigParser()
            config.read(file)
            self.logger.info(f"Storing: {x}, {y}")
            if x == account_Read_Ini().enabled_status_text():
                config.set("Account_Module_Data", "end_enabled_status", y)
                config.write(file.open('w'))
            elif x == account_Read_Ini().enrollments_text():
                config.set("Account_Module_Data", "end_enrollments_count", y)
                config.write(file.open('w'))
            elif x == account_Read_Ini().users_text():
                config.set("Account_Module_Data", "end_users_count", y)
                config.write(file.open('w'))
            elif x == account_Read_Ini().max_investigation_length_text():
                config.set("Account_Module_Data", "end_max_investigation_length_count", y)
                config.write(file.open('w'))
            elif x == account_Read_Ini().enrollment_groups_text():
                config.set("Account_Module_Data", "end_enrollment_groups_count", y)
                config.write(file.open('w'))
            elif x == account_Read_Ini().notification_groups_text():
                config.set("Account_Module_Data", "end_notification_groups_count", y)
                config.write(file.open('w'))
            elif x == account_Read_Ini().stations_text():
                config.set("Account_Module_Data", "end_stations_count", y)
                config.write(file.open('w'))
            elif x == account_Read_Ini().first_name_text():
                config.set("Account_Module_Data", "end_first_name", y)
                config.write(file.open('w'))
            elif x == account_Read_Ini().middle_name_text():
                config.set("Account_Module_Data", "end_middle_name", y)
                config.write(file.open('w'))
            elif x == account_Read_Ini().last_name_text():
                config.set("Account_Module_Data", "end_last_name", y)
                config.write(file.open('w'))
            elif x == account_Read_Ini().company_text():
                config.set("Account_Module_Data", "end_company", y)
                config.write(file.open('w'))
            elif x == account_Read_Ini().department_text():
                config.set("Account_Module_Data", "end_department", y)
                config.write(file.open('w'))
            elif x == account_Read_Ini().title_text():
                config.set("Account_Module_Data", "end_title", y)
                config.write(file.open('w'))
            elif x == account_Read_Ini().email_text():
                config.set("Account_Module_Data", "end_email", y)
                config.write(file.open('w'))
            elif x == account_Read_Ini().home_phone_text():
                config.set("Account_Module_Data", "end_home_phone", y)
                config.write(file.open('w'))
            elif x == account_Read_Ini().work_phone_text():
                config.set("Account_Module_Data", "end_work_phone", y)
                config.write(file.open('w'))
            elif x == account_Read_Ini().fax_number_text():
                config.set("Account_Module_Data", "end_fax_number", y)
                config.write(file.open('w'))
            elif x == account_Read_Ini().address_text():
                config.set("Account_Module_Data", "end_address", y)
                config.write(file.open('w'))
            elif x == account_Read_Ini().address_2_text():
                config.set("Account_Module_Data", "end_address_2", y)
                config.write(file.open('w'))
            elif x == account_Read_Ini().city_text():
                config.set("Account_Module_Data", "end_city", y)
                config.write(file.open('w'))
            elif x == account_Read_Ini().state_text():
                config.set("Account_Module_Data", "end_state", y)
                config.write(file.open('w'))
            elif x == account_Read_Ini().zip_code_text():
                config.set("Account_Module_Data", "end_zip_code", y)
                config.write(file.open('w'))
            elif x == account_Read_Ini().timezone_text():
                config.set("Account_Module_Data", "end_timezone", y)
                config.write(file.open('w'))
            elif x == account_Read_Ini().case_TTL_text():
                config.set("Account_Module_Data", "end_case_TTL", y)
                config.write(file.open('w'))
            else:
                self.logger.info(f"some error appeared while storing to ini")
        except Exception as ex:
            self.logger.info(f"store_data_to_common_ini_file_after_execution ex: {ex.args}")
