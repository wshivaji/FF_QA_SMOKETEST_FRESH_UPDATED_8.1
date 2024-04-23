import time
from pathlib import Path

import pytest
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from All_Config_Packages._12_Identify_and_Enroll_Config_Files.Identify_and_Enroll_Readd_INI import \
    Read_Identify_and_Enroll_Components
from Base_Package.Web_Driver import web_driver
from Base_Package.Web_Logger import web_logger
from Base_Package.Login_Logout_Ops import login
from All_Config_Packages._21_SSPR_Config_Fiels.Sspr_Read_INI import sspr_read_ini
from All_Config_Packages._22_Zones_Module_Read_INI.zones_module_read_ini import zones_Read_Ini


class Zones_pom(web_driver, web_logger):
    d = web_driver.d()
    logger = web_logger.logger_obj()
    status = []

    def open_zones_panel_and_verify_zones_panel_displayed(self):
        try:
            self.logger.info("********************************** TC_zones_001 Started *******************************")
            self.status.clear()
            login().login_to_cloud_if_not_done(self.d)
            self.click_on_zones_menu()
            self.verify_zones_panel_heading()
            # self.get_zones_list_enlisted_on_zones_panel_and_verify_names()
            self.close_all_panel_one_by_one()
            self.logger.info(f"status: {self.status}")
            self.logger.info("************* test_TC_zones_001 end  **************")
            if False in self.status:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_zones_001_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.info(f"open_zones_panel_and_verify_zones_panel_displayed ex: {ex.args}")

    def verify_zone_list_enlisted_and_zone_names_displayed_as_expected(self):
        try:
            self.logger.info("********************************** TC_zones_002 Started *******************************")
            self.status.clear()
            login().login_to_cloud_if_not_done(self.d)
            self.click_on_zones_menu()
            self.verify_zones_panel_heading()
            self.get_zones_list_enlisted_on_zones_panel_and_verify_names()
            self.close_all_panel_one_by_one()
            self.logger.info(f"status: {self.status}")
            self.logger.info("************* test_TC_zones_002 end  **************")
            if False in self.status:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_zones_002_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.info(f"verify_zone_list_enlisted_and_zone_names_displayed_as_expected ex: {ex.args}")

    def verify_zone_list_enlisted_and_zone_details_btn_displayed_as_expected(self):
        try:
            self.logger.info("********************************** TC_zones_003 Started *******************************")
            self.status.clear()
            login().login_to_cloud_if_not_done(self.d)
            self.click_on_zones_menu()
            self.verify_zones_panel_heading()
            self.get_zones_list_enlisted_on_zones_panel_and_verify_details_btn_displayed()
            self.close_all_panel_one_by_one()
            self.logger.info(f"status: {self.status}")
            self.logger.info("************* test_TC_zones_003 end  **************")
            if False in self.status:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_zones_003_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.info(f"verify_zone_list_enlisted_and_zone_details_btn_displayed_as_expected ex: {ex.args}")

    def verify_zone_list_enlisted_and_zone_select_checkbox_displayed_as_expected(self):
        try:
            self.logger.info("********************************** TC_zones_004 Started *******************************")
            self.status.clear()
            login().login_to_cloud_if_not_done(self.d)
            self.click_on_zones_menu()
            self.verify_zones_panel_heading()
            self.get_zones_list_enlisted_on_zones_panel_and_verify_zone_checkbox_displayed()
            self.close_all_panel_one_by_one()
            self.logger.info(f"status: {self.status}")
            self.logger.info("************* test_TC_zones_004 end  **************")
            if False in self.status:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_zones_004_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.info(f"verify_zone_list_enlisted_and_zone_select_checkbox_displayed_as_expected ex: {ex.args}")

    # **************************** user methods *************************************

    def get_zones_list_enlisted_on_zones_panel_and_verify_zone_checkbox_displayed(self):
        try:
            self.explicit_wait(5, "XPATH", zones_Read_Ini().zone_checkbox_list_by_xpath(), self.d)
            zones_checkbox_list = self.d.find_elements(By.XPATH, zones_Read_Ini().zone_checkbox_list_by_xpath())
            self.logger.info(f"number of zones listed: {len(zones_checkbox_list)}")
            if len(zones_checkbox_list) > 0:
                zone_names_list = self.d.find_elements(By.XPATH, zones_Read_Ini().zone_name_list_by_xpath())
                for i in range(len(zones_checkbox_list)):
                    self.logger.info(f"zone name: {zone_names_list[i].text}")
                    self.logger.info(f"zone details btn visible: {zones_checkbox_list[i].is_displayed()}")
                    if zones_checkbox_list[i].is_displayed():
                        self.status.append(True)
                    else:
                        self.status.append(False)
        except Exception as ex:
            self.logger.info(f"get_zones_list_enlisted_on_zones_panel_and_verify_zone_checkbox_displayed ex: {ex.args}")

    def get_zones_list_enlisted_on_zones_panel_and_verify_details_btn_displayed(self):
        try:
            self.explicit_wait(5, "XPATH", zones_Read_Ini().zone_details_btn_list_by_xpath(), self.d)
            zones_details_btn_list = self.d.find_elements(By.XPATH, zones_Read_Ini().zone_details_btn_list_by_xpath())
            self.logger.info(f"number of zones listed: {len(zones_details_btn_list)}")
            if len(zones_details_btn_list) > 0:
                zone_names_list = self.d.find_elements(By.XPATH, zones_Read_Ini().zone_name_list_by_xpath())
                for i in range(len(zones_details_btn_list)):
                    self.logger.info(f"zone name: {zone_names_list[i].text}")
                    self.logger.info(f"zone details btn visible: {zones_details_btn_list[i].is_displayed()}")
                    if zones_details_btn_list[i].is_displayed():
                        self.status.append(True)
                    else:
                        self.status.append(False)
        except Exception as ex:
            self.logger.info(f"get_zones_list_enlisted_on_zones_panel_and_verify_details_btn_displayed ex: {ex.args}")

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
            # web_driver.implicit_wait(self, web_driver.one_second, self.d)
            # web_driver.explicit_wait(self, web_driver.one_second, close_all_panels_menu, self.d)
            if len(close_all_panels_menu) > 0:
                close_all_panels_menu[0].click()
                time.sleep(web_driver.one_second)
                try:
                    self.d.switch_to.alert.accept()
                except Exception as ex:
                    self.logger.info(f"Alert handled {ex.args}")
            else:
                pass
            time.sleep(web_driver.one_second)

        except Exception as ex:
            self.logger.error(f"Exception crated: {ex.args}")
            self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\close_all_panels_exception.png")
            return False

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

    def get_zones_list_enlisted_on_zones_panel_and_verify_names(self):
        try:
            zone_name_list_expected = zones_Read_Ini().zone_names().split(',')
            self.logger.info(f"expected zone list: {zone_name_list_expected}")

            self.explicit_wait(5, "XPATH", zones_Read_Ini().zone_list_by_xpath(), self.d)
            zones_list = self.d.find_elements(By.XPATH, zones_Read_Ini().zone_list_by_xpath())
            self.logger.info(f"number of zones listed: {len(zones_list)}")
            if len(zones_list) > 0:
                zone_names_list = self.d.find_elements(By.XPATH, zones_Read_Ini().zone_name_list_by_xpath())
                for i in range(len(zones_list)):
                    self.logger.info(f"zone name: {zone_names_list[i].text}")
                    if zone_names_list[i].is_displayed():
                        self.status.append(True)
                    else:
                        self.status.append(False)
                    if zone_names_list[i].text == zone_name_list_expected[i]:
                        self.status.append(True)
                    else:
                        self.status.append(False)
        except Exception as ex:
            self.logger.info(f"get_zones_list_enlisted_on_zones_panel ex: {ex.args}")

    def verify_zones_panel_heading(self):
        try:
            zones_panel_heading = self.explicit_wait(5, "XPATH", zones_Read_Ini().zones_panel_heading_by_xpath(), self.d)
            self.logger.info(f"zones panel heading visible: {zones_panel_heading.is_displayed()}")
            if zones_panel_heading.is_displayed():
                self.status.append(True)
            else:
                self.status.append(False)
                self.logger.info("zones panel heading is not displayed.")
        except Exception as ex:
            self.logger.info(f"verify_zones_panel_heading ex: {ex.args}")

    def click_on_zones_menu(self):
        try:
            zones_menu = self.explicit_wait(5, "XPATH", zones_Read_Ini().zones_menu_item(), self.d)
            self.logger.info(f"zone menu item is visible: {zones_menu.is_displayed()}")
            if zones_menu.is_displayed():
                zones_menu.click()
            else:
                self.logger.info("zones menu item is not displayed.")

        except Exception as ex:
            self.logger.info(f"click_on_zones_menu ex: {ex.args}")


