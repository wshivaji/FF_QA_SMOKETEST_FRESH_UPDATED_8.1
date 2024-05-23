import time

from All_Config_Packages._10_Events_Config_Files.Events_Read_Ini import events_Read_Ini
from All_Config_Packages._2_Portal_Menu_Module_Config_Files.Portal_Menu_Module_Read_INI import \
    Portal_Menu_Module_read_ini
from All_Config_Packages._7_Visitor_Search_Module_Config_Files.Visitor_Search_Read_INI import \
    Read_Visitor_Search_Components
from Base_Package.Web_Driver import web_driver
from Base_Package.Web_Logger import web_logger
from selenium.webdriver.common.by import By
from Base_Package.Login_Logout_Ops import login
from Base_Package.Login_Logout_Ops import logout
from All_Config_Packages.Store_Groups_Config_Files.Store_Groups_Read_INI import store_group_page_read_ini


class Store_Groups_Module_pom(web_driver, web_logger):
    d = web_driver.d()
    logger = web_logger.logger_obj()
    status = []

    def close_all_panels(self):
        try:
            cloud_menu = self.explicit_wait(10, "XPATH", Portal_Menu_Module_read_ini().get_CLOUD_MENU_button_by_xpath(),
                                            self.d)
            cloud_menu.click()
            time.sleep(web_driver.one_second)
            close_all_panels = self.explicit_wait(10, "XPATH", Portal_Menu_Module_read_ini().
                                                  get_close_all_panels_menu_by_xpath(), self.d)
            close_all_panels.click()
        except Exception as ex:
            self.logger.info(f"close all panels got an exception as: {ex}")

    def select_region_from_org_hierarchy(self):
        try:
            # self.explicit_wait(5, "XPATH", events_Read_Ini().regions_xpath(), self.d)
            time.sleep(web_driver.two_second)
            region_list = self.d.find_elements(By.XPATH, events_Read_Ini().regions_xpath())
            region_checkbox_list = self.d.find_elements(By.XPATH, events_Read_Ini().region_checkbox_xpath())

            self.logger.info(f"region length: {len(region_list)}")
            if len(region_list) > 0:
                for i in range(len(region_list)):
                    if region_list[i].text == events_Read_Ini().edge_name():
                        region_checkbox_list[i].click()
            else:
                self.logger.info(f"region name list not displayed.")
            save_btn = self.explicit_wait(5, "XPATH", events_Read_Ini().save_zone_button_by_xpath(), self.d)
            if save_btn.is_displayed():
                self.logger.info(f"save btn is visible: {save_btn.is_displayed()}")
                save_btn.click()
            else:
                self.logger.info("save btn not displayed.")
        except Exception as ex:
            self.logger.info(f"select_region_from_org_hierarchy ex: {ex.args}")

    def create_three_store_groups_for_different_stores(self):
        try:
            self.logger.info("********** Test_EG_01 Begin  **********")
            status = []
            login().login_with_persona_user(self.d, "super it admin")
            time.sleep(web_driver.one_second)

            store_group_menu = self.explicit_wait(10, "XPATH", store_group_page_read_ini().
                                                  get_store_groups_menu_by_xpath(), self.d)
            if store_group_menu:
                store_group_menu.click()
            time.sleep(web_driver.one_second)

            self.explicit_wait(10, "XPATH", store_group_page_read_ini().get_title_on_store_groups_panel_by_xpath(),
                               self.d)
            description = store_group_page_read_ini().get_store_group_description()
            edge_name = Read_Visitor_Search_Components().zone_data_input()
            x = store_group_page_read_ini().get_store_group_name()
            store_group = x.split(',')

            for i in range(len(store_group)):
                action_button = self.explicit_wait(10, "XPATH", store_group_page_read_ini().
                                                   get_action_dropdown_on_store_groups_panel_by_xpath(), self.d)
                if action_button:
                    action_button.click()
                    time.sleep(web_driver.one_second)
                    create_store_group_option = self.explicit_wait(10, "XPATH", store_group_page_read_ini().
                                                                   get_create_store_group_option_by_xpath(), self.d)
                    create_store_group_option.click()
                    time.sleep(web_driver.one_second)
                    name_field = self.explicit_wait(10, "XPATH", store_group_page_read_ini().
                                                    get_name_field_for_creating_store_group_by_xpath(), self.d)
                    name_field.send_keys(store_group[i])
                    self.logger.info(f"store name entered as {store_group[i]}")
                    time.sleep(web_driver.one_second)
                    description_field = self.explicit_wait(10, "XPATH", store_group_page_read_ini().
                                                           get_description_field_by_xpath(), self.d)
                    description_field.send_keys(description)
                    time.sleep(web_driver.one_second)
                    org_selection_button = self.explicit_wait(10, "XPATH", store_group_page_read_ini().
                                                              get_org_selection_button_by_xpath(), self.d)
                    org_selection_button.click()
                    self.select_region_from_org_hierarchy()
                    time.sleep(web_driver.one_second)
                    save_button = self.explicit_wait(10, "XPATH", store_group_page_read_ini().
                                                     get_save_button_on_store_group_creation_panel_by_xpath(), self.d)
                    save_button.click()
                    time.sleep(web_driver.one_second)
                    success_message = self.explicit_wait(10, "XPATH", store_group_page_read_ini().
                                                         get_store_group_creation_success_message_by_xpath(), self.d)
                    if success_message.text == store_group_page_read_ini().\
                            get_success_message_after_store_group_creation():
                        self.status.append(True)
                        self.logger.info(f"store group {store_group[i]} created successfully!")
                    else:
                        self.status.append(False)
            self.logger.info(f"status: {self.status}")
            if False in status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_SLT_0_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_SLT_0_failed.png")
                return False
            else:
                return True
            # logout().logout_from_core()

        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_SLT_0_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_SLT_0_exception.png")
            self.logger.error(f"TC_SLT_0 got exception as: {ex.args}")
            return False

        # finally:
        #     logout().logout_from_core(self.d)
