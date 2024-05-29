import configparser
import time
from pathlib import Path

import pyautogui

from All_Config_Packages._1_Portal_Login_Module_Config_Files.Portal_Login_Page_Read_INI import \
    Portal_login_page_read_ini
from All_Config_Packages._6_Notification_Groups_Module_Config_Files.Notification_Groups_Read_INI import \
    Read_Notification_Groups_Components
from Base_Package.Web_Driver import web_driver
from Base_Package.Web_Logger import web_logger
from selenium.webdriver.common.by import By
from All_Config_Packages._2_Portal_Menu_Module_Config_Files.Portal_Menu_Module_Read_INI import \
    Portal_Menu_Module_read_ini
from All_POM_Packages.Users_Module_POM.Users_Module_POM import Users_Module_pom
from All_Config_Packages._4_Users_Module_Config_Files.Users_Read_INI import Read_Users_Components
from All_Config_Packages._0_login_logout_config_file.login_logout_read_ini import LoginLogout_Read_ini
from Base_Package.Login_Logout_Ops import login
from Base_Package.Login_Logout_Ops import logout


class Portal_Menu_Module_pom(web_driver, web_logger):
    d = web_driver.d()
    logger = web_logger.logger_obj()
    status = []

    def load_portal_login_page_if_not_loaded(self):
        try:
            if self.d.title != None and self.d.title == LoginLogout_Read_ini().get_portal_title():
                self.logger.info("title is none or matching")
                pass
            else:
                self.logger.info(" no url ")
                self.d.get(LoginLogout_Read_ini().get_portal_url())

                self.d.maximize_window()
                time.sleep(web_driver.two_second)

            return self.d
        except Exception as ex:
            self.logger.error(ex)

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

    def close_all_panels(self):
        try:
            cloud_menu = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_CLOUD_MENU_button_by_xpath())
            cloud_menu.click()
            time.sleep(web_driver.one_second)
            close_all_panels = self.explicit_wait(10, "XPATH", Portal_Menu_Module_read_ini().
                                                  get_close_all_panels_menu_by_xpath(), self.d)
            close_all_panels = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().
                                                  get_close_all_panels_menu_by_xpath())
            close_all_panels.click()
        except Exception as ex:
            self.logger.info(f"close all panels got an exception as: {ex}")

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

    def logout_from_cloud_menu(self):
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

    def persona_users_permissions_validation(self, user):
        try:
            time.sleep(web_driver.one_second)

            cloud_menu_list = self.d.find_elements(By.XPATH, Portal_Menu_Module_read_ini().get_actual_personas_menus_by_xpath())
            self.logger.info(f"cloud menu list length: {len(cloud_menu_list)}")

            users = Read_Notification_Groups_Components().get_user_name_input_data()
            users = users.split(',')

            x = Portal_Menu_Module_read_ini().get_operator_menus()
            operator_permissions = x.split(',')
            y = Portal_Menu_Module_read_ini().get_responder_menus()
            responder_permissions = y.split(',')
            z = Portal_Menu_Module_read_ini().get_approver_menus()
            approver_permissions = z.split(',')
            a = Portal_Menu_Module_read_ini().get_executive_menus()
            executive_permissions = a.split(',')
            b = Portal_Menu_Module_read_ini().get_it_admin_menus()
            it_admin_permissions = b.split(',')

            op_count = 0
            re_count = 0
            app_count = 0
            exe_count = 0
            admin_count = 0

            if user == users[0]:
                for i in range(len(operator_permissions)):
                    for j in range(len(cloud_menu_list)):
                        if cloud_menu_list[j].is_displayed():
                            if cloud_menu_list[j].text == operator_permissions[i]:
                                self.logger.info(f"{cloud_menu_list[j].text} menu is displayed..")
                                op_count = op_count + 1
                                self.status.append(True)
                if len(operator_permissions) == op_count:
                    self.logger.info(f"***** For {users[0]} user Expected menus are visible..")
                    self.status.append(True)
                else:
                    self.logger.info(f"***** For {users[0]} user Expected menus are not visible..")
                    self.status.append(False)

            elif user == users[1]:
                for i in range(len(responder_permissions)):
                    for j in range(len(cloud_menu_list)):
                        if cloud_menu_list[j].is_displayed():
                            if cloud_menu_list[j].text == responder_permissions[i]:
                                self.logger.info(f"{cloud_menu_list[j].text} menu is displayed..")
                                re_count = re_count + 1
                                self.status.append(True)
                if len(responder_permissions) == re_count:
                    self.logger.info(f"***** For {users[1]} user Expected menus are visible..")
                    self.status.append(True)
                else:
                    self.logger.info(f"***** For {users[1]} user Expected menus are not visible..")
                    self.status.append(False)

            elif user == users[2]:
                self.logger.info(f"length of app: {len(approver_permissions)}")
                for i in range(len(approver_permissions)):
                    for j in range(len(cloud_menu_list)):
                        if cloud_menu_list[j].is_displayed():
                            if cloud_menu_list[j].text == approver_permissions[i]:
                                self.logger.info(f"{cloud_menu_list[j].text} menu is displayed..")
                                app_count = app_count + 1
                                self.status.append(True)

                if len(approver_permissions) == app_count:
                    self.logger.info(f"***** For {users[2]} user Expected menus are visible..")
                    self.status.append(True)
                else:
                    self.logger.info(f"***** For {users[2]} user Expected menus are not visible..")
                    self.status.append(False)

            elif user == users[3]:
                self.logger.info(f"length of app: {len(executive_permissions)}")
                for i in range(len(executive_permissions)):
                    for j in range(len(cloud_menu_list)):
                        if cloud_menu_list[j].is_displayed():
                            if cloud_menu_list[j].text == executive_permissions[i]:
                                self.logger.info(f"{cloud_menu_list[j].text} menu is displayed..")
                                exe_count = exe_count+ 1
                                self.status.append(True)

                if len(executive_permissions) == exe_count:
                    self.logger.info(f"***** For {users[3]} user Expected menus are visible..")
                    self.status.append(True)
                else:
                    self.logger.info(f"***** For {users[3]} user Expected menus are not visible..")
                    self.status.append(False)

            elif user == users[4]:
                self.logger.info(f"length of app: {len(it_admin_permissions)}")
                for i in range(len(it_admin_permissions)):
                    for j in range(len(cloud_menu_list)):
                        if cloud_menu_list[j].is_displayed():
                            if cloud_menu_list[j].text == it_admin_permissions[i]:
                                self.logger.info(f"{cloud_menu_list[j].text} menu is displayed..")
                                admin_count = admin_count+ 1
                                self.status.append(True)

                if len(it_admin_permissions) == admin_count:
                    self.logger.info(f"***** For {users[4]} user Expected menus are visible..")
                    self.status.append(True)
                else:
                    self.logger.info(f"***** For {users[4]} user Expected menus are not visible..")
                    self.status.append(False)

            else:
                self.logger.info("User is not persona user..")

            self.logout_from_cloud_menu()

        except Exception as ex:
            self.logger.info(f"persona users permissions validation got an exception as:{ex}")

    def Verify_all_submenus_are_visible_and_clickable_on_Cloud_Menu(self):
        try:
            self.logger.info("********** TC_PM_1 started ********")
            self.status.clear()
            # # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            # login().login_to_localhost_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            self.explicit_wait(10,"XPATH", Portal_Menu_Module_read_ini().get_events_menu_by_xpath(), self.d)
            events_menu_list = self.d.find_elements(By.XPATH, Portal_Menu_Module_read_ini().get_events_menu_by_xpath())
            events_menu = self.wait_for_element_to_appear(events_menu_list, Portal_Menu_Module_read_ini().get_events_menu_by_xpath())
            expected_title = Portal_Menu_Module_read_ini().get_expected_events_text()
            if events_menu.is_displayed():
                if events_menu.text == expected_title:
                    self.logger.info(f"Events menu is visible in menu items...")
                    self.status.append(True)
            else:
                self.status.append(False)
            icon = Portal_Menu_Module_read_ini().get_icon_by_xpath()
            exclamatory_icon = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_events_menu_by_xpath() +
                                                   icon)
            if exclamatory_icon.is_displayed():
                self.logger.info("exclamatory icon is visible..")
                self.status.append(True)
            else:
                self.status.append(False)
            events_menu.click()
            time.sleep(web_driver.two_second)
            actual_title_list = self.d.find_elements(By.XPATH, Portal_Menu_Module_read_ini().get_title_on_Events_panel_by_xpath())
            actual_title = self.wait_for_element_to_appear(actual_title_list, Portal_Menu_Module_read_ini().get_title_on_Events_panel_by_xpath())

            self.logger.info(f"actual title: {actual_title.text}")
            self.logger.info(f"expected title: {expected_title}")
            if actual_title.text == expected_title:
                self.status.append(True)
            else:
                self.status.append(False)
            self.close_all_panels()
            # ****************************************** Tags Menu ***************************************
            self.explicit_wait(10, "XPATH", Portal_Menu_Module_read_ini().get_Tags_menu_by_xpath(), self.d)
            tags_menu_list = self.d.find_elements(By.XPATH, Portal_Menu_Module_read_ini().get_Tags_menu_by_xpath())
            tags_menu = self.wait_for_element_to_appear(tags_menu_list,
                                                        Portal_Menu_Module_read_ini().get_Tags_menu_by_xpath())
            expected_title = Portal_Menu_Module_read_ini().get_expected_tags_text()
            time.sleep(web_driver.one_second)
            if tags_menu.is_displayed():
                if tags_menu.text == expected_title:
                    self.logger.info(f"Tags menu is visible in menu items...")
                    self.status.append(True)
            else:
                self.status.append(False)
            icon = Portal_Menu_Module_read_ini().get_icon_by_xpath()
            tag_icon = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_Tags_menu_by_xpath() + icon)
            if tag_icon.is_displayed():
                self.logger.info("tag icon is visible..")
                self.status.append(True)
            else:
                self.status.append(False)
            tags_menu.click()
            time.sleep(web_driver.two_second)
            actual_title_list = self.d.find_elements(By.XPATH,
                                                     Portal_Menu_Module_read_ini().get_title_on_Tags_panel_by_xpath())
            actual_title = self.wait_for_element_to_appear(actual_title_list,
                                                           Portal_Menu_Module_read_ini().get_title_on_Tags_panel_by_xpath())
            self.logger.info(f"actual title: {actual_title.text}")
            self.logger.info(f"expected title: {expected_title}")
            if actual_title.text == expected_title:
                self.status.append(True)
            else:
                self.status.append(False)
            self.close_all_panels()
            # ***********************************************************************************
            self.explicit_wait(10, "XPATH", Portal_Menu_Module_read_ini().get_Identify_and_Enroll_menu_by_xpath(),
                               self.d)
            identify_enroll_menu = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().
                                                       get_Identify_and_Enroll_menu_by_xpath())
            expected_title = Portal_Menu_Module_read_ini().get_expected_identify_enroll_text()

            if identify_enroll_menu.is_displayed():
                if identify_enroll_menu.text == expected_title:
                    self.logger.info(f"Identify & Enroll menu is visible in menu items...")
                    self.status.append(True)
            else:
                self.status.append(False)
            icon = Portal_Menu_Module_read_ini().get_icon_by_xpath()
            camera_icon = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().
                                              get_Identify_and_Enroll_menu_by_xpath() + icon)
            if camera_icon.is_displayed():
                self.logger.info("camera icon is visible..")
                self.status.append(True)
            else:
                self.status.append(False)
            identify_enroll_menu.click()
            time.sleep(web_driver.two_second)
            actual_title = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().
                                               get_title_on_Identify_Enroll_panel_by_xpath()).text
            self.logger.info(f"actual title: {actual_title}")
            self.logger.info(f"expected title: {expected_title}")
            if actual_title == expected_title:
                self.status.append(True)
            else:
                self.status.append(False)
            self.close_all_panels()

            # ************************************************************************
            self.explicit_wait(10, "XPATH", Portal_Menu_Module_read_ini().
                               get_Detect_Faces_menu_by_xpath(), self.d)
            detect_faces_menu = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().
                                                    get_Detect_Faces_menu_by_xpath())
            expected_title = Portal_Menu_Module_read_ini().get_expected_detect_faces_text()

            if detect_faces_menu.is_displayed():
                if detect_faces_menu.text == expected_title:
                    self.logger.info(f"Detect Faces menu is visible in menu items...")
                    self.status.append(True)
            else:
                self.status.append(False)
            icon = Portal_Menu_Module_read_ini().get_icon_by_xpath()
            camera_icon = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().
                                              get_Detect_Faces_menu_by_xpath() + icon)
            if camera_icon.is_displayed():
                self.logger.info("camera icon is visible..")
                self.status.append(True)
            else:
                self.status.append(False)
            detect_faces_menu.click()
            time.sleep(web_driver.three_second)
            actual_title = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().
                                               get_title_on_Detect_Faces_panel_by_xpath()).text

            self.logger.info(f"actual title: {actual_title}")
            expected_title = Portal_Menu_Module_read_ini().get_expected_detect_faces_text()
            self.logger.info(f"expected title: {expected_title}")
            if actual_title == expected_title:
                self.status.append(True)
            else:
                self.status.append(False)
            self.close_all_panels()
            # *******************************************************************************

            self.explicit_wait(10, "XPATH", Portal_Menu_Module_read_ini().
                               get_Enrollments_menu_by_xpath(), self.d)
            enrollments_menu = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().
                                                   get_Enrollments_menu_by_xpath())
            expected_title = Portal_Menu_Module_read_ini().get_expected_enrollments_text()

            if enrollments_menu.is_displayed():
                if enrollments_menu.text == expected_title:
                    self.logger.info(f"Enrollments menu is visible in menu items...")
                    self.status.append(True)
            else:
                self.status.append(False)
            icon = Portal_Menu_Module_read_ini().get_icon_by_xpath()
            person_icon = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_Enrollments_menu_by_xpath() +
                                              icon)
            if person_icon.is_displayed():
                self.logger.info("person icon is visible..")
                self.status.append(True)
            else:
                self.status.append(False)
            enrollments_menu.click()
            time.sleep(web_driver.two_second)
            actual_title = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().
                                               get_title_on_Enrollments_panel_by_xpath()).text
            self.logger.info(f"actual title: {actual_title}")
            self.logger.info(f"expected title: {expected_title}")
            if actual_title == expected_title:
                self.status.append(True)
            else:
                self.status.append(False)
            self.close_all_panels()

            # **********************************************************************
            self.explicit_wait(10, "XPATH", Portal_Menu_Module_read_ini().
                               get_Enrollment_Groups_menu_by_xpath(), self.d)
            enrollment_groups_menu = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().
                                                         get_Enrollment_Groups_menu_by_xpath())
            expected_title = Portal_Menu_Module_read_ini().get_expected_enrollment_groups_text()

            if enrollment_groups_menu.is_displayed():
                if enrollment_groups_menu.text == expected_title:
                    self.logger.info(f"Enrollment Groups menu is visible in menu items...")
                    self.status.append(True)
            else:
                self.status.append(False)
            icon = Portal_Menu_Module_read_ini().get_icon_by_xpath()
            group_icon = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().
                                             get_Enrollment_Groups_menu_by_xpath() + icon)
            if group_icon.is_displayed():
                self.logger.info("group icon is visible..")
                self.status.append(True)
            else:
                self.status.append(False)
            enrollment_groups_menu.click()
            time.sleep(web_driver.two_second)
            actual_title = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().
                                               get_title_on_Enrollment_Groups_panel_by_xpath()).text
            self.logger.info(f"actual title: {actual_title}")
            self.logger.info(f"expected title: {expected_title}")
            if actual_title == expected_title:
                self.status.append(True)
            else:
                self.status.append(False)
            self.close_all_panels()
            # ***********************************************************************
            self.explicit_wait(10, "XPATH", Portal_Menu_Module_read_ini().
                               get_Notification_Groups_menu_by_xpath(), self.d)
            notification_groups_menu = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().
                                                           get_Notification_Groups_menu_by_xpath())
            expected_title = Portal_Menu_Module_read_ini().get_expected_notification_groups_text()

            if notification_groups_menu.is_displayed():
                if notification_groups_menu.text == expected_title:
                    self.logger.info(f"Notification Groups menu is visible in menu items...")
                    self.status.append(True)
            else:
                self.status.append(False)
            icon = Portal_Menu_Module_read_ini().get_icon_by_xpath()
            alert_icon = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().
                                             get_Notification_Groups_menu_by_xpath() + icon)
            if alert_icon.is_displayed():
                self.logger.info("alert icon is visible..")
                self.status.append(True)
            else:
                self.status.append(False)
            notification_groups_menu.click()
            time.sleep(web_driver.two_second)
            actual_title = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().
                                               get_title_on_Notification_Groups_panel_by_xpath()).text
            self.logger.info(f"actual title: {actual_title}")
            self.logger.info(f"expected title: {expected_title}")
            if actual_title == expected_title:
                self.status.append(True)
            else:
                self.status.append(False)
            self.close_all_panels()

            # ***************************************************************************
            self.explicit_wait(10, "XPATH", Portal_Menu_Module_read_ini().
                               get_Visitor_Search_menu_by_xpath(), self.d)
            visitor_search_menu = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().
                                                      get_Visitor_Search_menu_by_xpath())
            expected_title = Portal_Menu_Module_read_ini().get_expected_visitor_search_text()

            if visitor_search_menu.is_displayed():
                if visitor_search_menu.text == expected_title:
                    self.logger.info(f"Visitor Search menu is visible in menu items...")
                    self.status.append(True)
            else:
                self.status.append(False)
            icon = Portal_Menu_Module_read_ini().get_icon_by_xpath()
            search_icon = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().
                                              get_Visitor_Search_menu_by_xpath() + icon)
            if search_icon.is_displayed():
                self.logger.info("search icon is visible..")
                self.status.append(True)
            else:
                self.status.append(False)
            visitor_search_menu.click()
            time.sleep(web_driver.two_second)
            actual_title = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().
                                               get_title_on_Visitor_Search_panel_by_xpath()).text
            self.logger.info(f"actual title: {actual_title}")
            self.logger.info(f"expected title: {expected_title}")
            if actual_title == expected_title:
                self.status.append(True)
            else:
                self.status.append(False)
            self.close_all_panels()

            # *****************************************************************************
            self.explicit_wait(10, "XPATH", Portal_Menu_Module_read_ini().
                               get_Visitor_Search_Jobs_menu_by_xpath(), self.d)
            visitor_search_jobs_menu = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().
                                                           get_Visitor_Search_Jobs_menu_by_xpath())
            expected_title = Portal_Menu_Module_read_ini().get_expected_visitor_search_jobs_text()

            if visitor_search_jobs_menu.is_displayed():
                if visitor_search_jobs_menu.text == visitor_search_jobs_menu:
                    self.logger.info(f"Visitor Search Jobs menu is visible in menu items...")
                    self.status.append(True)
            else:
                self.status.append(False)
            icon = Portal_Menu_Module_read_ini().get_icon_by_xpath()
            list_icon = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().
                                            get_Visitor_Search_Jobs_menu_by_xpath() + icon)
            if list_icon.is_displayed():
                self.logger.info("list icon is visible..")
                self.status.append(True)
            else:
                self.status.append(False)
            visitor_search_jobs_menu.click()
            time.sleep(web_driver.three_second)
            actual_title = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().
                                               get_title_on_Visitor_Search_Jobs_panel_by_xpath()).text
            self.logger.info(f"actual title: {actual_title}")
            self.logger.info(f"expected title: {expected_title}")
            if actual_title == expected_title:
                self.status.append(True)
            else:
                self.status.append(False)
            self.close_all_panels()
            # **********************************************************************************
            self.explicit_wait(10, "XPATH", Portal_Menu_Module_read_ini().get_Notes_menu_by_xpath(), self.d)
            notes_menu = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_Notes_menu_by_xpath())
            expected_title = Portal_Menu_Module_read_ini().get_expected_notes_text()

            if notes_menu.is_displayed():
                if notes_menu.text == expected_title:
                    self.logger.info(f"Notes menu is visible in menu items...")
                    self.status.append(True)
            else:
                self.status.append(False)
            icon = Portal_Menu_Module_read_ini().get_icon_by_xpath()
            notes_icon = self.d.find_element(By.XPATH,
                                             Portal_Menu_Module_read_ini().get_Notes_menu_by_xpath() + icon)
            if notes_icon.is_displayed():
                self.logger.info("notes icon is visible..")
                self.status.append(True)
            else:
                self.status.append(False)
            notes_menu.click()
            time.sleep(web_driver.three_second)
            actual_title = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().
                                               get_title_on_Notes_panel_by_xpath()).text
            self.logger.info(f"actual title: {actual_title}")
            self.logger.info(f"expected title: {expected_title}")
            if actual_title == expected_title:
                self.status.append(True)
            else:
                self.status.append(False)
            self.close_all_panels()
            # *********************************************************************
            self.explicit_wait(10, "XPATH", Portal_Menu_Module_read_ini().get_Locations_menu_by_xpath(), self.d)
            locations_menu = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_Locations_menu_by_xpath())
            expected_title = Portal_Menu_Module_read_ini().get_expected_locations_text()
            if locations_menu.is_displayed():
                if locations_menu.text == expected_title:
                    self.logger.info(f"Locations menu is visible in menu items...")
                    self.status.append(True)
            else:
                self.status.append(False)
            icon = Portal_Menu_Module_read_ini().get_icon_by_xpath()
            location_icon = self.d.find_element(By.XPATH,
                                                Portal_Menu_Module_read_ini().get_Locations_menu_by_xpath() + icon)
            if location_icon.is_displayed():
                self.logger.info("location icon is visible..")
                self.status.append(True)
            else:
                self.status.append(False)
            locations_menu.click()
            time.sleep(web_driver.two_second)
            cancel_button = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().
                                                get_cancel_button_on_location_panel_by_xpath())
            if cancel_button.is_displayed():
                cancel_button.click()
                self.status.append(True)
            else:
                self.status.append(False)
            self.close_all_panels()

            # *****************************************************************
            self.explicit_wait(10, "XPATH", Portal_Menu_Module_read_ini().get_Users_menu_by_xpath(), self.d)
            users_menu = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_Users_menu_by_xpath())
            expected_title = Portal_Menu_Module_read_ini().get_expected_users_text()

            if users_menu.is_displayed():
                if users_menu.text == expected_title:
                    self.logger.info(f"Users menu is visible in menu items...")
                    self.status.append(True)
            else:
                self.status.append(False)
            icon = Portal_Menu_Module_read_ini().get_icon_by_xpath()
            user_icon = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_Users_menu_by_xpath() + icon)
            if user_icon.is_displayed():
                self.logger.info("user icon is visible..")
                self.status.append(True)
            else:
                self.status.append(False)
            users_menu.click()
            time.sleep(web_driver.two_second)
            actual_title = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().
                                               get_title_on_Users_panel_by_xpath()).text
            self.logger.info(f"actual title: {actual_title}")
            self.logger.info(f"expected title: {expected_title}")
            if actual_title == expected_title:
                self.status.append(True)
            else:
                self.status.append(False)
            self.close_all_panels()

            # **********************************************************************
            self.explicit_wait(10, "XPATH", Portal_Menu_Module_read_ini().
                               get_User_Roles_menu_by_xpath(), self.d)
            user_roles_menu = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().
                                                  get_User_Roles_menu_by_xpath())
            expected_title = Portal_Menu_Module_read_ini().get_expected_user_roles_text()

            if user_roles_menu.is_displayed():
                if user_roles_menu.text == expected_title:
                    self.logger.info(f"User Roles menu is visible in menu items...")
                    self.status.append(True)
            else:
                self.status.append(False)
            icon = Portal_Menu_Module_read_ini().get_icon_by_xpath()
            user_roles_icon = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_User_Roles_menu_by_xpath()
                                                  + icon)
            if user_roles_icon.is_displayed():
                self.logger.info("user roles icon is visible..")
                self.status.append(True)
            else:
                self.status.append(False)
            user_roles_menu.click()
            time.sleep(web_driver.two_second)
            actual_title = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().
                                               get_title_on_User_Roles_panel_by_xpath()).text
            self.logger.info(f"actual title: {actual_title}")
            self.logger.info(f"expected title: {expected_title}")
            if actual_title == expected_title:
                self.status.append(True)
            else:
                self.status.append(False)
            self.close_all_panels()

            # ***************************************************************
            self.explicit_wait(10, "XPATH", Portal_Menu_Module_read_ini().get_Zones_menu_by_xpath(), self.d)
            zones_menu = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_Zones_menu_by_xpath())
            expected_title = Portal_Menu_Module_read_ini().get_expected_zones_text()

            if zones_menu.is_displayed():
                if zones_menu.text == expected_title:
                    self.logger.info(f"Zones menu is visible in menu items...")
                    self.status.append(True)
            else:
                self.status.append(False)
            icon = Portal_Menu_Module_read_ini().get_icon_by_xpath()
            dot_circle_icon = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_Zones_menu_by_xpath() +
                                                  icon)
            if dot_circle_icon.is_displayed():
                self.logger.info("dot circle icon is visible..")
                self.status.append(True)
            else:
                self.status.append(False)
            zones_menu.click()
            time.sleep(web_driver.three_second)
            actual_title = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().
                                               get_title_on_Zones_panel_by_xpath()).text
            self.logger.info(f"actual title: {actual_title}")
            expected_title = Portal_Menu_Module_read_ini().get_expected_zones_text()
            self.logger.info(f"expected title: {expected_title}")
            if actual_title == expected_title:
                self.status.append(True)
            else:
                self.status.append(False)
            self.close_all_panels()

            # ************************************************************
            self.explicit_wait(10, "XPATH", Portal_Menu_Module_read_ini().get_Account_menu_by_xpath(), self.d)
            account_menu = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_Account_menu_by_xpath())
            expected_title = Portal_Menu_Module_read_ini().get_expected_account_text()
            if account_menu.is_displayed():
                if account_menu.text == expected_title:
                    self.logger.info(f"Account menu is visible in menu items...")
                    self.status.append(True)
            else:
                self.status.append(False)
            icon = Portal_Menu_Module_read_ini().get_icon_by_xpath()
            lock_icon = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_Account_menu_by_xpath() + icon)
            if lock_icon.is_displayed():
                self.logger.info("lock icon is visible..")
                self.status.append(True)
            else:
                self.status.append(False)
            account_menu.click()
            time.sleep(web_driver.two_second)
            actual_title = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().
                                               get_title_on_Account_panel_by_xpath()).text
            self.logger.info(f"actual title: {actual_title}")
            self.logger.info(f"expected title: {expected_title}")
            if actual_title == expected_title:
                self.status.append(True)
            else:
                self.status.append(False)
            self.close_all_panels()

            # **********************************************************
            self.explicit_wait(10, "XPATH", Portal_Menu_Module_read_ini().get_Reporting_menu_by_xpath(), self.d)
            reporting_menu = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_Reporting_menu_by_xpath())
            expected_title = Portal_Menu_Module_read_ini().get_expected_reporting_text()

            if reporting_menu.is_displayed():
                if reporting_menu.text == expected_title:
                    self.logger.info(f"Reporting menu is visible in menu items...")
                    self.status.append(True)
            else:
                self.status.append(False)
            icon = Portal_Menu_Module_read_ini().get_icon_by_xpath()
            chart_icon = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_Reporting_menu_by_xpath() +
                                             icon)
            if chart_icon.is_displayed():
                self.logger.info("chart icon is visible..")
                self.status.append(True)
            else:
                self.status.append(False)
            reporting_menu.click()
            time.sleep(web_driver.two_second)
            actual_title = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().
                                               get_title_on_Reporting_panel_by_xpath()).text
            self.logger.info(f"actual title: {actual_title}")
            self.logger.info(f"expected title: {expected_title}")
            if actual_title == expected_title:
                self.status.append(True)
            else:
                self.status.append(False)
            self.close_all_panels()

            # ******************************************************************
            insights_dashboard_menu = self.explicit_wait(10, "XPATH",
                                                         Portal_Menu_Module_read_ini().get_Dashboard_menu_by_xpath(),
                                                         self.d)
            expected_text = Portal_Menu_Module_read_ini().get_expected_dashboard_text()
            if insights_dashboard_menu.is_displayed():
                if insights_dashboard_menu.text == expected_text:
                    self.logger.info(f"Insights Dashboard menu is visible in menu items...")
                    self.status.append(True)
            else:
                self.status.append(False)
            dollar_icon = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().
                                              get_dollar_icon_on_dashboard_menu_by_xpath())
            if dollar_icon.is_displayed():
                self.logger.info("dollar icon is visible..")
                self.status.append(True)
            else:
                self.status.append(False)
            insights_dashboard_menu.click()
            time.sleep(web_driver.two_second)
            self.d.switch_to.window(self.d.window_handles[1])
            time.sleep(web_driver.three_second)
            actual_title = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().
                                               get_title_on_Dashboard_panel_by_xpath()).text
            self.logger.info(f"actual title: {actual_title}")
            expected_title = Portal_Menu_Module_read_ini().get_expected_overview_dashboard_text()
            self.logger.info(f"expected title: {expected_title}")
            if actual_title == expected_title:
                self.status.append(True)
                self.close_current_tab()
            else:
                self.status.append(False)

            # ******************************************************************
            self.explicit_wait(10, "XPATH", Portal_Menu_Module_read_ini().get_Notifier_menu_by_xpath(), self.d)
            notifier_menu = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_Notifier_menu_by_xpath())
            expected_title = Portal_Menu_Module_read_ini().get_expected_notifier_text()

            if notifier_menu.is_displayed():
                if notifier_menu.text == expected_title:
                    self.logger.info(f"Notifier menu is visible in menu items...")
                    self.status.append(True)
            else:
                self.status.append(False)
            icon = Portal_Menu_Module_read_ini().get_icon_by_xpath()
            horn_icon = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_Notifier_menu_by_xpath() + icon)
            if horn_icon.is_displayed():
                self.logger.info("horn icon is visible..")
                self.status.append(True)
            else:
                self.status.append(False)
            notifier_menu.click()
            time.sleep(web_driver.two_second)
            actual_title = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().
                                               get_title_on_Notifier_panel_by_xpath()).text
            self.logger.info(f"actual title: {actual_title}")
            self.logger.info(f"expected title: {expected_title}")
            if actual_title == expected_title:
                self.status.append(True)
            else:
                self.status.append(False)
            close_notifier_panel_btn = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().
                                                           get_close_notifier_button_by_xpath())
            close_notifier_panel_btn.click()

            # *****************************************************************
            self.explicit_wait(10, "XPATH", Portal_Menu_Module_read_ini().get_Audit_Log_Report_menu_by_xpath(), self.d)
            alr_menu = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_Audit_Log_Report_menu_by_xpath())
            expected_title = Portal_Menu_Module_read_ini().get_expected_audit_log_report_text()

            if alr_menu.is_displayed():
                if alr_menu.text == expected_title:
                    self.logger.info(f"Audit Log Report menu is visible in menu items...")
                    self.status.append(True)
            else:
                self.status.append(False)

            alr_icon = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().
                                           get_shield_icon_on_alr_menu_by_xpath())
            if alr_icon.is_displayed():
                self.logger.info("audit log report icon is visible..")
                self.status.append(True)
            else:
                self.status.append(False)
            alr_menu.click()
            time.sleep(web_driver.two_second)
            self.d.switch_to.window(self.d.window_handles[1])
            time.sleep(web_driver.three_second)
            actual_title = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().
                                               get_title_on_Audit_Log_Report_panel_by_xpath()).text
            self.logger.info(f"actual title: {actual_title}")
            self.logger.info(f"expected title: {expected_title}")
            if actual_title == expected_title:
                self.status.append(True)
                self.close_current_tab()
            else:
                self.status.append(False)

            self.logger.info(f"status: {self.status}")
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {web_driver.screenshots_path}\\TC_PM_1.png")
                self.d.save_screenshot(f"{web_driver.screenshots_path}\\TC_PM_1.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {web_driver.screenshots_path}\\TC_PM_1_exception.png")
            self.d.save_screenshot(f"{web_driver.screenshots_path}\\TC_PM_1_exception.png")
            self.logger.error(f"TC_PM_1 got exception as: {ex}")

    def Verify_for_Operator_user_PME_Tags_IE_DF_Enrollments_EG_VS_VSJ_Notes_Loc_Zones_Reporting_IDB_Notifier_these_menus_are_visible_on_the_cloud_menu_items(self):
        try:
            self.logger.info("********** TC_PM_2 started ********")
            self.status.clear()
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)

            x = Read_Notification_Groups_Components().get_user_name_input_data()
            username = x.split(',')
            self.logger.info(f"username expected: {username[0]}")

            Users_Module_pom().click_user_on_cloud_menu()

            user_search_filter = self.d.find_element(By.XPATH,
                                                     Read_Notification_Groups_Components().search_box_by_xpath())
            user_search_filter.clear()
            user_search_filter.send_keys(username[0])
            time.sleep(web_driver.one_second)

            users_list = self.d.find_elements(By.XPATH, Read_Notification_Groups_Components().users_list_by_xpath())

            time.sleep(web_driver.one_second)

            if users_list[0].text == username[0]:
                self.logger.info(f"{users_list[0].text} user is present...")
                self.status.append(True)
            else:
                self.status.append(False)

            self.logout_from_cloud_menu()
            login().login_with_persona_user(self.d, username[0])
            time.sleep(web_driver.one_second)
            login().accept_terms_and_conditions_for_login_for_new_user(self.d)
            self.persona_users_permissions_validation(username[0])

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_PM_2.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_PM_2.png")
                return False
            else:
                return True

        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_PM_2_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_PM_2_exception.png")
            self.logger.error(f"TC_PM_2 got exception as: {ex}")
        finally:
            logout().logout_from_core(self.d)

    def Verify_for_Responder_user_PME_Tags_IE_DF_Enrollments_EG_NG_VS_VSJ_Notes_Loc_US_UR_Zones_Reporting_IDB_Notifier_ALR_these_menus_are_visible_on_the_cloud_menu_items(
            self):
        try:
            self.logger.info("********** TC_PM_3 started ********")
            self.status.clear()
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)

            x = Read_Notification_Groups_Components().get_user_name_input_data()
            username = x.split(',')
            self.logger.info(f"username expected: {username[1]}")

            Users_Module_pom().click_user_on_cloud_menu()

            user_search_filter = self.d.find_element(By.XPATH,
                                                     Read_Notification_Groups_Components().search_box_by_xpath())
            user_search_filter.clear()
            user_search_filter.send_keys(username[1])
            time.sleep(web_driver.one_second)

            users_list = self.d.find_elements(By.XPATH, Read_Notification_Groups_Components().users_list_by_xpath())

            time.sleep(web_driver.one_second)

            if users_list[0].text == username[1]:
                self.logger.info(f"****** {users_list[0].text} user is present *******")
                self.status.append(True)
            else:
                self.status.append(False)

            self.logout_from_cloud_menu()
            login().login_with_persona_user(self.d, username[1])
            login().accept_terms_and_conditions_for_login_for_new_user(self.d)
            self.persona_users_permissions_validation(username[1])

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_PM_3.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_PM_3.png")
                return False
            else:
                return True

        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_PM_3_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_PM_3_exception.png")
            self.logger.error(f"TC_PM_3 got exception as: {ex}")
        finally:
            logout().logout_from_core(self.d)

    def Verify_for_Approver_or_supervisor_user_PME_Tags_IE_DF_Enrollments_EG_NG_VS_VSJ_Notes_Loc_US_UR_Zones_Reporting_IDB_Notifier_ALR_these_menus_are_visible_on_the_cloud_menu_items(
            self):
        try:
            self.logger.info("********** TC_PM_4 started ********")
            self.status.clear()
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)

            x = Read_Notification_Groups_Components().get_user_name_input_data()
            username = x.split(',')
            self.logger.info(f"username expected: {username[2]}")

            Users_Module_pom().click_user_on_cloud_menu()

            user_search_filter = self.d.find_element(By.XPATH,
                                                     Read_Notification_Groups_Components().search_box_by_xpath())
            user_search_filter.clear()
            user_search_filter.send_keys(username[2])
            time.sleep(web_driver.one_second)

            users_list = self.d.find_elements(By.XPATH, Read_Notification_Groups_Components().users_list_by_xpath())

            time.sleep(web_driver.one_second)

            if users_list[0].text == username[2]:
                self.logger.info(f"****** {users_list[0].text} user is present *******")
                self.status.append(True)
            else:
                self.status.append(False)

            self.logout_from_cloud_menu()
            login().login_with_persona_user(self.d, username[2])

            login().accept_terms_and_conditions_for_login_for_new_user(self.d)
            self.persona_users_permissions_validation(username[2])

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_PM_4.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_PM_4.png")
                return False
            else:
                return True

        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_PM_4_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_PM_4_exception.png")
            self.logger.error(f"TC_PM_4 got exception as: {ex}")
        finally:
            logout().logout_from_core(self.d)

    def Verify_for_Executive_user_PME_Tags_IE_DF_Enrollments_EG_NG_VS_VSJ_Notes_Loc_US_UR_Zones_Account_Reporting_IDB_Notifier_ALR_these_menus_are_visible_on_the_cloud_menu_items(
            self):
        try:
            self.logger.info("********** TC_015 started ********")
            self.status.clear()
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)

            x = Read_Notification_Groups_Components().get_user_name_input_data()
            username = x.split(',')
            self.logger.info(f"username expected: {username[3]}")

            Users_Module_pom().click_user_on_cloud_menu()

            user_search_filter = self.d.find_element(By.XPATH,
                                                     Read_Notification_Groups_Components().search_box_by_xpath())
            user_search_filter.clear()
            user_search_filter.send_keys(username[3])
            time.sleep(web_driver.one_second)

            users_list = self.d.find_elements(By.XPATH, Read_Notification_Groups_Components().users_list_by_xpath())

            time.sleep(web_driver.one_second)

            if users_list[0].text == username[3]:
                self.logger.info(f"****** {users_list[0].text} user is present *******")
                self.status.append(True)
            else:
                self.status.append(False)

            self.logout_from_cloud_menu()
            login().login_with_persona_user(self.d, username[3])
            login().accept_terms_and_conditions_for_login_for_new_user(self.d)
            self.persona_users_permissions_validation(username[3])

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_PM_5.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_PM_5.png")
                return False
            else:
                return True

        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_PM_5_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_PM_5_exception.png")
            self.logger.error(f"TC_PM_5 got exception as: {ex}")
        finally:
            logout().logout_from_core(self.d)

    def Verify_for_IT_Admin_user_PME_Tags_IE_DF_Enrollments_EG_NG_VS_VSJ_Notes_Loc_US_UR_SG_Zones_Account_Reporting_IDB_Notifier_ALR_these_menus_are_visible_on_the_cloud_menu_items(
            self):
        try:
            self.logger.info("********** TC_PM_6 started ********")
            self.status.clear()
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)

            x = Read_Notification_Groups_Components().get_user_name_input_data()
            username = x.split(',')
            self.logger.info(f"username expected: {username[4]}")

            Users_Module_pom().click_user_on_cloud_menu()

            user_search_filter = self.d.find_element(By.XPATH,
                                                     Read_Notification_Groups_Components().search_box_by_xpath())
            user_search_filter.clear()
            user_search_filter.send_keys(username[4])
            time.sleep(web_driver.one_second)

            users_list = self.d.find_elements(By.XPATH, Read_Notification_Groups_Components().users_list_by_xpath())

            time.sleep(web_driver.one_second)

            if users_list[0].text == username[4]:
                self.logger.info(f"****** {users_list[0].text} user is present *******")
                self.status.append(True)
            else:
                self.status.append(False)

            self.logout_from_cloud_menu()
            login().login_with_persona_user(self.d, username[4])
            login().accept_terms_and_conditions_for_login_for_new_user(self.d)
            self.persona_users_permissions_validation(username[4])

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_PM_6.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_PM_6.png")
                return False
            else:
                return True

        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_PM_6_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_PM_6_exception.png")
            self.logger.error(f"TC_PM_6 got exception as: {ex}")
        finally:
            logout().logout_from_core(self.d)
